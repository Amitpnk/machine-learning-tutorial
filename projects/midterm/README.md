# Mid-term Project

**Due: End of Week 7**

## Objective

Build a complete, end-to-end ML pipeline on a dataset of your choice, applying everything from Modules 1–6.

## Requirements

Your submission must include all of the following:

### 1. Data Pipeline
- [ ] Load a real-world dataset (not a toy dataset)
- [ ] Perform thorough EDA with at least 5 visualizations
- [ ] Handle missing values, outliers, and encoding
- [ ] Build a reusable Scikit-learn preprocessing pipeline

### 2. Modeling
- [ ] Train at least **3 different model types** (e.g., Logistic Regression, Random Forest, XGBoost)
- [ ] Justify your choice of evaluation metric for the problem
- [ ] Compare models using cross-validation (minimum 5-fold)
- [ ] Tune hyperparameters on the best model using Optuna or GridSearchCV

### 3. Evaluation
- [ ] Report final metrics on a held-out test set
- [ ] Plot confusion matrix (classification) or residuals (regression)
- [ ] Interpret feature importances or coefficients

### 4. Code Quality
- [ ] Notebook runs top to bottom without errors (`Restart & Run All`)
- [ ] Each section has a markdown header and a brief explanation
- [ ] No hardcoded paths — use relative paths from project root

## Suggested Datasets

| Dataset | Task | Source |
|---------|------|--------|
| Titanic | Binary Classification | Kaggle |
| House Prices | Regression | Kaggle |
| Heart Disease | Binary Classification | UCI ML Repo |
| Adult Income | Binary Classification | UCI ML Repo |
| Bike Sharing | Regression | UCI ML Repo |

## Submission

1. Push your completed notebook to your GitHub fork
2. Open a Pull Request with title: `[Midterm] Your Name — Dataset Name`
3. Include a 3-sentence summary in the PR description: dataset, best model, final metric

## Grading (100 pts)

| Component | Points |
|-----------|--------|
| EDA & Data Pipeline | 25 |
| Model Training & Comparison | 30 |
| Hyperparameter Tuning | 15 |
| Evaluation & Interpretation | 20 |
| Code Quality & Documentation | 10 |
