"""
Download all course datasets that can be fetched without a Kaggle API key.
For Kaggle datasets, see datasets/README.md for manual instructions.
"""

import os
import urllib.request
import zipfile
from pathlib import Path

RAW = Path(__file__).parent / "raw"
RAW.mkdir(parents=True, exist_ok=True)


def download(url, dest_path, label):
    if dest_path.exists():
        print(f"  [skip] {label} already exists")
        return
    print(f"  [download] {label}...")
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dest_path)
    print(f"  [done] {label}")


def unzip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_to)
    zip_path.unlink()


def fetch_uci_sms_spam():
    dest = RAW / "sms_spam" / "SMSSpamCollection"
    download(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip",
        RAW / "sms_spam" / "smsspamcollection.zip",
        "SMS Spam Collection",
    )
    if (RAW / "sms_spam" / "smsspamcollection.zip").exists():
        unzip(RAW / "sms_spam" / "smsspamcollection.zip", RAW / "sms_spam")


def fetch_movielens_100k():
    dest = RAW / "movielens" / "ml-100k"
    if dest.exists():
        print("  [skip] MovieLens 100K already exists")
        return
    zip_path = RAW / "movielens" / "ml-100k.zip"
    download(
        "https://files.grouplens.org/datasets/movielens/ml-100k.zip",
        zip_path,
        "MovieLens 100K",
    )
    if zip_path.exists():
        unzip(zip_path, RAW / "movielens")


def fetch_sklearn_datasets():
    from sklearn.datasets import fetch_california_housing, load_iris, load_breast_cancer
    import pandas as pd

    print("  [sklearn] California Housing...")
    housing = fetch_california_housing(as_frame=True)
    out = RAW / "california_housing"
    out.mkdir(exist_ok=True)
    housing.frame.to_csv(out / "california_housing.csv", index=False)

    print("  [sklearn] Iris...")
    iris = load_iris(as_frame=True)
    out = RAW / "iris"
    out.mkdir(exist_ok=True)
    iris.frame.to_csv(out / "iris.csv", index=False)

    print("  [sklearn] Breast Cancer...")
    bc = load_breast_cancer(as_frame=True)
    out = RAW / "breast_cancer"
    out.mkdir(exist_ok=True)
    bc.frame.to_csv(out / "breast_cancer.csv", index=False)

    print("  [done] sklearn built-in datasets")


if __name__ == "__main__":
    print("\nDownloading course datasets...")
    print("\n[1/3] SMS Spam Collection (UCI)")
    fetch_uci_sms_spam()
    print("\n[2/3] MovieLens 100K")
    fetch_movielens_100k()
    print("\n[3/3] Scikit-learn built-in datasets")
    fetch_sklearn_datasets()
    print("\nAll done! Data saved to datasets/raw/")
    print("For Kaggle datasets (Titanic, Credit Card Fraud), see datasets/README.md")
