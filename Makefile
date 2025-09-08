.PHONY: deploy clean-deploy test-deploy build test lint help

all: deploy

deploy:
	docker-compose up -d --build

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


test:
	pip install requests
	cd tests && python3 test_students.py -v


lint:
	ruff check --fix --exit-zero --quiet .


help:
	@echo "Available commands:"
	@echo "  make deploy       - Deploy with Docker Compose"
	@echo "  make clean-deploy - Clean up deployment" 
	@echo "  make test-deploy  - Test deployment endpoints"
	@echo "  make build        - Build containers"
	@echo "  make test         - Run Python tests"
	@echo "  make lint         - Run code linting"