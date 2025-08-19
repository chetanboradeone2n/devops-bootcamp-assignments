## Table of Contents
- [Problem Statement](#problem-statement)
- [What This Repository Solves](#what-this-repository-solves)
- [Features](#features)
- [Tools & Technologies Used](#tools--technologies-used)
- [Project Structure](#project-structure)
- [API Endpoints Overview](#api-endpoints-overview)
- [Setup Instructions](#setup-instructions)
- [Testing the API](#testing-the-api)

# Assignment 2 & 3 - Containerizing the REST API

The assignment 2 & 3 builds upon Assignment 1 by containerizing the Student REST API using Docker and Docker Compose. The application now runs in containers, making it more portable and easier to deploy.


## Problem Statement
In many applications, CRUD operations form the foundation of data management. The assignment 2 & 3 aims to simulate a real-world scenario where you containerise a versioned, environment-configurable RESTful API to manage student data using a PostgreSQL database. This assignment focuses to containerize a simple, yet extensible, REST API web server capable of performing CRUD operations on student records, with an emphasis on using environment variables for configuration and supporting database schema migrations.

## What This Repository Solves
This repository provides a solution to containerise building and managing student data through a REST API interface. The backend is powered by Python Flask and connected to a PostgreSQL database. The API includes versioned endpoints (e.g., `/api/v1/`) for future scalability, supports schema migrations via SQL files, and uses environment variables for secure configuration. This solution can be easily extended to larger systems and can serve as a base for integrating authentication, authorization, and frontend interfaces.

## Features
The API supports the following operations:
- Add a new student.
- Get all students.
- Get a student by ID.
- Update existing student information.
- Delete a student record.

## Tools & Technologies Used
- **Python 3** – Main programming language
- **Flask** – Web framework to build the REST API
- **PostgreSQL** – Relational database to store student records
- **Docker** – Containerization platform
- **Docker Compose** – Container orchestration for local development
- **PIP** – Python package manager
- **GIT** – Version control system
- **Makefile** – To automate tasks like running the server, migrations, etc.
- **psycopg2** – PostgreSQL driver for Python
- **python-dotenv** – To manage environment variables
- **SQL migration files** – For database schema changes
- **Postman** – To test API endpoints (collection included)

## Project Structure

``` 
── app
│   ├── controllers
│   │   ├── __init__.py
│   │   └── student_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── student.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── database.py
│   └── views
│       ├── __init__.py
│       └── student_views.py
├── main.py
├── Makefile
├── migrate.sh
├── migrations
│   └── 001_create_students_table.sql
├── README.md
├── requirements.txt
├── Student_API_MVC_Collection.json
|── Dockerfile
|── docker-compose.yml


```

## Project Structure Explanation:
1. The `app/` directory contains the MVC components:
   - `controllers/`: Contains `student_controller.py` that handles the business logic
   - `models/`: Contains `student.py` that defines the data structure and database operations
   - `views/`: Contains `student_views.py` that manages the API endpoints and request/response handling
   - `utils/`: Contains `database.py` for database connection management
2. The `main.py` is the entry point of the Flask application.
3. The `requirements.txt` lists all dependencies needed to run the project.
4. The `migrations/001_create_students_table.sql` file defines the database schema migration.
5. The `.env.example` file provides a template for database credentials (copy to `.env` locally).
6. The `Makefile` automates processes like setting up the virtual environment, running the Flask app, and applying migrations.
7. The `migrate.sh` script handles the database migration process.
8. The `Student_API_MVC_Collection.json` file contains predefined API requests for testing.
9. The `Dockerfile` provides the multi-stage dockerfile script, used for creating the container image.
10. The `docker-compose.yml` file has script to start both the flask and the postgres container
11. The `README.md` file provides setup and usage instructions.

## API Endpoints Overview
All endpoints are prefixed with `/api/v1/students`.
- `GET /api/v1/healthcheck` - Checks if the Flask application is running and returns a 200 status code with a JSON response (e.g., `{"status": "ok"}`).
- `GET /api/v1/students` – Fetch all students.
- `GET /api/v1/students/<id>` – Fetch a single student by ID.
- `POST /api/v1/students` – Add a new student (requires JSON body with `name`, `email`, and optional `age`).
- `PUT /api/v1/students/<id>` – Update an existing student's info.
- `DELETE /api/v1/students/<id>` – Delete a student.
  

# Flask Student API Setup Instructions - Local Setup & Docker Setup 

## Local Setup (Without Docker)

This section describes how to set up and run the **Flask Student API** on your local machine without Docker.  
You’ll need **Python**, **PostgreSQL**, and other tools installed.

### Steps

#### 1. Clone the Repository 
``` bash 
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
cd devops-bootcamp-assignments

```
### 2. Set Up a Virtual Environment

Create and activate a Python virtual environment to isolate dependencies:
``` bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
``` bash 
pip install -r requirements.txt
```

## 4. Install PostgreSQL Client Libraries

Make sure the PostgreSQL client library (libpq) is installed, as psycopg2 requires it:

Ubuntu/Debian:
``` bash
sudo apt-get install -y libpq-dev
```
``` bash
macOS:

brew install postgresql
```

## 5. Set Up PostgreSQL Database

Start your local PostgreSQL server:

Create a database named student_db:
``` bash 
psql -U postgres -c "CREATE DATABASE student_db;"
```

## 6. Add the Environment Variables in the .env file

``` bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_db
DB_USER=postgres
DB_PASSWORD=your_password
```
Replace your_password with your PostgreSQL user password.

## 7. Apply Database Migrations

Run the migration script to create the students table:
``` bash
bash migrate.sh
or 
make migrate
```
## 8. Run the Flask Application

Start the Flask app using the Makefile or directly by using Python:
```bash
make run   # If Makefile has a run command
Or:
python main.py
```

The Flask app will start on http://localhost:5000.

## With Docker & Docker Compose 

### Steps

## 1. Clone the Repository

```bash
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
cd devops-bootcamp-assignments
```

## 2. Build and Run with Docker Compose

```bash
docker-compose up --build -d
```

This command will:
- Build the Python application using multi-stage builds
- Create and start the PostgreSQL container
- Set up the database with initial migrations
- Start the Flask application

The following services will be available:
- Flask API: http://localhost:5000
- PostgreSQL: localhost:5432

## 3. Verify Services

Check if containers are running:
```bash
docker-compose ps
```

Check application logs:
```bash
docker-compose logs flask-app

```

* **Expected Output**:
```text
venv/bin/python3 app.py
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://192.168.29.85:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 126-069-887
```


## Docker Commands Reference

* `docker-compose up -d` - Start all services in detached mode
* `docker-compose down` - Stop and remove all containers
* `docker-compose logs` - View logs from all services
* `docker-compose ps` - List running services
* `docker-compose restart` - Restart services
* `docker-compose build` - Rebuild services


## Testing the API

You can test the API using the following methods:

### 1. Using Postman (Recommended)
1. Import the `Student_API_MVC_Collection.json` file into Postman
2. The collection includes pre-configured requests for all endpoints
3. Example requests included:

**Create Student (POST /api/v1/students)**
```json
{
    "name": "abc xyz",
    "email": "john@example.com",
    "age": 20
}
```

**Update Student (PUT /api/v1/students/{id})**
```json
{
    "name": "mno pqr",
    "email": "john.smith@example.com",
    "age": 21
}
```

### 2. Using cURL
Here are some example cURL commands:

**Health Check**
```bash
curl http://localhost:5000/api/v1/healthcheck
```

**Get All Students**
```bash
curl http://localhost:5000/api/v1/students
```

**Create Student**
```bash
curl -X POST http://localhost:5000/api/v1/students \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "age": 20}'
```

### 3. Using Browser
- Health Check: Visit http://localhost:5000/api/v1/healthcheck
- Get All Students: Visit http://localhost:5000/api/v1/students
- Note: Browser only supports GET requests directly. For POST, PUT, DELETE operations, use Postman or cURL.