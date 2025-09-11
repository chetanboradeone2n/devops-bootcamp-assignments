# Vault Secret Setup

## ⚠️ Security Note
The Vault token used by External Secrets Operator is **NOT** stored in Git for security reasons. It must be created directly in the Kubernetes cluster.

## Setup Instructions

### Automatic Setup (Recommended)
Run the provided script to create the Vault secret:

```bash
./setup-vault-secret.sh
```

### Manual Setup
If you need to create the secret manually:

1. **Port forward to Vault:**
   ```bash
   kubectl port-forward -n vault svc/vault-service 8200:8200 &
   ```

2. **Create a limited-privilege token:**
   ```bash
   VAULT_TOKEN=$(kubectl exec -n vault deployment/vault-deployment -- sh -c \
     'VAULT_ADDR=http://127.0.0.1:8200 vault token create -policy=external-secrets-policy -ttl=24h -format=json' \
     | jq -r '.auth.client_token')
   ```

3. **Create the Kubernetes secret:**
   ```bash
   kubectl create secret generic vault-limited-token \
     -n external-secrets \
     --from-literal=token="$VAULT_TOKEN"
   ```

4. **Kill port forward:**
   ```bash
   pkill -f "kubectl port-forward"
   ```

## Verification
Check that External Secrets can sync:

```bash
kubectl get externalsecrets -n student-api
```

Both `flask-app-secret` and `postgres-secret` should show `STATUS: SecretSynced` and `READY: True`.

## Security Features
- ✅ **Limited Privileges**: Token only has read access to `secret/data/*`
- ✅ **TTL**: Token expires after 24 hours
- ✅ **No Git Exposure**: Token never stored in version control
- ✅ **Policy-Based**: Uses `external-secrets-policy` with minimal permissions

## Troubleshooting
If secrets fail to sync:

1. Check the ClusterSecretStore status:
   ```bash
   kubectl describe clustersecretstore vault-backend
   ```

2. Check External Secrets Operator logs:
   ```bash
   kubectl logs -n external-secrets deployment/external-secrets
   ```

3. Recreate the token using the setup script above.