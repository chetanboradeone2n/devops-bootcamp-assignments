from flask import Flask
from app.utils.database import db_manager
from app.views.student_views import student_bp
import logging
import os

def create_app(config_name=None):
    """Application factory pattern."""
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s'
    )
    
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'default')
    
    from config import config
    config_obj = config[config_name]()
    app.config.from_object(config_obj)
    
    # Initialize database connection pool
    db_manager.init_pool(config_obj)
    
    # Register blueprints
    app.register_blueprint(student_bp)
    
    # Global error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Endpoint not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Server Error: {error}')
        return {'error': 'Internal server error'}, 500
    
    return app
