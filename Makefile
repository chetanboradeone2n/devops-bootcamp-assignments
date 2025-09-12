.PHONY: deploy clean-deploy test-deploy build test lint help

all: deploy

#deploy:
#	docker-compose up -d --build

clean-deploy:
	docker-compose down
	docker-compose down -v


test-deploy:
	@echo "Testing deployment endpoints..."
	@echo "Nginx (Load Balancer): $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/v1/healthcheck)"
	@echo "API 1 Direct: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8081/api/v1/healthcheck)"  
	@echo "API 2 Direct: $$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8082/api/v1/healthcheck)"


build:
	docker-compose build


#test:
#	pip install requests
#	cd tests && python3 test_students.py -v


lint:
	ruff check --fix --exit-zero --quiet .

# Build Docker image only (CI-friendly)
build:
	docker build -t devops-bootcamp-assignments-flask-app .

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
	docker tag devops-bootcamp-assignments-flask-app:latest $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:latest
	docker push $(DOCKER_USERNAME)/devops-bootcamp-assignments-flask-app:latest

