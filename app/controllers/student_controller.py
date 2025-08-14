from app.models.student import Student
import logging

logger = logging.getLogger(__name__)

class StudentController:
    """Controller for student business logic."""
    
    @staticmethod
    def get_all_students():
        """Get all students."""
        try:
            students = Student.get_all()
            return [student.to_dict() for student in students], None
        except Exception as e:
            logger.error(f"Controller error getting all students: {e}")
            return None, str(e)
    
    @staticmethod
    def get_student_by_id(student_id):
        """Get student by ID."""
        try:
            student = Student.get_by_id(student_id)
            if not student:
                return None, "Student not found"
            return student.to_dict(), None
        except Exception as e:
            logger.error(f"Controller error getting student {student_id}: {e}")
            return None, str(e)
    
    @staticmethod
    def create_student(student_data):
        """Create a new student."""
        try:
            # Validate required fields
            if not student_data.get('name') or not student_data.get('email'):
                return None, "Name and Email are required"
            
            # Additional validation can be added here
            if not StudentController._is_valid_email(student_data.get('email')):
                return None, "Invalid email format"
            
            student = Student.create(
                name=student_data['name'],
                email=student_data['email'],
                age=student_data.get('age')
            )
            return student.to_dict(), None
        except Exception as e:
            logger.error(f"Controller error creating student: {e}")
            return None, str(e)
    
    @staticmethod
    def update_student(student_id, student_data):
        """Update an existing student."""
        try:
            student = Student.get_by_id(student_id)
            if not student:
                return None, "Student not found"
            
            # Validate email if provided
            if student_data.get('email') and not StudentController._is_valid_email(student_data.get('email')):
                return None, "Invalid email format"
            
            updated_student = student.update(
                name=student_data.get('name'),
                email=student_data.get('email'),
                age=student_data.get('age')
            )
            return updated_student.to_dict(), None
        except Exception as e:
            logger.error(f"Controller error updating student {student_id}: {e}")
            return None, str(e)
    
    @staticmethod
    def delete_student(student_id):
        """Delete a student."""
        try:
            student = Student.get_by_id(student_id)
            if not student:
                return False, "Student not found"
            
            success = student.delete()
            if success:
                return True, "Student deleted successfully"
            else:
                return False, "Failed to delete student"
        except Exception as e:
            logger.error(f"Controller error deleting student {student_id}: {e}")
            return False, str(e)
    
    @staticmethod
    def _is_valid_email(email):
        """Basic email validation."""
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None
    
    @staticmethod
    def validate_student_data(data, required_fields=None):
        """Validate student data."""
        if required_fields is None:
            required_fields = ['name', 'email']
        
        errors = []
        
        # Check required fields
        for field in required_fields:
            if not data.get(field):
                errors.append(f"{field.capitalize()} is required")
        
        # Validate email format
        if data.get('email') and not StudentController._is_valid_email(data['email']):
            errors.append("Invalid email format")
        
        # Validate age if provided
        if data.get('age') is not None:
            try:
                age = int(data['age'])
                if age < 0 or age > 150:
                    errors.append("Age must be between 0 and 150")
            except (ValueError, TypeError):
                errors.append("Age must be a valid number")
        
        return errors
