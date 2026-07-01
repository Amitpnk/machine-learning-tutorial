import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer


def make_pipeline(numeric_features, categorical_features, model):
    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])
    return Pipeline([("preprocessor", preprocessor), ("model", model)])


def encode_features(df, target_col, drop_cols=None):
    df = df.copy()
    if drop_cols:
        df = df.drop(columns=drop_cols, errors="ignore")
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df


def detect_outliers_iqr(series):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return (series < lower) | (series > upper)


def summarize_missing(df):
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)
    return pd.DataFrame({"missing": missing, "pct": pct}).query("missing > 0").sort_values("pct", ascending=False)
