# Assignment 3 - One-Click Local Development Setup

This project sets up a simple Flask-based REST API for managing student records, along with a PostgreSQL database using Docker Compose. The goal is to simplify local development by providing a one-click setup using Makefile and Docker Compose.

---

## 📚 Learning Outcomes

- Understand how to use `docker-compose` to orchestrate services.
- Learn to write and use a `Makefile` for development tasks.
- Create a simple one-click local development environment.
- Automate dependency setup and service orchestration.

---

## 🧩 Prerequisites

Ensure the following tools are **pre-installed** on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If not installed, you may provide bash helper functions/scripts to install them for new team members.

---

## 🚀 Project Structure

```bash
assignment3/
├── app.py
├── db/
│   └── init.sql
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

---

## ⚙️ Makefile Targets

The following `make` targets are available to manage the local development environment:

| Target         | Description                                         |
|----------------|-----------------------------------------------------|
| `make build`   | Builds the Docker image for the Flask API          |
| `make up`      | Starts both API and DB containers via Docker Compose |
| `make down`    | Stops and removes all running containers            |
| `make logs`    | Tails the logs of all running containers            |
| `make ps`      | Shows the status of all Docker Compose services     |

---

## 🧪 How It Works

1. **Database Setup**
   - A PostgreSQL container is started.
   - On initialization, it runs the SQL in `db/init.sql` to create the `students` table.

2. **Flask REST API**
   - A Python Flask container exposes API routes:
     - `GET /api/v1/healthcheck`
     - `GET /api/v1/students`
     - `POST /api/v1/students`
     - `PUT /api/v1/students/<id>`
     - `DELETE /api/v1/students/<id>`

3. **Docker Compose**
   - Orchestrates `web` and `db` containers.
   - Ensures `db` is started before `web` using `depends_on`.

---

## 🛠️ Steps to Run

Run the following commands in order:

```bash
# Step 1: Build the Docker images
make build

# Step 2: Start the database and REST API containers
make up

# Step 3: View container status
make ps

# Step 4: Check logs if needed
make logs
```

To stop all services:

```bash
make down
```

---

## 🌐 API Endpoints

Once the containers are up, you can access the API at:

```http
GET     http://localhost:5000/api/v1/healthcheck
GET     http://localhost:5000/api/v1/students
POST    http://localhost:5000/api/v1/students
PUT     http://localhost:5000/api/v1/students/<id>
DELETE  http://localhost:5000/api/v1/students/<id>
```

---

## 👨‍💻 Author

Chetan Borade

---

## 📎 License

This project is for educational purposes only.

