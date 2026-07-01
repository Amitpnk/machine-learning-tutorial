import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc


def plot_confusion_matrix(y_true, y_pred, labels=None, figsize=(6, 5)):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    return fig


def plot_roc_curve(y_true, y_scores, label="Model", figsize=(6, 5)):
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(fpr, tpr, label=f"{label} (AUC = {roc_auc:.3f})")
    ax.plot([0, 1], [0, 1], "k--", label="Random")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_feature_importance(model, feature_names, top_n=20, figsize=(8, 6)):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1][:top_n]
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(range(top_n), importances[indices][::-1], align="center")
    ax.set_yticks(range(top_n))
    ax.set_yticklabels([feature_names[i] for i in indices[::-1]])
    ax.set_title(f"Top {top_n} Feature Importances")
    ax.set_xlabel("Importance")
    plt.tight_layout()
    return fig


def plot_learning_curves(train_sizes, train_scores, val_scores, figsize=(8, 5)):
    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)
    val_mean = val_scores.mean(axis=1)
    val_std = val_scores.std(axis=1)

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(train_sizes, train_mean, label="Train")
    ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2)
    ax.plot(train_sizes, val_mean, label="Validation")
    ax.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.2)
    ax.set_xlabel("Training Size")
    ax.set_ylabel("Score")
    ax.set_title("Learning Curves")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_training_history(history, metrics=("loss", "accuracy"), figsize=(12, 4)):
    n = len(metrics)
    fig, axes = plt.subplots(1, n, figsize=figsize)
    if n == 1:
        axes = [axes]
    for ax, metric in zip(axes, metrics):
        ax.plot(history.history[metric], label="Train")
        val_key = f"val_{metric}"
        if val_key in history.history:
            ax.plot(history.history[val_key], label="Validation")
        ax.set_title(metric.capitalize())
        ax.set_xlabel("Epoch")
        ax.legend()
    plt.tight_layout()
    return fig
