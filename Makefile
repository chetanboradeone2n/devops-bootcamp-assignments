.PHONY: run migrate clean help build test lint docker-login docker-push ci k8s-deploy k8s-clean k8s-test helm-deploy helm-clean helm-test

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
	docker push $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:$(IMAGE_TAG)

# All CI stages
ci: build test lint docker-login docker-push

# Helm deployment
helm-deploy:
	helm install external-secrets helm/external-secrets --namespace external-secrets --create-namespace
	helm install vault helm/vault --namespace vault --create-namespace
	helm install postgresql helm/postgresql --namespace student-api --create-namespace
	helm install student-api helm/student-api --namespace student-api

# Clean up Helm resources
helm-clean:
	helm uninstall student-api --namespace student-api --ignore-not-found
	helm uninstall postgresql --namespace student-api --ignore-not-found
	helm uninstall vault --namespace vault --ignore-not-found
	helm uninstall external-secrets --namespace external-secrets --ignore-not-found

# Test Helm deployment
helm-test:
	@echo "Testing API endpoints..."
	@kubectl port-forward -n student-api service/flask-app-service 5000:5000 &
	@sleep 3
	@echo "Health check: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/api/v1/healthcheck)"
	@echo "Get students: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/api/v1/students)"
	@pkill -f "kubectl port-forward" || true

# Kubernetes deployment (legacy)
k8s-deploy:
	kubectl apply -f k8s/

# Clean up Kubernetes resources (legacy)
k8s-clean:
	kubectl delete -f k8s/ --ignore-not-found=true

# Test Kubernetes API (legacy)
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
	@echo "  make helm-deploy - Deploy using Helm charts"
	@echo "  make helm-clean  - Clean up Helm releases"
	@echo "  make helm-test   - Test Helm deployment"
	@echo "  make k8s-deploy  - Deploy to Kubernetes (legacy)"
	@echo "  make k8s-clean   - Clean up Kubernetes resources (legacy)"
	@echo "  make k8s-test    - Test API endpoints (legacy)"
	@echo "  make build       - Build with Docker Compose"
	@echo "  make test        - Run Python tests"
	@echo "  make lint        - Run code linting"