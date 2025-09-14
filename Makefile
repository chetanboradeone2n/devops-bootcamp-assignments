.PHONY: run migrate clean help build deploy test cleanup lint docker-login docker-push ci

# Variables
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

# Default target
all: setup run

# Build Docker image only (CI-friendly)
build:
	docker build -t devops-bootcamp-assignments-flask-app .
	sleep 30

# Deploy containers for testing
deploy:
	docker-compose up -d --build
	@echo "Waiting for application to be ready..."
	sleep 15

# Run tests
test:
	pip install requests
	cd tests && python3 test_students.py -v

# Clean up containers after testing
cleanup:
	docker-compose down --remove-orphans || true

# Perform code linting
lint:
	ruff check --fix --exit-zero --quiet .

# Docker login
docker-login:
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin

# Docker build and push
docker-push:
	docker tag devops-bootcamp-assignments-flask-app:latest $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:latest
	docker push $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:latest

# All CI stages
ci: build deploy test cleanup lint docker-login docker-push

# # Set up the virtual environment and install dependencies
# setup:
# 	python3 -m venv $(VENV)
# 	$(PIP) install -r requirements.txt

# # Run the Flask applicatio.n
# run:
# 	$(PYTHON) main.py

# # Apply database migrations

# migrate:
# 	@if [ ! -f .env ]; then echo "Error: .env file not found"; exit 1; fi
# 	@export $(cat .env | xargs); \
# 	if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_NAME" ] || [ -z "$DB_PASSWORD" ]; then \
# 		echo "Error: Environment variables DB_HOST, DB_USER, DB_NAME, and DB_PASSWORD must be set"; exit 1; \
# 	fi; \
# 	echo "Creating database if it doesn't exist..."; \
# 	psql -h "$DB_HOST" -U "$DB_USER" -d postgres -c "CREATE DATABASE IF NOT EXISTS $DB_NAME;" || { echo "Failed to create database"; exit 1; }; \
# 	echo "Applying migration to create students table..."; \
# 	psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -f migrations/001_create_students_table.sql || { echo "Migration failed"; exit 1; }; \
# 	echo "Migration completed successfully."
# # Clean up (remove virtual environment)
# clean:
# 	rm -rf $(VENV)

# # Help target to display available commands
# help:
# 	@echo "Available commands:"
# 	@echo "  make setup    - Set up the virtual environment and install dependencies"
# 	@echo "  make run      - Run the Flask application"
# 	@echo "  make migrate  - Apply database migrations"
# 	@echo "  make clean    - Remove the virtual environment"
# 	@echo "  make help     - Show this help message"