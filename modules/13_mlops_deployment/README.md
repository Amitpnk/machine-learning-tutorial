# Module 13 — MLOps & Model Deployment

**Week 13 · 4 Hours**

## Learning Objectives

- Explain model decisions with SHAP and LIME
- Track experiments, metrics, and artifacts with MLflow
- Version datasets and models with DVC
- Build a FastAPI REST endpoint for a trained model
- Containerize the API with Docker
- Deploy to AWS SageMaker with monitoring enabled
- Set up CI/CD with GitHub Actions for automated retraining

## Notebooks

| # | Notebook | YouTube Episode |
|---|----------|----------------|
| 01 | [01_model_explainability.ipynb](notebooks/01_model_explainability.ipynb) | Ep 53 — SHAP & LIME Explained |
| 02 | [02_mlflow_tracking.ipynb](notebooks/02_mlflow_tracking.ipynb) | Ep 54 — MLflow Experiment Tracking |
| 03 | [03_fastapi_serving.ipynb](notebooks/03_fastapi_serving.ipynb) | Ep 55 — Serve ML Models with FastAPI |
| 04 | [04_docker_deployment.ipynb](notebooks/04_docker_deployment.ipynb) | Ep 56 — Docker for ML Engineers |
| 05 | [05_sagemaker_deployment.ipynb](notebooks/05_sagemaker_deployment.ipynb) | Ep 57 — Deploy to AWS SageMaker |

## Lab

[lab/lab_deploy_pipeline.ipynb](lab/lab_deploy_pipeline.ipynb) — Package model → FastAPI → Docker → SageMaker endpoint + MLflow tracking

## Additional Files

- [api/main.py](api/main.py) — FastAPI application
- [docker/Dockerfile](docker/Dockerfile) — Container definition
- [docker/docker-compose.yml](docker/docker-compose.yml) — Local orchestration
- [mlflow/tracking_setup.md](mlflow/tracking_setup.md) — MLflow server setup guide

## Key Tools

`mlflow` · `dvc` · `fastapi` · `uvicorn` · `docker` · `boto3` (SageMaker)
