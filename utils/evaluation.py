import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score,
)


def classification_report_df(y_true, y_pred, average="weighted"):
    return pd.DataFrame({
        "accuracy": [accuracy_score(y_true, y_pred)],
        "precision": [precision_score(y_true, y_pred, average=average, zero_division=0)],
        "recall": [recall_score(y_true, y_pred, average=average, zero_division=0)],
        "f1": [f1_score(y_true, y_pred, average=average, zero_division=0)],
    }).round(4)


def regression_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return pd.DataFrame({"MAE": [mae], "MSE": [mse], "RMSE": [rmse], "R2": [r2]}).round(4)


def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    nonzero = y_true != 0
    return np.mean(np.abs((y_true[nonzero] - y_pred[nonzero]) / y_true[nonzero])) * 100
