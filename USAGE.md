# Assignment 7 - How to Use the Application

## Quick Start

### 1. Deploy Everything
```bash
make k8s-deploy
```

### 2. Test the API
```bash
make k8s-test
```

### 3. Clean Up (when done)
```bash
make k8s-clean
```

## Manual Testing

### Option 1: Port Forward (Recommended)
```bash
# Start port forwarding
kubectl port-forward -n student-api service/flask-app-service 5000:5000

# In another terminal, test endpoints:
curl http://localhost:5000/api/v1/healthcheck
curl http://localhost:5000/api/v1/students
curl http://localhost:5000/api/v1/students/1
```

### Option 2: NodePort (if accessible)
```bash
curl http://$(minikube ip):30000/api/v1/healthcheck
curl http://$(minikube ip):30000/api/v1/students
```

## API Endpoints

- **GET /api/v1/healthcheck** - Health check
- **GET /api/v1/students** - Get all students  
- **GET /api/v1/students/{id}** - Get student by ID
- **POST /api/v1/students** - Create new student
- **PUT /api/v1/students/{id}** - Update student
- **DELETE /api/v1/students/{id}** - Delete student

## Create Student Example
```bash
curl -X POST http://localhost:5000/api/v1/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Student","email":"test@example.com","age":25}'
```

## Check Status
```bash
# Check pods
kubectl get pods -n student-api

# Check services  
kubectl get svc -n student-api

# Check secrets (should be from Vault via ESO)
kubectl get secrets -n student-api
```

## Architecture Components

### Namespaces Created:
- `student-api` - Flask app and PostgreSQL
- `vault` - HashiCorp Vault for secrets
- `external-secrets` - External Secrets Operator

### Services:
- `flask-app-service` (ClusterIP) - Internal access
- `flask-app-nodeport` (NodePort) - External access on port 30000
- `postgres-service` (ClusterIP) - Database access
- `vault-service` (ClusterIP) - Vault access

## Postman Collection
Use `Student_API_MVC_Collection.json` for testing all endpoints with Postman.

## Assignment Requirements Met:
✅ ConfigMaps for environment variables  
✅ External Secrets for DB credentials from Vault  
✅ Kubernetes manifests in proper structure  
✅ Init container for DB migrations  
✅ REST API exposed via services  
✅ All endpoints return 200 status codes