from app.utils.database import db_manager
import logging

logger = logging.getLogger(__name__)

class Student:
    """Student model for database operations."""
    
    def __init__(self, id=None, name=None, email=None, age=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
    
    def to_dict(self):
        """Convert Student object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }
    
    @classmethod
    def from_row(cls, row):
        """Create Student object from database row."""
        if not row:
            return None
        return cls(id=row[0], name=row[1], email=row[2], age=row[3])
    
    @classmethod
    def get_all(cls):
        """Retrieve all students from database."""
        try:
            with db_manager.get_db_cursor() as (conn, cur):
                cur.execute("SELECT * FROM students")
                rows = cur.fetchall()
                return [cls.from_row(row) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving all students: {e}")
            raise
    
    @classmethod
    def get_by_id(cls, student_id):
        """Retrieve a student by ID."""
        try:
            with db_manager.get_db_cursor() as (conn, cur):
                cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
                row = cur.fetchone()
                return cls.from_row(row)
        except Exception as e:
            logger.error(f"Error retrieving student {student_id}: {e}")
            raise
    
    def save(self):
        """Save student to database (create or update)."""
        try:
            if self.id is None:
                # Create new student
                with db_manager.get_db_cursor() as (conn, cur):
                    cur.execute(
                        "INSERT INTO students (name, email, age) VALUES (%s, %s, %s) RETURNING id",
                        (self.name, self.email, self.age)
                    )
                    self.id = cur.fetchone()[0]
                logger.info(f"Created new student with ID: {self.id}")
            else:
                # Update existing student
                with db_manager.get_db_cursor() as (conn, cur):
                    cur.execute(
                        "UPDATE students SET name = %s, email = %s, age = %s WHERE id = %s",
                        (self.name, self.email, self.age, self.id)
                    )
                logger.info(f"Updated student with ID: {self.id}")
            return self
        except Exception as e:
            logger.error(f"Error saving student: {e}")
            raise
    
    @classmethod
    def create(cls, name, email, age=None):
        """Create a new student."""
        student = cls(name=name, email=email, age=age)
        return student.save()
    
    def update(self, name=None, email=None, age=None):
        """Update student attributes."""
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if age is not None:
            self.age = age
        return self.save()
    
    def delete(self):
        """Delete student from database."""
        if self.id is None:
            raise ValueError("Cannot delete student without ID")
        
        try:
            with db_manager.get_db_cursor() as (conn, cur):
                cur.execute("DELETE FROM students WHERE id = %s", (self.id,))
                deleted_rows = cur.rowcount
                if deleted_rows == 0:
                    return False
                logger.info(f"Deleted student with ID: {self.id}")
                return True
        except Exception as e:
            logger.error(f"Error deleting student {self.id}: {e}")
            raise
    
    @classmethod
    def delete_by_id(cls, student_id):
        """Delete student by ID."""
        student = cls.get_by_id(student_id)
        if student:
            return student.delete()
        return False
    
    def exists(self):
        """Check if student exists in database."""
        if self.id is None:
            return False
        return self.get_by_id(self.id) is not None
