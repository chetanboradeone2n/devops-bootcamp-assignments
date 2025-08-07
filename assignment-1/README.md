## Table of Contents
- [Problem Statement](#problem-statement)
- [What This Repository Solves](#what-this-repository-solves)
- [Features](#features)
- [Tools & Technologies Used](#tools--technologies-used)
- [Project Structure](#project-structure)
- [API Endpoints Overview](#api-endpoints-overview)
- [Setup Instructions](#setup-instructions)
- [Testing the API](#testing-the-api)

# Assignment 1 - Simple REST API Web Server

## Problem Statement
In many applications, CRUD operations form the foundation of data management. This assignment aims to simulate a real-world scenario where you build a versioned, environment-configurable RESTful API to manage student data using a PostgreSQL database. This assignment focuses on creating a simple, yet extensible, REST API web server capable of performing CRUD operations on student records, with an emphasis on using environment variables for configuration and supporting database schema migrations.

## What This Repository Solves
This repository provides a solution for building and managing student data through a REST API interface. The backend is powered by Python Flask and connected to a PostgreSQL database. The API includes versioned endpoints (e.g., `/api/v1/`) for future scalability, supports schema migrations via SQL files, and uses environment variables for secure configuration. This solution can be easily extended to larger systems and can serve as a base for integrating authentication, authorization, and frontend interfaces.

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
- **PIP** – Python package manager
- **GIT** – Version control system
- **Makefile** – To automate tasks like running the server, migrations, etc.
- **psycopg2** – PostgreSQL driver for Python
- **python-dotenv** – To manage environment variables
- **SQL migration files** – For database schema changes
- **Postman** – To test API endpoints (collection included)

## Project Structure

```
assignment-1/
├── app.py
├── requirements.txt
├── migrations/
│   └── 001_create_students_table.sql
├── .env.example          # Template for environment variables (not committed)
├── Makefile              # Automates setup, run, and migration tasks
├── postman_collection.json  # Postman collection for API testing
├── README.md
└── venv/                 # Virtual environment (local, not committed)

``` 


## Project Structure Explanation:
1. The `app.py` contains the main Flask application.
2. The `requirements.txt` lists all dependencies needed to run the project.
3. The `migrations/001_create_students_table.sql` file defines the database schema migration.
4. The `.env.example` file provides a template for database credentials (copy to `.env` locally).
5. The `Makefile` automates processes like setting up the virtual environment, running the Flask app, and applying migrations.
6. The `postman_collection.json` file contains predefined API requests for testing.
7. The `README.md` file provides setup and usage instructions.

## API Endpoints Overview
All endpoints are prefixed with `/api/v1/students`.
- `GET /api/v1/healthcheck` - Checks if the Flask application is running and returns a 200 status code with a JSON response (e.g., `{"status": "ok"}`).
- `GET /api/v1/students` – Fetch all students.
- `GET /api/v1/students/<id>` – Fetch a single student by ID.
- `POST /api/v1/students` – Add a new student (requires JSON body with `name`, `email`, and optional `age`).
- `PUT /api/v1/students/<id>` – Update an existing student's info.
- `DELETE /api/v1/students/<id>` – Delete a student.
  

# Flask Student API Setup Instructions

## 1. Clone the Repository
 ```bash
   git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
   cd devops-bootcamp-assignments/assignment-1
 ```

## 2. Set Up the Virtual Environment and Install Dependencies

```bash
make setup
source venv/bin/activate # For macOS/Linux; use venv\Scripts\activate for Windows
```

## 3. Configure Environment Variables

* Copy the .env.example file to .env:
```bash
cp .env.example .env
```

* Edit .env with your PostgreSQL credentials (do not commit .env):
```text
DB_HOST=localhost
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=your_password
```

* Ensure .env is added to .gitignore.

## 4. Run Database Migrations

```bash
make migrate
```

* This command creates the database (if it doesn't exist) and applies the schema from migrations/001_create_students_table.sql to create the students table.

## 5. Start the Flask Application

```bash
make run
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

## 6. Makefile Commands for Reference

* `make setup` - Set up the virtual environment and install dependencies.
* `make run` - Run the Flask application.
* `make migrate` - Apply database migrations.
* `make clean` - Remove the virtual environment.
* `make help` - Show this help message.

## Testing the API

You can test the API using the following methods:

### 1. Command Line
Use curl:
```bash
curl http://localhost:5000/api/v1/healthcheck
```

### 2. Browser
Visit http://localhost:5000/api/v1/healthcheck.

### 3. Postman
Import the postman_collection.json file and use the predefined requests to test all endpoints (e.g., GET, POST, PUT, DELETE).