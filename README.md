# Python API with FastAPI

Simple FastAPI application with health checks, configuration management, and structured logging.

## Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your values

# Run
uvicorn main:app --reload

# Test
curl http://localhost:8000/health
```

Interactive docs: http://localhost:8000/docs

## Project Structure

```
.
├── main.py           # FastAPI application
├── config.py         # Configuration management
├── requirements.txt  # Dependencies
├── .env             # Local config (gitignored)
└── .env.example     # Config template
```

## Configuration

| Variable    | Default   | Description            |
| ----------- | --------- | ---------------------- |
| `APP_NAME`  | `API-1`   | Application identifier |
| `LOG_LEVEL` | `DEBUG`   | Logging level          |
| `HOST`      | `0.0.0.0` | Server host            |
| `PORT`      | `8000`    | Server port            |

### Different Environments

```bash
# Local
.env file

# Docker
docker run -e APP_NAME=X -e LOG_LEVEL=INFO ...

# Kubernetes
envFrom:
  - configMapRef:
      name: api-config
```

## API Endpoints

| Endpoint  | Description     |
| --------- | --------------- |
| `/`       | Welcome message |
| `/health` | Health check    |
| `/docs`   | Swagger UI      |
| `/redoc`  | ReDoc           |

## Features

✅ Externalized configuration  
✅ Auto-reload in development  
✅ Structured logging  
✅ Request tracking middleware  
✅ Health checks  
✅ 12-factor app compliant

## Running Options

```bash
# Development (auto-reload)
uvicorn main:app --reload

# With custom config
APP_NAME="Orders-API" uvicorn main:app --reload

# Production (multiple workers)
uvicorn main:app --workers 4

# Direct execution
python main.py
```

## Kubernetes Example

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  APP_NAME: "python-api"
  LOG_LEVEL: "INFO"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-api
spec:
  template:
    spec:
      containers:
        - name: api
          image: python-api:latest
          envFrom:
            - configMapRef:
                name: api-config
          ports:
            - containerPort: 8000
```

## Troubleshooting

**Port in use**: `lsof -i :8000 && kill -9 <PID>`  
**Missing deps**: `pip install -r requirements.txt`  
**Config issues**: Check `.env` exists and restart server

## Dependencies

- FastAPI 0.109.0
- Uvicorn 0.27.0
- python-dotenv 1.0.0

**Requirements**: Python 3.8+

---

**Status**: ✅ Production-ready | **Config**: ✅ Externalized | **Logging**: ✅ Structured
EOF
cat README.md
Salida

# Python API with FastAPI

Simple FastAPI application with health checks, configuration management, and structured logging.

## Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your values

# Run
uvicorn main:app --reload

# Test
curl http://localhost:8000/health
```

Interactive docs: http://localhost:8000/docs

## Project Structure

```
.
├── main.py           # FastAPI application
├── config.py         # Configuration management
├── requirements.txt  # Dependencies
├── .env             # Local config (gitignored)
└── .env.example     # Config template
```

## Configuration

| Variable    | Default   | Description            |
| ----------- | --------- | ---------------------- |
| `APP_NAME`  | `API-1`   | Application identifier |
| `LOG_LEVEL` | `DEBUG`   | Logging level          |
| `HOST`      | `0.0.0.0` | Server host            |
| `PORT`      | `8000`    | Server port            |

### Different Environments

```bash
# Local
.env file

# Docker
docker run -e APP_NAME=X -e LOG_LEVEL=INFO ...

# Kubernetes
envFrom:
  - configMapRef:
      name: api-config
```

## API Endpoints

| Endpoint  | Description     |
| --------- | --------------- |
| `/`       | Welcome message |
| `/health` | Health check    |
| `/docs`   | Swagger UI      |
| `/redoc`  | ReDoc           |

## Features

✅ Externalized configuration  
✅ Auto-reload in development  
✅ Structured logging  
✅ Request tracking middleware  
✅ Health checks  
✅ 12-factor app compliant

## Running Options

```bash
# Development (auto-reload)
uvicorn main:app --reload

# With custom config
APP_NAME="Orders-API" uvicorn main:app --reload

# Production (multiple workers)
uvicorn main:app --workers 4

# Direct execution
python main.py
```

## Kubernetes Example

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  APP_NAME: "python-api"
  LOG_LEVEL: "INFO"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-api
spec:
  template:
    spec:
      containers:
        - name: api
          image: python-api:latest
          envFrom:
            - configMapRef:
                name: api-config
          ports:
            - containerPort: 8000
```

## Troubleshooting

**Port in use**: `lsof -i :8000 && kill -9 <PID>`  
**Missing deps**: `pip install -r requirements.txt`  
**Config issues**: Check `.env` exists and restart server

## Dependencies

- FastAPI 0.109.0
- Uvicorn 0.27.0
- python-dotenv 1.0.0

**Requirements**: Python 3.8+

---

**Status**: ✅ Production-ready | **Config**: ✅ Externalized | **Logging**: ✅ Structured
