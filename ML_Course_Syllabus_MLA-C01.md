# Machine Learning Course Syllabus
## Aligned to AWS Certified Machine Learning Engineer – Associate (MLA-C01)

**Course Title:** Machine Learning Engineering on AWS — MLA-C01 Exam Prep  
**Duration:** 12 Weeks (48 Hours)  
**Level:** Intermediate  
**Certification Target:** AWS Certified Machine Learning Engineer – Associate (MLA-C01)  
**Minimum Passing Score:** 720 / 1000  
**Prerequisites:** Basic Python, 1+ year experience with AWS services, familiarity with data engineering concepts

---

## MLA-C01 Exam Domain Weightings

| Domain | Topic | Weight |
|---|---|---|
| Domain 1 | Data Preparation for Machine Learning | **28%** |
| Domain 2 | ML Model Development | **26%** |
| Domain 3 | Deployment and Orchestration of ML Workflows | **22%** |
| Domain 4 | ML Solution Monitoring, Maintenance, and Security | **24%** |

> **Exam Format:** 65 questions (50 scored + 15 unscored) — Multiple choice, Multiple response, Ordering, Matching, Case Study  
> **Time:** 170 minutes | **Testing:** Pearson VUE (in-person or online proctored)

---

## Course Learning Outcomes

By the end of this course, students will be able to:

- Ingest, transform, validate, and prepare data for ML modeling using AWS services
- Select appropriate ML algorithms and use SageMaker built-in algorithms and JumpStart foundation models
- Train, tune, and evaluate models using Amazon SageMaker
- Deploy ML models using real-time, batch, serverless, and asynchronous endpoints
- Build CI/CD pipelines using CodePipeline, CodeBuild, and SageMaker Pipelines
- Monitor models for drift, bias, and performance degradation using SageMaker Model Monitor
- Secure ML infrastructure with IAM, VPC, encryption, and compliance controls
- Optimize infrastructure costs using AWS cost management tools

---

## MODULE 1: ML Foundations & AWS ML Landscape
### Week 1 — Introduction to ML & AWS AI/ML Services

> **Exam Alignment:** Domain 2 (Task 2.1) — Choosing a modeling approach; AWS AI services

**ML Fundamentals:**
- What is Machine Learning? Supervised, Unsupervised, Reinforcement Learning
- ML vs AI vs Deep Learning — the landscape
- The ML pipeline: Data → Model → Train → Evaluate → Deploy → Monitor
- Common ML algorithms and when to use them (classification, regression, clustering, anomaly detection)
- Model interpretability considerations during algorithm selection

**AWS AI/ML Service Landscape:**
- Pre-built AI services: Amazon Rekognition, Amazon Transcribe, Amazon Translate, Amazon Comprehend, Amazon Polly, Amazon Lex, Amazon Textract, Amazon Kendra, Amazon Fraud Detector, Amazon Personalize
- When to use AI services vs. custom ML models vs. foundation models
- Amazon Bedrock — Foundation Models (FMs) overview
- Amazon SageMaker — end-to-end ML platform overview
- SageMaker JumpStart — pre-built models and solution templates

**Hands-on Lab:**
- Explore Amazon SageMaker Studio UI
- Deploy a pre-built model using SageMaker JumpStart
- Test Amazon Rekognition and Amazon Comprehend via console

---

### Week 2 — Math & Python Refresher for ML

> **Exam Alignment:** Domain 2 (Task 2.2) — Training and refining models (foundational knowledge)

**Math Refresher:**
- Linear Algebra: Vectors, Matrices, Dot products
- Calculus: Derivatives, Partial derivatives, Chain rule (used in backpropagation)
- Probability & Statistics: Distributions, Bayes' Theorem, Expectation, Variance

**Python ML Ecosystem:**
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn: pipelines, preprocessing, model API
- Introduction to TensorFlow/Keras and PyTorch (used with SageMaker script mode)

**Hands-on Lab:**
- NumPy & Pandas data manipulation exercises
- Build a basic Scikit-learn pipeline in SageMaker Studio notebook

---

## MODULE 2: Data Preparation for Machine Learning
### *(Domain 1 — 28% of Exam)*

---

### Week 3 — Data Ingestion & Storage on AWS

> **Exam Alignment:** Domain 1, Task 1.1 — Ingest and store data

**Data Formats & Ingestion:**
- Data formats for ML: CSV, JSON, Apache Parquet, Apache ORC, Apache Avro, RecordIO
- Choosing formats based on data access patterns and ML workload type
- Validated vs. non-validated data formats

**AWS Data Sources & Storage:**
- Amazon S3 — primary ML data lake storage; S3 Transfer Acceleration
- Amazon EFS and Amazon FSx for NetApp ONTAP — shared file storage for training
- Amazon EBS — block storage for compute instances
- Amazon RDS and Amazon DynamoDB — relational and NoSQL sources
- Extracting data from multiple sources and merging datasets

**AWS Streaming Ingestion:**
- Amazon Kinesis Data Streams and Amazon Data Firehose
- Amazon Managed Service for Apache Flink
- Apache Kafka on Amazon MSK
- AWS Lambda for real-time stream transformation

**SageMaker Data Ingestion:**
- Ingesting data into SageMaker Data Wrangler
- Ingesting features into SageMaker Feature Store (online vs. offline store)

**Data Storage Decision Framework:**
- Cost vs. performance vs. data structure tradeoffs
- Troubleshooting capacity and scalability issues in data pipelines

**Hands-on Lab:**
- Upload and organize an ML dataset in Amazon S3
- Create a Kinesis Data Stream and consume records via Lambda
- Ingest a dataset into SageMaker Data Wrangler

---

### Week 4 — Feature Engineering & Data Transformation

> **Exam Alignment:** Domain 1, Task 1.2 — Transform data and perform feature engineering

**Data Cleaning Techniques:**
- Detecting and treating outliers
- Imputing missing values (mean, median, mode, model-based)
- Deduplication and combining datasets

**Feature Engineering:**
- Scaling and standardization (MinMax, StandardScaler, RobustScaler)
- Feature splitting and binning
- Log transformation and normalization
- Encoding categorical variables: One-hot encoding, Binary encoding, Label encoding, Target encoding, Tokenization

**AWS Tools for Transformation:**
- AWS Glue — serverless ETL; Glue DataBrew for visual data preparation
- AWS Glue Data Quality — validate data quality rules
- Apache Spark on Amazon EMR — large-scale data transformation
- SageMaker Data Wrangler — 300+ built-in transforms, export to SageMaker Pipelines
- AWS Lambda — lightweight real-time data transformations

**Data Annotation & Labeling:**
- SageMaker Ground Truth — human-in-the-loop labeling
- Amazon Augmented AI (Amazon A2I) — human review workflows
- Amazon Mechanical Turk — crowdsourced labeling

**SageMaker Feature Store:**
- Creating, managing, and versioning features
- Online store (low-latency inference) vs. offline store (batch training)

**Hands-on Lab:**
- Build a Glue ETL job to transform raw S3 data to Parquet
- Apply feature engineering transforms in SageMaker Data Wrangler
- Register features in SageMaker Feature Store

---

### Week 5 — Data Integrity, Bias Detection & Compliance

> **Exam Alignment:** Domain 1, Task 1.3 — Ensure data integrity and prepare data for modeling

**Data Quality & Validation:**
- Validating data quality with AWS Glue DataBrew and AWS Glue Data Quality
- Data profiling and statistics

**Pre-Training Bias Detection:**
- Understanding pre-training bias metrics: Class Imbalance (CI), Difference in Proportions of Labels (DPL)
- Bias in numeric, text, and image data
- Strategies to address class imbalance: synthetic data generation (SMOTE), resampling, oversampling/undersampling
- Selection bias and measurement bias
- Using SageMaker Clarify for pre-training bias analysis

**Data Preparation to Reduce Prediction Bias:**
- Dataset splitting strategies (stratified split, time-based split)
- Dataset shuffling
- Data augmentation for images and text
- Configuring data to load into training resources (EFS, FSx)

**Data Security & Compliance:**
- Encrypting data at rest (SSE-S3, SSE-KMS) and in transit (TLS)
- Data classification, anonymization, and masking
- PII and PHI compliance requirements
- AWS Lake Formation — data governance and fine-grained access control
- Data residency considerations

**Hands-on Lab:**
- Run a data quality validation job with AWS Glue Data Quality
- Detect pre-training bias using SageMaker Clarify
- Apply KMS encryption to an S3 ML dataset bucket

---

## MODULE 3: ML Model Development
### *(Domain 2 — 26% of Exam)*

---

### Week 6 — Supervised & Unsupervised Algorithms + SageMaker Built-ins

> **Exam Alignment:** Domain 2, Task 2.1 — Choose a modeling approach

**Core ML Algorithms & Use Cases:**
- Regression: Linear Regression, Ridge (L2), Lasso (L1), ElasticNet
- Classification: Logistic Regression, Decision Trees, KNN, SVM, Naive Bayes
- Ensemble methods: Random Forest, XGBoost, LightGBM, AdaBoost, Gradient Boosting
- Unsupervised: K-Means, DBSCAN, PCA, Autoencoders
- Anomaly Detection: Isolation Forest, One-Class SVM
- Recommender Systems: Collaborative Filtering, Matrix Factorization

**SageMaker Built-in Algorithms:**
- Linear Learner — regression and classification
- XGBoost — gradient boosting (most commonly tested)
- K-Means — clustering
- PCA — dimensionality reduction
- Random Cut Forest (RCF) — anomaly detection
- Object Detection, Image Classification, Semantic Segmentation — computer vision
- BlazingText — word embeddings and text classification
- DeepAR — time series forecasting
- Factorization Machines — recommender systems
- Seq2Seq — sequence-to-sequence tasks
- IP Insights — network anomaly detection
- Tabular Learner (via SageMaker Autopilot)

**Model Selection Framework:**
- Feasibility assessment: data volume, problem complexity, latency requirements
- Cost vs. accuracy vs. interpretability tradeoffs
- When to use built-in algorithms vs. custom code vs. foundation models (Amazon Bedrock)
- SageMaker Autopilot — automated ML for tabular data

**Hands-on Lab:**
- Train an XGBoost model using SageMaker built-in algorithm
- Use SageMaker Autopilot to auto-select best model for a classification dataset

---

### Week 7 — Model Training, Regularization & Hyperparameter Tuning

> **Exam Alignment:** Domain 2, Task 2.2 — Train and refine models

**Training Process Concepts:**
- Epoch, steps, batch size, learning rate
- Forward propagation and Backpropagation
- Loss functions: Binary Cross-Entropy, Categorical Cross-Entropy, MSE
- Optimizers: SGD, Momentum, Adam, AdamW

**Reducing Training Time:**
- Early stopping
- Distributed training: data parallelism vs. model parallelism
- SageMaker distributed training libraries (SageMaker Data Parallelism Library, Model Parallelism Library)
- Using Spot Instances for cost-efficient training (`use_spot_instances=True`)
- Checkpoint management for Spot training interruptions

**Overfitting, Underfitting & Regularization:**
- Bias-variance tradeoff
- L1 (Lasso) and L2 (Ridge) regularization
- Dropout layers
- Weight decay
- Feature selection to reduce noise
- Preventing catastrophic forgetting in fine-tuning

**Hyperparameter Tuning:**
- Manual tuning, Random Search, Grid Search, Bayesian Optimization
- SageMaker Automatic Model Tuning (AMT) — Bayesian optimization at scale
- Tuning ranges and parameter types (continuous, integer, categorical)
- Warm start tuning jobs

**Transfer Learning & Fine-tuning:**
- Fine-tuning pre-trained models using custom datasets
- SageMaker JumpStart fine-tuning
- Amazon Bedrock — fine-tuning foundation models (continued pre-training, instruction tuning)

**Model Size Reduction:**
- Pruning, data type alteration (float16, int8), feature selection, model compression
- SageMaker Neo — compile models for edge and cloud inference targets

**Model Versioning:**
- SageMaker Model Registry — register, version, approve/reject models
- Managing model artifacts in S3

**Using SageMaker Script Mode:**
- Bring your own training script (TensorFlow, PyTorch, MXNet)
- Custom containers with BYOC (Bring Your Own Container)
- Integrating models built outside SageMaker

**Hands-on Lab:**
- Train a PyTorch model on SageMaker using script mode
- Run a hyperparameter tuning job with SageMaker AMT
- Register a trained model in SageMaker Model Registry

---

### Week 8 — Model Evaluation & Bias Analysis

> **Exam Alignment:** Domain 2, Task 2.3 — Analyze model performance

**Model Evaluation Metrics:**
- Classification: Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC, Log Loss
- Regression: MAE, MSE, RMSE, R²
- Clustering: Silhouette Score, Elbow Method
- Ranking: NDCG, MAP

**Model Diagnostics:**
- Overfitting: high training accuracy, low validation accuracy
- Underfitting: high bias, poor performance on both sets
- Learning curves and validation curves
- Convergence issues and debugging with SageMaker Debugger

**Post-Training Bias & Explainability:**
- SageMaker Clarify — detect post-training bias and explain model predictions
- Bias metrics: DPPL, DI, AD, CDDL
- SHAP values for global and local feature importance
- A/B testing: shadow variant vs. production variant comparison

**Performance Baselines & Reproducibility:**
- Creating performance baselines for model comparison
- Reproducible experiments using SageMaker Experiments
- Assessing tradeoffs between accuracy, training time, and cost

**Hands-on Lab:**
- Evaluate a trained SageMaker model using Clarify for bias and explainability
- Use SageMaker Debugger to identify convergence issues
- Compare two model variants using SageMaker Experiments

---

## MODULE 4: Deployment and Orchestration of ML Workflows
### *(Domain 3 — 22% of Exam)*

---

### Week 9 — ML Model Deployment on AWS

> **Exam Alignment:** Domain 3, Task 3.1 — Select deployment infrastructure; Task 3.2 — Create and script infrastructure

**SageMaker Endpoint Types:**
- Real-time endpoints — low-latency synchronous inference
- Asynchronous endpoints — large payloads, long processing times
- Serverless endpoints — auto-scales to zero, pay-per-invocation
- Batch Transform — offline bulk inference on S3 datasets
- Multi-model endpoints (MME) — host multiple models on a single endpoint
- Multi-container endpoints — different frameworks in one endpoint

**Compute Selection:**
- CPU vs. GPU instance types for training vs. inference
- Memory-optimized, compute-optimized, inference-optimized instances (ml.inf1, ml.inf2, ml.trn1)
- Choosing instance families based on latency, throughput, and cost requirements
- SageMaker Inference Recommender — right-size instance selection

**Deployment Strategies:**
- Blue/Green deployment — zero-downtime cutover
- Canary deployment — gradual traffic shifting
- Linear deployment — incremental rollout
- Rollback strategies and versioning

**Edge Deployment:**
- SageMaker Neo — compile and optimize models for edge devices
- AWS IoT Greengrass — deploy ML models to edge hardware

**Containers & Custom Inference:**
- SageMaker provided containers (built-in)
- BYOC (Bring Your Own Container) for custom inference
- Amazon ECR — store and version container images
- Amazon ECS and Amazon EKS — Kubernetes-based inference at scale
- AWS Lambda — lightweight serverless inference behind endpoints

**Infrastructure as Code (IaC):**
- AWS CloudFormation — declarative infrastructure templates
- AWS CDK — programmatic infrastructure in Python/TypeScript
- On-demand vs. provisioned resources; auto scaling policies
- SageMaker endpoint auto scaling (Target Tracking, Step Scaling)
- Configuring SageMaker endpoints within VPC network

**Hands-on Lab:**
- Deploy a model to a SageMaker real-time endpoint
- Configure an asynchronous endpoint for a large-payload use case
- Write a CloudFormation template to provision a SageMaker endpoint
- Set up auto scaling on a SageMaker endpoint

---

### Week 10 — CI/CD Pipelines & ML Orchestration

> **Exam Alignment:** Domain 3, Task 3.3 — Automated orchestration and CI/CD pipelines

**CI/CD Fundamentals for ML:**
- Difference between CI/CD for software vs. ML (data + model + code versioning)
- Gitflow and GitHub Flow branching strategies
- CI/CD stages: Source → Build → Test → Deploy → Monitor

**AWS CI/CD Services:**
- AWS CodePipeline — pipeline orchestration, stage-by-stage automation
- AWS CodeBuild — build and test ML training containers
- AWS CodeDeploy — deploy models to SageMaker or EC2
- AWS CodeArtifact — artifact management for ML dependencies
- Configuring, troubleshooting, and debugging CodePipeline stages

**ML Pipeline Orchestration:**
- SageMaker Pipelines — define, automate, and visualize ML workflows
- Pipeline steps: Processing, Training, Tuning, Evaluation, RegisterModel, CreateModel, Transform, Deploy
- Amazon Managed Workflows for Apache Airflow (MWAA) — DAG-based orchestration
- AWS Step Functions — serverless workflow orchestration
- Amazon EventBridge rules — trigger pipelines on events (data arrival, schedules)

**Automated Model Retraining:**
- Triggering retraining pipelines on model drift detection
- Integrating data ingestion with orchestration services
- Automated testing in CI/CD: unit tests, integration tests, end-to-end tests

**Deployment Rollback & Safety:**
- Blue/Green and canary deployment automation in CodeDeploy
- Shadow mode testing before production cutover
- Model version approval workflows in SageMaker Model Registry

**Hands-on Lab:**
- Build a SageMaker Pipeline with processing, training, evaluation, and registration steps
- Create a CodePipeline that automates model retraining on new data arrival
- Configure an EventBridge rule to trigger a SageMaker Pipeline on S3 upload

---

## MODULE 5: ML Solution Monitoring, Maintenance, and Security
### *(Domain 4 — 24% of Exam)*

---

### Week 11 — Monitoring, Observability & Cost Optimization

> **Exam Alignment:** Domain 4, Task 4.1 — Monitor model inference; Task 4.2 — Monitor and optimize infrastructure and costs

**Model Monitoring Concepts:**
- Data drift — distribution shift in input features over time
- Concept drift — change in the relationship between input and output
- Model performance degradation — accuracy drop in production
- Baseline statistics and constraint files for drift detection

**SageMaker Model Monitor:**
- Data Quality Monitor — detect feature distribution drift
- Model Quality Monitor — detect accuracy/performance drift
- Bias Drift Monitor — detect post-deployment bias changes (using SageMaker Clarify)
- Feature Attribution Drift Monitor — detect SHAP value shifts
- Monitoring schedules, CloudWatch alerts on violations

**A/B Testing & Shadow Variants:**
- Production variant vs. shadow variant traffic splitting
- Analyzing performance differences between model variants

**Infrastructure Monitoring:**
- Amazon CloudWatch — metrics, logs, dashboards, alarms
- Amazon CloudWatch Logs Insights — query log data
- AWS X-Ray — distributed tracing for ML inference services
- AWS CloudTrail — audit API calls, log and invoke retraining activities
- Amazon EventBridge — respond to CloudWatch alarm state changes
- Amazon QuickSight — dashboards for ML performance metrics

**Key Infrastructure Metrics:**
- CPU/GPU utilization, memory usage, disk I/O
- Model latency (p50, p90, p99), throughput, invocations per instance
- Auto scaling triggers: latency thresholds, invocation counts

**Cost Optimization:**
- AWS Cost Explorer — analyze ML spending trends
- AWS Budgets — set spending thresholds and alerts
- AWS Trusted Advisor — rightsizing and cost recommendations
- AWS Compute Optimizer — EC2 and SageMaker instance rightsizing
- SageMaker Savings Plans — commit for discounted pricing
- Spot Instances for training (up to 90% cost savings)
- Reserved Instances for steady-state inference workloads
- Serverless endpoints for low-traffic models (zero idle cost)
- Resource tagging strategy for cost allocation and tracking

**Hands-on Lab:**
- Configure SageMaker Model Monitor to detect data drift on a live endpoint
- Set up CloudWatch alarms and dashboards for endpoint metrics
- Analyze ML infrastructure costs using AWS Cost Explorer with tagging

---

### Week 12 — Security, Compliance & Capstone Project

> **Exam Alignment:** Domain 4, Task 4.3 — Secure AWS resources

**Identity & Access Management (IAM):**
- IAM roles, policies, and groups for ML systems
- Principle of least privilege for SageMaker roles
- SageMaker Role Manager — simplified role creation for ML personas
- Bucket policies for S3 ML data access control
- Service Control Policies (SCPs) via AWS Organizations

**Network Security for ML:**
- Amazon VPC — isolate SageMaker training and inference within private subnets
- Security groups and NACLs for ML resource access control
- VPC endpoints — private connectivity to S3 and SageMaker without internet
- AWS Direct Connect — dedicated private network connectivity
- Configuring SageMaker endpoints inside VPC

**Encryption & Data Protection:**
- Encryption at rest: SSE-S3, SSE-KMS, SageMaker notebook and endpoint encryption
- Encryption in transit: TLS for all API calls and data transfers
- AWS KMS — key management for ML artifacts and data stores
- SageMaker security features: network isolation, inter-container traffic encryption

**Compliance & Auditing:**
- SageMaker compliance features (HIPAA, PCI DSS eligibility)
- AWS Config — configuration compliance monitoring
- AWS CloudTrail — full audit log of all ML API activity
- AWS Service Catalog — enforce approved ML infrastructure templates
- Monitoring and logging for continued security compliance
- Troubleshooting and debugging security issues

**CI/CD Security:**
- Securing CodePipeline stages with IAM roles
- Scanning container images in Amazon ECR for vulnerabilities
- Secrets management with AWS Secrets Manager and SSM Parameter Store

**Capstone Project:**

Students complete one end-to-end AWS ML project covering all four exam domains:
1. **Data Prep:** Ingest raw data into S3 → Glue ETL → Feature Store
2. **Model Dev:** Train using SageMaker built-in or script mode → Tuning with AMT → Register in Model Registry
3. **Deployment:** Deploy to SageMaker endpoint → Set up auto scaling → CI/CD pipeline with SageMaker Pipelines
4. **Monitoring:** Enable Model Monitor → CloudWatch dashboards → IAM and VPC security config

**Suggested Capstone Ideas:**
1. Fraud Detection pipeline — Kinesis ingestion, XGBoost, real-time endpoint, Model Monitor
2. Customer Churn Prediction — Glue ETL, SageMaker Autopilot, batch transform, CloudWatch monitoring
3. Document Intelligence — Amazon Textract + Comprehend, S3, Lambda, EventBridge trigger
4. Recommender System — Feature Store, Factorization Machines, SageMaker Pipelines CI/CD
5. Image Classification — SageMaker JumpStart fine-tuning, ECR container, CodePipeline

**Deliverables:**
- GitHub repository with all code, notebooks, and CloudFormation/CDK templates
- SageMaker Pipeline screenshot (all stages green)
- Deployed endpoint URL with test invocation
- 10-minute demo presentation with architecture diagram

---

## AWS Services Coverage Map

| Exam Domain | Key AWS Services |
|---|---|
| Data Preparation (28%) | S3, Glue, Glue DataBrew, Glue Data Quality, Kinesis, Data Firehose, EMR, Lake Formation, SageMaker Data Wrangler, SageMaker Feature Store, SageMaker Ground Truth, A2I, Mechanical Turk, Athena, Redshift |
| Model Development (26%) | SageMaker (built-in algorithms, Autopilot, JumpStart, Script Mode, Debugger, Clarify, Experiments, AMT, Model Registry), Amazon Bedrock, Rekognition, Comprehend, Transcribe, Translate, Personalize, Fraud Detector |
| Deployment & Orchestration (22%) | SageMaker Endpoints (real-time, async, serverless, batch), SageMaker Pipelines, SageMaker Neo, ECR, ECS, EKS, Lambda, EC2, CodePipeline, CodeBuild, CodeDeploy, MWAA, Step Functions, EventBridge, CloudFormation, CDK, API Gateway |
| Monitoring & Security (24%) | SageMaker Model Monitor, SageMaker Clarify, CloudWatch, CloudWatch Logs, X-Ray, CloudTrail, Cost Explorer, Budgets, Trusted Advisor, Compute Optimizer, IAM, KMS, VPC, Config, QuickSight, AWS Organizations |

---

## Course Schedule Summary

| Week | Domain | Topic | MLA-C01 Task |
|---|---|---|---|
| 1 | Foundations | Intro to ML & AWS AI/ML Services | Domain 2 – Task 2.1 |
| 2 | Foundations | Math Refresher & Python Ecosystem | Domain 2 – Task 2.2 |
| 3 | **Domain 1 (28%)** | Data Ingestion & Storage on AWS | Task 1.1 |
| 4 | **Domain 1 (28%)** | Feature Engineering & Transformation | Task 1.2 |
| 5 | **Domain 1 (28%)** | Data Integrity, Bias Detection & Compliance | Task 1.3 |
| 6 | **Domain 2 (26%)** | Algorithms & SageMaker Built-ins | Task 2.1 |
| 7 | **Domain 2 (26%)** | Model Training, Tuning & Regularization | Task 2.2 |
| 8 | **Domain 2 (26%)** | Model Evaluation, Bias & Explainability | Task 2.3 |
| 9 | **Domain 3 (22%)** | Model Deployment on AWS | Task 3.1, 3.2 |
| 10 | **Domain 3 (22%)** | CI/CD Pipelines & ML Orchestration | Task 3.3 |
| 11 | **Domain 4 (24%)** | Monitoring, Observability & Cost Optimization | Task 4.1, 4.2 |
| 12 | **Domain 4 (24%)** | Security, Compliance & Capstone Project | Task 4.3 |

---

## Assessment & Grading

| Component | Weight | MLA-C01 Alignment |
|---|---|---|
| Weekly Quizzes (10 × 2%) | 20% | All 4 domains |
| Lab Assignments (8 hands-on labs) | 30% | Practical SageMaker skills |
| Mid-term Exam — Mock MLA-C01 (Week 6) | 20% | Domains 1 & 2 (54%) |
| Capstone Project (Week 12) | 30% | All 4 domains end-to-end |

**Grading Scale:**

| Grade | Score |
|---|---|
| A+ | 90–100% |
| A | 80–89% |
| B | 70–79% |
| C | 60–69% |
| F | Below 60% |

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Cloud Platform | AWS (SageMaker, Glue, S3, Kinesis, ECR, ECS, EKS, Lambda, CodePipeline) |
| ML Frameworks | Scikit-learn, XGBoost, TensorFlow, PyTorch (via SageMaker script mode) |
| Data Processing | AWS Glue, Glue DataBrew, Apache Spark on EMR, Pandas |
| Orchestration | SageMaker Pipelines, AWS Step Functions, Amazon MWAA (Airflow) |
| CI/CD | AWS CodePipeline, CodeBuild, CodeDeploy |
| Monitoring | SageMaker Model Monitor, Amazon CloudWatch, AWS X-Ray, CloudTrail |
| Security | AWS IAM, Amazon VPC, AWS KMS, AWS Config, SageMaker Role Manager |
| Cost Management | AWS Cost Explorer, AWS Budgets, AWS Trusted Advisor |
| IaC | AWS CloudFormation, AWS CDK |
| IDE | Amazon SageMaker Studio, Jupyter Lab, VS Code |

---

## Recommended Resources

### Official AWS Resources
- [AWS MLA-C01 Exam Guide (PDF)](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)
- [AWS Skill Builder — MLA-C01 Exam Prep](https://skillbuilder.aws/)
- [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [AWS Well-Architected ML Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/)

### Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Machine Learning Engineering on AWS* — Joshua Arvin Lat
- *Data Science on AWS* — Chris Fregly & Antje Barth (O'Reilly)

### Practice Exams
- AWS Skill Builder Official Practice Exam (paid)
- Tutorials Dojo MLA-C01 Practice Tests
- Stephane Maarek & Abhishek Singh — Udemy MLA-C01 Practice Tests
- ExamTopics MLA-C01 (20 free questions)

### Online Courses
- AWS Skill Builder: Machine Learning Engineer – Associate Learning Plan
- Stephane Maarek — AWS Certified Machine Learning Engineer Associate (Udemy)
- Andrew Ng — Machine Learning Specialization (Coursera) — for ML fundamentals

---

*Last Updated: June 2026 | Aligned to MLA-C01 Exam Guide v1.0*
