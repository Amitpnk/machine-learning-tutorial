# Machine Learning Course Syllabus

**Course Title:** Machine Learning: From Foundations to Production  
**Duration:** 12 Weeks (48 Hours)  
**Level:** Intermediate  
**Prerequisites:** Basic Python, Linear Algebra, Statistics fundamentals

---

## Course Overview

This course provides a comprehensive, hands-on journey through Machine Learning — covering core algorithms, model evaluation, deep learning, and real-world deployment. By the end, students will be equipped to build, evaluate, and deploy ML systems in production environments.

---

## Learning Outcomes

By the end of this course, students will be able to:

- Understand the mathematical foundations underpinning ML algorithms
- Implement supervised, unsupervised, and reinforcement learning models
- Build and train neural networks using modern frameworks
- Evaluate and tune models for production-grade performance
- Deploy ML models using cloud platforms (AWS, Azure, GCP)
- Apply MLOps practices for model lifecycle management

---

## Module 1: Foundations of Machine Learning (Week 1–2)

### Week 1 — Introduction & Math Refresher

**Topics:**
- What is Machine Learning? Types: Supervised, Unsupervised, Reinforcement Learning
- ML vs AI vs Deep Learning — the landscape
- The ML pipeline: Data → Model → Evaluation → Deployment
- Python ecosystem: NumPy, Pandas, Matplotlib, Scikit-learn

**Math Refresher:**
- Linear Algebra: Vectors, Matrices, Dot products, Eigenvalues
- Calculus: Derivatives, Partial derivatives, Chain rule
- Probability & Statistics: Distributions, Bayes' Theorem, Expectation

**Hands-on Lab:**
- Setting up the ML environment (Jupyter, Conda, VS Code)
- NumPy & Pandas data manipulation exercises

---

### Week 2 — Data Preprocessing & EDA

**Topics:**
- Exploratory Data Analysis (EDA) techniques
- Handling missing values, outliers, duplicates
- Feature scaling: Normalization vs Standardization
- Encoding categorical variables: Label, One-Hot, Target Encoding
- Train/Validation/Test split strategies
- Cross-validation: K-Fold, Stratified K-Fold

**Hands-on Lab:**
- EDA on real-world dataset (Titanic / House Prices)
- Building a preprocessing pipeline with Scikit-learn

---

## Module 2: Supervised Learning (Week 3–5)

### Week 3 — Regression Algorithms

**Topics:**
- Linear Regression: Gradient Descent, Cost Function (MSE)
- Polynomial Regression
- Ridge (L2) and Lasso (L1) Regularization
- ElasticNet Regression
- Evaluation metrics: MAE, MSE, RMSE, R²

**Hands-on Lab:**
- Predict house prices using Linear & Ridge Regression
- Visualizing regularization effects

---

### Week 4 — Classification Algorithms

**Topics:**
- Logistic Regression: Sigmoid, Log Loss
- Decision Trees: Gini Impurity, Entropy, Pruning
- K-Nearest Neighbors (KNN)
- Support Vector Machines (SVM): Kernels, Margin
- Naive Bayes Classifier
- Evaluation metrics: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix

**Hands-on Lab:**
- Spam email classification
- ROC curve comparison across classifiers

---

### Week 5 — Ensemble Methods

**Topics:**
- Bagging: Random Forest
- Boosting: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost
- Stacking and Blending
- Feature Importance
- Hyperparameter Tuning: GridSearchCV, RandomizedSearchCV, Optuna

**Hands-on Lab:**
- Kaggle-style competition — credit risk prediction
- XGBoost vs LightGBM benchmarking

---

## Module 3: Unsupervised Learning (Week 6)

### Week 6 — Clustering & Dimensionality Reduction

**Clustering:**
- K-Means: Elbow Method, Silhouette Score
- DBSCAN: Density-based clustering
- Hierarchical Clustering: Dendrograms
- Gaussian Mixture Models (GMM)

**Dimensionality Reduction:**
- Principal Component Analysis (PCA)
- t-SNE and UMAP for visualization
- Autoencoders (intro)

**Anomaly Detection:**
- Isolation Forest
- One-Class SVM

**Hands-on Lab:**
- Customer segmentation with K-Means
- Visualizing high-dimensional data with t-SNE

---

## Module 4: Deep Learning (Week 7–9)

### Week 7 — Neural Networks Fundamentals

**Topics:**
- Biological inspiration vs Artificial Neurons
- Perceptron and Multi-Layer Perceptron (MLP)
- Activation functions: ReLU, Sigmoid, Tanh, Softmax, GELU
- Forward propagation and Backpropagation (derivation)
- Loss functions: Binary CE, Categorical CE, MSE
- Optimizers: SGD, Momentum, RMSProp, Adam, AdamW
- Batch Normalization, Dropout, Weight Initialization

**Frameworks:**
- TensorFlow / Keras
- PyTorch

**Hands-on Lab:**
- Build an MLP from scratch with NumPy
- MNIST digit classification with Keras

---

### Week 8 — Convolutional Neural Networks (CNNs)

**Topics:**
- Convolution operation, Filters, Feature Maps
- Pooling layers: Max Pooling, Average Pooling
- CNN architectures: LeNet, AlexNet, VGG, ResNet, EfficientNet
- Transfer Learning and Fine-tuning
- Data Augmentation techniques

**Hands-on Lab:**
- Image classification with ResNet (transfer learning)
- Custom CNN for CIFAR-10

---

### Week 9 — Sequence Models & NLP Basics

**Topics:**
- Recurrent Neural Networks (RNN), LSTM, GRU
- Vanishing/Exploding Gradient problem
- Text preprocessing: Tokenization, Stemming, Lemmatization
- Word Embeddings: Word2Vec, GloVe, FastText
- Attention Mechanism
- Transformer architecture overview
- Introduction to BERT and GPT

**Hands-on Lab:**
- Sentiment analysis with LSTM
- Text classification using pre-trained BERT (HuggingFace)

---

## Module 5: Specialized ML Topics (Week 10)

### Week 10 — Reinforcement Learning & Recommender Systems

**Reinforcement Learning:**
- Markov Decision Processes (MDPs)
- Q-Learning and Deep Q-Networks (DQN)
- Policy Gradient Methods
- OpenAI Gym environments

**Recommender Systems:**
- Collaborative Filtering (User-based, Item-based)
- Matrix Factorization (SVD, ALS)
- Content-Based Filtering
- Hybrid Approaches

**Hands-on Lab:**
- Train a DQN agent on CartPole
- Build a movie recommender with collaborative filtering

---

## Module 6: MLOps & Model Deployment (Week 11)

### Week 11 — From Model to Production

**Model Evaluation & Explainability:**
- Bias-Variance Tradeoff
- Learning curves and model diagnostics
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)

**MLOps Fundamentals:**
- Experiment tracking: MLflow, Weights & Biases
- Model versioning and registry
- CI/CD for ML pipelines
- Data versioning with DVC

**Model Deployment:**
- REST API with FastAPI / Flask
- Containerization: Docker
- Serving models: TensorFlow Serving, TorchServe
- Cloud deployment: AWS SageMaker, Azure ML, Google Vertex AI

**Hands-on Lab:**
- Package an ML model as a REST API with FastAPI
- Deploy to AWS SageMaker endpoint

---

## Module 7: Capstone Projects (Week 12)

### Week 12 — End-to-End ML Projects

Students complete one end-to-end project covering:
- Problem framing and dataset selection
- EDA and feature engineering
- Model selection, training, and tuning
- Evaluation and explainability
- Deployment with monitoring

**Suggested Project Ideas:**
1. Real-time Fraud Detection System
2. Medical Image Classification (X-rays / MRI)
3. Customer Churn Prediction Pipeline
4. NLP-based Resume Screening Tool
5. Stock Price Trend Prediction

**Deliverables:**
- GitHub repository with clean code
- Jupyter notebooks with documented analysis
- Deployed API endpoint
- 10-minute demo presentation

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Data | NumPy, Pandas, Matplotlib, Seaborn |
| ML Frameworks | Scikit-learn, XGBoost, LightGBM |
| Deep Learning | TensorFlow/Keras, PyTorch |
| NLP | HuggingFace Transformers, NLTK, SpaCy |
| MLOps | MLflow, DVC, Docker |
| Cloud | AWS SageMaker / Azure ML |
| IDE | Jupyter Lab, VS Code, Google Colab |

---

## Assessment & Grading

| Component | Weight |
|---|---|
| Weekly Quizzes (10 × 2%) | 20% |
| Lab Assignments (6 labs) | 30% |
| Mid-term Project (Week 6) | 20% |
| Capstone Project (Week 12) | 30% |

**Grading Scale:**

| Grade | Score |
|---|---|
| A+ | 90–100% |
| A | 80–89% |
| B | 70–79% |
| C | 60–69% |
| F | Below 60% |

---

## Recommended Resources

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- *Pattern Recognition and Machine Learning* — Christopher Bishop
- *The Hundred-Page Machine Learning Book* — Andriy Burkov

### Online Platforms
- Kaggle (datasets and competitions)
- Papers With Code (latest research)
- HuggingFace Hub (pre-trained models)
- AWS SageMaker Studio Lab (free compute)

### Courses for Reference
- fast.ai — Practical Deep Learning
- Andrew Ng — Machine Learning Specialization (Coursera)
- DeepLearning.AI — Deep Learning Specialization

---

## Course Schedule Summary

| Week | Module | Topic |
|---|---|---|
| 1 | Foundations | Intro to ML + Math Refresher |
| 2 | Foundations | Data Preprocessing & EDA |
| 3 | Supervised | Regression Algorithms |
| 4 | Supervised | Classification Algorithms |
| 5 | Supervised | Ensemble Methods |
| 6 | Unsupervised | Clustering & Dimensionality Reduction |
| 7 | Deep Learning | Neural Network Fundamentals |
| 8 | Deep Learning | CNNs & Transfer Learning |
| 9 | Deep Learning | RNNs, LSTMs & NLP Basics |
| 10 | Specialized | Reinforcement Learning & Recommender Systems |
| 11 | MLOps | Model Deployment & Production |
| 12 | Capstone | End-to-End Project |

---

*Last Updated: June 2026*
