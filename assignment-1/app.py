from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Use connection pooling for better database connection management
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "mydatabase"),
    user=os.getenv("DB_USER", "myuser"),
    password=os.getenv("DB_PASSWORD", "mypassword")
)

@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route("/api/v1/students", methods=["GET"])
def get_students():
    conn = None
    cur = None
    try:
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        students = [
            {"id": row[0], "name": row[1], "email": row[2], "age": row[3]}
            for row in rows
        ]
        return jsonify(students), 200
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Error in get_students: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            db_pool.putconn(conn)

@app.route("/api/v1/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    conn = None
    cur = None
    try:
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cur.fetchone()
        if row is None:
            return jsonify({"error": "Student not found"}), 404
        student = {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3]
        }
        return jsonify(student), 200
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Error in get_student: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            db_pool.putconn(conn)

@app.route("/api/v1/students", methods=["POST"])
def add_student():
    conn = None
    cur = None
    try:
        data = request.get_json()
        if not data or not data.get("name") or not data.get("email"):
            return jsonify({"error": "Name and Email are required"}), 400

        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, email, age) VALUES (%s, %s, %s) RETURNING id",
            (data["name"], data["email"], data.get("age"))
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return jsonify({
            "id": new_id,
            "name": data["name"],
            "email": data["email"],
            "age": data.get("age")
        }), 201
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Error in add_student: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            db_pool.putconn(conn)

@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    conn = None
    cur = None
    try:
        data = request.get_json()
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        if not cur.fetchone():
            return jsonify({"error": "Student not found"}), 404

        cur.execute(
            "UPDATE students SET name = %s, email = %s, age = %s WHERE id = %s",
            (data.get("name"), data.get("email"), data.get("age"), student_id)
        )
        conn.commit()
        return jsonify({"message": "Student updated"}), 200
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Error in update_student: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            db_pool.putconn(conn)

@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = None
    cur = None
    try:
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        if not cur.fetchone():
            return jsonify({"error": "Student not found"}), 404

        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        return jsonify({"message": "Student deleted"}), 200
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Error in delete_student: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            db_pool.putconn(conn)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
