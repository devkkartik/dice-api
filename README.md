# 🎲 Dice API

A simple Python Web API built with [FastAPI](https://fastapi.tiangolo.com/) that simulates rolling a dice.

## 🚀 Features

- Exposes a single endpoint `/roll`
- Returns a random integer between 1 and 6

---

## 📦 Installation & Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/devkkartik/dice-api.git
cd dice-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

---

## 🐳 Run with Docker

### 1. Build image

```bash
docker build -t dice-api:latest .
```

### 2. Run container

```bash
docker run -d -p 8000:8000 --name dice-api-container dice-api:latest
```

### 3. Test API

```bash
curl http://localhost:8000/roll
```

---

## 🚀 Deploy on Kubernetes (Minikube)

### 1. Start Minikube

```bash
minikube start --driver=docker
```

### 2. Build and load Docker image into Minikube

```bash
docker build -t dice-api:latest .
minikube image load dice-api:latest
```

### 3. Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 4. Verify pods

```bash
kubectl get pods
```

### 5. Access service

```bash
minikube service dice-api-service --url
```

### 6. Test API

```bash
curl http://<URL_FROM_ABOVE>/roll
```
