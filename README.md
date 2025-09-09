## Table of Contents
- [Problem Statement](#problem-statement)
- [What This Repository Solves](#what-this-repository-solves)
- [Features](#features)
- [Tools & Technologies Used](#tools--technologies-used)
- [Project Structure](#project-structure)
- [API Endpoints Overview](#api-endpoints-overview)
- [Setup Instructions](#setup-instructions)
- [UTM Vagrant Deployment](#utm-vagrant-deployment)
- [Assignment 5 Service URLs](#assignment-5-service-urls)
- [Assignment 5 Testing](#assignment-5-testing)
- [Testing the API](#testing-the-api)

#  Deploy the Flask Application On Bare Metal UTM Vagrant Using Nginx as Reverse Proxy

Assignment 5 builds on Assignment 4. Here the flask application is deployed on bare metal UTM vagrant. Two API containers are created and nginx is used as a reverse proxy load balancer between the two flask applications. Both of these flask applications are connected to the PostgreSQL container. 


## Problem Statement
As applications grow and user traffic increases, a single server instance becomes a bottleneck and single point of failure. Assignment 5 aims to simulate a real-world scenario where you implement **load balancing** for a containerized RESTful API. The challenge is to distribute incoming requests across multiple Flask application instances using Nginx as a reverse proxy, while maintaining data consistency through a shared PostgreSQL database. This setup demonstrates high availability concepts and prepares the application for production-scale traffic using UTM Vagrant as a bare metal virtualization platform. 

## What This Repository Solves
This repository demonstrates how to implement load balancing for a Flask REST API using Nginx as a reverse proxy. 

The solution includes:
- Two Flask application instances running on different ports (8081, 8082)
- Nginx reverse proxy with round-robin load balancing
- Containerized deployment using Docker Compose
- High availability and horizontal scaling concepts

## Features

### API Operations:
The Student REST API supports the following CRUD operations:
- Add a new student.
- Get all students.
- Get a student by ID.
- Update existing student information.
- Delete a student record.

### Assignment 5 Infrastructure Features:
- **Load Balancing**: Nginx reverse proxy distributes requests across multiple Flask instances
- **High Availability**: If one Flask instance fails, requests continue through the other instance
- **Bare Metal Virtualization**: Deployment on UTM Vagrant virtual machine
- **Container Orchestration**: Docker Compose manages multi-service architecture
- **Health Monitoring**: Individual instance health checks and logging
- **Round-Robin Distribution**: Automatic request distribution across backend services

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
- **Nginx** – Reverse Proxy and Load Balancer
- **UTM** – Application that allows to create Virtual Environment


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
|── nginx.conf
|── Vagrantfile
|── provision.sh


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
11. The `Vagranatfile` has instructions to virtual machines, create and cofigure network, allot memory, cpu, etc.
12. The `provision.sh` has bash setup commands that installs docker, docker compose and make.
13. The `nginx.conf` has the reverse proxy script that does load balancing between two api containers and lets them connect to the postgreSql
14. The `README.md` file provides setup and usage instructions. 

## Load Balanced API Access if Using UTM Vagrant
All endpoints are now accessible through the Nginx reverse proxy:
- **Nginx Proxy**: http://localhost:8080
- **Direct Access**:
  - Flask App 1: http://localhost:8081
  - Flask App 2: http://localhost:8082

## API Endpoints Overview
All endpoints are prefixed with `/api/v1/students`.
- `GET /api/v1/healthcheck` - Checks if the Flask application is running and returns a 200 status code with a JSON response (e.g., `{"status": "ok"}`).
- `GET /api/v1/students` – Fetch all students.
- `GET /api/v1/students/<id>` – Fetch a single student by ID.
- `POST /api/v1/students` – Add a new student (requires JSON body with `name`, `email`, and optional `age`).
- `PUT /api/v1/students/<id>` – Update an existing student's info.
- `DELETE /api/v1/students/<id>` – Delete a student.
  

# Flask Student API Setup Instructions - Local Setup & Docker Setup  - Assignment 4 and Previous Branches

## Local Setup (Without Docker)

This section describes how to set up and run the **Flask Student API** on your local machine without Docker.  
You’ll need **Python**, **PostgreSQL**, and other tools mentioned in the prequisite section.

### Steps

### 1. Clone the Repository 
``` bash 
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git
cd devops-bootcamp-assignments

```
### 2. Set Up a Virtual Environment

Create and activate a Python virtual environment to isolate dependencies:
``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
``` bash 
pip install -r requirements.txt
```

## 4. Install PostgreSQL Client Libraries

Make sure the PostgreSQL client library (libpq) is installed, as psycopg2 requires it:

``` bash
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
- Flask API (Load Balanced): http://localhost:8080
- Flask API Instance 1: http://localhost:8081
- Flask API Instance 2: http://localhost:8082
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

## For Setting Up UTM, Vagrant

UTM Vagrant Deployment

## Prerequisites
- **UTM**: Virtual machine manager for macOS
- **Vagrant**: Infrastructure automation tool

## Vagrant Setup Steps

### 1. Start Vagrant Environment

```bash
# To Start the Vagrant
vagrant up
```

### 2. SSH into Vagrant VM

```bash
# To get inside the Vagrant
vagrant ssh
```

### 3. Navigate to Project Directory

```bash
cd /vagrant
```

### 4. Deploy Load Balanced Application

```bash
# do vagrant ssh and then run the below command
docker-compose up --build -d
```

### 5. Verify All Services Running

```bash
# Check container status
docker ps

# Expected output: 4 containers running
# - postgres (student_db)
# - flask-app1 (student_api_1)
# - flask-app2 (student_api_2)
# - nginx (nginx_contanier_reverse_proxy)
```

### Vagrant Commands Reference:

```bash
vagrant up          # Start the virtual machine
vagrant ssh         # SSH into the VM
vagrant halt        # Stop the VM
vagrant destroy     # Remove the VM completely
vagrant status      # Check VM status
vagrant reload      # Restart VM with new Vagrantfile config
```

```bash
# View all running services
docker-compose ps

# Service logs
docker logs student_api_1                    # Flask instance 1
docker logs student_api_2                    # Flask instance 2
docker logs nginx_contanier_reverse_proxy    # Nginx load balancer
docker logs student_db                       # PostgreSQL database
```

### Load Balancing Verification:

#### Monitor Nginx Access Logs:

```bash
# Watch nginx logs in real-time
docker logs -f nginx_contanier_reverse_proxy
```

#### Monitor Individual Flask Instances:

```bash
docker logs -f student_api_1
docker logs -f student_api_2
```

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

**Health Check (Load Balanced)**
```bash
curl http://localhost:8080/api/v1/healthcheck
```

**Get All Students (Load Balanced)**
```bash
curl http://localhost:8080/api/v1/students
```

**Create Student (Load Balanced)**
```bash
curl -X POST http://localhost:8080/api/v1/students \
  -H "Content-Type: application/json" \
  -d '{"name": "abc", "email": "abc@example.com", "age": 20}'
```

### 3. Using Browser 
- **Load Balanced Health Check**: Visit http://localhost:8080/api/v1/healthcheck
- **Load Balanced Student List**: Visit http://localhost:8080/api/v1/students
- **Direct Flask 1 Access**: Visit http://localhost:8081/api/v1/healthcheck
- **Direct Flask 2 Access**: Visit http://localhost:8082/api/v1/healthcheck

**Note**: 
- Browser only supports GET requests directly. For POST, PUT, DELETE operations, use Postman or cURL.
- Refresh the load balanced URL multiple times to observe requests being distributed between Flask instances.

---

##  Troubleshooting

### Common Issues & Solutions:

#### 1. Nginx 502 Bad Gateway
**Problem**: Cannot access http://localhost:8080  
**Symptoms**: "502 Bad Gateway" error in browser

**Solutions**:
```bash
# Check if all containers are running
docker ps

# Restart nginx container
docker-compose restart nginx

# Verify nginx configuration is loaded
docker exec nginx_contanier_reverse_proxy cat /etc/nginx/nginx.conf

# Check nginx error logs
docker logs nginx_contanier_reverse_proxy
```

#### 2. Load Balancing Not Working
**Problem**: All requests go to same Flask instance  
**Symptoms**: Only one Flask container shows activity in logs

**Solutions**:
```bash
# Test individual Flask instances
curl http://localhost:8081/api/v1/healthcheck
curl http://localhost:8082/api/v1/healthcheck

# Restart all services
docker-compose down && docker-compose up -d

# Check nginx upstream configuration
docker exec nginx_contanier_reverse_proxy nginx -t
```

#### 3. Vagrant VM Issues
**Problem**: VM won't start or SSH fails  
**Symptoms**: `vagrant up` fails or `vagrant ssh` connection refused

**Solutions**:
```bash
# Check VM status
vagrant status

# Restart VM
vagrant halt && vagrant up

# Rebuild VM completely (if corrupted)
vagrant destroy && vagrant up
```

### Debug Commands:
```bash
# Container network inspection
docker network ls
docker network inspect devops-bootcamp-assignments_default

# Container inspection
docker inspect nginx_contanier_reverse_proxy
docker inspect student_api_1

# Resource monitoring
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```