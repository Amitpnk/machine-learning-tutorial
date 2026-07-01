# Datasets

Data files are **not committed** to this repo (see `.gitignore`). Use the download script below.

## Download All Datasets

```bash
python datasets/download_datasets.py
```

This will populate `datasets/raw/` with all required files for the course.

## Dataset Index

| Module | Dataset | Source | Size |
|--------|---------|--------|------|
| M1, M3 | Titanic | [Kaggle](https://www.kaggle.com/c/titanic) | ~60 KB |
| M4 | California Housing | scikit-learn built-in | ~1 MB |
| M5 | SMS Spam Collection | [UCI ML Repo](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) | ~500 KB |
| M5 | Credit Card Fraud | [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) | ~150 MB |
| M6 | Credit Risk (German) | [UCI ML Repo](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) | ~100 KB |
| M7 | Mall Customers | [Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python) | ~4 KB |
| M7 | MNIST | torchvision / keras built-in | ~11 MB |
| M9 | CIFAR-10 | torchvision built-in | ~163 MB |
| M10 | IMDB Sentiment | HuggingFace datasets | ~84 MB |
| M11 | MovieLens 100K | [GroupLens](https://grouplens.org/datasets/movielens/100k/) | ~5 MB |
| M11 | AirPassengers | statsmodels built-in | ~1 KB |
| M12 | CartPole-v1 | gymnasium built-in | — |

## Manual Downloads (Kaggle API Required)

For Kaggle datasets, first [set up your API key](https://www.kaggle.com/docs/api):

```bash
# Install Kaggle CLI
pip install kaggle

# Place kaggle.json in ~/.kaggle/
kaggle competitions download -c titanic -p datasets/raw/titanic/
kaggle datasets download -d mlg-ulb/creditcardfraud -p datasets/raw/creditcard/
```

## License Notes

- Titanic: Kaggle competition data
- MNIST, CIFAR-10: Yann LeCun / Alex Krizhevsky (free for research use)
- MovieLens 100K: GroupLens Research (non-commercial use)
- All other datasets: check their respective source pages
