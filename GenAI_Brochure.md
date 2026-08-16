# Generative AI Engineering — Brochure Copy

Marketing-ready topic lists for the 11-module Generative AI course.
Two versions below: **full brochure** (multi-page / web) and **one-page leaflet** (print).

---
---

# VERSION 1 — FULL BROCHURE

# Generative AI Engineering
### Build. Measure. Deploy.

**Duration:** 11 modules + capstone
**Format:** Live sessions with hands-on labs
**Prerequisites:** Python basics
**Includes:** Slides, runnable notebooks, project reviews, capstone mentoring

---

## Module 1 — Generative AI & LLM Foundations
- What is Generative AI, and where LLMs fit
- How LLMs work: tokens, context, and prediction
- LLM properties: context window, hallucination, non-determinism
- Prompt engineering techniques that work in production
- Token counting, pricing, and latency — cost from day one
- Environment setup, API keys, and project structure

## Module 2 — ML Foundations for Generative AI
- Linear and logistic regression: what "training" really means
- Neural networks and backpropagation
- Building an ANN with Keras/PyTorch
- Model evaluation basics: accuracy, overfitting, validation

## Module 3 — Transformers & Attention
- Why transformers replaced everything before them
- Self-attention explained with a worked example
- Encoder, decoder, and why chat models are decoder-only
- Layers of a transformer, end to end
- Decoding methods and temperature control
- KV cache: why long conversations cost more

## Module 4 — Embeddings & Semantic Representation
- What embeddings are and why they power search
- Word2Vec intuition: king − man + woman
- Modern sentence embedding models
- Cosine similarity and vector space reasoning
- Choosing an embedding model: quality vs. cost

## Module 5 — Hugging Face & Open-Source LLMs
- Navigating the Hugging Face Hub
- Pipelines, tokenizers, and pre-trained models
- Fine-tuning DistilBERT on your own dataset
- Running open-source LLMs: Llama, Mistral, Groq, Ollama
- Open weights vs. hosted APIs: cost and control

## Module 6 — LangChain Essentials
- LangChain architecture and core components
- LCEL: composing chains the modern way
- Prompt templates and reusable components
- Streaming, callbacks, and debugging chains
- Multi-provider setup: swap models in one line

## Module 7 — Structured Output & Model I/O
- Why free text breaks production systems
- Pydantic models as output contracts
- Nested models, enums, and safe defaults
- `with_structured_output` and tool-calling schemas
- Document loaders: PDF, CSV, web, and YouTube
- Validation, retries, and repair loops

## Module 8 — RAG I: Ingestion, Chunking & Vector Search
- Why RAG: private data, fresh data, citations
- The RAG pipeline end to end
- Document loading and real-world PDF handling
- Chunking strategies and how to choose one
- Vector databases: FAISS, Chroma, pgvector
- FAISS index types and HNSW tuning

## Module 9 — RAG II: Hybrid Search, Reranking & Evaluation
- Diagnosing a failing RAG system
- BM25 and hybrid search with rank fusion
- Cross-encoder rerankers — the biggest quality win
- Query rewriting and multi-query retrieval
- Building a golden test set
- RAGAS: faithfulness, relevance, context precision
- Proving every improvement with a number

## Module 10 — LangGraph: State, Memory & Agents
- From chains to graphs: why agents need state
- Tool calling and writing tools models can use
- The ReAct loop: reason → act → observe
- LangGraph nodes, edges, and conditional routing
- Conversational memory and persistence
- Human-in-the-loop approval gates
- Agentic RAG: letting the model decide when to retrieve
- SQL, CSV, and DataFrame agents

## Module 11 — Agent Safety, Tools & Deployment
- Prompt injection: direct and via retrieved documents
- OWASP Top 10 for LLM Applications
- Guardrails, PII redaction, and output filtering
- Sandboxing code-executing agents
- Serving with FastAPI: streaming and rate limits
- Tracing and monitoring with LangSmith
- Cost control: caching and model routing

## Capstone Project
- Build a production GenAI system of your choice
- Measured evaluation with baseline and improvement
- Deployed, traced, and cost-analyzed
- Security-reviewed and presented

---

### What You'll Build
- A fine-tuned transformer model
- A document Q&A system with citations
- An evaluated RAG pipeline with measurable improvements
- A tool-using AI agent with LangGraph
- A deployed, monitored API service

### Tools & Technologies
`Python` · `PyTorch` · `Hugging Face` · `Transformers` · `LangChain` · `LCEL` · `LangGraph` ·
`Pydantic` · `FAISS` · `ChromaDB` · `BM25` · `RAGAS` · `LangSmith` · `FastAPI` · `Ollama` · `Groq`

### Who Should Attend
- Software developers moving into AI
- Data scientists and ML engineers
- Final-year and postgraduate students
- Technical leads evaluating GenAI for their teams

### Outcomes
Design, build, evaluate, secure, and deploy production Generative AI systems — and prove they work
with real numbers.

---
---

# VERSION 2 — ONE-PAGE LEAFLET

# Generative AI Engineering
### Build. Measure. Deploy.
**11 Modules + Capstone · Hands-on Labs · Python Prerequisite**

---

**01 · Generative AI & LLM Foundations**
How LLMs work, prompt engineering, and cost from day one

**02 · ML Foundations for GenAI**
Regression, neural networks, and what training really means

**03 · Transformers & Attention**
Self-attention, encoders and decoders, decoding methods

**04 · Embeddings & Semantic Representation**
Word2Vec to modern embeddings, and the math behind search

**05 · Hugging Face & Open-Source LLMs**
Fine-tune your own model; run Llama, Mistral, and Groq

**06 · LangChain Essentials**
LCEL, prompt templates, streaming, and multi-provider setup

**07 · Structured Output & Model I/O**
Pydantic contracts, tool schemas, and document loaders

**08 · RAG I — Chunking & Vector Search**
Build a document Q&A system with FAISS and Chroma

**09 · RAG II — Reranking & Evaluation**
Hybrid search, cross-encoders, and RAGAS scoring

**10 · LangGraph — Memory & Agents**
Tool-calling agents, state, and human-in-the-loop control

**11 · Agent Safety & Deployment**
Prompt injection defense, FastAPI serving, and monitoring

**Capstone Project**
Ship a production system — measured, deployed, and defended

---

### You Will Build
A fine-tuned model · A document Q&A system · An evaluated RAG pipeline ·
An AI agent · A deployed, monitored API

### Stack
Python · PyTorch · Hugging Face · LangChain · LangGraph · Pydantic ·
FAISS · RAGAS · LangSmith · FastAPI · Ollama

### For
Developers moving into AI · Data scientists · Final-year and PG students · Technical leads

> **What makes this different:** most courses teach you to call an API.
> This one teaches you to prove it works, secure it, and ship it.

---
---

# COPYWRITING NOTES (internal — remove before printing)

**Lead with Modules 9 and 11.** Evaluation and security are the two things almost no competing
brochure lists. "Prove it works with numbers" and "secure your agents" are claims competitors cannot
match. Consider pulling them into the headline area rather than leaving them at positions 9 and 11.

**Modules 2–3 are the credibility signal.** Most short courses skip transformers and jump to
LangChain. "You'll understand attention, not just call an API" separates this from API-wrapper
courses — good for the "why us" section.

**Module 5 is the proof of substance.** "Fine-tune your own model" is concrete and verifiable.
Many courses at the same price never train anything.

**Headline options:**
- Build. Measure. Deploy. *(current — recommended, matches the course's actual discipline)*
- From Prompt to Production
- Beyond the API Call
- Generative AI You Can Actually Ship

**Avoid:** "Master AI in 11 modules", "Become an AI expert", any income or placement guarantee.
The audience for this course is technical and will discount the whole brochure for one inflated claim.
