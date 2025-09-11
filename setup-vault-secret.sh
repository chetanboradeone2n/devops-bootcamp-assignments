#!/bin/bash
# Script to create Vault token secret for External Secrets Operator
# This secret is NOT stored in Git for security reasons

echo "Creating Vault limited-privilege token..."

# Port forward to Vault (run in background)
kubectl port-forward -n vault svc/vault-service 8200:8200 &
PORT_FORWARD_PID=$!

# Wait for port forward to be ready
sleep 3

# Create limited-privilege token
VAULT_TOKEN=$(kubectl exec -n vault deployment/vault-deployment -- sh -c 'VAULT_ADDR=http://127.0.0.1:8200 vault token create -policy=external-secrets-policy -ttl=24h -format=json' | jq -r '.auth.client_token')

# Kill port forward
kill $PORT_FORWARD_PID 2>/dev/null || true

if [ -z "$VAULT_TOKEN" ]; then
    echo "Error: Failed to create Vault token"
    exit 1
fi

echo "Creating Kubernetes secret with Vault token..."

# Create the secret in Kubernetes
kubectl create secret generic vault-limited-token \
  -n external-secrets \
  --from-literal=token="$VAULT_TOKEN" \
  --dry-run=client -o yaml | kubectl apply -f -

echo "Secret created successfully!"
echo "Token: $VAULT_TOKEN"