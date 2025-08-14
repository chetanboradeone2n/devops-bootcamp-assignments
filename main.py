from flask import Flask
from app.views.student_views import student_bp
from app.utils.database import db_manager
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Simple configuration class
class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "mydatabase")
    DB_USER = os.getenv("DB_USER", "myuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")
    DB_POOL_MIN = 1
    DB_POOL_MAX = 20

# Initialize database pool
db_manager.init_pool(Config())

# Register blueprint
app.register_blueprint(student_bp)

# Global error handlers
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Endpoint not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Server Error: {error}')
    return {'error': 'Internal server error'}, 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")