from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route("/api/v1/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

@app.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and Email are required"}), 400
    
    student_id = len(students) + 1
    student = {
        "id": student_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "age": data.get("age", None)
    }
    students.append(student)
    return jsonify(student), 201

@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student["id"] == student_id:
            student["name"] = data.get("name", student["name"])
            student["email"] = data.get("email", student["email"])
            student["age"] = data.get("age", student["age"])
            return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



