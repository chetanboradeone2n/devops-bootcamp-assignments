from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="db",  # service name from docker-compose
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cur = conn.cursor()

@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route("/api/v1/students", methods=["GET"])
def get_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3]
        })
    return jsonify(students), 200

@app.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and Email are required"}), 400

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

@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    if not cur.fetchone():
        return jsonify({"error": "Student not found"}), 404

    cur.execute(
        "UPDATE students SET name = %s, email = %s, age = %s WHERE id = %s",
        (data.get("name"), data.get("email"), data.get("age"), student_id)
    )
    conn.commit()
    return jsonify({"message": "Student updated"}), 200

@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    if not cur.fetchone():
        return jsonify({"error": "Student not found"}), 404

    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    return jsonify({"message": "Student deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
