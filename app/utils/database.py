import psycopg2
import os
from psycopg2.extras import RealDictCursor
from psycopg2 import pool

class DatabaseManager:
    def __init__(self):
        self.connection_pool = None
        self.connection = None
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = os.getenv('DB_PORT', '5432')
        self.database = os.getenv('DB_NAME', 'student_db')
        self.user = os.getenv('DB_USER', 'postgres')
        self.password = os.getenv('DB_PASSWORD', 'password')
    
    def init_pool(self, config=None):
        """Initialize connection pool"""
        try:
            print(f"Attempting to connect to database at {self.host}:{self.port}")
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,  # min and max connections
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print(f"Connection pool created for database: {self.database}")
            
            # Test the connection
            conn = self.connection_pool.getconn()
            cur = conn.cursor()
            cur.execute('SELECT 1')
            print("Database connection test successful!")
            cur.close()
            self.connection_pool.putconn(conn)
        except Exception as error:
            print(f"Error creating connection pool: {error}")
            raise error
    
    def get_connection(self):
        """Get connection from pool or create new connection"""
        if self.connection_pool:
            try:
                return self.connection_pool.getconn()
            except Exception as error:
                print(f"Error getting connection from pool: {error}")
                return self.connect()
        else:
            return self.connect()
    
    def put_connection(self, connection):
        """Return connection to pool"""
        if self.connection_pool and connection:
            self.connection_pool.putconn(connection)
    
    def connect(self):
        """Create a single connection"""
        try:
            print(f"Attempting to connect to database with settings:")
            print(f"Host: {self.host}, Port: {self.port}, DB: {self.database}, User: {self.user}")
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                cursor_factory=RealDictCursor
            )
            print(f"Successfully connected to database: {self.database}")
            return connection
        except Exception as error:
            print(f"Error connecting to database: {error}")
            print(f"Connection parameters: host={self.host}, port={self.port}, database={self.database}, user={self.user}")
            return None
    
    def get_db_cursor(self):
        """Get a database cursor from the connection pool with context management"""
        class CursorContextManager:
            def __init__(self, db_manager):
                self.db_manager = db_manager
                self.conn = None
                self.cur = None

            def __enter__(self):
                self.conn = self.db_manager.get_connection()
                if not self.conn:
                    raise Exception("Failed to get database connection")
                self.cur = self.conn.cursor()
                return self.conn, self.cur

            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None:
                    # No exception occurred, commit the transaction
                    self.conn.commit()
                else:
                    # An exception occurred, rollback
                    self.conn.rollback()
                
                if self.cur:
                    self.cur.close()
                if self.conn:
                    self.db_manager.put_connection(self.conn)
                    
        return CursorContextManager(self)
    
    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            if not connection:
                raise Exception("Failed to establish database connection")
                
            cursor = connection.cursor()
            print(f"Executing query: {query}")
            if params:
                print(f"With parameters: {params}")
                
            cursor.execute(query, params)
            
            # If it's a SELECT query, fetch results
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                if not results:
                    print("Query returned no results")
                    return []  # Return empty list instead of None
                return results
            else:
                # For INSERT, UPDATE, DELETE - commit the transaction
                connection.commit()
                return cursor.rowcount
                
        except Exception as error:
            if connection:
                connection.rollback()
            print(f"Error executing query: {error}")
            print(f"Query was: {query}")
            if params:
                print(f"Parameters were: {params}")
            raise error
        finally:
            if cursor:
                cursor.close()
            if connection and self.connection_pool:
                self.put_connection(connection)
    
    def disconnect(self):
        """Close connection pool"""
        if self.connection_pool:
            self.connection_pool.closeall()
            print("Connection pool closed")
        elif self.connection:
            self.connection.close()
            print("Database connection closed")

# Global database manager instance
db_manager = DatabaseManager()