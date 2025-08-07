## Table of Contents
- [Problem Statement]
- [What This Repository Solves]
- [Features]
- [Tools & Technologies Used]
- [Project Structure]
- [API Endpoints Overview]
- [Setup Instructions]
- [Testing the API]


# Assignment 1 - Simple REST API Web Server

## Problem Statement

In many applications, CRUD operations form the foundation of data management. This assignment aims to simulate a real-world scenario where you build a versioned, environment-configurable RESTful API to manage student data using a backend database. This assignment focuses on creating a simple, yet extensible, REST API web server capable of performing CRUD operations on student records using a PostgreSQL database.

## What This Repository Solves

This repository provides a solution for building and managing student data through a REST API interface. The backend is powered by Python Flask and connected to a PostgreSQL database. The repository includes versioned API endpoints, schema migration support, and a Makefile to streamline local development workflows. This solution can be easily extended to larger systems and can serve as a base for integrating authentication, authorization, and frontend interfaces.

## Features

The API supports the following operations:

-  Add a new student.
-  Get all students.
-  Get a student by ID.
-  Update existing student information.
-  Delete a student record.

## Tools & Technologies Used

- **Python 3** – Main programming language
- **Flask** – Web framework to build the REST API
- **PostgreSQL** – Relational database to store student records
- **PIP** – Python package manager
- **GIT** – Version control system
- **Makefile** – To automate tasks like running the server, migrations, etc.
- **psycopg2** – PostgreSQL driver for Python
- **dotenv** – To manage environment variables
- **Flask-Migrate / SQL migration files** – For database schema changes
- **Postman** - To use different requests

## Project Structure

assignment-1/
├── app.py 
├── requirements.txt 
├── migrations/
│ └── 001_create_students_table.sql 
├── .env 
├── Makefile 
└── migrate.sh
└── README.md 

## Project Structure Explanation :

1. The app.py contains the main flask application
2. The requirements.txt has a list of all the dependencies that we need to install to run this project.
3. The Migrations/001_create_students_table.sql folder/file has the migration schema.
4. The .env file has the credentials required to login and create Database in Postgresql.
5. The Makefile automates the procresses like running the setting up the venv for python, runing or stopping app.py flask application, etc.
6. Shell script to run database migration by loading environment variables from .env file.
7. The README.md file has all the necessary setup instructions.

##  API Endpoints Overview

I have mentioned all the endpoints below - 
All endpoints are prefixed with `/api/v1/students`
- `GET /api/v1/healthcheck` - Checks if the flask applications is running ang gives a 200 status code in return if its healthy.
- `GET /api/v1/students` – Fetch all students
- `GET /api/v1/students/<id>` – Fetch a single student by ID
- `POST /api/v1/students` – Add a new student (requires JSON body)
- `PUT /api/v1/students/<id>` – Update an existing student's info
- `DELETE /api/v1/students/<id>` – Delete a student

## Setup Instructions 
1. Clone the devops-bootcamp-assignments repository.
git clone https://github.com/chetanboradeone2n/devops-bootcamp-assignments.git

2. Go inside the Assignment-1 folder.
cd devops-bootcamp-assignments
cd assignment-1

3. Create a Virtual Environment 
python3 -m venv namevenv
source namevenv/bin/activate   # For MAC and Linux Operating Systems
namevenv\Scripts\activate      # For Windows Operating System

4. Install Dependencies 
make setup 

## Some Makefile Commands for Reference 
make setup    - Set up the virtual environment and install dependencies
make run      - Run the Flask application
make migrate  - Apply database migrations
make clean    - Remove the virtual environment
make help     - Show this help message

5. Create .env file for storing the Database Credentials
touch .env

6. Add the database credentials in the .env file
For Example - 

DB_HOST=localhost
DB_NAME=students
DB_USER=your_username
DB_PASSWORD=your_password

7. Run the Database migration to create the students table.
make migrate 

Why to Run the "make migrate" command?
7.1. We run the make migrate command in the terminal to connects to the PostgreSQL database using credentials from .env
7.2 It also applies the schema from migrations/001_create_students_table.sql to create the students table. 

8. Start the flask application
make run

Desired Output after executing the "make run" command

venv/bin/python3 app.py
 * Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.29.85:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 126-069-887

9. Test flask api
You can check the flask api by three ways.
9.1 Through command line - curl localhost:5000/api/v1/healthcheck
9.2 Through browser - localhost:5000/api/v1/healthcheck
9.3 Through Postman - Select the GET method and the type localhost:5000/api/v1 and then click on send.




