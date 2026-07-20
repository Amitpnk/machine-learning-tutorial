# Machine Learning Course Syllabus

**Course Title:** Machine Learning: From Foundations to Production + Generative AI  
**Duration:** 14 Weeks (56 Hours)  
**Prerequisites:** Basic Python, Git basics, familiarity with statistics concepts

---

## Course Objectives

By the end of this course, students will be able to:

- Build end-to-end ML systems using industry-standard tools and frameworks
- Understand mathematical foundations underpinning ML algorithms
- Implement supervised, unsupervised, and deep learning models
- Build generative models (diffusion, GANs) for images and text
- Build, evaluate, and deploy LLM, RAG, and agentic Generative AI applications
- Develop production-ready ML/LLM pipelines with MLOps and LLMOps best practices
- Apply CI/CD, monitoring, safety, and cloud deployment strategies for ML systems


---

## Module 1: Python & Development Environment
### Week 1 — Python for Machine Learning

**Topics:**
- What is Machine Learning? Types: Supervised, Unsupervised, Reinforcement Learning
- ML vs AI vs Deep Learning vs Generative AI — the landscape
- Python refresher: data types, functions, OOP, list comprehensions
- NumPy: arrays, broadcasting, vectorized operations
- Pandas: DataFrames, merging, groupby, time series handling (with a note on Polars for large data)
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

## Module 9: Computer Vision & Generative Vision
### Week 9 — CNNs, Transfer Learning & Image Generation

**Topics:**
- Convolution operation: filters, feature maps, receptive field
- Pooling layers: Max Pooling, Average Pooling
- CNN architectures: LeNet, AlexNet, VGG, ResNet, EfficientNet
- YOLO: introduction to real-time object detection
- Image Segmentation: semantic vs. instance segmentation (intro)
- OCR basics: Optical Character Recognition pipeline
- Transfer Learning and Fine-tuning: freezing layers, custom heads
- Data Augmentation: flipping, rotation, cropping, color jitter

**Generative Vision (intro):**
- Autoencoders and Variational Autoencoders (VAEs)
- GANs: generator/discriminator, training dynamics, common failure modes
- Diffusion Models: forward/reverse process, latent diffusion, how Stable Diffusion works
- Text-to-image pipelines with the Diffusers library

**Hands-on Lab:**
- Image classification with ResNet (transfer learning on custom dataset)
- Object detection introduction with a pre-trained YOLO model
- Generate images with a pre-trained Stable Diffusion model (Diffusers)

---

## Module 10: NLP Fundamentals & Transformers
### Week 10 — From Embeddings to Transformers

**NLP Fundamentals:**
- Text preprocessing: Tokenization (subword / BPE), Stemming, Lemmatization
- Word Embeddings: Word2Vec, GloVe, FastText
- Sequence Models: RNN, LSTM, GRU
- Vanishing/Exploding Gradient problem

**Transformers:**
- Attention Mechanism: self-attention, multi-head attention
- Transformer architecture: encoder, decoder, positional encoding
- Model families and when to use each:
  - Encoder-only (BERT) — understanding/classification
  - Decoder-only (GPT-style) — generation
  - Encoder-decoder (T5) — sequence-to-sequence
- Fine-tuning BERT for downstream NLP tasks

**Hands-on Lab:**
- Sentiment analysis with LSTM
- Text classification using pre-trained BERT (HuggingFace Transformers)

---

## Module 11: LLMs, RAG & Agentic AI
### Week 11 — Building Generative AI Applications

**LLM Foundations:**
- How decoder-only LLMs work: pretraining, tokenization, context windows
- Sampling controls: temperature, top-p, max tokens
- Prompt Engineering: zero-shot, few-shot, chain-of-thought
- Structured outputs (JSON) and function/tool calling
- Open vs. closed models: Claude / GPT / Gemini APIs vs. Llama / Mistral (run locally with Ollama or vLLM)

**Fine-tuning & Alignment:**
- Full fine-tuning vs. Parameter-Efficient Fine-Tuning (PEFT): LoRA, QLoRA
- Instruction tuning; alignment with RLHF and DPO (overview)
- Decision framework: Prompting vs. RAG vs. Fine-tuning — when to use which

**Retrieval-Augmented Generation (RAG):**
- Embeddings and semantic search
- Vector Databases: FAISS, ChromaDB, pgvector, Qdrant, Pinecone
- RAG pipeline: chunking, retrieval, reranking, generation
- Advanced RAG: hybrid search, rerankers, GraphRAG, agentic RAG

**Agentic AI:**
- Tool use and the ReAct loop
- Agent orchestration with LangGraph; multi-agent patterns
- Model Context Protocol (MCP): connecting agents to tools and data

**Hands-on Lab:**
- Build a PDF chatbot using RAG (LangChain / LlamaIndex + FAISS)
- Build a tool-using agent with LangGraph
- Fine-tune a small open model with LoRA/QLoRA

---

## Module 12: Time Series & Recommender Systems
### Week 12 — Forecasting & Recommendations

**Time Series Forecasting:**
- Time series components: trend, seasonality, noise
- ARIMA and SARIMA models
- Prophet: forecasting library for business data
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

## Module 13: MLOps, LLMOps & Model Deployment
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

**LLMOps & GenAI in Production:**
- LLM evaluation: LLM-as-judge, RAGAS, faithfulness/groundedness, hallucination detection
- Observability & tracing: LangSmith / Langfuse, prompt and trace logging
- Prompt versioning, token & cost management, caching, streaming
- LLM serving: vLLM, Text Generation Inference
- Safety & guardrails: prompt injection, PII handling, output validation

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
- Set up MLflow experiment tracking and a RAGAS evaluation run for a RAG app

---

## Module 14: Capstone Project
### Week 14 — End-to-End Production ML / GenAI Project

Students complete one full end-to-end project covering:

- Problem framing and dataset selection
- Data collection, cleaning, and feature engineering
- Model selection, training, evaluation, and tuning
- Explainability (SHAP/LIME) or LLM evaluation (RAGAS/LLM-as-judge)
- MLOps/LLMOps pipeline: experiment tracking, versioning, CI/CD
- Deployment: REST API + cloud endpoint
- Monitoring: data/concept drift, performance, and (for GenAI) safety tracking

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
| GenAI | Agentic RAG Assistant (LangGraph + Vector DB) |
| GenAI | Fine-tuned Domain Chatbot (LoRA) with evaluation harness |
| Computer Vision | Object Detection Pipeline |
| Generative Vision | Text-to-Image or Image Editing App (Diffusion) |

**Deliverables:**
- GitHub Repository with clean, documented code
- Jupyter notebooks covering EDA and modeling
- Deployed API endpoint (AWS / Azure / local Docker)
- Architecture diagram
- Evaluation report (metrics or LLM/RAG eval results)
- 10-minute demo presentation with slides

---

## Elective Module (Optional): Reinforcement Learning
### RL Fundamentals & Deep RL

> Offered as an optional/self-paced module. RLHF and DPO (Module 11) build directly on these ideas, so this module is recommended for students going deeper into alignment.

**Topics:**
- Markov Decision Processes (MDPs): states, actions, rewards, transitions
- Bellman Equation and value functions
- Q-Learning: tabular Q-table approach
- Deep Q-Networks (DQN): neural network as Q-function approximator
- Policy Gradient Methods: REINFORCE algorithm
- Actor-Critic methods (overview)
- Connection to LLMs: how RLHF uses these methods to align models
- Gymnasium (formerly OpenAI Gym): environment setup and agent interaction

**Hands-on Lab:**
- Train a Q-Learning agent on a simple gridworld
- Train a DQN agent on CartPole with PyTorch
- Visualize reward curves and training stability

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.11+ |
| Data | NumPy, Pandas, Polars, Matplotlib, Seaborn |
| ML Frameworks | Scikit-learn, XGBoost, LightGBM, CatBoost |
| Deep Learning | TensorFlow / Keras, PyTorch |
| Generative Models | Diffusers (Stable Diffusion), PyTorch |
| NLP & LLMs | HuggingFace Transformers, LangChain, LangGraph, LlamaIndex, Ollama, vLLM |
| Vector Databases | FAISS, ChromaDB, pgvector, Qdrant, Pinecone |
| LLMOps & Eval | RAGAS, LangSmith / Langfuse |
| Computer Vision | OpenCV, torchvision, YOLO |
| Time Series | Prophet, statsmodels |
| MLOps | MLflow, DVC, GitHub Actions |
| Deployment | FastAPI, Flask, Docker, TensorFlow Serving, TorchServe |
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
| 9 | Module 9 | Computer & Generative Vision | CNN, ResNet, YOLO, GAN, Diffusion |
| 10 | Module 10 | NLP & Transformers | RNN/LSTM, Attention, BERT, GPT/T5 |
| 11 | Module 11 | LLMs, RAG & Agentic AI | Prompting, LoRA, RAG, LangGraph, MCP |
| 12 | Module 12 | Time Series & Recommenders | ARIMA, Prophet, Collaborative Filtering |
| 13 | Module 13 | MLOps, LLMOps & Deployment | MLflow, Docker, FastAPI, RAGAS, SageMaker |
| 14 | Module 14 | Capstone Project | End-to-End Production Project |
| — | Elective | Reinforcement Learning | Q-Learning, DQN, Policy Gradient |

---

## Recommended Resources

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- *Pattern Recognition and Machine Learning* — Christopher Bishop
- *The Hundred-Page Machine Learning Book* — Andriy Burkov
- *Natural Language Processing with Transformers* — Tunstall, von Werra & Wolf
- *Build a Large Language Model (From Scratch)* — Sebastian Raschka

### Online Platforms
- Kaggle (datasets, notebooks, competitions)
- HuggingFace Hub (pre-trained models and datasets)
- Papers With Code (state-of-the-art benchmarks)
- AWS SageMaker Studio Lab (free GPU compute)
- Google Colab (free notebook environment)

### Courses & Docs for Reference
- fast.ai — Practical Deep Learning for Coders
- Andrew Ng — Machine Learning Specialization (Coursera)
- DeepLearning.AI — Deep Learning Specialization & GenAI short courses (RAG, LangChain, Fine-tuning)
- LangChain / LangGraph documentation and cookbooks
- Model provider docs (Anthropic, OpenAI, Google) for prompting, tool use, and structured outputs

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

## Final Outcome

Students graduating from this course will be capable of designing, developing, evaluating, deploying, monitoring, and maintaining modern **Machine Learning** and **Generative AI** applications — production-ready and industry-relevant.
