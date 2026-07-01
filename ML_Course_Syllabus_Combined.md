# Machine Learning: From Foundations to Production + Generative AI

**Course Title:** Machine Learning: From Foundations to Production + Generative AI  
**Duration:** 14 Weeks (56 Hours)  
**Level:** Intermediate (College Students / Working Professionals)  
**Prerequisites:** Basic Python, Git basics, familiarity with statistics concepts

---

## Course Objectives

By the end of this course, students will be able to:

- Build end-to-end ML systems using industry-standard tools and frameworks
- Understand mathematical foundations underpinning ML algorithms
- Implement supervised, unsupervised, deep learning, and reinforcement learning models
- Develop production-ready ML pipelines with MLOps best practices
- Build and deploy LLM and RAG-based Generative AI applications
- Apply CI/CD, monitoring, and cloud deployment strategies for ML systems

---

## Assessment & Grading

| Component | Weight |
|---|---|
| Weekly Quizzes | 20% |
| Lab Assignments | 30% |
| Mid-term Project (Week 7) | 20% |
| Final Capstone Project (Week 14) | 30% |

| Grade | Score |
|---|---|
| A+ | 90–100% |
| A | 80–89% |
| B | 70–79% |
| C | 60–69% |
| F | Below 60% |

---

## Module 1: Python & Development Environment
### Week 1 — Python for Machine Learning

**Topics:**
- Python refresher: data types, functions, OOP, list comprehensions
- NumPy: arrays, broadcasting, vectorized operations
- Pandas: DataFrames, merging, groupby, time series handling
- Matplotlib & Seaborn: plotting and visualization
- Scikit-learn: overview of the ML API (fit, transform, predict)
- Jupyter Notebook and VS Code setup
- Git & GitHub basics: clone, commit, push, pull requests

**Hands-on Lab:**
- Data analysis using Pandas on a real-world dataset
- Visualization exercise with Matplotlib and Seaborn

---

## Module 2: Mathematics & Statistics for ML
### Week 2 — Math Refresher

**Linear Algebra:**
- Vectors, Matrices, Dot products
- Matrix multiplication and Eigenvalues
- Importance in ML: weights, transformations, PCA

**Calculus:**
- Derivatives and partial derivatives
- Gradient Descent intuition and derivation
- Chain Rule (used in backpropagation)

**Statistics:**
- Probability fundamentals
- Bayes' Theorem and Naive Bayes connection
- Distributions: Normal, Binomial, Poisson
- Hypothesis Testing, p-value, confidence intervals

**Hands-on Lab:**
- Implement gradient descent from scratch in NumPy
- Statistical analysis and hypothesis testing on a sample dataset

---

## Module 3: Data Engineering & Exploratory Data Analysis
### Week 3 — Data Collection, Cleaning & EDA

**Data Collection:**
- Reading data: CSV, Excel, JSON, SQL databases
- Fetching data from APIs (REST, JSON responses)
- Web scraping overview (BeautifulSoup, requests)

**Data Cleaning:**
- Handling missing values: imputation strategies (mean, median, KNN, model-based)
- Detecting and treating outliers (IQR, Z-score)
- Deduplication and inconsistent formatting
- Feature scaling: Normalization vs. Standardization
- Encoding categorical variables: Label, One-Hot, Target, Binary Encoding

**Exploratory Data Analysis (EDA):**
- Univariate and bivariate visualization
- Correlation heatmaps and pair plots
- Feature engineering fundamentals
- Data leakage — what it is and how to avoid it
- Train/Validation/Test split strategies
- Cross-validation: K-Fold, Stratified K-Fold

**Hands-on Lab:**
- Full EDA pipeline on the Titanic dataset
- Build a reusable preprocessing pipeline with Scikit-learn

---

## Module 4: Supervised Learning — Regression
### Week 4 — Regression Algorithms

**Topics:**
- Linear Regression: Gradient Descent, Cost Function (MSE), Normal Equation
- Polynomial Regression: capturing non-linear patterns
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)
- ElasticNet: combining L1 and L2

**Evaluation Metrics:**
- MAE (Mean Absolute Error)
- MSE and RMSE (Root Mean Squared Error)
- R² (Coefficient of Determination)

**Hands-on Lab:**
- Predict house prices using Linear, Ridge, and Lasso Regression
- Visualize regularization effects and coefficient shrinkage
- Polynomial regression on a non-linear dataset

---

## Module 5: Supervised Learning — Classification
### Week 5 — Classification Algorithms

**Topics:**
- Logistic Regression: Sigmoid function, Log Loss, decision boundary
- Decision Trees: Gini Impurity, Entropy, Pruning
- Random Forest: bootstrap aggregation, feature importance
- Support Vector Machines (SVM): kernels, margin, hyperplane
- K-Nearest Neighbors (KNN): distance metrics, choosing k
- Naive Bayes Classifier: Gaussian, Multinomial, Bernoulli

**Evaluation Metrics:**
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix, ROC Curve, AUC

**Handling Imbalanced Data:**
- SMOTE (Synthetic Minority Over-sampling Technique)
- Class Weights in model training
- Oversampling and undersampling strategies

**Hands-on Lab:**
- Spam email classification
- ROC curve comparison across classifiers
- Apply SMOTE on an imbalanced fraud dataset

---

## Module 6: Ensemble Learning & Hyperparameter Tuning
### Week 6 — Ensemble Methods

**Ensemble Techniques:**
- Bagging: variance reduction via parallel learners
- Random Forest: how randomness improves generalization
- Gradient Boosting: sequential error correction
- XGBoost: regularized boosting, GPU support, tree pruning
- LightGBM: leaf-wise growth, fast training on large datasets
- CatBoost: native categorical feature handling
- Stacking and Blending: combining multiple model predictions

**Hyperparameter Tuning:**
- Grid Search (GridSearchCV)
- Random Search (RandomizedSearchCV)
- Optuna: modern Bayesian optimization framework
- Bayesian Optimization fundamentals

**Hands-on Lab:**
- Kaggle-style credit risk prediction competition
- XGBoost vs. LightGBM benchmarking
- Optuna hyperparameter tuning pipeline

> **Mid-term Project assigned at end of Week 6 — due Week 7**

---

## Module 7: Unsupervised Learning
### Week 7 — Clustering & Dimensionality Reduction

**Clustering Algorithms:**
- K-Means: Elbow Method, Silhouette Score
- Hierarchical Clustering: Dendrograms, Agglomerative vs. Divisive
- DBSCAN: density-based, noise handling, no cluster-count needed
- Gaussian Mixture Models (GMM): probabilistic soft clustering

**Dimensionality Reduction:**
- Principal Component Analysis (PCA): variance explained, scree plot
- t-SNE: non-linear visualization for high-dimensional data
- UMAP: faster alternative to t-SNE with global structure preservation

**Anomaly Detection:**
- Isolation Forest: tree-based anomaly scoring
- One-Class SVM: boundary-based outlier detection

**Hands-on Lab:**
- Customer segmentation with K-Means
- Visualizing MNIST with t-SNE and UMAP
- Anomaly detection on a network traffic dataset

> **Mid-term Project due: End-to-end pipeline using Modules 1–6**

---

## Module 8: Deep Learning Fundamentals
### Week 8 — Neural Networks

**Topics:**
- Biological inspiration vs. Artificial Neurons
- Perceptron and Multi-Layer Perceptron (MLP)
- Activation Functions: ReLU, Sigmoid, Tanh, Softmax, GELU
- Forward Propagation and Backpropagation (step-by-step derivation)
- Loss Functions: Binary CE, Categorical CE, MSE, Huber Loss
- Optimizers: SGD, Momentum, RMSProp, Adam, AdamW
- Regularization: Batch Normalization, Dropout, Weight Decay
- Weight Initialization strategies (Xavier, He)

**Frameworks:**
- TensorFlow / Keras: Sequential and Functional API
- PyTorch: tensors, autograd, training loop

**Hands-on Lab:**
- Build an MLP from scratch using NumPy
- MNIST digit classification with Keras
- PyTorch custom training loop exercise

---

## Module 9: Computer Vision
### Week 9 — CNNs & Transfer Learning

**Topics:**
- Convolution operation: filters, feature maps, receptive field
- Pooling layers: Max Pooling, Average Pooling
- CNN architectures: LeNet, AlexNet, VGG, ResNet, EfficientNet
- YOLO: introduction to real-time object detection
- Image Segmentation: semantic vs. instance segmentation (intro)
- OCR basics: Optical Character Recognition pipeline
- Transfer Learning and Fine-tuning: freezing layers, custom heads
- Data Augmentation: flipping, rotation, cropping, color jitter

**Hands-on Lab:**
- Image classification with ResNet (transfer learning on custom dataset)
- Object detection introduction with a pre-trained YOLO model
- Build a custom CNN for CIFAR-10

---

## Module 10: NLP & Generative AI
### Week 10 — Language Models, LLMs & RAG

**NLP Fundamentals:**
- Text preprocessing: Tokenization, Stemming, Lemmatization
- Word Embeddings: Word2Vec, GloVe, FastText
- Sequence Models: RNN, LSTM, GRU
- Vanishing/Exploding Gradient problem
- Attention Mechanism: self-attention, multi-head attention
- Transformer architecture: encoder, decoder, positional encoding
- BERT: pre-training and fine-tuning for NLP tasks

**Generative AI:**
- LLM Fundamentals: how large language models work
- Prompt Engineering: zero-shot, few-shot, chain-of-thought
- Embeddings and semantic search
- Vector Databases: FAISS, ChromaDB, Pinecone
- RAG (Retrieval-Augmented Generation): architecture and pipeline
- AI Agents: tool use, ReAct loops, LangChain agents
- Fine-tuning vs. Prompting: when to use which approach

**Hands-on Lab:**
- Sentiment analysis with LSTM
- Text classification using pre-trained BERT (HuggingFace)
- Build a PDF chatbot using RAG with LangChain + FAISS

---

## Module 11: Time Series & Recommender Systems
### Week 11 — Forecasting & Recommendations

**Time Series Forecasting:**
- Time series components: trend, seasonality, noise
- ARIMA and SARIMA models
- Prophet: Facebook's forecasting library for business data
- LSTM-based time series forecasting
- Evaluation: MAPE, MAE, RMSE on temporal data

**Recommender Systems:**
- Collaborative Filtering: User-based and Item-based
- Content-Based Filtering: feature similarity
- Matrix Factorization: SVD, ALS
- Hybrid Recommender Systems

**Hands-on Lab:**
- Stock/sales forecasting with Prophet and LSTM
- Build a movie recommender with collaborative filtering (MovieLens dataset)

---

## Module 12: Reinforcement Learning
### Week 12 — RL Fundamentals & Deep RL

**Topics:**
- Markov Decision Processes (MDPs): states, actions, rewards, transitions
- Bellman Equation and value functions
- Q-Learning: tabular Q-table approach
- Deep Q-Networks (DQN): neural network as Q-function approximator
- Policy Gradient Methods: REINFORCE algorithm
- Actor-Critic methods (overview)
- OpenAI Gym: environment setup and agent interaction

**Hands-on Lab:**
- Train a Q-Learning agent on a simple gridworld
- Train a DQN agent on CartPole with PyTorch
- Visualize reward curves and training stability

---

## Module 13: MLOps & Model Deployment
### Week 13 — From Model to Production

**Model Explainability:**
- Bias-Variance Tradeoff
- Learning curves and model diagnostics
- SHAP (SHapley Additive exPlanations): global and local feature importance
- LIME (Local Interpretable Model-agnostic Explanations)

**MLOps Fundamentals:**
- Experiment tracking: MLflow (runs, metrics, artifacts, model registry)
- Data versioning: DVC (Data Version Control)
- Model monitoring: data drift, concept drift, performance degradation
- Feature stores: overview and purpose

**CI/CD for ML:**
- CI/CD principles applied to ML pipelines
- GitHub Actions: automated testing and model retraining triggers
- Docker: containerizing ML models and APIs

**Model Deployment:**
- REST API with FastAPI and Flask
- Serving models: TensorFlow Serving, TorchServe
- Cloud deployment:
  - AWS SageMaker: endpoints, batch transform, pipelines
  - Azure ML: managed endpoints, designer
  - Google Vertex AI: model registry, online prediction

**Hands-on Lab:**
- Package a trained model as a FastAPI REST endpoint
- Containerize with Docker and run locally
- Deploy to AWS SageMaker endpoint with monitoring enabled
- Set up MLflow experiment tracking

---

## Module 14: Capstone Project
### Week 14 — End-to-End Production ML Project

Students complete one full end-to-end project covering:

- Problem framing and dataset selection
- Data collection, cleaning, and feature engineering
- Model selection, training, evaluation, and tuning
- Explainability (SHAP/LIME)
- MLOps pipeline: experiment tracking, versioning, CI/CD
- Deployment: REST API + cloud endpoint
- Monitoring: data drift and performance tracking

**Suggested Project Ideas:**

| Domain | Project |
|---|---|
| Finance | Real-time Fraud Detection System |
| Business | Customer Churn Prediction Pipeline |
| Finance | Stock / Sales Forecasting |
| HR Tech | NLP-based Resume Screening Tool |
| Healthcare | Medical Image Classification (X-rays / MRI) |
| Retail | Recommendation Engine |
| Agriculture | Plant Disease Detection (CNN) |
| Document AI | OCR System or PDF Question Answering |
| GenAI | Chatbot using RAG + LangChain |
| Computer Vision | Object Detection Pipeline |

**Deliverables:**
- GitHub Repository with clean, documented code
- Jupyter notebooks covering EDA and modeling
- Deployed API endpoint (AWS / Azure / local Docker)
- Architecture diagram
- 10-minute demo presentation with slides

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Data | NumPy, Pandas, Matplotlib, Seaborn |
| ML Frameworks | Scikit-learn, XGBoost, LightGBM, CatBoost |
| Deep Learning | TensorFlow / Keras, PyTorch |
| NLP & GenAI | HuggingFace Transformers, LangChain, FAISS, ChromaDB |
| Computer Vision | OpenCV, torchvision, YOLO |
| Time Series | Prophet, statsmodels |
| MLOps | MLflow, DVC, GitHub Actions |
| Deployment | FastAPI, Flask, Docker, TensorFlow Serving |
| Cloud | AWS SageMaker, Azure ML, Google Vertex AI |
| Version Control | Git, GitHub |
| IDE | Jupyter Lab, VS Code, Google Colab |

---

## Course Schedule Summary

| Week | Module | Topic | Key Skills |
|---|---|---|---|
| 1 | Module 1 | Python for ML | NumPy, Pandas, Git |
| 2 | Module 2 | Math & Statistics | Linear Algebra, Calculus, Probability |
| 3 | Module 3 | Data Engineering & EDA | Cleaning, Feature Engineering |
| 4 | Module 4 | Regression | Linear, Ridge, Lasso, ElasticNet |
| 5 | Module 5 | Classification | Logistic, SVM, KNN, Naive Bayes |
| 6 | Module 6 | Ensemble Methods | XGBoost, LightGBM, Optuna |
| 7 | Module 7 | Unsupervised Learning | K-Means, PCA, t-SNE, UMAP |
| 8 | Module 8 | Deep Learning | MLP, Backprop, TensorFlow, PyTorch |
| 9 | Module 9 | Computer Vision | CNN, ResNet, YOLO, Transfer Learning |
| 10 | Module 10 | NLP & Generative AI | BERT, Transformers, RAG, LLM Agents |
| 11 | Module 11 | Time Series & Recommenders | ARIMA, Prophet, Collaborative Filtering |
| 12 | Module 12 | Reinforcement Learning | Q-Learning, DQN, Policy Gradient |
| 13 | Module 13 | MLOps & Deployment | MLflow, Docker, FastAPI, SageMaker |
| 14 | Module 14 | Capstone Project | End-to-End Production Project |

---

## Recommended Resources

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- *Pattern Recognition and Machine Learning* — Christopher Bishop
- *The Hundred-Page Machine Learning Book* — Andriy Burkov

### Online Platforms
- Kaggle (datasets, notebooks, competitions)
- HuggingFace Hub (pre-trained models and datasets)
- Papers With Code (state-of-the-art benchmarks)
- AWS SageMaker Studio Lab (free GPU compute)
- Google Colab (free notebook environment)

### Courses for Reference
- fast.ai — Practical Deep Learning for Coders
- Andrew Ng — Machine Learning Specialization (Coursera)
- DeepLearning.AI — Deep Learning Specialization
- LangChain documentation and cookbooks

---

## Final Outcome

Students graduating from this course will be capable of designing, developing, evaluating, deploying, monitoring, and maintaining modern **Machine Learning** and **Generative AI** applications — production-ready and industry-relevant.

---

*Last Updated: July 2026*
