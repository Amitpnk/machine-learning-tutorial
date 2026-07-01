import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ML Model API", version="1.0")

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.joblib")
model = None


@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model not found at {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)


class PredictRequest(BaseModel):
    features: list[float]


class PredictResponse(BaseModel):
    prediction: float | int | str
    probability: float | None = None


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    X = np.array(request.features).reshape(1, -1)
    prediction = model.predict(X)[0]
    probability = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)[0]
        probability = float(proba.max())
    return PredictResponse(prediction=prediction, probability=probability)
