# Generative AI — 10-Module Applied Course (Revised)

**Format:** 10 modules × 4 hours = 40 contact hours
**Split per module:** 1.5 h concept · 2.5 h lab
**Audience:** working developers and final-year students building LLM applications
**Prerequisites:** Python (functions, classes, `pip`/venv), REST APIs and JSON, Git basics
**Stack:** Python 3.11+, LangChain, LangGraph, Pydantic, FAISS/pgvector, FastAPI, AWS Bedrock

> This is a revision of the original 10-module outline. It keeps the same length, the same vendor
> choices, and the same applied character. What changed: evaluation, tool calling/agents, and
> security are now first-class; classical ML and duplicated RAG content were cut to make room; and
> misfiled topics were moved next to the topic they belong with.

---

## Course Outcomes

By the end, a student can:

1. Explain what an LLM is doing well enough to debug it — tokens, context, decoding, cost
2. Get reliable structured output from a model using Pydantic and schema validation
3. Build a RAG system over real documents, and **prove with numbers** that a change improved it
4. Build an agent that calls tools safely, with bounded cost and a human approval gate
5. Serve it behind FastAPI, trace it, and defend it against prompt injection
6. Choose between prompting, RAG, and fine-tuning on evidence rather than fashion

---

## Module 1: AI Foundations & the LLM

**Concepts:**
- AI vs. ML vs. deep learning vs. generative AI — where LLMs sit
- The application layer: chatbots, copilots, agents, extraction pipelines — what's actually built
- What an LLM is: next-token prediction, pretraining, post-training, the "assistant" persona
- LLM properties: context window, knowledge cutoff, non-determinism, hallucination
- Why hallucination happens — likelihood is not truth
- Frontier APIs vs. open weights; capability tiers and when a small model is enough

**Engineering setup:**
- Virtual environments (`venv` / `uv`), pinned dependencies, `.env` secret handling
- Project repo scaffold used for every lab in this course
- First API call: request, response, and reading the usage object

**Token & cost literacy (do not skip):**
- Tokenization: why token count ≠ word count, why Indian languages cost more per sentence
- Input vs. output vs. cached tokens — the actual billing model
- Latency: time-to-first-token vs. total time

**Lab:**
- Set up the course repo; call a hosted model and a local Ollama model from the same interface
- Print tokens and rupee cost for every call; build a tiny cost-logging wrapper you reuse all term
- Compare three model tiers on one task: quality, latency, cost per 1,000 calls

---

## Module 2: Models, Structured Output & Pydantic

**Model landscape:**
- Types of models: text, embedding, reranking, vision, speech — and what each is *for*
- Model classification by access: hosted API, open weights, on-device
- Instruct vs. reasoning models — what changes, and when the extra cost is justified
- A 30-minute grounding in what "training" means, using linear regression as the toy example
  *(this is context, not a topic — do not spend a session on classical ML)*

**Calling models from code:**
- Provider SDKs vs. LangChain's unified interface — the tradeoff
- Messages, roles, system prompts, and multi-turn state
- Streaming responses and why users perceive them as faster
- Error handling: rate limits, timeouts, retries with backoff

**Structured output — the backbone of every real integration:**
- Why free text is unusable downstream
- JSON understanding: parsing, validation, and the failure modes of "just ask for JSON"
- Pydantic models as the output contract: fields, types, validators
- Nested models, `Optional`, `Enum`, and `default_factory` for safe defaults
- Schema design the model can actually satisfy — flat beats deeply nested
- Letting the model say "I don't know" in a parseable way, instead of inventing a value
- Tool/function calling as structured output — introduced here, used in Module 8

**Lab:**
- Extract structured records from 100 messy support tickets into a nested Pydantic model
- Measure schema-validity rate; add a repair loop; measure again
- Deliberately design one bad schema and one good schema for the same task; compare validity rates

---

## Module 3: Prompt Engineering & Evaluation

> Evaluation is introduced here, in week 3, not at the end. Every lab from this point forward is
> submitted with a test set and a number. This is the single change that most improves outcomes.

**Prompting techniques:**
- Zero-shot, few-shot, chain-of-thought — what each is actually for
- Instruction placement, delimiters, role framing, explicit output contracts
- Few-shot example selection: coverage and ordering effects
- Decomposition and chaining vs. one giant prompt
- Prompting reasoning models differently — why "think step by step" can hurt them
- Anti-patterns: politeness padding, contradictory instructions, unbounded output specs

**Controlling generation:**
- Temperature, top-p, top-k — what each knob does and when to touch it
- Temperature 0 is not determinism; what actually varies
- Max tokens, stop sequences, and truncation bugs

**Evaluation — the professional skill:**
- Why "it looks good in the demo" fails
- Building a golden test set from real inputs (50 real examples beat 5,000 synthetic)
- Deterministic checks first: schema validity, exact match, regex, keyword presence
- LLM-as-judge: writing a rubric, pairwise comparison, and checking the judge against humans
- Tracking cost and latency alongside quality

**Lab:**
- Build a reusable eval harness (pytest + a judge) — **every later lab imports this**
- Score 5 prompt variants against a 50-example labeled set; pick a winner on evidence
- Break your own prompt: find three inputs producing wrong or unsafe output, then fix it

---

## Module 4: Transformers & Embeddings

**Transformer internals (concept depth, not research depth):**
- Why transformers replaced RNNs — parallelism and long-range dependency
- Layers of a transformer: embedding → attention → feed-forward → normalization → output
- Self-attention: queries, keys, values, with one worked numeric example
- Multi-head attention and what different heads latch onto
- Encoder vs. decoder vs. encoder-decoder — and why chat models are decoder-only
- Positional encoding, and why long context degrades in the middle

**Decoding:**
- How tokens are actually chosen: greedy, beam search, sampling, top-k, top-p
- Connecting the decoding method back to the temperature behavior seen in Module 3

**Inference mechanics you will pay for:**
- Prefill vs. decode; why input tokens are cheap and output tokens are not
- KV cache: what it stores and why long conversations get slower and costlier
- Prompt caching: cache-aware prompt ordering for real savings

**Embeddings:**
- What an embedding is; how embedding models are trained
- Cosine similarity, dot product, and why cosine is the default
- Choosing an embedding model: quality vs. dimension vs. cost vs. multilingual support
- Text embeddings vs. reranking models — different jobs, common confusion

**Lab:**
- Implement scaled dot-product attention in NumPy; verify against PyTorch
- Visualize attention weights on a short sentence
- Embed 5,000 documents; explore the space; find near-duplicates and outliers by cosine similarity
- Measure latency growth as conversation length increases; plot the curve

---

## Module 5: RAG Foundations & Document Ingestion

**Why RAG:**
- The problem it solves: private data, fresh data, and citations
- The loop: ingest → chunk → embed → index → retrieve → assemble prompt → generate → cite
- RAG vs. long context vs. fine-tuning — a cost-and-accuracy decision

**Ingestion — the part that actually takes the time:**
- Document loaders: PDF, DOCX, HTML, CSV, and scanned pages
- PyPDF vs. layout-aware extraction; when a PDF loader silently mangles tables
- Cleaning: headers, footers, page numbers, OCR noise
- Metadata capture: source, page, section, date, permissions — you will need all of it later

**Chunking:**
- Why chunking exists and what breaks when it's wrong
- Methods: fixed-size, recursive character, token-based, semantic, document-structure-aware
- LangChain text splitters: `RecursiveCharacterTextSplitter`, token splitters, markdown/header splitters
- Chunk size and overlap: the tradeoff, and how to test it rather than guess

**Prompts with RAG:**
- Assembling context: ordering, delimiters, and per-chunk source labels
- Requiring citations in the output schema
- Forced refusal when retrieval returns nothing relevant — designed, not hoped for

**Lab:**
- Build an end-to-end RAG pipeline over a real 300-page corpus including tables and one scanned PDF
- Test three chunking strategies against the Module 3 eval harness; report which won and by how much
- Implement citations and a refusal path; adversarially confirm it refuses when it should

---

## Module 6: Vector Search — FAISS, HNSW & Vector Databases

**Search fundamentals:**
- Exact vs. approximate nearest neighbor; the recall/latency tradeoff
- Similarity metrics revisited: cosine, dot, L2 — and matching the metric to the model
- Why brute force is fine at 10k documents and fatal at 10M

**FAISS:**
- Index types: `IndexFlatL2`, `IndexFlatIP`, `IVF`, `IVFPQ`, `HNSW`
- Building, training, saving, and loading an index
- Product quantization: memory savings vs. recall loss
- ID mapping and keeping metadata in sync with vectors

**HNSW:**
- The graph intuition: navigable small worlds and layered search
- Parameters that matter: `M`, `efConstruction`, `efSearch` — build time vs. query time vs. recall
- Where HNSW beats IVF and where it doesn't

**Production vector stores:**
- FAISS vs. ChromaDB vs. pgvector vs. Qdrant — selection criteria, not brand loyalty
- Metadata filtering, and the pre- vs. post-filtering performance trap
- Access control: per-user document isolation, and testing that it holds
- Incremental indexing, deletes, and the cost of re-embedding when you change models

**Lab:**
- Index 100k vectors in FAISS with three index types; chart recall@k vs. query latency vs. memory
- Tune HNSW `efSearch`; find the knee of the curve for your corpus
- Implement per-user access filtering; write a test proving no cross-tenant leakage

---

## Module 7: Retrieval Quality — Hybrid Search, Reranking & RAG Evaluation

> Most RAG systems fail at retrieval, not generation. This module is where a working demo becomes
> a system you can trust.

**Diagnosing a bad RAG:**
- The two failure surfaces: did we retrieve the right thing, or did we generate badly from it?
- A decision tree from symptom to root cause
- RAG precautions: stale indexes, chunk-boundary loss, metric mismatch, embedding-model drift,
  context stuffing, and citation hallucination

**BM25 and hybrid search:**
- Lexical search: term frequency, inverse document frequency, and what BM25 adds
- Where dense embeddings fail and keywords win: IDs, error codes, product names, exact quotes
- Hybrid retrieval and reciprocal rank fusion; weighting the two signals

**Reranking:**
- Bi-encoder vs. cross-encoder — why cross-encoders are more accurate and much slower
- The two-stage pattern: retrieve 50 cheaply, rerank to 5 accurately
- Cross-encoder reranker models and late-interaction alternatives
- Latency budgeting for a reranker in an interactive app

**Query transformation:**
- Query rewriting, decomposition for multi-part questions, and multi-query retrieval

**RAG evaluation:**
- Retrieval metrics: recall@k, MRR, NDCG — and building the labeled set to compute them
- Generation metrics with RAGAS: faithfulness, answer relevance, context precision
- Citation-accuracy checking
- The rule: no pipeline change ships without a before/after number

**Lab:**
- Baseline your Module 5 pipeline with RAGAS; record the numbers
- Add BM25 + RRF hybrid search; measure the delta
- Add a cross-encoder reranker; measure the delta and the added latency
- Write a one-page recommendation: which changes are worth their cost in production

---

## Module 8: Tool Calling, Agents & LangGraph

> The original outline introduced LangGraph without tool calling. LangGraph without tools is just a
> graph library. This module makes the agent real.

**Tool calling:**
- Function/tool schemas — the same Pydantic skill from Module 2, applied
- Writing tool descriptions the model can actually use (the most underrated skill in agents)
- Argument validation and returning errors the model can recover from
- Tool granularity: a few powerful tools vs. many narrow ones

**The agent loop:**
- ReAct: reason → act → observe → repeat, and how it terminates
- Memory: scratchpads, message history, and long-term vector memory
- Failure modes: infinite loops, tool thrashing, silent partial failure, cost blowups
- Bounding agents: step limits, timeouts, spend caps, circuit breakers

**LangGraph:**
- Why a graph instead of a chain: cycles, branching, and durable state
- `StateGraph`: state schema (a Pydantic/TypedDict model), nodes, edges
- Nodes as functions and nodes as classes; conditional edges and routing
- Checkpointing and resuming a run; human-in-the-loop interrupts and approval gates
- Graph patterns worth knowing: sequential chain, conditional router, supervisor/worker multi-agent,
  parallel fan-out with merge — *these are the "types" that matter, not framework taxonomy*
- Callbacks and streaming: surfacing intermediate steps to the user
- When a plain chain or a deterministic workflow beats an agent — usually

**Agentic RAG:**
- Letting the model decide whether, what, and how many times to retrieve
- Connecting Module 7's retriever as a tool rather than a fixed pipeline step

**Model Context Protocol (30-minute orientation):**
- The M×N integration problem and why MCP exists
- Hosts, clients, servers; tools, resources, prompts
- Consuming an existing MCP server from an agent
- *Optional extension module for institutions with time — building a server with FastMCP*

**Lab:**
- Build a tool-using agent in LangGraph with a Pydantic state model and three real tools
- Add a human-approval interrupt before any write or destructive action
- Convert your Module 7 RAG pipeline into an agentic retriever; compare against the fixed pipeline
- Instrument every step: tokens, latency, cost, tool outcome — then bound the worst case

---

## Module 9: Serving, Safety & Observability

**FastAPI for LLM applications:**
- Endpoint design: request/response models with Pydantic, dependency injection
- Streaming responses (SSE) and why they change perceived latency
- Timeouts, backpressure, and graceful degradation when the provider is slow
- Background tasks for long-running agent runs
- API keys, per-user rate limiting, and spend caps

**AWS Bedrock (as one concrete provider):**
- Model access, IAM, and the invoke/converse APIs
- Bedrock Knowledge Bases and Guardrails — what they give you and what they lock you into
- Bedrock vs. direct provider APIs vs. self-hosted: cost and control tradeoffs
- *The pattern generalizes — Azure AI Foundry and Vertex AI are the same shape*

**Security — assume adversarial users:**
- Prompt injection: direct, and indirect via retrieved documents or tool output
- The lethal trifecta: private data + untrusted content + external communication
- Data exfiltration paths: markdown images, links, tool arguments, verbose errors
- OWASP Top 10 for LLM Applications, walked through with live examples
- Defenses that work: least-privilege tools, allowlists, output filtering, human approval,
  sandboxing, and treating all model output as untrusted input to the next stage

**Guardrails:**
- Input classification and output filtering
- PII detection and redaction before text leaves your system
- Grounding requirements, citation enforcement, and designed abstention
- Measuring the false-positive cost of a guardrail on legitimate traffic

**Observability & cost control:**
- Tracing with LangSmith or Langfuse: spans, tool calls, token accounting
- The metrics that matter: p95 latency, error taxonomy, cost per request, cache hit rate
- Semantic caching and model routing (cheap model first, escalate hard cases)

**Lab:**
- Serve your Module 8 agent behind a streaming FastAPI endpoint with auth and rate limits
- Wire tracing; produce a dashboard of latency, cost, and quality
- Red-team a classmate's system: plant an injection in a document their RAG will retrieve
- Fix every finding on your own system and prove each fix with a test

---

## Module 10: Capstone Project

**Two graded builds across the term** (start Project 1 after Module 7):

**Project 1 — Domain RAG Assistant** *(begun in Module 7, due in Module 9)*
A chatbot over a real corpus with hybrid search, a reranker, citations, and a refusal path.
Must include RAGAS numbers showing the baseline and each improvement.

**Project 2 — Capstone** *(Module 10)*
Choose one:
- **Workflow agent** — LangGraph agent with real tools and a human approval gate
- **Document intelligence** — PDF → validated nested Pydantic records, with a human-review queue
  for low-confidence extractions
- **Domain assistant, productionized** — Project 1 deployed, traced, cost-modeled, and red-teamed
- **Your own** — instructor-approved, same bar

**Every capstone must ship:**

| Requirement | Evidence |
|---|---|
| A real user problem | One-page problem statement naming an actual user |
| Working system, runs from a clean clone | Repository + README |
| Golden eval set with baseline and measured improvement | Eval report with numbers |
| Cost and latency measured | Cost per request, p95 latency |
| Deployed behind FastAPI, traced | Live URL or container + trace screenshots |
| Security review | Injection test results and fixes |
| Honest failure analysis | What broke, what you'd do differently |

**Defense:** 15-minute demo + Q&A, including "show me the number that proves this claim" and
"open this file and explain why you wrote it this way."

---

## Assessment

| Component | Weight |
|---|---|
| Weekly labs (9 graded) | 35% |
| Project 1 — RAG assistant | 20% |
| Capstone project | 30% |
| Quizzes (10 min, start of each module) | 10% |
| Peer red-teaming and code review quality | 5% |

**Lab rubric:** runs from a clean clone (20%) · correctness (25%) · measurement with an honest
baseline (30%) · analysis (15%) · code quality and no leaked secrets (10%).

> A lab reporting an honest negative result with clean methodology scores higher than one claiming
> a win it cannot demonstrate. Say this on day one and enforce it from Module 3.

---

## AI-Use Policy

Teaching AI tooling while banning AI tools is incoherent. Use disclosure instead:

- **Labs and projects:** AI assistance allowed and encouraged; disclose in `AI_USE.md`
- **Quizzes:** closed-book, no AI
- **All code:** you must be able to explain and modify any line under live questioning
- **Evaluation numbers:** never fabricated — this is misconduct, not a style issue

Enforcement is the oral defense, announced in Module 1 and applied from Module 2.

---

## Compute & Budget

| Modules | Requirement |
|---|---|
| 1–4 | Any laptop, 8 GB RAM; free API tier; Ollama for local models |
| 5–7 | 16 GB RAM recommended for local FAISS over 100k vectors |
| 8–9 | API credits; AWS account with Bedrock access and a spend cap |
| 10 | Cloud free tier or a small VM for deployment |

**Budget:** roughly **₹1,500–3,000 (US $20–35) per student** in API credits across the term.
Module 1 teaches cost measurement before students can burn credits accidentally. Every lab has a
local-model fallback via Ollama.

---

## What Changed From the Original Outline

| Change | Reason |
|---|---|
| **Added evaluation (Module 3)** and required numbers in every later lab | The single largest gap; without it students cannot prove anything works |
| **Added tool calling and the agent loop (Module 8)** | LangGraph without tools is a graph library; agents are the top hiring ask |
| **Added security and prompt injection (Module 9)** | Every RAG and agent system built in this course is vulnerable by default |
| **Added token/cost literacy (Module 1)** | Students ship things that cost too much and never find out |
| **Cut linear regression as a topic** | Classical ML; kept only as a 30-minute analogy for "what training means" |
| **Merged three overlapping RAG modules into two** | Original modules 5, 6, 7 had fuzzy, duplicated boundaries |
| **Moved PDF loader → ingestion; cross-encoder → reranking; guardrails → safety** | Each was filed away from the topic it belongs with |
| **Merged the two project modules into one capstone** | Original modules 9 and 10 re-taught Pydantic and prompting already covered |
| **Raised Pydantic details to one coherent topic** | `default_factory` is a five-minute detail, not a syllabus line item |
| **Reframed "types of LangGraph"** as agent patterns | Framework taxonomy is not the transferable skill; patterns are |
