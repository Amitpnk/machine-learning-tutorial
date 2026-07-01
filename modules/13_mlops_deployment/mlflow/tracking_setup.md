# MLflow Tracking Setup

## Local Server (Development)

```bash
# Start MLflow tracking server
mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --default-artifact-root ./mlruns

# Open UI
open http://localhost:5000
```

## Via Docker Compose

```bash
cd modules/13_mlops_deployment/docker
docker compose up mlflow
```

## In Notebooks / Scripts

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", 0.94)
    mlflow.sklearn.log_model(model, "model")
```

## Model Registry

```python
# Register after logging
mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="fraud-detector"
)

# Load from registry
model = mlflow.sklearn.load_model("models:/fraud-detector/Production")
```
