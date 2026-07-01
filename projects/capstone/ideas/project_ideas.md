# Capstone Project Ideas

## 1. Real-time Fraud Detection System
**Domain:** Finance  
**Type:** Binary Classification  
**Dataset:** [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) (Kaggle)  
**Key challenges:** Extreme class imbalance (0.17% fraud), latency requirements for real-time scoring  
**Suggested stack:** XGBoost + SMOTE + FastAPI + Docker + SageMaker endpoint  

## 2. Customer Churn Prediction Pipeline
**Domain:** Business / Telecom  
**Type:** Binary Classification  
**Dataset:** [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn) (Kaggle)  
**Key challenges:** Interpretability for business stakeholders (SHAP is critical here)  
**Suggested stack:** LightGBM + SHAP + MLflow + FastAPI  

## 3. Stock / Sales Forecasting
**Domain:** Finance / Retail  
**Type:** Time Series Forecasting  
**Dataset:** Yahoo Finance API or [Store Sales](https://www.kaggle.com/c/store-sales-time-series-forecasting) (Kaggle)  
**Key challenges:** Multiple seasonality, external regressors, confidence intervals  
**Suggested stack:** Prophet + LSTM + FastAPI  

## 4. NLP Resume Screening Tool
**Domain:** HR Tech  
**Type:** Multi-class Classification + NLP  
**Dataset:** [Resume Dataset](https://www.kaggle.com/gauravduttakiit/resume-dataset) (Kaggle)  
**Key challenges:** Text preprocessing, class imbalance across job categories  
**Suggested stack:** BERT (HuggingFace) fine-tuning + FastAPI  

## 5. Medical Image Classification
**Domain:** Healthcare  
**Type:** Image Classification  
**Dataset:** [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) (Kaggle)  
**Key challenges:** Small dataset, need for high recall (medical context), model trust  
**Suggested stack:** ResNet50 transfer learning + Grad-CAM explainability + FastAPI  

## 6. Recommendation Engine
**Domain:** Retail / Media  
**Type:** Collaborative Filtering + Content-Based  
**Dataset:** [MovieLens](https://grouplens.org/datasets/movielens/) or Amazon Product Reviews  
**Key challenges:** Cold start problem, scalability  
**Suggested stack:** Matrix Factorization (ALS) + Hybrid model + FastAPI  

## 7. Plant Disease Detection (CNN)
**Domain:** Agriculture  
**Type:** Image Classification  
**Dataset:** [PlantVillage](https://www.kaggle.com/emmarex/plantdisease) (Kaggle) — 38 classes  
**Key challenges:** Multi-class imbalance, real-world image quality variation  
**Suggested stack:** EfficientNet + transfer learning + Docker + FastAPI  

## 8. OCR / PDF Question Answering
**Domain:** Document AI  
**Type:** GenAI / RAG  
**Dataset:** Your own PDF collection  
**Key challenges:** Chunking strategy, retrieval quality, hallucination  
**Suggested stack:** LangChain + FAISS + OpenAI / open-source LLM + FastAPI  

## 9. RAG Chatbot
**Domain:** GenAI  
**Type:** RAG + LLM  
**Dataset:** Company docs, Wikipedia subset, or course PDFs  
**Key challenges:** Chunking, embedding quality, context window management  
**Suggested stack:** LangChain + ChromaDB + GPT-4o-mini / Llama 3 + Streamlit + Docker  

## 10. Object Detection Pipeline
**Domain:** Computer Vision  
**Type:** Object Detection  
**Dataset:** [Open Images](https://storage.googleapis.com/openimages/web/index.html) or custom labeled set  
**Key challenges:** Labeling effort, inference speed, mAP tuning  
**Suggested stack:** YOLOv8 (ultralytics) + FastAPI + Docker  
