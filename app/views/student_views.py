from flask import Blueprint, request, jsonify
from app.controllers.student_controller import StudentController
import logging

logger = logging.getLogger(__name__)

# Create blueprint for student routes
student_bp = Blueprint('students', __name__, url_prefix='/api/v1')

@student_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

@student_bp.route('/students', methods=['GET'])
def get_students():
    """Get all students."""
    try:
        students, error = StudentController.get_all_students()
        if error:
            return jsonify({'error': error}), 500
        return jsonify(students), 200
    except Exception as e:
        logger.error(f"Unexpected error in get_students: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student by ID."""
    try:
        student, error = StudentController.get_student_by_id(student_id)
        if error:
            if error == "Student not found":
                return jsonify({'error': error}), 404
            return jsonify({'error': error}), 500
        return jsonify(student), 200
    except Exception as e:
        logger.error(f"Unexpected error in get_student: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Validate data
        errors = StudentController.validate_student_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Create student
        student, error = StudentController.create_student(data)
        if error:
            return jsonify({'error': error}), 400
        
        return jsonify(student), 201
    except Exception as e:
        logger.error(f"Unexpected error in create_student: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student."""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Validate data (not all fields required for update)
        errors = StudentController.validate_student_data(data, required_fields=[])
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Update student
        student, error = StudentController.update_student(student_id, data)
        if error:
            if error == "Student not found":
                return jsonify({'error': error}), 404
            return jsonify({'error': error}), 400
        
        return jsonify(student), 200
    except Exception as e:
        logger.error(f"Unexpected error in update_student: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student."""
    try:
        success, message = StudentController.delete_student(student_id)
        if not success:
            if message == "Student not found":
                return jsonify({'error': message}), 404
            return jsonify({'error': message}), 500
        
        return jsonify({'message': message}), 200
    except Exception as e:
        logger.error(f"Unexpected error in delete_student: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Error handlers for the blueprint
@student_bp.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({'error': 'Bad request'}), 400

@student_bp.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({'error': 'Resource not found'}), 404

@student_bp.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500
