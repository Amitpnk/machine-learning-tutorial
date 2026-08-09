# The Complete Machine Learning & Generative AI Engineering Course

**Course Title:** The Complete Machine Learning & Generative AI Engineering Course  
**Duration:** 20 Weeks (80 Hours) core track + optional electives  
**Format:** 4 hours/week — concept walkthrough, live coding, and a graded hands-on lab  
**Prerequisites:** Basic Python, Git basics, familiarity with statistics concepts 

---

## Course Objectives

By the end of this course, students will be able to:

- Build end-to-end ML systems using industry-standard tools and frameworks
- Understand the mathematical foundations underpinning ML algorithms
- Implement supervised, unsupervised, and deep learning models
- Train models efficiently at scale on GPUs (mixed precision, distributed training)
- Build generative models (diffusion, GANs) for images, and understand modern transformer internals
- Adapt foundation models through prompting, context engineering, RAG, and fine-tuning
- Integrate agents with external tools and data using the Model Context Protocol (MCP)
- Work across modalities: text, vision, and speech
- Optimize and serve models efficiently (quantization, distillation, high-throughput inference)
- Develop production-ready ML/LLM pipelines with MLOps and LLMOps best practices
- Evaluate systems for fairness, safety, and regulatory compliance
- Apply CI/CD, monitoring, and cloud deployment strategies for ML systems

---

## Course Structure

| Part | Weeks | Focus |
|---|---|---|
| **Part I — Foundations** | 1–7 | Python, math, data, classical ML |
| **Part II — Deep Learning** | 8–11 | Neural networks, scale, vision, transformers |
| **Part III — Generative AI** | 12–16 | LLMs, fine-tuning, RAG, agents, multimodal |
| **Part IV — Production** | 17–20 | Optimization, MLOps, governance, capstone |

---

# PART I — FOUNDATIONS

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
- Environment management: `uv` / conda, reproducible dependency pinning
- Git & GitHub basics: clone, commit, push, pull requests

**AI-Assisted Development:**
- Using coding agents (Claude Code, Copilot, Cursor) as a learning and productivity tool
- Where they help and where they mislead — verifying generated ML code
- Reading and debugging code you didn't write

**Hands-on Lab:**
- Data analysis using Pandas on a real-world dataset
- Visualization exercise with Matplotlib and Seaborn
- Set up a reproducible project repo with pinned dependencies and pre-commit hooks

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
- Sampling bias and why benchmark numbers mislead

**Hands-on Lab:**
- Implement gradient descent from scratch in NumPy
- Statistical analysis and hypothesis testing on a sample dataset

---

## Module 3: Data Engineering & Exploratory Data Analysis
### Week 3 — Data Collection, Cleaning & EDA

**Data Collection:**
- Reading data: CSV, Excel, JSON, Parquet, SQL databases
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

**Data-Centric AI:**
- Why data quality beats model tweaking — the data-centric shift
- Data validation contracts: Pandera, Great Expectations
- Label quality, annotation error, and inter-annotator agreement
- Synthetic data generation: when it helps, when it poisons your model
- Dataset documentation: datasheets and provenance tracking

**Hands-on Lab:**
- Full EDA pipeline on the Titanic dataset
- Build a reusable preprocessing pipeline with Scikit-learn
- Write a data validation suite that fails CI on schema or distribution drift

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
- Threshold selection and probability calibration (Platt scaling, isotonic)

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
- Why gradient boosting still beats deep learning on tabular data

**Hyperparameter Tuning:**
- Grid Search (GridSearchCV)
- Random Search (RandomizedSearchCV)
- Optuna: modern Bayesian optimization framework
- Bayesian Optimization fundamentals
- Successive halving and Hyperband

**Hands-on Lab:**
- Kaggle-style credit risk prediction competition
- XGBoost vs. LightGBM benchmarking
- Optuna hyperparameter tuning pipeline with pruning

---

## Module 7: Unsupervised Learning
### Week 7 — Clustering & Dimensionality Reduction

**Clustering Algorithms:**
- K-Means: Elbow Method, Silhouette Score
- Hierarchical Clustering: Dendrograms, Agglomerative vs. Divisive
- DBSCAN / HDBSCAN: density-based, noise handling, no cluster-count needed
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

> **Checkpoint Project 1 due: End-to-end classical ML pipeline using Modules 1–7**

---

# PART II — DEEP LEARNING

## Module 8: Deep Learning Fundamentals
### Week 8 — Neural Networks

**Topics:**
- Biological inspiration vs. Artificial Neurons
- Perceptron and Multi-Layer Perceptron (MLP)
- Activation Functions: ReLU, GELU, SiLU/Swish, Sigmoid, Tanh, Softmax
- Forward Propagation and Backpropagation (step-by-step derivation)
- Loss Functions: Binary CE, Categorical CE, MSE, Huber Loss
- Optimizers: SGD, Momentum, RMSProp, Adam, AdamW
- Learning rate schedules: warmup, cosine decay, one-cycle
- Regularization: Batch Norm, Layer Norm / RMSNorm, Dropout, Weight Decay
- Weight Initialization strategies (Xavier, He)

**Frameworks:**
- PyTorch: tensors, autograd, training loop, `nn.Module`
- TensorFlow / Keras: Sequential and Functional API

**Hands-on Lab:**
- Build an MLP from scratch using NumPy (forward + backward pass by hand)
- MNIST digit classification with Keras
- PyTorch custom training loop with LR scheduling

---

## Module 9: Training at Scale & GPU Engineering
### Week 9 — Making Training Fast, Cheap, and Reproducible

> New-generation ML work is bottlenecked by training infrastructure, not by model code. This week covers the difference between a notebook that trains and a pipeline that scales.

**GPU Fundamentals:**
- How GPUs execute deep learning: SMs, warps, memory hierarchy
- VRAM budgeting: parameters vs. gradients vs. optimizer states vs. activations
- Reading `nvidia-smi` and interpreting utilization vs. memory-bound workloads
- Choosing hardware: consumer GPU vs. A100/H100 vs. TPU vs. cloud spot instances

**Efficient Training Techniques:**
- Mixed precision training: FP16, BF16, FP8, and loss scaling
- Gradient accumulation for large effective batch sizes
- Gradient checkpointing: trading compute for memory
- `torch.compile`, kernel fusion, and Flash Attention
- Efficient data loading: `DataLoader` workers, prefetching, memory pinning, WebDataset

**Distributed Training:**
- Data parallelism vs. model parallelism vs. pipeline parallelism
- PyTorch DDP (DistributedDataParallel)
- FSDP (Fully Sharded Data Parallel) and the ZeRO stages
- DeepSpeed and HuggingFace Accelerate
- Multi-GPU and multi-node basics; communication overhead

**Experiment Discipline:**
- Seeding and reproducibility (and why exact reproducibility is often impossible on GPU)
- Profiling with the PyTorch Profiler and identifying bottlenecks
- Experiment tracking with Weights & Biases / MLflow
- Checkpointing, resumption, and fault tolerance

**Hands-on Lab:**
- Profile a slow training loop and make it 3× faster (mixed precision + dataloader fixes)
- Train the same model on 1 GPU vs. multi-GPU with DDP and compare throughput
- Fit a model that doesn't fit in memory using gradient checkpointing + accumulation

---

## Module 10: Computer Vision & Generative Vision
### Week 10 — CNNs, Transfer Learning & Image Generation

**Topics:**
- Convolution operation: filters, feature maps, receptive field
- Pooling layers: Max Pooling, Average Pooling
- CNN architectures: LeNet, AlexNet, VGG, ResNet, EfficientNet
- Vision Transformers (ViT): patches as tokens, CNN vs. ViT tradeoffs
- YOLO: real-time object detection
- Image Segmentation: semantic vs. instance segmentation; Segment Anything (SAM)
- OCR basics: Optical Character Recognition pipeline
- Transfer Learning and Fine-tuning: freezing layers, custom heads
- Data Augmentation: flipping, rotation, cropping, color jitter, MixUp/CutMix
- Self-supervised pretraining: contrastive learning, CLIP

**Generative Vision:**
- Autoencoders and Variational Autoencoders (VAEs)
- GANs: generator/discriminator, training dynamics, common failure modes
- Diffusion Models: forward/reverse process, latent diffusion, how Stable Diffusion works
- Samplers and schedulers; classifier-free guidance
- Conditioning and control: ControlNet, inpainting, image-to-image
- Fine-tuning image models: LoRA and DreamBooth
- Video generation: an overview of the current landscape

**Hands-on Lab:**
- Image classification with ResNet (transfer learning on a custom dataset)
- Object detection with a pre-trained YOLO model
- Generate images with Stable Diffusion (Diffusers) and control output with ControlNet
- Train a LoRA to teach a diffusion model a new subject or style

---

## Module 11: NLP & Transformer Internals
### Week 11 — From Embeddings to Modern Transformers

**NLP Fundamentals:**
- Text preprocessing: Tokenization (BPE, WordPiece, SentencePiece), Stemming, Lemmatization
- Tokenizer economics: why tokenization drives cost, context limits, and multilingual gaps
- Word Embeddings: Word2Vec, GloVe, FastText
- Sequence Models: RNN, LSTM, GRU
- Vanishing/Exploding Gradient problem

**The Transformer:**
- Attention Mechanism: self-attention, multi-head attention, Q/K/V intuition
- Transformer architecture: encoder, decoder, residual streams, layer norm placement
- Positional encoding: absolute, learned, and rotary (RoPE)
- Model families and when to use each:
  - Encoder-only (BERT) — understanding/classification
  - Decoder-only (GPT-style) — generation
  - Encoder-decoder (T5) — sequence-to-sequence

**Modern Transformer Engineering:**
- KV cache: how autoregressive generation actually runs, and why memory grows
- Attention variants: Multi-Query (MQA) and Grouped-Query Attention (GQA)
- Flash Attention: IO-aware exact attention
- Mixture of Experts (MoE): sparse activation, routing, why total ≠ active parameters
- Long-context techniques: position interpolation, sliding window, and the "lost in the middle" problem
- State-space alternatives (Mamba) — an overview
- Scaling laws: how compute, data, and parameters trade off

**Hands-on Lab:**
- Sentiment analysis with LSTM
- Text classification using pre-trained BERT (HuggingFace Transformers)
- Implement single-head self-attention from scratch in NumPy, then a minimal GPT block in PyTorch
- Measure KV cache growth and latency vs. context length on a small local model

---

# PART III — GENERATIVE AI

## Module 12: LLMs, Prompting & Context Engineering
### Week 12 — Working With Foundation Models

**LLM Foundations:**
- How decoder-only LLMs work: pretraining, post-training, tokenization, context windows
- Decoding strategies: greedy, beam search, temperature, top-k, top-p, repetition penalty
- Why LLMs hallucinate: next-token prediction vs. truth
- Open vs. closed models: frontier APIs (Claude, GPT, Gemini) vs. open weights (Llama, Mistral, Qwen, DeepSeek)
- Running models locally with Ollama, LM Studio, and llama.cpp
- Model selection: capability tiers, latency, and cost per task

**Reasoning Models & Test-Time Compute:**
- Reasoning models vs. standard instruct models — what changed
- Extended thinking / reasoning tokens and how they're billed
- Test-time compute scaling: thinking longer instead of training bigger
- Self-consistency, best-of-N sampling, and verifier models
- When reasoning models are worth the cost — and when they're overkill

**Prompt Engineering:**
- Zero-shot, few-shot, and chain-of-thought prompting
- Role prompting, delimiters, and instruction placement
- Structured outputs: JSON mode, schema-constrained decoding (Outlines, Instructor)
- Tool/function calling fundamentals
- Prompt injection basics — treating model input as untrusted

**Context Engineering:**
- Beyond prompt engineering: managing the entire context window as a budget
- What belongs in context: instructions, examples, retrieved data, tool results, history
- Context rot: why quality degrades as windows fill
- Compaction, summarization, and progressive disclosure strategies
- Prompt caching: cache-aware context ordering and cost reduction
- Multi-turn state management and memory

**Hands-on Lab:**
- Build a prompt evaluation harness: variants scored against a labeled test set
- Force reliable JSON output with schema-constrained decoding and validate it
- Benchmark a reasoning model vs. a standard model on the same task (accuracy, latency, cost)
- Run a local open-weights model with Ollama and compare to a frontier API

---

## Module 13: Fine-Tuning & Model Adaptation
### Week 13 — Teaching Models New Behavior

**When to Fine-Tune:**
- The decision framework: prompting → context/RAG → fine-tuning
- What fine-tuning is good at (format, tone, narrow tasks) and bad at (adding facts)
- Cost, latency, and maintenance tradeoffs vs. prompting

**Supervised Fine-Tuning (SFT):**
- Dataset construction: instruction/response formatting, chat templates
- Data quality over quantity — why 1,000 good examples beat 100,000 scraped ones
- Synthetic data generation and distillation from a stronger model
- Full fine-tuning vs. Parameter-Efficient Fine-Tuning (PEFT)
- LoRA: low-rank adapters, rank and alpha selection, target modules
- QLoRA: 4-bit base weights, training large models on a single GPU
- Adapter merging and serving multiple LoRAs

**Preference Tuning & Alignment:**
- Why SFT alone isn't enough — the alignment problem
- RLHF: reward models and PPO (conceptual)
- DPO (Direct Preference Optimization) and ORPO — simpler modern alternatives
- Reinforcement learning with verifiable rewards, and how reasoning models are trained
- Catastrophic forgetting and how to detect it

**Evaluating a Fine-Tune:**
- Held-out task evals, regression suites, and side-by-side comparisons
- Overfitting signals in generative models
- Deciding whether the fine-tune actually beat the prompt baseline

**Hands-on Lab:**
- Build an instruction dataset from raw domain data (including synthetic augmentation)
- Fine-tune a small open model with LoRA/QLoRA on a single GPU
- Run DPO on a preference dataset and compare to the SFT-only checkpoint
- Evaluate all three (base / SFT / DPO) against the prompted baseline and report the honest result

---

## Module 14: Retrieval-Augmented Generation & Vector Search
### Week 14 — Grounding Models in Your Data

**Embeddings & Vector Search:**
- Embedding models: how they're trained, choosing one, dimensionality tradeoffs
- Matryoshka embeddings and dimension truncation
- Similarity metrics: cosine, dot product, Euclidean
- ANN index structures: HNSW, IVF, product quantization
- Vector Databases: FAISS, ChromaDB, pgvector, Qdrant, Pinecone, Weaviate

**Building a RAG Pipeline:**
- The core loop: chunk → embed → index → retrieve → generate
- Chunking strategies: fixed, recursive, semantic, and document-structure-aware
- Metadata filtering and access control at retrieval time
- Handling PDFs, tables, and messy real-world documents
- Prompt assembly and citation/grounding requirements

**Advanced RAG:**
- Hybrid search: dense + sparse (BM25) with reciprocal rank fusion
- Rerankers: cross-encoders and ColBERT-style late interaction
- Query transformation: rewriting, decomposition, HyDE
- Contextual retrieval: enriching chunks before embedding
- GraphRAG: knowledge graphs for multi-hop questions
- Agentic RAG: letting the model decide what and when to retrieve
- Long-context vs. RAG — when you can skip retrieval entirely

**RAG Evaluation:**
- The two failure surfaces: retrieval quality vs. generation quality
- Retrieval metrics: recall@k, MRR, NDCG
- Generation metrics: faithfulness, answer relevance, context precision (RAGAS)
- Building a golden test set from real user questions

**Hands-on Lab:**
- Build a PDF chatbot with RAG (LangChain / LlamaIndex + a vector DB)
- Measure the baseline, then improve it with hybrid search and a reranker — quantify each gain
- Build a RAGAS evaluation suite and use it to justify every pipeline change
- Add citations and refusal behavior when retrieval returns nothing relevant

---

## Module 15: Agentic AI & Model Context Protocol
### Week 15 — Agents, Tools & Standardized Integration

**Agent Foundations:**
- From chatbots to agents: the ReAct loop (reason → act → observe)
- Tool/function calling: schema design, argument validation, error handling
- Writing tool descriptions the model can actually use
- Memory: short-term context, scratchpads, long-term vector memory
- Planning strategies: task decomposition, reflection, self-critique
- Failure modes: infinite loops, tool thrashing, cost blowups — and how to bound them

**Agent Orchestration:**
- LangGraph: state machines, nodes, edges, conditional routing
- Human-in-the-loop checkpoints and interrupts
- Multi-agent patterns: supervisor/worker, hand-offs, parallel fan-out
- When multi-agent helps and when a single agent with good tools is better
- Framework landscape: LangGraph vs. CrewAI vs. Claude Agent SDK vs. OpenAI Agents SDK

**Model Context Protocol (MCP):**
- Why MCP exists: the M×N integration problem, standardizing tool and data access
- Architecture: hosts, clients, and servers
- Server primitives: tools, resources, and prompts
- Transports: stdio (local) vs. HTTP/SSE (remote)
- Using existing MCP servers (filesystem, database, GitHub, web search)
- Writing a custom MCP server with the Python SDK
- Connecting MCP servers to agents (Claude Desktop / Claude Code, LangGraph adapters)
- MCP vs. plain function calling — when each is the right choice
- Security: authorization, scoping tool access, prompt-injection risk via tool output

**Computer-Use & Coding Agents:**
- Browser and computer-use agents — capabilities and current limits
- How coding agents work: file tools, shell access, and verification loops
- Sandboxing untrusted execution

**Agent Evaluation & Safety:**
- Trajectory evaluation: judging the steps taken, not just the final answer
- Tracing multi-step agent runs (LangSmith / Langfuse)
- Least-privilege tool design and permission boundaries
- Guardrails on destructive actions and spend limits

**Hands-on Lab:**
- Build a tool-using research agent with LangGraph (search + calculator + file tools)
- Build a custom MCP server exposing a database and an internal API as tools
- Connect the MCP server to an agent client and trace a full multi-step run
- Add a human-approval checkpoint before any write or destructive tool call
- Red-team your own agent: get it to misuse a tool via injected content, then fix it

---

## Module 16: Multimodal & Speech AI
### Week 16 — Beyond Text

**Vision-Language Models (VLMs):**
- How VLMs work: vision encoders, projection layers, and unified token streams
- Capabilities: image QA, chart/diagram reading, UI understanding, spatial grounding
- Prompting with images: resolution, detail settings, and cost implications
- Document AI: extracting structured data from invoices, forms, and scanned PDFs
- Multimodal RAG: indexing and retrieving images alongside text

**Speech & Audio:**
- Automatic Speech Recognition (ASR): Whisper architecture, streaming vs. batch
- Diarization, timestamps, and handling accents and noise
- Text-to-Speech (TTS): modern neural voices and voice cloning
- Realtime voice agents: the latency budget, barge-in, and turn detection
- Speech-to-speech models vs. the ASR → LLM → TTS pipeline

**Multimodal Generation:**
- Any-to-any models — the current landscape
- Video understanding and generation overview

**Hands-on Lab:**
- Build a document extraction pipeline: scanned PDF → structured JSON with a VLM
- Transcribe and diarize a meeting recording with Whisper, then summarize with action items
- Build a realtime voice assistant and measure end-to-end latency at each stage
- Build a multimodal RAG system that retrieves both text passages and diagrams

> **Checkpoint Project 2 due: A working GenAI application using Modules 12–16**

---

# PART IV — PRODUCTION

## Module 17: Model Optimization & Efficient Serving
### Week 17 — Making Models Fast and Affordable

**Why Optimization Matters:**
- Inference cost dominates lifetime model spend
- Latency budgets: TTFT (time to first token) vs. throughput
- The accuracy/latency/cost triangle

**Model Compression:**
- Quantization theory: INT8, INT4, and what precision you actually lose
- Post-training quantization: GPTQ, AWQ, bitsandbytes
- Quantization-aware training
- GGUF and llama.cpp for CPU and edge inference
- Pruning: structured vs. unstructured sparsity
- Knowledge distillation: training a small model from a large one
- Small Language Models (SLMs) and on-device inference

**High-Throughput Serving:**
- Continuous batching and PagedAttention (vLLM)
- Speculative decoding and draft models
- Prefix/prompt caching at the server level
- KV cache management and quantization
- Serving stacks: vLLM, SGLang, TGI, TensorRT-LLM
- Autoscaling GPU workloads and managing cold starts

**Classical Model Optimization:**
- ONNX Runtime and TensorRT for non-LLM models
- Batch vs. real-time inference architectures
- CPU-only deployment strategies

**Hands-on Lab:**
- Quantize an open model to 4-bit and measure the accuracy/speed/memory tradeoff
- Benchmark vLLM vs. naive HuggingFace generation under concurrent load
- Distill a fine-tuned model into a smaller one and compare cost per 1M tokens
- Export a scikit-learn/PyTorch model to ONNX and benchmark CPU inference

---

## Module 18: MLOps, LLMOps & Deployment
### Week 18 — From Model to Production

**Model Explainability:**
- Bias-Variance Tradeoff
- Learning curves and model diagnostics
- SHAP (SHapley Additive exPlanations): global and local feature importance
- LIME (Local Interpretable Model-agnostic Explanations)

**MLOps Fundamentals:**
- Experiment tracking: MLflow / Weights & Biases (runs, metrics, artifacts, model registry)
- Data and model versioning: DVC
- Feature stores: purpose, and training/serving skew
- Pipeline orchestration: Airflow, Prefect, Dagster
- Model monitoring: data drift, concept drift, performance degradation
- Automated retraining triggers and rollback strategies

**LLMOps & GenAI in Production:**
- LLM evaluation: LLM-as-judge, RAGAS, faithfulness/groundedness, hallucination detection
- Building eval suites that survive model upgrades
- Observability & tracing: LangSmith / Langfuse, prompt and trace logging
- Prompt versioning and A/B testing in production
- Token and cost management, caching, streaming, fallback chains
- Handling rate limits, retries, and provider outages

**Testing & CI/CD for ML:**
- Testing ML code: unit tests, data tests, model behavior tests
- CI/CD principles applied to ML pipelines
- GitHub Actions: automated testing and model retraining triggers
- Docker: containerizing ML models and APIs
- Kubernetes basics for ML workloads; KServe / Ray Serve

**Deployment:**
- REST API with FastAPI; streaming responses with SSE
- Serving classical models: TensorFlow Serving, TorchServe
- Cloud deployment:
  - AWS SageMaker / Bedrock: endpoints, batch transform, pipelines
  - Azure ML / Azure AI Foundry: managed endpoints
  - Google Vertex AI: model registry, online prediction

**Hands-on Lab:**
- Package a trained model as a streaming FastAPI endpoint
- Containerize with Docker and deploy to a cloud endpoint with monitoring
- Set up MLflow tracking plus an automated RAGAS eval that gates deployment in CI
- Simulate data drift and trigger an automated retraining pipeline

---

## Module 19: Responsible AI, Safety & Governance
### Week 19 — Shipping Systems You Can Defend

> Increasingly the blocker on deploying ML is not capability but compliance and trust. This module is written for engineers who will be asked to justify a model to a regulator, a security team, or a customer.

**Fairness & Bias:**
- Where bias enters: data collection, labeling, proxies, feedback loops
- Fairness metrics: demographic parity, equalized odds, equal opportunity
- The impossibility result — why you cannot satisfy all fairness criteria at once
- Bias auditing with Fairlearn; mitigation before, during, and after training
- Disparate impact in practice: lending, hiring, and healthcare case studies

**Privacy & Data Protection:**
- PII detection and redaction (Presidio) in training data and prompts
- Differential privacy fundamentals
- Federated learning overview
- Membership inference and training-data extraction attacks
- GDPR/DPDP considerations: consent, retention, and the right to erasure

**LLM Safety & Security:**
- Prompt injection: direct and indirect, and why there is no complete fix
- Jailbreaks, data exfiltration via tool use, and the lethal trifecta
- Guardrail layers: input filtering, output validation, structured refusal
- Red-teaming methodology and building an adversarial test suite
- The OWASP Top 10 for LLM Applications

**Governance & Compliance:**
- The EU AI Act: risk tiers and what each requires
- NIST AI Risk Management Framework
- Model cards, system cards, and datasheets for datasets
- Audit trails, human oversight requirements, and incident response
- Content provenance: watermarking and C2PA

**Hands-on Lab:**
- Audit a credit model for disparate impact with Fairlearn, then mitigate and report the accuracy cost
- Build a PII redaction layer in front of an LLM API
- Red-team a RAG chatbot with an indirect prompt-injection payload hidden in a document
- Write a model card and risk assessment for your checkpoint project

---

## Module 20: Capstone Project
### Week 20 — End-to-End Production ML / GenAI Project

Students complete one full end-to-end project covering:

- Problem framing, success metrics, and dataset selection
- Data collection, validation, cleaning, and feature engineering
- Model selection, training, evaluation, and tuning
- Explainability (SHAP/LIME) or LLM evaluation (RAGAS / LLM-as-judge)
- Optimization: quantization or distillation with a measured cost/latency tradeoff
- MLOps/LLMOps pipeline: experiment tracking, versioning, CI/CD
- Deployment: REST API + cloud endpoint
- Monitoring: data/concept drift, performance, cost, and safety tracking
- A responsible AI review: fairness or safety audit with documented findings

**Suggested Project Ideas:**

| Domain | Project |
|---|---|
| Finance | Real-time Fraud Detection System |
| Business | Customer Churn Prediction Pipeline |
| Finance | Stock / Sales Forecasting |
| HR Tech | NLP-based Resume Screening Tool (with a mandatory bias audit) |
| Healthcare | Medical Image Classification (X-rays / MRI) |
| Retail | Recommendation Engine |
| Agriculture | Plant Disease Detection (CNN) |
| Document AI | VLM-based Invoice/Form Extraction Pipeline |
| GenAI | Agentic RAG Assistant (LangGraph + Vector DB) |
| GenAI | MCP-powered Assistant (custom MCP server + agent client) |
| GenAI | Fine-tuned Domain Chatbot (LoRA + DPO) with an evaluation harness |
| Voice AI | Realtime Voice Agent with function calling |
| Computer Vision | Object Detection or Segmentation Pipeline |
| Generative Vision | Text-to-Image or Image Editing App (Diffusion + ControlNet) |
| Efficiency | Distill and self-host a task model; beat an API baseline on cost |

**Deliverables:**
- GitHub Repository with clean, documented, tested code
- Jupyter notebooks covering EDA and modeling
- Deployed API endpoint (AWS / Azure / GCP / local Docker)
- Architecture diagram
- Evaluation report (metrics or LLM/RAG eval results, including failure analysis)
- Model card with a fairness or safety assessment
- 10-minute demo presentation with slides

---

## Elective Modules (Optional)

> Self-paced modules outside the 20-week core track. Offered as add-on weeks or independent study depending on cohort needs.

### Elective A — Time Series & Recommender Systems

> Recommended for students targeting forecasting, retail, or personalization roles. Builds on Modules 3–8.

**Time Series Forecasting:**
- Time series components: trend, seasonality, noise
- ARIMA and SARIMA models
- Prophet: forecasting library for business data
- LSTM-based time series forecasting
- Foundation models for time series (TimeGPT, Chronos) — an overview
- Evaluation: MAPE, MAE, RMSE on temporal data; backtesting correctly

**Recommender Systems:**
- Collaborative Filtering: User-based and Item-based
- Content-Based Filtering: feature similarity
- Matrix Factorization: SVD, ALS
- Two-tower neural retrieval and embedding-based recommenders
- Hybrid Recommender Systems; cold-start strategies

**Hands-on Lab:**
- Stock/sales forecasting with Prophet and LSTM, evaluated with proper backtesting
- Build a movie recommender with collaborative filtering (MovieLens dataset)

---

### Elective B — Reinforcement Learning

> RLHF, DPO, and reasoning-model training (Module 13) build directly on these ideas. Recommended for students going deeper into alignment.

**Topics:**
- Markov Decision Processes (MDPs): states, actions, rewards, transitions
- Bellman Equation and value functions
- Q-Learning: tabular Q-table approach
- Deep Q-Networks (DQN): neural network as Q-function approximator
- Policy Gradient Methods: REINFORCE algorithm
- Actor-Critic methods and PPO
- Connection to LLMs: how RLHF and verifiable-reward RL align and train reasoning models
- Gymnasium (formerly OpenAI Gym): environment setup and agent interaction

**Hands-on Lab:**
- Train a Q-Learning agent on a simple gridworld
- Train a DQN agent on CartPole with PyTorch
- Visualize reward curves and training stability

---

### Elective C — Causal Inference & Graph ML

> Recommended for students in product analytics, experimentation, or fraud/network domains.

**Causal Inference:**
- Correlation vs. causation; why predictive accuracy doesn't imply intervention value
- Potential outcomes and confounding
- A/B testing: power analysis, sequential testing, common pitfalls
- Uplift modeling and heterogeneous treatment effects
- DoWhy and EconML

**Graph Machine Learning:**
- Graph representations and node/edge features
- Graph Neural Networks: GCN, GraphSAGE, GAT
- Applications: fraud rings, recommendation, knowledge graphs
- PyTorch Geometric

**Hands-on Lab:**
- Estimate the causal effect of a marketing intervention with DoWhy
- Build a GNN for fraud detection on a transaction graph

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.11+ |
| Environment | uv / conda, Docker, pre-commit |
| Data | NumPy, Pandas, Polars, DuckDB, Matplotlib, Seaborn |
| Data Quality | Pandera, Great Expectations |
| ML Frameworks | Scikit-learn, XGBoost, LightGBM, CatBoost |
| Deep Learning | PyTorch, TensorFlow / Keras, HuggingFace Accelerate, DeepSpeed |
| Generative Models | Diffusers (Stable Diffusion), ControlNet |
| NLP & LLMs | HuggingFace Transformers, PEFT, TRL, LangChain, LlamaIndex |
| Local Inference | Ollama, llama.cpp, LM Studio |
| Agents & Tooling | Model Context Protocol (MCP), MCP Python SDK, LangGraph, Claude Agent SDK, CrewAI |
| Vector Databases | FAISS, ChromaDB, pgvector, Qdrant, Pinecone, Weaviate |
| Structured Output | Outlines, Instructor, Pydantic |
| LLMOps & Eval | RAGAS, LangSmith / Langfuse, DeepEval |
| Serving & Optimization | vLLM, SGLang, TGI, ONNX Runtime, TensorRT, bitsandbytes |
| Computer Vision | OpenCV, torchvision, YOLO, SAM |
| Speech & Multimodal | Whisper, faster-whisper, TTS engines |
| Time Series | Prophet, statsmodels, sktime |
| MLOps | MLflow, Weights & Biases, DVC, Airflow / Prefect, GitHub Actions |
| Deployment | FastAPI, Docker, Kubernetes, Ray Serve, TorchServe |
| Responsible AI | Fairlearn, SHAP, LIME, Presidio |
| Cloud | AWS SageMaker / Bedrock, Azure ML, Google Vertex AI |
| Version Control | Git, GitHub |
| IDE | VS Code, Jupyter Lab, Google Colab, Claude Code |

---

## Course Schedule Summary

| Week | Module | Topic | Key Skills |
|---|---|---|---|
| 1 | Module 1 | Python for ML | NumPy, Pandas, Git, AI-assisted dev |
| 2 | Module 2 | Math & Statistics | Linear Algebra, Calculus, Probability |
| 3 | Module 3 | Data Engineering & EDA | Cleaning, Feature Engineering, Validation |
| 4 | Module 4 | Regression | Linear, Ridge, Lasso, ElasticNet |
| 5 | Module 5 | Classification | Logistic, SVM, KNN, Calibration |
| 6 | Module 6 | Ensemble Methods | XGBoost, LightGBM, Optuna |
| 7 | Module 7 | Unsupervised Learning | K-Means, PCA, t-SNE, UMAP |
| 8 | Module 8 | Deep Learning | MLP, Backprop, PyTorch, Keras |
| 9 | Module 9 | Training at Scale | Mixed Precision, DDP/FSDP, Profiling |
| 10 | Module 10 | Vision & Generative Vision | CNN, ViT, YOLO, SAM, Diffusion |
| 11 | Module 11 | NLP & Transformer Internals | Attention, RoPE, KV Cache, MoE |
| 12 | Module 12 | LLMs & Context Engineering | Prompting, Reasoning Models, Caching |
| 13 | Module 13 | Fine-Tuning & Alignment | LoRA/QLoRA, DPO, Distillation |
| 14 | Module 14 | RAG & Vector Search | Hybrid Search, Rerankers, RAGAS |
| 15 | Module 15 | Agentic AI & MCP | ReAct, LangGraph, MCP Servers |
| 16 | Module 16 | Multimodal & Speech | VLMs, Document AI, Whisper, Voice |
| 17 | Module 17 | Optimization & Serving | Quantization, vLLM, Distillation |
| 18 | Module 18 | MLOps & LLMOps | MLflow, Docker, K8s, CI/CD, Drift |
| 19 | Module 19 | Responsible AI & Safety | Fairness, Red-teaming, EU AI Act |
| 20 | Module 20 | Capstone Project | End-to-End Production Project |
| — | Elective A | Time Series & Recommenders | ARIMA, Prophet, Collaborative Filtering |
| — | Elective B | Reinforcement Learning | Q-Learning, DQN, PPO |
| — | Elective C | Causal Inference & Graph ML | DoWhy, Uplift, GNNs |

---

## Recommended Resources

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *The Hundred-Page Machine Learning Book* — Andriy Burkov
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- *Pattern Recognition and Machine Learning* — Christopher Bishop
- *Natural Language Processing with Transformers* — Tunstall, von Werra & Wolf
- *Build a Large Language Model (From Scratch)* — Sebastian Raschka
- *AI Engineering* — Chip Huyen
- *Designing Machine Learning Systems* — Chip Huyen
- *Fairness and Machine Learning* — Barocas, Hardt & Narayanan (free online)

### Online Platforms
- Kaggle (datasets, notebooks, competitions)
- HuggingFace Hub (pre-trained models, datasets, Spaces)
- Papers With Code (state-of-the-art benchmarks)
- LMArena / open LLM leaderboards (model comparison)
- Google Colab and AWS SageMaker Studio Lab (free GPU compute)

### Courses & Docs for Reference
- fast.ai — Practical Deep Learning for Coders
- Andrej Karpathy — *Neural Networks: Zero to Hero* (build GPT from scratch)
- Andrew Ng — Machine Learning Specialization (Coursera)
- DeepLearning.AI — Deep Learning Specialization & GenAI short courses
- HuggingFace — LLM Course, Diffusion Course, and Agents Course
- Model Context Protocol — official spec and server examples (modelcontextprotocol.io)
- LangChain / LangGraph documentation and cookbooks
- vLLM and PyTorch distributed training documentation
- Model provider docs (Anthropic, OpenAI, Google) for prompting, tool use, and structured outputs
- OWASP Top 10 for LLM Applications

---

## Assessment & Grading

| Component | Weight |
|---|---|
| Weekly Quizzes | 15% |
| Lab Assignments | 25% |
| Checkpoint Project 1 — Classical ML (Week 7) | 15% |
| Checkpoint Project 2 — GenAI Application (Week 16) | 15% |
| Final Capstone Project (Week 20) | 30% |

| Grade | Score |
|---|---|
| A+ | 90–100% |
| A | 80–89% |
| B | 70–79% |
| C | 60–69% |
| F | Below 60% |

---

## Compute Requirements

| Need | Minimum | Recommended |
|---|---|---|
| Weeks 1–7 | Any laptop | 16 GB RAM |
| Weeks 8–11 | Google Colab (free tier) | Colab Pro or a 12 GB+ VRAM GPU |
| Weeks 12–17 | Colab Pro + API credits | 24 GB VRAM GPU or cloud rental (A100/H100 hourly) |
| Weeks 18–20 | Cloud free tier | AWS/GCP/Azure credits for deployment |

> Budget for API credits across Weeks 12–16 (roughly $20–50 per student). Open-weights models via Ollama are used wherever possible to keep costs down.

---

## Final Outcome

Students graduating from this course will be capable of designing, developing, evaluating, optimizing, deploying, monitoring, and governing modern **Machine Learning** and **Generative AI** systems — production-ready, cost-aware, and defensible to both a security review and a regulator.
