# Assignment 2 - Containerise REST API

## 📚 Learning Outcomes

- Understand how to Dockerise a Python REST API.
- Learn how to write multi-stage Dockerfiles.
- Follow Dockerfile best practices to reduce image size.
- Learn how to inject environment variables at runtime.

---

## 📌 Problem Statement

Containerise the provided Flask-based REST API using Docker.

---

## ✅ Expectations

- The API must run using a Docker image.
- Use a **multi-stage Dockerfile** for building and running.
- Support environment variable injection at runtime.
- Ensure small Docker image size using best practices.
- Avoid using the `latest` tag; use **semantic versioning** instead.
- Add appropriate **Makefile** targets for building and running the container.
- Provide clear instructions in this README to build and run the Docker image.

---

## 🐳 Docker Instructions

### 🏗️ Build the Docker Image

```bash
docker build -t student-api:1.0.0 .
```

> ⚠️ Avoid using the `latest` tag. Use semantic versioning like `1.0.0`, `1.1.0`, etc.

### 🚀 Run the Docker Container

```bash
docker run -p 5000:5000 \
  -e FLASK_ENV=development \
  student-api:1.0.0
```

> You can pass other environment variables as needed using `-e`.


---

## 📎 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/v1/healthcheck`        | Health check endpoint |
| GET    | `/api/v1/students`           | Retrieve all students |
| POST   | `/api/v1/students`           | Add a new student |
| PUT    | `/api/v1/students/<id>`      | Update student details |
| DELETE | `/api/v1/students/<id>`      | Delete a student |

---

## 📦 Requirements

All required Python dependencies are listed in `requirements.txt`. These are automatically installed in the **builder stage** of the Dockerfile using:

```dockerfile
RUN pip install --upgrade pip && pip install --user -r requirements.txt
```

---

## 📁 File Structure

```
.
├── Dockerfile
├── app.py
├── requirements.txt
├── Makefile
└── README.md  <-- You are here!
```

---

## 🧼 Image Optimization

- Uses `python:3.11-slim` as base image.
- Separates build dependencies using **multi-stage builds**.
- Reduces image size by excluding pip cache and unused tools.

---

## 🧪 Testing the API

After running the container, test endpoints using:

```bash
curl http://localhost:5000/api/v1/healthcheck
```

Or use Postman/Insomnia for full CRUD operations.

---

## 🧑‍💻 Author

Assignment created for DevOps Bootcamp.


