# Deployment

This directory contains deployment configurations, containerization files, and infrastructure setup for Browser Agent.

## Contents

### Container Configuration
- **[Dockerfile](Dockerfile)** - Docker container build configuration
- **[docker-compose.yml](docker-compose.yml)** - Multi-container orchestration setup

### Deployment Structure

```
deployment/
├── Dockerfile              # Main application container
├── docker-compose.yml      # Local development stack
├── docker-compose.prod.yml # Production configuration
├── kubernetes/             # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── helm/                   # Helm charts
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── terraform/              # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── scripts/                # Deployment scripts
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

## Docker Deployment

### Building the Container

```bash
# Build the Docker image
docker build -t browser-agent:latest -f deployment/Dockerfile .

# Build with specific tag
docker build -t browser-agent:v1.0.0 -f deployment/Dockerfile .

# Build with build arguments
docker build --build-arg PYTHON_VERSION=3.11 -t browser-agent:latest .
```

### Running with Docker

```bash
# Run single container
docker run -d \
  --name browser-agent \
  -p 8080:8080 \
  -e API_KEY="your-api-key" \
  -v $(pwd)/config:/app/config \
  browser-agent:latest

# Run with environment file
docker run -d \
  --name browser-agent \
  -p 8080:8080 \
  --env-file .env \
  browser-agent:latest

# Run interactively for debugging
docker run -it --rm \
  -p 8080:8080 \
  browser-agent:latest /bin/bash
```

### Docker Compose

#### Development Setup

```bash
# Start development stack
docker-compose -f deployment/docker-compose.yml up -d

# View logs
docker-compose -f deployment/docker-compose.yml logs -f

# Stop stack
docker-compose -f deployment/docker-compose.yml down

# Rebuild and restart
docker-compose -f deployment/docker-compose.yml up --build -d
```

#### Production Setup

```bash
# Start production stack
docker-compose -f deployment/docker-compose.prod.yml up -d

# Scale services
docker-compose -f deployment/docker-compose.prod.yml up -d --scale app=3

# Update services
docker-compose -f deployment/docker-compose.prod.yml pull
docker-compose -f deployment/docker-compose.prod.yml up -d
```

## Container Configuration

### Dockerfile Best Practices

```dockerfile
# Multi-stage build example
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser . /app
WORKDIR /app

# Switch to non-root user
USER appuser

# Set environment variables
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONPATH=/app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Expose port
EXPOSE 8080

# Start application
CMD ["python", "-m", "brouser_agent.main"]
```

### Environment Variables

```bash
# Required environment variables
API_KEY=your-api-key
BROWSER_TYPE=chrome
HEADLESS=true

# Optional environment variables
LOG_LEVEL=INFO
DEBUG=false
PORT=8080
WORKERS=4
TIMEOUT=300

# Database configuration
DATABASE_URL=postgresql://user:pass@db:5432/browser_agent
REDIS_URL=redis://redis:6379/0

# External service configuration
MCP_SERVER_URL=http://mcp-server:8081
WEBHOOK_URL=https://your-webhook-endpoint.com
```

## Kubernetes Deployment

### Basic Deployment

```yaml
# deployment/kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: browser-agent
  labels:
    app: browser-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: browser-agent
  template:
    metadata:
      labels:
        app: browser-agent
    spec:
      containers:
      - name: browser-agent
        image: browser-agent:latest
        ports:
        - containerPort: 8080
        env:
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: browser-agent-secrets
              key: api-key
        - name: BROWSER_TYPE
          value: "chrome"
        - name: HEADLESS
          value: "true"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Service Configuration

```yaml
# deployment/kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: browser-agent-service
spec:
  selector:
    app: browser-agent
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP
```

### Ingress Configuration

```yaml
# deployment/kubernetes/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: browser-agent-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: browser-agent.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: browser-agent-service
            port:
              number: 80
```

### Deploying to Kubernetes

```bash
# Apply all manifests
kubectl apply -f deployment/kubernetes/

# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services

# View logs
kubectl logs -f deployment/browser-agent

# Scale deployment
kubectl scale deployment browser-agent --replicas=5

# Update deployment
kubectl set image deployment/browser-agent browser-agent=browser-agent:v1.1.0

# Rollback deployment
kubectl rollout undo deployment/browser-agent
```

## Helm Charts

### Chart Structure

```
deployment/helm/browser-agent/
├── Chart.yaml
├── values.yaml
├── values-prod.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── _helpers.tpl
```

### Installing with Helm

```bash
# Install chart
helm install browser-agent deployment/helm/browser-agent/

# Install with custom values
helm install browser-agent deployment/helm/browser-agent/ \
  --values deployment/helm/browser-agent/values-prod.yaml

# Upgrade release
helm upgrade browser-agent deployment/helm/browser-agent/

# Uninstall release
helm uninstall browser-agent

# List releases
helm list
```

## Cloud Deployment

### AWS ECS

```json
{
  "family": "browser-agent",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "browser-agent",
      "image": "your-account.dkr.ecr.region.amazonaws.com/browser-agent:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "BROWSER_TYPE",
          "value": "chrome"
        },
        {
          "name": "HEADLESS",
          "value": "true"
        }
      ],
      "secrets": [
        {
          "name": "API_KEY",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:browser-agent-secrets"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/browser-agent",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

### Google Cloud Run

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: browser-agent
  annotations:
    run.googleapis.com/ingress: all
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/maxScale: "10"
        run.googleapis.com/cpu-throttling: "false"
        run.googleapis.com/memory: "1Gi"
        run.googleapis.com/cpu: "1000m"
    spec:
      containerConcurrency: 10
      timeoutSeconds: 300
      containers:
      - image: gcr.io/project-id/browser-agent:latest
        ports:
        - containerPort: 8080
        env:
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: browser-agent-secrets
              key: api-key
        - name: BROWSER_TYPE
          value: chrome
        - name: HEADLESS
          value: "true"
        resources:
          limits:
            memory: 1Gi
            cpu: 1000m
```

### Azure Container Instances

```yaml
apiVersion: 2019-12-01
location: eastus
name: browser-agent
properties:
  containers:
  - name: browser-agent
    properties:
      image: your-registry.azurecr.io/browser-agent:latest
      resources:
        requests:
          cpu: 1.0
          memoryInGb: 1.5
      ports:
      - port: 8080
        protocol: TCP
      environmentVariables:
      - name: BROWSER_TYPE
        value: chrome
      - name: HEADLESS
        value: "true"
      - name: API_KEY
        secureValue: your-api-key
  osType: Linux
  restartPolicy: Always
  ipAddress:
    type: Public
    ports:
    - protocol: TCP
      port: 8080
    dnsNameLabel: browser-agent
```

## Monitoring and Logging

### Health Checks

```python
# Health check endpoint
from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/health')
def health_check():
    """Basic health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'uptime': time.time() - start_time
    })

@app.route('/ready')
def readiness_check():
    """Readiness check for Kubernetes."""
    # Check if application is ready to serve requests
    try:
        # Check database connection
        # Check external dependencies
        return jsonify({'status': 'ready'})
    except Exception as e:
        return jsonify({'status': 'not ready', 'error': str(e)}), 503

@app.route('/metrics')
def metrics():
    """Prometheus-style metrics endpoint."""
    return jsonify({
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent
    })
```

### Logging Configuration

```yaml
# Fluentd configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/containers/browser-agent*.log
      pos_file /var/log/fluentd-containers.log.pos
      tag kubernetes.*
      format json
      time_format %Y-%m-%dT%H:%M:%S.%NZ
    </source>
    
    <match kubernetes.**>
      @type elasticsearch
      host elasticsearch.logging.svc.cluster.local
      port 9200
      index_name browser-agent
    </match>
```

## Security

### Container Security

```dockerfile
# Security best practices in Dockerfile

# Use specific version tags
FROM python:3.11.5-slim

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install security updates
RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Set secure file permissions
COPY --chown=appuser:appuser . /app
RUN chmod -R 755 /app

# Drop privileges
USER appuser

# Use read-only filesystem
# Add to docker run: --read-only --tmpfs /tmp
```

### Secrets Management

```bash
# Kubernetes secrets
kubectl create secret generic browser-agent-secrets \
  --from-literal=api-key="your-api-key" \
  --from-literal=db-password="your-db-password"

# Docker secrets
echo "your-api-key" | docker secret create api_key -

# Use in docker-compose
version: '3.8'
services:
  app:
    image: browser-agent:latest
    secrets:
      - api_key
    environment:
      - API_KEY_FILE=/run/secrets/api_key

secrets:
  api_key:
    external: true
```

## Deployment Scripts

### Automated Deployment

```bash
#!/bin/bash
# deployment/scripts/deploy.sh

set -e

VERSION=${1:-latest}
ENVIRONMENT=${2:-staging}

echo "Deploying Browser Agent v$VERSION to $ENVIRONMENT"

# Build and push image
docker build -t browser-agent:$VERSION .
docker tag browser-agent:$VERSION your-registry/browser-agent:$VERSION
docker push your-registry/browser-agent:$VERSION

# Deploy to Kubernetes
kubectl set image deployment/browser-agent \
  browser-agent=your-registry/browser-agent:$VERSION \
  --namespace=$ENVIRONMENT

# Wait for rollout
kubectl rollout status deployment/browser-agent --namespace=$ENVIRONMENT

# Run health check
./deployment/scripts/health-check.sh $ENVIRONMENT

echo "Deployment complete!"
```

### Rollback Script

```bash
#!/bin/bash
# deployment/scripts/rollback.sh

set -e

ENVIRONMENT=${1:-staging}
REVISION=${2:-1}

echo "Rolling back Browser Agent in $ENVIRONMENT (revision: $REVISION)"

# Rollback deployment
kubectl rollout undo deployment/browser-agent \
  --to-revision=$REVISION \
  --namespace=$ENVIRONMENT

# Wait for rollout
kubectl rollout status deployment/browser-agent --namespace=$ENVIRONMENT

# Run health check
./deployment/scripts/health-check.sh $ENVIRONMENT

echo "Rollback complete!"
```

## Best Practices

1. **Use multi-stage builds** to reduce image size
2. **Run as non-root user** for security
3. **Implement health checks** for monitoring
4. **Use secrets management** for sensitive data
5. **Tag images properly** for version control
6. **Monitor resource usage** and set limits
7. **Implement graceful shutdown** handling
8. **Use read-only filesystems** when possible
9. **Keep images updated** with security patches
10. **Test deployments** in staging environment first

## Troubleshooting

### Common Issues

1. **Container won't start**
   ```bash
   # Check logs
   docker logs container-name
   kubectl logs deployment/browser-agent
   
   # Check resource limits
   kubectl describe pod pod-name
   ```

2. **Health check failures**
   ```bash
   # Test health endpoint
   curl http://localhost:8080/health
   
   # Check application logs
   kubectl logs -f deployment/browser-agent
   ```

3. **Image pull errors**
   ```bash
   # Check image exists
   docker pull your-registry/browser-agent:latest
   
   # Check registry credentials
   kubectl get secrets
   ```

### Getting Help

- Check container logs for error messages
- Verify environment variables and secrets
- Test health endpoints manually
- Review resource limits and requests
- See [../docs/CONTRIBUTING.md](../docs/CONTRIBUTING.md) for development setup
- Open an issue for deployment problems

---

**Production Note:** Always test deployments thoroughly in staging environments before deploying to production.