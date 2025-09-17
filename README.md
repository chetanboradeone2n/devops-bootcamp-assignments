## Table of Contents
- [Problem Statement](#problem-statement)
- [What This Repository Solves](#what-this-repository-solves)
- [Features](#features)
- [Tools & Technologies Used](#tools--technologies-used)
- [Project Structure](#project-structure)
- [API Endpoints Overview](#api-endpoints-overview)
- [Setup Instructions](#setup-instructions)
- [CI/CD Pipeline](#cicd-pipeline)
- [Observability Stack](#observability-stack)
- [Testing the API](#testing-the-api)


# DevOps Bootcamp Assignments

This project shows how to build and deploy a Student REST API with complete monitoring. It starts with a simple Flask app, then adds Docker containers, automated testing, Kubernetes deployment, and a full monitoring system. Everything is automated and includes proper security and monitoring.

## Problem Statement
In many projects, CRUD operations are the base for handling data. In Assignment 2 & 3, the Student REST API was containerized with Docker and Docker Compose, connected to a PostgreSQL database, and supported versioned endpoints and migrations. Assignment 4 builds on top of this by adding automation through GitHub Actions. The goal is to set up a CI pipeline that builds Docker images, runs containers, tests the API endpoints, performs code linting, and finally pushes the image to Docker Hub.

## What This Repository Solves
This project shows how to build a complete application with monitoring:
- **Automated Building**: GitHub Actions builds and tests the app automatically
- **Kubernetes Deployment**: Runs the app on Kubernetes using Helm charts
- **Automated Deployment**: ArgoCD automatically deploys new versions
- **Secret Management**: Vault keeps passwords and secrets safe
- **Complete Monitoring**: Tracks app performance, logs, and sends alerts
- **Security**: Proper permissions and secure configurations


## Features
The API supports the following operations:
- Add a new student
- Get all students
- Get a student by ID
- Update existing student information
- Delete a student record

## Tools & Technologies Used
- **Python 3** – Main programming language
- **Flask** – Web framework to build the REST API
- **PostgreSQL** – Relational database to store student records
- **Docker** – Containerization platform
- **Docker Compose** – Container orchestration for local development
- **GitHub Actions** – To automate the Continuous Integration process
- **Kubernetes** – Container orchestration platform
- **Helm** – Kubernetes package manager
- **Prometheus & Grafana** – Monitoring and visualization
- **Vault** – Secrets management
- **Makefile** – To automate tasks like running the server, migrations, etc.
- **ruff** – To perform code linting
- **Postman** – To test API endpoints (collection included)

## Project Structure

```
├── .github/
│   └── workflows/
│       └── assignment4ci.yml
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── student_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── database.py
│   └── views/
│       ├── __init__.py
│       └── student_views.py
├── migrations/
│   └── 001_create_students_table.sql
├── tests/
│   └── test_students.py
├── main.py
├── Makefile
├── migrate.sh
├── README.md
├── requirements.txt
├── Student_API_MVC_Collection.json

├── Dockerfile
├── docker-compose.yml

```

## Project Structure Explanation:
1. The `.github/workflows/` directory contains the CI pipeline configuration
2. The `app/` directory contains the MVC components:
   - `controllers/`: Contains `student_controller.py` that handles the business logic
   - `models/`: Contains `student.py` that defines the data structure and database operations
   - `views/`: Contains `student_views.py` that manages the API endpoints and request/response handling
   - `utils/`: Contains `database.py` for database connection management
3. The `tests/` directory contains automated test scripts for API endpoints
4. The `main.py` is the entry point of the Flask application
5. The `requirements.txt` lists all dependencies needed to run the project
6. The `migrations/001_create_students_table.sql` file defines the database schema migration
7. The `.env.example` file provides a template for database credentials (copy to `.env` locally)
8. The `Makefile` automates processes like setting up the virtual environment, running the Flask app, applying migrations, building Docker images, running tests, code linting, and pushing to Docker Hub
9. The `migrate.sh` script handles the database migration process
10. The `Student_API_MVC_Collection.json` file contains predefined API requests for testing
11. The `Dockerfile` provides the multi-stage dockerfile script, used for creating the container image
12. The `docker-compose.yml` file has script to start both the flask and the postgres container

## API Endpoints Overview
All endpoints are prefixed with `/api/v1/students`.
- `GET /api/v1/healthcheck` - Checks if the Flask application is running and returns a 200 status code with a JSON response (e.g., `{"status": "ok"}`)
- `GET /api/v1/students` – Fetch all students
- `GET /api/v1/students/<id>` – Fetch a single student by ID
- `POST /api/v1/students` – Add a new student (requires JSON body with `name`, `email`, and optional `age`)
- `PUT /api/v1/students/<id>` – Update an existing student's info
- `DELETE /api/v1/students/<id>` – Delete a student

# Flask Student API Setup Instructions - Local Setup & Docker Setup 

## Local Setup (Without Docker)

This section describes how to set up and run the **Flask Student API** on your local machine without Docker.  

You'll need **Python**, **PostgreSQL**, and other tools mentioned in the prerequisite section.

### Steps

### 1. Clone the Repository 
```bash 
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
cd devops-bootcamp-assignments
```

### 2. Set Up a Virtual Environment

Create and activate a Python virtual environment to isolate dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash 
pip install -r requirements.txt

```

### 4. Install PostgreSQL Client Libraries

Make sure the PostgreSQL client library (libpq) is installed, as psycopg2 requires it:

```bash
brew install postgresql
```

### 5. Set Up PostgreSQL Database

Start your local PostgreSQL server and create a database named student_db:
```bash 
psql -U postgres -c "CREATE DATABASE student_db;"
```

### 6. Add the Environment Variables in the .env file

```bash

DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_db
DB_USER=postgres
DB_PASSWORD=your_password
```
Replace your_password with your PostgreSQL user password.

### 7. Apply Database Migrations

Run the migration script to create the students table:
```bash
bash migrate.sh
# or 
make migrate
```

### 8. Run the Flask Application

Start the Flask app using the Makefile or directly by using Python:
```bash
make run   # If Makefile has a run command
# Or:
python main.py
```

The Flask app will start on http://localhost:5000.

## With Docker & Docker Compose 

### Steps

### 1. Clone the Repository

```bash
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
cd devops-bootcamp-assignments
```

### 2. Build and Run with Docker Compose

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

### 3. Verify Services

Check if containers are running:
```bash
docker-compose ps

```

Check application logs:
```bash
docker-compose logs flask-app
```

**Expected Output**:
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

- `docker-compose up -d` - Start all services in detached mode
- `docker-compose down` - Stop and remove all containers
- `docker-compose logs` - View logs from all services
- `docker-compose ps` - List running services
- `docker-compose restart` - Restart services
- `docker-compose build` - Rebuild services

## CI/CD Pipeline

This project implements a comprehensive CI/CD pipeline using GitHub Actions that automatically builds, tests, and deploys the Student API.

### Pipeline Overview

The CI pipeline consists of the following stages:
1. **Build API** - Sets up the environment and builds the Docker containers
2. **Run Tests** - Executes automated API endpoint tests
3. **Perform Code Linting** - Checks code quality using ruff
4. **Docker Login** - Authenticates with Docker Hub
5. **Docker Build and Push** - Builds and pushes the validated image to Docker Hub

### Self-Hosted Runner Setup

The pipeline runs on a self-hosted GitHub runner for better control and performance.

#### Setting up Self-Hosted Runner:

1. Navigate to your GitHub repository settings
2. Go to **Settings > Actions > Runners**
3. Click **New self-hosted runner**
4. Choose your operating system (macOS/Windows/Linux)
5. Follow the installation commands provided by GitHub
6. Execute the runner:
   ```bash
   ./run.sh
   ```
7. Verify the runner appears as "Active" in your GitHub repository settings

### Pipeline Triggers

The CI pipeline is configured to trigger in the following scenarios:

- **Branch-specific pushes**: Only triggers when code is pushed to the `setup-a-ci-pipeline4` branch
- **Manual trigger**: Developers can manually trigger the pipeline using the `workflow_dispatch` event from the GitHub Actions UI

### Required GitHub Secrets

Configure the following secrets in your GitHub repository settings (**Settings > Secrets and variables > Actions**):

- `DOCKER_USERNAME` - Your Docker Hub username
- `DOCKER_PASSWORD` - Your Docker Hub password or access token
- `POSTGRES_DB` - PostgreSQL database name
- `POSTGRES_USER` - PostgreSQL username
- `POSTGRES_PASSWORD` - PostgreSQL password
- `POSTGRES_HOST_AUTH_METHOD` - PostgreSQL authentication method
- `DB_HOST` - Database host
- `DB_PORT` - Database port
- `DB_NAME` - Database name
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password

### Makefile Integration

The CI pipeline utilizes Makefile targets for consistent automation:

```bash
# Build the Docker image
make docker-build

# Run API tests
make test

# Perform code linting
make lint

# Push image to Docker Hub
make docker-push
```

### Pipeline Benefits

- **Automated Quality Checks**: Every code push triggers automated testing and linting
- **Consistent Builds**: Docker ensures the same environment across all stages
- **Fail-Fast Approach**: Pipeline stops on first failure, preventing bad code from progressing
- **Manual Control**: Developers can manually trigger builds when needed
- **Branch Protection**: Only specific branches trigger the pipeline, preventing unnecessary runs

## Monitoring Setup

The project includes a complete monitoring system that watches the app and sends alerts:

### What's Included
- **Prometheus** - Collects numbers about how the app is running
- **Grafana** - Shows charts and graphs of app performance
- **Loki** - Stores all the app logs in one place
- **Promtail** - Collects logs from the app containers
- **Database Monitor** - Watches PostgreSQL database performance
- **Website Monitor** - Checks if ArgoCD, Vault, and Student API are working
- **Server Monitor** - Tracks CPU, memory, and disk usage
- **Kubernetes Monitor** - Watches the Kubernetes cluster health

### What You Can See
- **5 Dashboards**: Database stats, app logs, server health, Kubernetes status, website uptime
- **Alerts**: Gets notified when CPU/disk is full, app has errors, or services go down
- **Slack Messages**: Sends alerts to Slack channel automatically
- **Secure Setup**: All passwords stored safely in Vault

### How to Deploy
```bash
helm install observability ./helm/observability
```

This monitoring system watches everything and tells you when something goes wrong.

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

### 4. Automated Testing
The project includes automated tests that run as part of the CI pipeline:

```bash
# Run tests locally
cd tests
python3 test_students.py -v

# Or using make command
make test
```

The automated tests verify:
- Health check endpoint functionality
- CRUD operations for students
- API response formats and status codes
- Database connectivity and data persistence