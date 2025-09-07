.PHONY: run migrate clean help build test lint docker-login docker-push ci k8s-deploy k8s-clean k8s-test

# Variables
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

# Default target
all: setup run

# Build API
build:
	docker-compose up -d --build

# Run tests
test:
	pip install requests
	cd tests && python3 test_students.py -v

# Perform code linting
lint:
	ruff check --fix --exit-zero --quiet .

# Docker login
docker-login:
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin

# Docker build and push
docker-push:
	docker push $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:latest

# All CI stages
ci: build test lint docker-login docker-push

# Kubernetes deployment
k8s-deploy:
	kubectl apply -f k8s/

# Clean up Kubernetes resources
k8s-clean:
	kubectl delete -f k8s/ --ignore-not-found=true

# Test Kubernetes API
k8s-test:
	@echo "Testing API endpoints..."
	@kubectl port-forward -n student-api service/flask-app-service 5000:5000 &
	@sleep 3
	@echo "Health check: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/api/v1/healthcheck)"
	@echo "Get students: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/api/v1/students)"
	@pkill -f "kubectl port-forward" || true

# Help
help:
	@echo "Available commands:"
	@echo "  make k8s-deploy  - Deploy to Kubernetes"
	@echo "  make k8s-clean   - Clean up Kubernetes resources"
	@echo "  make k8s-test    - Test API endpoints"
	@echo "  make build       - Build with Docker Compose"
	@echo "  make test        - Run Python tests"
	@echo "  make lint        - Run code linting"