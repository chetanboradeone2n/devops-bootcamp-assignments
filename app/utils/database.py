import psycopg2
from psycopg2 import pool
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Simple database connection pool manager."""
    
    def __init__(self):
        self.db_pool = None
    
    def init_pool(self, config):
        """Initialize the database connection pool."""
        try:
            self.db_pool = psycopg2.pool.SimpleConnectionPool(
                config.DB_POOL_MIN,
                config.DB_POOL_MAX,
                host=config.DB_HOST,
                database=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD
            )
            logger.info("Database connection pool initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database pool: {e}")
            raise
    
    @contextmanager
    def get_db_cursor(self):
        """Context manager for database operations."""
        if not self.db_pool:
            raise RuntimeError("Database pool not initialized")
        
        conn = None
        cur = None
        try:
            conn = self.db_pool.getconn()
            cur = conn.cursor()
            yield conn, cur
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Database operation error: {e}")
            raise
        finally:
            if cur:
                cur.close()
            if conn:
                self.db_pool.putconn(conn)

# Global database manager instance
db_manager = DatabaseManager()
