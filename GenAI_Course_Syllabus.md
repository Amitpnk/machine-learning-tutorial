# Generative AI Engineering — Course Syllabus

**Course Title:** Generative AI Engineering: From Foundation Models to Production Systems
**Course Code:** GENAI-501
**Duration:** 16 weeks (96 contact hours) — 6 hours/week
**Weekly Split:** 2 h concept lecture · 3 h supervised lab · 1 h code review / paper discussion
**Level:** Advanced undergraduate, postgraduate, or professional certificate
**Credits:** 6 (equivalent) · **Cohort size:** 20–40 with 1 instructor + 1 TA
**Delivery:** In-person or hybrid; every module is lab-first and graded on working software
**Core Stack:** Python 3.11+, PyTorch, HuggingFace, LangGraph, MCP

> **Relationship to the ML course:** This is the deep, standalone Generative AI track. It expands
> Part III of [`ML_GenAI_Course_Syllabus.md`](ML_GenAI_Course_Syllabus.md) from 5 weeks into a full
> 16-week course with its own capstone. Institutions can run the two back-to-back (ML first, GenAI
> second) or run this one alone for students who already know Python and basic ML.

---

## Who This Course Is For

| Audience | Fit |
|---|---|
| CS/IT students in final year or postgrad | Strong fit — this is the employable half of the AI stack |
| Working software engineers moving into AI | Strong fit — assumes engineering maturity, not a research background |
| Data scientists / ML engineers | Strong fit — fills the gap between "trains models" and "ships LLM systems" |
| Absolute beginners to programming | Not a fit — take a Python + ML foundations course first |

### Prerequisites

**Required**
- Python: functions, classes, decorators, type hints, virtual environments
- Git and GitHub: branch, commit, pull request
- REST APIs and JSON; ability to read library documentation
- Comfort with the command line

**Assumed, but re-taught briefly in Week 0**
- Basic ML vocabulary: training/validation split, overfitting, gradient descent, embeddings
- Basic linear algebra: vectors, matrices, dot products
- Neural network basics: layers, loss, backpropagation (conceptual depth is enough)

**Explicitly NOT required**
- Prior LLM, deep learning, or research experience
- Owning a GPU — every lab has a Colab / free-tier path

> **Placement check (Week 0):** a 60-minute diagnostic — write a Python class with type hints, call a
> REST API and parse the JSON, explain what a train/test split is for, and clone + run a repo.
> Students failing two or more items should take the foundations course first.

---

## Course Outcomes

By the end of this course, a student can:

| # | Outcome | Bloom Level | Assessed By |
|---|---|---|---|
| CO1 | Explain how modern generative models work — tokenization, attention, pretraining, post-training, decoding | Understand | Quizzes, Week 2 mini-GPT |
| CO2 | Engineer prompts and context windows as a budgeted, testable, cost-aware resource | Apply | Labs 3–4, Project 1 |
| CO3 | Build and measurably improve a retrieval system over messy real documents | Create | Project 1, Lab 6 |
| CO4 | Adapt an open-weights model with LoRA/QLoRA and preference tuning, and prove it beat the prompted baseline | Create | Labs 7–8 |
| CO5 | Design and ship an agent that uses tools safely, including a custom MCP server | Create | Project 2, Lab 10 |
| CO6 | Work across modalities: vision-language, document AI, image generation, and voice | Apply | Labs 11–12 |
| CO7 | Optimize, serve, monitor, and cost-govern a GenAI system in production | Analyze | Labs 13–14, Capstone |
| CO8 | Evaluate, red-team, and govern a system against safety, security, and regulatory requirements | Evaluate | Lab 15, Capstone defense |

**The evaluation thread.** Evals are not a Week 15 topic in this course. From Week 4 onward, *every*
lab submission must include a test set and a number. A change without a measurement is not accepted
as an improvement. This single habit is what separates people who ship GenAI from people who demo it.

---

## Course Structure

| Part | Weeks | Focus | Ends With |
|---|---|---|---|
| **Week 0** | 0 | Bridge & setup | Environment verified, diagnostic passed |
| **Part A — Foundations** | 1–4 | How generative models work; prompting, reasoning, context, evals | Graded eval harness |
| **Part B — Grounding & Adaptation** | 5–8 | Embeddings, RAG, fine-tuning, alignment | **Project 1: RAG system** |
| **Part C — Agents & Multimodal** | 9–12 | Tools, orchestration, MCP, vision, voice | **Project 2: Agent + MCP server** |
| **Part D — Production & Governance** | 13–16 | Serving, LLMOps, safety, capstone | **Capstone + defense** |

---

# WEEK 0 — BRIDGE & SETUP

### Pre-Course Week (self-paced, ~6 hours, mandatory, ungraded)

**Environment:**
- Python 3.11+ with `uv`; project scaffold, pinned dependencies, pre-commit hooks
- VS Code / Cursor / Claude Code; Jupyter; Google Colab account
- API keys for at least one frontier provider; Ollama installed for local open-weights models
- Repo hygiene: one Git repo per student, used for every lab in the course

**ML refresher — only what this course actually needs:**
- Vectors, dot products, cosine similarity — the math behind embeddings
- Gradient descent and loss, at intuition depth
- What "training", "inference", "parameters", and "checkpoint" really mean
- Train/validation/test discipline, and why leakage invalidates every result that follows

**AI-assisted development, done honestly:**
- Coding agents as a learning accelerator, not a substitute for understanding
- The course rule: you may generate code, you must be able to explain and defend every line
- Verifying generated ML code — where agents confidently produce plausible nonsense

**Deliverable:** a working repo that runs `hello_llm.py` against both a hosted API and a local Ollama
model, printing token counts and cost for each.

---

# PART A — FOUNDATIONS OF GENERATIVE MODELS

## Module 1: The Generative AI Landscape & How LLMs Work
### Week 1 — What You Are Actually Programming Against

**Framing the field:**
- AI vs. ML vs. deep learning vs. generative AI vs. "AI engineering" — precise definitions
- The three eras: task-specific models → pretrained transfer → foundation models as a platform
- What changed for engineers: you no longer train the model, you *compose systems around* it
- The current model landscape: frontier APIs (Claude, GPT, Gemini families) vs. open weights
  (Llama, Qwen, Mistral, DeepSeek, Gemma) — capability tiers, licensing, and where each wins

**How an LLM produces text:**
- Tokenization: BPE, vocabulary, why token counts ≠ word counts, why non-English costs more
- Pretraining: next-token prediction, data scale, compute, and what the model actually learns
- Post-training: instruction tuning, preference tuning, and the resulting "assistant" persona
- Context windows: what goes in them, what they cost, how attention scales with length
- Decoding: greedy, temperature, top-k, top-p, min-p, repetition penalty
- Why models hallucinate: next-token likelihood is not a truth signal
- Scaling laws and their limits; why "just make it bigger" stopped being the only lever

**Engineering economics from day one:**
- Tokens in / tokens out / cached tokens — the actual billing model
- Latency components: time-to-first-token vs. tokens-per-second
- Capability-per-dollar: choose a model tier per *task*, not per project
- Small language models and on-device inference — when 4B beats 400B in practice

**Hands-on Lab:**
- Tokenize the same paragraph with three tokenizers; measure cost differences across languages
- Sweep temperature and top-p on one prompt; chart output diversity vs. factual drift
- Benchmark three model tiers on one task: accuracy, latency, cost per 1,000 calls
- Run a 7B open-weights model locally with Ollama; compare it honestly against a frontier API

**Reading:** provider docs on tokens and pricing; *AI Engineering* (Huyen), Ch. 1–2

---

## Module 2: Transformer Internals
### Week 2 — Open the Box, Then Build a Small One

> This is the one deliberately deep week. Students who understand attention debug LLM systems
> qualitatively better than students who treat the model as a black box.

**Architecture:**
- Embeddings and positional encoding: absolute → RoPE, and why position handling limits context
- Self-attention: queries, keys, values — mechanically, with a worked numeric example
- Multi-head attention, residual stream, layer norm (pre-norm vs. post-norm)
- Feed-forward blocks, and why most parameters live there
- Decoder-only vs. encoder-decoder; why decoder-only won for general-purpose generation

**Modern architecture changes worth knowing:**
- Grouped-query and multi-query attention — the KV-cache memory problem
- FlashAttention, and why memory bandwidth rather than FLOPs is the bottleneck
- Mixture-of-Experts: sparse activation, routing, active vs. total parameters
- Long-context techniques and their real degradation ("lost in the middle")
- State-space and hybrid architectures — where they are actually being used

**Inference mechanics that show up in your bill:**
- Prefill vs. decode; why input tokens are cheap and output tokens are not
- The KV cache: what it stores, how it grows, why batch size hits a memory wall
- Prompt caching: what gets cached, cache-aware prompt ordering, realistic savings

**Hands-on Lab:**
- Implement scaled dot-product attention in NumPy, then PyTorch; verify against `nn.MultiheadAttention`
- Train a character-level mini-GPT on a small corpus, end to end, from scratch
- Visualize attention maps; identify induction-like heads
- Measure KV-cache growth and latency as context length increases; plot the curve

**Reading:** *Attention Is All You Need*; Karpathy, *Neural Networks: Zero to Hero*;
Raschka, *Build a Large Language Model (From Scratch)*, Ch. 3–4

---

## Module 3: Prompting, Structured Output & Reasoning Models
### Week 3 — Making Models Do Exactly What You Need

**Prompt engineering that survives contact with production:**
- Zero-shot, few-shot, chain-of-thought — what each is actually for
- Instruction placement, delimiters, role framing, and explicit output contracts
- Few-shot example selection: coverage, ordering effects, dynamic selection
- Decomposition and prompt chaining vs. one heroic mega-prompt
- Self-consistency, best-of-N, and verifier patterns
- Anti-patterns: politeness padding, contradictory instructions, unbounded output specs

**Structured output — the backbone of every real integration:**
- Why free text is unusable downstream
- JSON mode, tool-call schemas, and constrained/grammar-based decoding
- Pydantic with Instructor / Outlines; validation, retries, and repair loops
- Designing schemas a model can fill reliably (flat beats deeply nested)
- Enum-and-null design, so "I don't know" is a parseable answer rather than a hallucination

**Reasoning models and test-time compute:**
- Reasoning models vs. instruct models — what actually differs
- Extended thinking / reasoning tokens: how they are billed, how to budget them
- Test-time compute scaling: spending at inference instead of training bigger
- Prompting reasoning models *differently* — why chain-of-thought instructions can hurt them
- Choosing: when a reasoning model is worth 10× the cost, and when it is pure waste

**Hands-on Lab:**
- Build a prompt-variant harness: 5 variants × a labeled test set, scored automatically
- Force schema-valid extraction from 200 messy support tickets; report validity and repair cost
- Head-to-head reasoning vs. instruct model on a multi-step task — accuracy, latency, cost, recommendation
- Break your own prompt: find three inputs producing invalid or unsafe output, then fix it

---

## Module 4: Context Engineering & Evaluation
### Week 4 — The Two Skills That Actually Separate Engineers

**Context engineering:**
- Beyond prompt engineering: the context window as a managed budget
- What competes for space: instructions, examples, retrieved chunks, tool results, history
- Context rot: measurable quality decay as the window fills
- Compaction, rolling summarization, and progressive disclosure
- Memory architectures: scratchpads, episodic memory, user profiles — and what to persist
- Cache-aware ordering: stable prefix first, volatile content last
- Multi-turn state: what to carry forward, what to drop, what to re-retrieve

**Evaluation — introduced here, required from here on:**
- Why "it looks good" fails: non-determinism, cherry-picking, demo bias
- Building a golden test set from real inputs (50 real examples beat 5,000 synthetic ones)
- Deterministic checks first: schema validity, regex, exact match, execution-based tests
- LLM-as-judge: rubric design, pairwise comparison, position-bias mitigation, calibration
- Meta-evaluation: measuring the judge itself against human labels
- Regression suites, CI gates, and the "no unmeasured merges" rule
- Cost and latency as first-class eval metrics, not afterthoughts

**Hands-on Lab:**
- Build a reusable eval harness (pytest + a judge) that every later lab in this course imports
- Construct a 60-example golden set with a documented labeling rubric
- Demonstrate context rot: hold the question fixed, grow the context, chart the accuracy decay
- Cut a working prompt's cost by 40%+ via caching and compaction without losing eval score

> **Assessment note:** the Week 4 harness is graded infrastructure. Every later lab is submitted with
> its eval output attached. Unmeasured submissions are returned ungraded.

---

# PART B — GROUNDING & ADAPTATION

## Module 5: Embeddings & Vector Search
### Week 5 — Semantic Retrieval From First Principles

**Embeddings:**
- What an embedding is; how embedding models are trained (contrastive objectives)
- Choosing one: quality vs. dimension vs. cost vs. multilingual support; reading MTEB critically
- Matryoshka embeddings and dimension truncation for cheap scale
- Similarity metrics: cosine, dot, Euclidean — and when the choice actually matters
- Domain adaptation: fine-tuning an embedding model on your own pairs
- Symmetric (similarity) vs. asymmetric (query→document) embedding tasks

**Vector search at scale:**
- Exact vs. approximate nearest neighbor; the recall/latency tradeoff
- Index structures: HNSW, IVF, product quantization — the parameters that matter
- Vector databases: FAISS, ChromaDB, pgvector, Qdrant, Pinecone, Weaviate — selection criteria
- Metadata filtering, and the pre- vs. post-filtering performance trap
- Multi-tenancy, access control, and per-user document isolation
- Incremental indexing, deletes, and re-embedding when you change models

**Hands-on Lab:**
- Build a semantic search engine over 10,000 documents; measure recall@k against labeled queries
- Compare three embedding models on the *same* retrieval set — cost, latency, recall
- Tune HNSW parameters; chart the recall vs. latency frontier
- Implement per-user access filtering and prove no cross-tenant leakage with a test

---

## Module 6: Retrieval-Augmented Generation
### Week 6 — Grounding Models in Real, Messy Data

**Baseline RAG:**
- The loop: ingest → chunk → embed → index → retrieve → assemble → generate → cite
- Chunking: fixed, recursive, semantic, document-structure-aware; overlap tradeoffs
- Real ingestion: PDFs, tables, scans, slide decks, code, HTML — the actual hard part
- Prompt assembly, citation requirements, and forced refusal when retrieval comes back empty

**Advanced retrieval:**
- Hybrid search: dense + BM25 with reciprocal rank fusion
- Rerankers: cross-encoders and late-interaction models — usually the single biggest win
- Query transformation: rewriting, decomposition, multi-query, HyDE
- Contextual retrieval: enriching each chunk with document context before embedding
- GraphRAG: knowledge graphs for multi-hop and "summarize across everything" questions
- Agentic RAG: letting the model decide whether, what, and how many times to retrieve
- Long-context vs. RAG vs. both — a cost-and-accuracy decision, not an ideology

**RAG evaluation:**
- Two failure surfaces, measured separately: retrieval quality and generation quality
- Retrieval metrics: recall@k, MRR, NDCG — and building the labeled set to compute them
- Generation metrics: faithfulness, answer relevance, context precision (RAGAS)
- Attribution and citation-accuracy checking
- Diagnosing "the RAG is bad": a decision tree from symptom to root cause

**Hands-on Lab (Project 1 build week):**
- Ingest a messy real corpus (300+ pages, including tables and scans) into a working pipeline
- Establish a baseline score, then add hybrid search, then a reranker — quantify each delta
- Build a RAGAS suite; justify every pipeline change with a number
- Implement citations and a refusal path; adversarially test that it refuses when it should

---

## Module 7: Fine-Tuning & Model Adaptation
### Week 7 — Teaching a Model New Behavior

**The decision framework, taught before any training runs:**
- The escalation ladder: prompt → few-shot → context/RAG → fine-tune → pretrain (almost never)
- What fine-tuning is good at: format, tone, narrow tasks, latency and cost reduction
- What it is bad at: injecting facts, keeping knowledge current
- Total cost of ownership: training, serving, re-training on model upgrades, eval maintenance

**Supervised fine-tuning:**
- Dataset construction: instruction/response format, chat templates, prompt masking
- Data quality over quantity — why 1,000 curated examples beat 100,000 scraped ones
- Synthetic data generation and distillation from a stronger teacher (and its license limits)
- Deduplication, contamination checks, and holding out an honest test set
- Full fine-tuning vs. PEFT; the memory math for a given GPU
- LoRA: rank, alpha, target modules — what each knob actually changes
- QLoRA: 4-bit base weights, training a large model on one consumer GPU
- Serving adapters: merging vs. hot-swapping multiple LoRAs behind one base model

**Hands-on Lab:**
- Build an instruction dataset from raw domain data, including a synthetic augmentation pass
- Fine-tune a small open model with LoRA and QLoRA on a single GPU/Colab; log with W&B
- Detect overfitting and catastrophic forgetting with a regression suite of general tasks
- Report the honest result: did the fine-tune beat a good prompt? Sometimes it will not — say so

---

## Module 8: Preference Tuning, Alignment & Reasoning Training
### Week 8 — How Models Learn What "Good" Means

**Why SFT alone is not enough:**
- Imitation vs. preference: the model learns *an* answer, not the *better* answer
- The alignment problem in practical terms: helpfulness, harmlessness, honesty tradeoffs

**Preference methods:**
- Reward models: how they're trained, and where they fail (reward hacking, distribution shift)
- RLHF with PPO — conceptual, with an honest account of its complexity
- DPO and ORPO: preference optimization without a separate reward model
- Building preference data: human pairs, AI feedback (RLAIF), constitutional-style critique
- GRPO and group-relative methods — why they became the practical default for reasoning

**Reinforcement learning with verifiable rewards:**
- Where a *programmatic* grader exists: math, code, unit tests, schema validity, tool success
- How reasoning models are trained this way, and why it generalizes better than reward-model RL
- Designing your own verifiable reward for a domain task
- Reward hacking in the wild: models that pass your check without doing the job

**Evaluating an adapted model:**
- Held-out task evals, general-capability regression, side-by-side human review
- Deciding to ship, iterate, or abandon — with a written recommendation

**Hands-on Lab:**
- Build a preference dataset (200+ pairs) with a documented annotation rubric
- Run DPO on the Week 7 SFT checkpoint; compare base / SFT / DPO on the same eval set
- Design a verifiable reward for a code or extraction task; train a small policy against it
- Break your own reward function — find an output that scores well and is obviously bad

> **Project 1 (RAG system) due:** 20-minute demo + evaluation report + failure analysis.

---

# PART C — AGENTS & MULTIMODAL SYSTEMS

## Module 9: Agent Foundations
### Week 9 — From Chatbot to System That Acts

**The agent loop:**
- ReAct: reason → act → observe → repeat; and how the loop terminates
- Tool/function calling: schema design, argument validation, error surfaces
- Writing tool descriptions the model can actually use — the most underrated skill in agents
- Tool granularity: a few powerful tools vs. many narrow ones
- Returning errors the model can recover from (and never returning raw stack traces)

**State and memory:**
- Short-term scratchpads, structured state objects, message-history management
- Long-term memory: vector, key-value, and profile memory; what to persist and what to expire
- Context compaction inside long agent runs

**Planning and reliability:**
- Task decomposition, reflection, self-critique — where each genuinely helps
- Deterministic workflows vs. autonomous agents: the boring choice is usually the right one
- Failure modes: infinite loops, tool thrashing, silent partial failure, cost blowups
- Bounding agents: step limits, timeouts, spend caps, circuit breakers
- Idempotency and retries for tools with real side effects

**Hands-on Lab:**
- Build a tool-using agent from scratch, no framework — the loop, the parser, the error handling
- Add three real tools: web search, a calculator, and a filesystem/database tool
- Instrument every step: tokens, latency, cost, tool outcome
- Induce three failure modes deliberately, then fix each with a bound or guardrail

---

## Module 10: Orchestration & the Model Context Protocol
### Week 10 — Frameworks, Multi-Agent Patterns, Standardized Tooling

**Orchestration:**
- LangGraph: state machines, nodes, edges, conditional routing, checkpointing
- Human-in-the-loop interrupts and approval gates
- Multi-agent patterns: supervisor/worker, hand-offs, parallel fan-out with result merging
- When multi-agent genuinely helps — and when one agent with better tools wins
- Framework landscape: LangGraph vs. CrewAI vs. Claude Agent SDK vs. OpenAI Agents SDK
- Durable execution: resuming long-running agents after a crash

**Model Context Protocol:**
- Why MCP exists: the M×N integration problem between agents and systems
- Architecture: hosts, clients, servers; the primitives — tools, resources, prompts
- Transports: stdio for local, HTTP/SSE for remote
- Consuming existing servers (filesystem, database, GitHub, search) from an agent
- MCP vs. plain function calling — choosing per project
- Security: scoping, authorization, and prompt injection arriving *through tool output*

**Building MCP servers with FastMCP:**
- The ecosystem untangled, and why online tutorials contradict each other:
  the low-level `mcp` protocol SDK · **FastMCP 1.0** (donated into the official SDK as
  `mcp.server.fastmcp`) · **FastMCP 2.0** (separately maintained, with auth, testing, deployment)
- Decorator-based servers: `@mcp.tool`, `@mcp.resource`, `@mcp.prompt`
- Type hints and docstrings *as* the schema; Pydantic models for complex arguments
- Context injection: logging, progress reporting, and sampling from inside a tool
- Local debugging with the MCP Inspector; in-memory testing with the FastMCP client
- Composition: mounting and proxying servers; generating one from OpenAPI or a FastAPI app
- Auth and deployment: bearer tokens, OAuth, remote hosting

**Agent evaluation:**
- Trajectory evaluation: grading the steps taken, not only the final answer
- Tracing multi-step runs (LangSmith / Langfuse); reading a trace to find the real failure
- Regression testing agents despite non-determinism

**Hands-on Lab (Project 2 build week):**
- Rebuild Week 9's agent in LangGraph with checkpointing and a human-approval gate
- Build a custom MCP server exposing a database and an internal API as safe tools
- Test it with FastMCP's in-memory client under pytest — no subprocess, no live model
- Wrap an existing FastAPI service as an MCP server in under 20 lines
- Connect it to an agent client and trace a full multi-step run end to end

---

## Module 11: Multimodal AI — Vision, Documents & Image Generation
### Week 11 — Beyond Text

**Vision-language models:**
- How VLMs work: vision encoder, projection layer, unified token stream
- Capabilities and limits: image QA, chart/diagram reading, UI understanding, spatial grounding
- Image cost mechanics: resolution, tiling, detail settings — images are expensive tokens
- Document AI: invoices, forms, IDs, scanned PDFs → validated structured JSON
- Layout-aware extraction, confidence handling, and when to route to a human
- Multimodal RAG: indexing figures, charts, and screenshots alongside text

**Image and video generation:**
- Diffusion models: forward/reverse process, denoising, latent diffusion — conceptually
- Text-to-image conditioning, classifier-free guidance, samplers and step counts
- Control: ControlNet, inpainting, image-to-image, structural conditioning
- Personalization: LoRA and textual inversion on a small image set
- Quality control in practice, plus provenance and watermarking (C2PA) obligations
- Video generation: current capability, cost, and where it is genuinely usable

**Hands-on Lab:**
- Build a document-extraction pipeline: scanned PDFs → schema-validated JSON, with an accuracy report
- Add a confidence threshold and a human-review queue for low-confidence extractions
- Build multimodal RAG that retrieves both passages and diagrams to answer a question
- Fine-tune an image-generation LoRA on 15–20 images; evaluate it against the base model

---

## Module 12: Voice, Realtime & Computer-Using Agents
### Week 12 — Agents in the Interaction Loop

**Speech:**
- ASR: Whisper-family architecture, streaming vs. batch, word-level timestamps
- Diarization, code-switching, accents, and noisy real-world audio
- TTS: modern neural voices, prosody control, and the consent line on voice cloning

**Realtime voice agents:**
- The latency budget: capture → ASR → LLM → TTS → playback, measured stage by stage
- Speech-to-speech models vs. the cascaded pipeline — quality, control, debuggability
- Turn detection, barge-in, and graceful handling of silence and interruption
- Tool calling inside a voice loop without dead air

**Computer-use and coding agents:**
- Browser and computer-use agents: what works now, what still fails
- How coding agents work: file tools, shell access, and verification/test loops
- Sandboxing untrusted execution: containers, network egress rules, filesystem scoping
- Evaluating an agent that acts on real systems, safely

**Hands-on Lab:**
- Build a realtime voice assistant; instrument and report latency at every stage
- Optimize toward sub-second perceived response, and document what you traded away
- Build a sandboxed coding agent that writes a function, runs tests, and iterates until green
- Give a browser agent a real 5-step task; log where and why it fails

> **Project 2 due:** an agent system with a custom MCP server, traces, and a trajectory eval.

---

# PART D — PRODUCTION, GOVERNANCE & CAPSTONE

## Module 13: Inference Optimization & Serving
### Week 13 — Making It Fast and Affordable

**The cost reality:**
- Inference dominates lifetime spend; a demo costing $0.30/request is not a product
- Latency budgets: TTFT vs. throughput, and which one users actually feel
- The accuracy / latency / cost triangle, made explicit per feature

**Compression:**
- Quantization: INT8, INT4, FP8 — what precision you lose and where it shows up
- Post-training quantization (GPTQ, AWQ, bitsandbytes) vs. quantization-aware training
- Distillation: training a small student on a large teacher's outputs for your narrow task
- Pruning and sparsity — realistic expectations
- Measuring degradation on *your* eval set, not on a public benchmark

**Serving:**
- vLLM and SGLang: PagedAttention, continuous batching, prefix caching
- Speculative decoding and draft models
- Batching strategy, concurrency limits, and queueing behavior under load
- Structured-output-aware serving; guided decoding at scale
- GPU sizing, memory math, and cold-start behavior
- Self-hosted vs. API: the honest break-even calculation

**System-level cost engineering:**
- Semantic caching and exact-match caching
- Model routing: cascade cheap → escalate hard cases, with a router you can measure
- Prompt compression and context trimming
- Batch/offline tiers for non-interactive work

**Hands-on Lab:**
- Quantize a fine-tuned model to INT4; chart quality loss vs. memory and throughput gain
- Serve it with vLLM; load-test at 1/10/50 concurrent users; chart TTFT and throughput
- Build a two-tier router; report accuracy retained and money saved on a real traffic sample
- Produce a one-page cost model for 100k requests/month: self-hosted vs. API, with break-even

---

## Module 14: LLMOps & Deployment
### Week 14 — From Notebook to Something You Can Operate

**Deployment:**
- FastAPI service design for LLM apps: streaming, timeouts, backpressure, graceful degradation
- Containerization and GPU-aware deployment; Kubernetes at a practical level
- Environment and secret management; key rotation
- Blue-green and canary rollouts for prompt, model, and pipeline changes

**Version everything:**
- Prompts, retrieval configs, model versions, and eval sets — all in Git, all reviewable
- Prompt-change pull requests with eval diffs attached (the core team workflow of this course)
- Reproducibility when a hosted model silently changes underneath you

**Observability:**
- Tracing (LangSmith / Langfuse / OpenTelemetry): spans, tool calls, token accounting
- The metrics that matter: latency percentiles, error taxonomy, cost per request, cache hit rate
- Quality monitoring in production: online evals, sampling for human review, user feedback loops
- Drift: input drift, retrieval-corpus drift, and provider model updates
- Alerting on cost and quality regressions, not just HTTP 500s

**CI/CD for GenAI:**
- Eval suites as CI gates; thresholds; handling non-determinism in tests
- Staging with recorded traffic; shadow deployments
- Incident response for AI systems: rollback paths, and the "turn it off" switch

**Hands-on Lab:**
- Deploy your Project 2 agent as a containerized, streaming FastAPI service
- Wire full tracing; produce a dashboard of latency, cost, and quality per endpoint
- Build a GitHub Actions pipeline that blocks a merge when the eval score drops more than 3%
- Simulate a regression (swap a model version), detect it via monitoring, and roll back

---

## Module 15: Safety, Security & Governance
### Week 15 — Shipping Something You Can Defend

**Security — assume adversarial users:**
- Prompt injection: direct, indirect, and via retrieved or tool-returned content
- The lethal trifecta: private data + untrusted content + external communication
- Data exfiltration paths: markdown images, links, tool arguments, error messages
- OWASP Top 10 for LLM Applications, walked through with live examples
- Agent-specific risk: excessive agency, confused deputy, over-scoped tools
- Defenses that work: least-privilege tools, allowlists, output filtering, human approval,
  sandboxing, and treating *all* model output as untrusted input to the next stage
- Supply chain: model provenance, malicious model files, unpinned MCP servers, dependency risk

**Safety and quality:**
- Guardrails: input classification, output filtering, topic and PII boundaries
- Jailbreak patterns and layered mitigation; why prompt-only defenses fail alone
- Hallucination controls: grounding requirements, citation enforcement, abstention design
- Systematic red-teaming: threat modeling, automated adversarial generation, severity triage

**Responsible AI:**
- Bias in generative systems: measuring it in outputs, not only in training data
- Privacy: PII detection and redaction (Presidio), retention, and provider data policies
- Copyright, licensing, and provenance — for models, training data, and generated output
- Cost and environmental transparency
- Transparency artifacts: model cards, system cards, and user-facing AI disclosure

**Regulation and compliance:**
- EU AI Act: risk tiers, GPAI obligations, timelines, and what a student project must document
- Sectoral overlays: healthcare, finance, education, hiring
- NIST AI RMF and ISO/IEC 42001 as practical checklists
- What auditors actually ask for — and building the paper trail as you go, not afterward

**Hands-on Lab:**
- Red-team a classmate's Project 2 agent; file severity-rated findings with reproductions
- Fix every high-severity finding on your own system and prove each fix with a test
- Implement layered guardrails; measure the false-positive cost on legitimate traffic
- Write your capstone governance pack: model card, risk assessment, data provenance, AI-use disclosure

---

## Module 16: Capstone
### Week 16 — Build, Measure, Defend

**Every capstone must include:**

| Requirement | Evidence |
|---|---|
| A real user problem, scoped to 4 weeks | Written problem statement + an identified user |
| A generative system beyond a single API call | Architecture diagram + repository |
| Retrieval, adaptation, *or* agentic tool use — at least one, done well | Working code |
| A golden eval set with a baseline and a measured improvement | Evaluation report with numbers |
| A cost and latency budget, measured under load | Load-test results |
| Deployed and traced | Live URL or reproducible container + dashboard |
| Security review with red-team findings addressed | Findings log with fixes |
| Governance pack | Model card, risk assessment, AI-use disclosure |
| Honest failure analysis | What broke, and what you would do differently |

**Suggested tracks:**
- **Domain expert assistant** — RAG over a real institutional corpus, with citations and refusal
- **Workflow agent** — a multi-step agent with a custom MCP server against real systems
- **Document intelligence** — a VLM extraction pipeline with human-review routing and SLAs
- **Adapted specialist** — a fine-tuned small model beating a frontier prompt on cost-per-task
- **Voice interface** — a realtime voice agent for a specific operational task
- **Creative tooling** — a controlled image/video generation pipeline with provenance
- **Evaluation infrastructure** — an eval and red-team harness that other teams actually adopt

**Deliverables:** repository · 8-page technical report · deployed demo ·
20-minute defense with live Q&A, including "show me the number that proves this"

> Teams of 1–3. Team size does not change the quality bar; it changes the scope expected.

---

# COURSE ADMINISTRATION

## Assessment & Grading

| Component | Weight | Notes |
|---|---|---|
| Weekly labs (14 graded) | 30% | Working code + eval output; lowest two dropped |
| Weekly quizzes | 10% | 15 minutes, start of lecture, concept recall |
| Project 1 — RAG system (Week 8) | 15% | Demo + eval report + failure analysis |
| Project 2 — Agent + MCP server (Week 12) | 15% | Demo + traces + trajectory eval |
| Capstone (Week 16) | 25% | Report, deployment, governance pack, defense |
| Participation: code review & red-teaming | 5% | Quality of review given, not just received |

| Grade | Score |
|---|---|
| A+ | 90–100% |
| A | 80–89% |
| B | 70–79% |
| C | 60–69% |
| F | Below 60% |

### Lab Rubric (applied to every weekly lab)

| Criterion | Weight |
|---|---|
| It runs from a clean clone, per your own README | 20% |
| Correctness of the core technique | 25% |
| Measurement: test set, baseline, and honest numbers | 30% |
| Analysis: what the numbers mean, what you would do next | 15% |
| Code quality: structure, typing, no leaked secrets | 10% |

> A lab reporting a *negative* result honestly, with clean methodology, scores higher than one
> claiming a win it cannot demonstrate. This is stated on day one and enforced from Week 4.

### Capstone Rubric

| Criterion | Weight |
|---|---|
| Problem framing and scope realism | 10% |
| Technical execution and architecture | 25% |
| Evaluation rigor: baseline, method, honest reporting | 25% |
| Production readiness: deployment, tracing, cost, latency | 15% |
| Safety, security, and governance | 15% |
| Communication: report and defense | 10% |

---

## Academic Integrity & AI-Use Policy

This course teaches AI tooling, so a blanket ban would be incoherent. The policy is disclosure-based.

| Activity | AI assistance |
|---|---|
| Weekly labs | **Allowed and encouraged**; disclose in a `AI_USE.md` per lab |
| Quizzes and diagnostics | **Not allowed** — closed-book, in-person |
| Project and capstone code | **Allowed**; you must explain and defend every line under questioning |
| Written analysis and reports | **Allowed for editing**, not for generating conclusions you did not reach |
| Evaluation results | **Never fabricated** — fabricated numbers are academic misconduct, full stop |

**Enforcement mechanism:** oral defense. Any submission may be selected for a 10-minute viva where
the student explains design decisions and modifies the code live. Inability to explain your own
submission is treated as non-submission. This is announced in Week 0 and applied from Week 1.

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Language & environment | Python 3.11+, `uv`, Docker, pre-commit |
| Core DL | PyTorch, HuggingFace Transformers, Accelerate |
| Model access | Frontier APIs (Claude / GPT / Gemini), Ollama, llama.cpp, LM Studio, vLLM |
| Prompting & structure | Pydantic, Instructor, Outlines |
| Embeddings & vector DBs | sentence-transformers, FAISS, ChromaDB, pgvector, Qdrant |
| RAG frameworks | LangChain, LlamaIndex, rerankers (cross-encoder / ColBERT-style) |
| Fine-tuning | PEFT, TRL, bitsandbytes, Unsloth, Axolotl |
| Agents & protocol | LangGraph, MCP, FastMCP, MCP Inspector, Claude Agent SDK, CrewAI |
| Multimodal | Diffusers, ControlNet, Whisper / faster-whisper, TTS engines |
| Evaluation | pytest, RAGAS, DeepEval, promptfoo, LLM-as-judge harnesses |
| Observability | LangSmith, Langfuse, OpenTelemetry, Weights & Biases |
| Serving & optimization | vLLM, SGLang, TGI, ONNX Runtime, TensorRT-LLM |
| Deployment | FastAPI, Docker, Kubernetes, Ray Serve, GitHub Actions |
| Safety & governance | Presidio, guardrail libraries, OWASP LLM Top 10, EU AI Act checklists |
| Cloud (optional) | AWS Bedrock/SageMaker, Azure AI Foundry, Google Vertex AI |

---

## Schedule Summary

| Week | Module | Topic | Key Skills |
|---|---|---|---|
| 0 | Bridge | Setup & ML refresher | Environment, repo, diagnostic |
| 1 | 1 | LLM landscape & mechanics | Tokens, decoding, model selection, cost |
| 2 | 2 | Transformer internals | Attention, KV cache, MoE, mini-GPT |
| 3 | 3 | Prompting & reasoning models | CoT, structured output, test-time compute |
| 4 | 4 | Context engineering & evals | Context budget, golden sets, LLM-as-judge |
| 5 | 5 | Embeddings & vector search | HNSW, recall@k, hybrid indexes |
| 6 | 6 | RAG | Chunking, reranking, GraphRAG, RAGAS |
| 7 | 7 | Fine-tuning | LoRA, QLoRA, synthetic data, distillation |
| 8 | 8 | Alignment & reasoning training | DPO, GRPO, RLVR, reward hacking |
| 9 | 9 | Agent foundations | ReAct, tool design, bounding, memory |
| 10 | 10 | Orchestration & MCP | LangGraph, FastMCP servers, tracing |
| 11 | 11 | Multimodal & image generation | VLMs, document AI, diffusion, LoRA |
| 12 | 12 | Voice & computer-use agents | ASR/TTS, latency budget, sandboxing |
| 13 | 13 | Optimization & serving | Quantization, vLLM, routing, cost model |
| 14 | 14 | LLMOps | Tracing, CI eval gates, canary, rollback |
| 15 | 15 | Safety & governance | Injection, red-teaming, EU AI Act |
| 16 | 16 | Capstone | Ship, measure, defend |

---

## Compute & Budget (per cohort of 30)

| Weeks | Minimum path | Recommended |
|---|---|---|
| 0–4 | Any laptop + free API tier | 16 GB RAM laptop, modest API credits |
| 5–6 | Laptop + local embeddings | 16 GB RAM; managed vector DB free tier |
| 7–8 | Colab free (T4) with QLoRA | Colab Pro or 24 GB VRAM GPU |
| 9–12 | Laptop + API credits | Same, plus a shared GPU for local models |
| 13–14 | Colab Pro | 24 GB+ VRAM GPU or hourly A100/H100 rental |
| 15–16 | Cloud free tier | Cloud credits for deployment |

**Budget guidance:** roughly **$40–80 per student** in API credits across the term, plus optional GPU
rental in Weeks 7–8 and 13. Costs drop substantially if the institution provides one shared
24 GB GPU box for fine-tuning and serving labs. Every lab is designed with a free-tier fallback path,
and Week 1 teaches cost measurement precisely so students do not burn credits by accident.

**Institutional prerequisites:** shared GitHub organization, a vector DB instance (pgvector on
existing Postgres is sufficient), one GPU box or Colab Pro allocation, and provider API accounts with
per-student spend caps.

---

## Faculty Notes

- **Highest-risk weeks:** Week 2 (transformer internals — allocate extra TA time) and Week 8
  (preference tuning — training instability frustrates students; provide a known-good config).
- **The habit that makes this course work:** refuse ungraded, unmeasured submissions from Week 4.
  It feels harsh for two weeks and then transforms the cohort's engineering quality.
- **Guest lecture slots that land well:** an AI engineer discussing a production incident (Week 14),
  and a security professional running a live injection demo (Week 15).
- **Refresh policy:** the model landscape shifts every term. Re-verify model names, pricing, and
  library APIs before each cohort; the *concepts* in this syllabus are stable, the *product names*
  are not. Weeks 1, 3, 10, and 13 need the most frequent updating.
- **Common failure to pre-empt:** students reaching for fine-tuning when prompting or RAG would win.
  Week 7's decision framework is taught before any training code for exactly this reason.

---

## Career Alignment

| Role | Modules that matter most |
|---|---|
| AI / LLM Engineer | 3, 4, 6, 9, 10, 13, 14 |
| RAG / Search Engineer | 5, 6, 13, 14 |
| Agent Engineer | 9, 10, 12, 15 |
| Applied ML Scientist (GenAI) | 2, 7, 8, 11 |
| LLMOps / Platform Engineer | 13, 14, 15 |
| AI Safety / Governance Analyst | 4, 15 |
| Multimodal / Document AI Engineer | 11, 12 |

Portfolio produced by course end: a mini-GPT, a reusable eval harness, an evaluated RAG system, a
fine-tuned and preference-tuned model with an honest comparison report, an agent with a custom MCP
server, a deployed and traced service with a cost model, and a red-teamed capstone with a governance
pack. That is a defensible portfolio for an AI engineering role.

---

## Self-Study Track

Learning this alone, without the cohort? Follow the same 16 modules, but compress to what builds
durable skill. The order matters more than the pace.

**Weeks 1–4 — build the instincts (non-negotiable).** Do the mini-GPT in Week 2 even though it feels
like a detour; it pays off every time you debug a context or latency problem later. Build the Week 4
eval harness properly and reuse it for everything afterward. Most self-learners skip evals and plateau
permanently at "it seems to work."

**Weeks 5–8 — pick a real corpus you care about.** Your own notes, a codebase, a set of papers, your
organization's docs. The same corpus for RAG, fine-tuning, and preference tuning makes the tradeoffs
visible in a way toy datasets never do.

**Weeks 9–12 — build one agent you would actually use.** Something that touches a real system you own.
Write the MCP server. This is the highest-leverage skill in the course right now.

**Weeks 13–16 — deploy something a stranger can use, then attack it.** Cost model, tracing, red-team.

**Five artifacts to have when you finish:**
1. A mini-GPT you wrote yourself and can explain line by line
2. An eval harness you reuse reflexively on every new prompt
3. A RAG system with a measured before/after improvement
4. An agent with a custom MCP server, deployed and traced
5. A written cost/latency analysis of something you actually shipped

**Time budget:** 10–12 h/week for 16 weeks at cohort pace; 6 h/week over ~28 weeks is a realistic
part-time pace. Do not stretch beyond that — the ecosystem moves faster than a two-year plan survives.

---

## Recommended Resources

### Books
- *AI Engineering* — Chip Huyen (the closest single book to this syllabus)
- *Build a Large Language Model (From Scratch)* — Sebastian Raschka
- *Natural Language Processing with Transformers* — Tunstall, von Werra & Wolf
- *Designing Machine Learning Systems* — Chip Huyen (production discipline)
- *Hands-On Large Language Models* — Alammar & Grootendorst (visual intuition)

### Courses & Reference
- Andrej Karpathy — *Neural Networks: Zero to Hero* (Week 2 companion)
- HuggingFace — LLM Course, Agents Course, Diffusion Course
- DeepLearning.AI — GenAI short courses (good per-topic, weak on integration)
- Model Context Protocol — official spec and reference servers (modelcontextprotocol.io)
- FastMCP documentation (gofastmcp.com)
- LangGraph documentation and cookbooks
- vLLM documentation
- Provider engineering docs (Anthropic, OpenAI, Google) — prompting, tool use, structured output

### Staying Current (assign one per week, student-presented)
- Papers: arXiv cs.CL and cs.AI, filtered through Papers With Code
- Practitioner sources: provider engineering blogs, LangChain/LlamaIndex blogs, Simon Willison's blog
- Leaderboards read *critically*: LMArena, MTEB, SWE-bench — teach benchmark contamination in Week 1
- Regulation: EU AI Act implementation timeline updates

---

## Final Outcome

Graduates can take a vague business problem, choose between prompting, retrieval, fine-tuning, and
agents on evidence rather than fashion, build the system, prove it works with numbers, serve it inside
a cost and latency budget, defend it against a red team, and document it for a regulator.

That is the job. Not "knows what a transformer is" — the job.
