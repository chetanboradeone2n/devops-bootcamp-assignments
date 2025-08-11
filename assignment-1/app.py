from app import create_app
import os

# Create Flask application using factory pattern
app = create_app()

if __name__ == "__main__":
    # Get configuration from environment or use defaults
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(debug=debug, host=host, port=port)
