# Agentic AI Engineering — 11-Module Applied Course

**Format:** 11 modules × 4 hours = 44 contact hours
**Split per module:** 1.5 h concept · 2.5 h lab
**Audience:** developers, data/automation engineers, and final-year students who can already call an LLM API
**Prerequisites:** Python (functions, classes, `venv`), REST APIs and JSON, Git basics, and either the
Generative AI course or equivalent working knowledge of LLMs, prompting, and RAG
**Stack:** Python 3.11+, LangChain 1.x, LangGraph 1.x, AG2 (AutoGen 2), CrewAI, n8n, MCP, LangSmith, FastAPI

> **Relationship to the Generative AI course.** This is the sequel, not a standalone. The GenAI course
> ends at "you can build and evaluate a RAG system." This course begins at "now make it decide, act,
> and recover." LLM internals, embeddings, chunking, and prompt engineering are *recapped in 20 minutes*
> in Module 1 and never re-taught. If you teach this as a standalone, add a 4-hour Module 0 covering
> LLM basics, prompting, and RAG — do not stretch the recap.

---

## Course Outcomes

By the end, a student can:

1. Explain the difference between a chain, a single agent, and a multi-agent system — and choose correctly
2. Build a tool-calling agent in LangChain and refactor it into a stateful LangGraph workflow
3. Design agent graphs with conditional routing, persistent memory, and human approval gates
4. Build self-correcting agents (Corrective RAG, reflection loops) instead of one-shot pipelines
5. Orchestrate role-based multi-agent teams in AG2 and CrewAI
6. Ship a production automation in n8n without writing application code, and know when *not* to
7. Expose and consume tools over MCP, and reason about the trust boundary it creates
8. **Prove an agent works** with a trajectory eval set, traces, and cost/latency numbers
9. Defend an agent against direct and indirect prompt injection, and scope its tool permissions
10. Serve an agent behind FastAPI with durable state, streaming, and a spend cap

---

## Source Material Map

This syllabus is built on the existing `Agentic AI/` folder. The status column is the work required before delivery.

| Folder | Maps to | Status |
|---|---|---|
| `1.Introduction_to_AgenticAI` | Module 1 | **Extend** — add agent design patterns; remove the CrewAI line or deliver Module 5 |
| `2.LangChain_AI_Agents` | Module 2 | **Rewrite** — notebook uses removed LangChain 0.1 APIs; will not run |
| `7.LangGraph_Part1` | Module 3 | **Ready** — add the missing `requirements.txt` |
| `8.LangGraph_Part2` | Module 4 | **Ready** — add `requirements.txt`; delete the `Original(1)` duplicate |
| `3.AutoGen` | Module 5 | **Extend** — add the CrewAI half |
| `4.n8n_Agents` | Module 6 | **Ready** — schedule inside one n8n trial window |
| `5.Agents_Automation` | Module 7 | **Ready** — Supabase/SERP credentials must be pre-provisioned |
| `6.MCP` | Module 8 | **Extend** — add the trust/permission discussion |
| — | Module 9 (Evaluation) | **New — build from scratch** |
| — | Module 10 (Security & Deployment) | **New — build from scratch** |
| — | Module 11 (Capstone) | **New — build from scratch** |

---

## Module 1: Agentic AI Foundations & Design Patterns

**Recap, timeboxed to 20 minutes — do not exceed:**
- LLM as next-token predictor; context window, hallucination, non-determinism
- What RAG solved and what it did not

**The actual content:**
- The standalone-LLM ceiling: no math, no fresh data, no side effects, no recovery
- Thought → Action → Observation: the ReAct loop as the atomic unit of agency
- The four properties of an agentic system: autonomy, tools, planning, memory
- **Single agent vs. agentic system** — one goal-directed loop vs. orchestrated specialists
- **Agent design patterns** (the transferable skill, taught as a taxonomy before any framework):
  prompt chaining · routing · parallelization · orchestrator–worker · evaluator–optimizer · autonomous loop
- **When *not* to build an agent** — if a deterministic chain solves it, an agent is a liability
- Framework landscape and honest selection criteria: LangGraph, AG2, CrewAI, n8n, MCP
- Case studies to dissect: Perplexity (search loop), Devin/Lovable (planner + codegen + deploy)

**Engineering setup (do it in class; everyone green before leaving):**
- `venv`/`uv`, the pinned course `requirements.txt`, `.env` secret handling — **no hard-coded keys, ever**
- The course repo scaffold reused in every lab
- Cost-logging wrapper: every lab prints tokens and rupee cost

**Lab:**
- Environment green-check: run the smoke-test notebook; every student prints a successful traced call
- Take 5 real workflows and classify each: deterministic chain, single agent, or multi-agent — justify
- Implement a ReAct loop **by hand in ~40 lines** (no framework) with one search tool and a step cap.
  This is the most valuable lab in the course — every framework afterwards is recognizable as this loop.

---

## Module 2: LangChain Agents & Agentic RAG

> **This module must be rewritten before delivery.** The current notebook uses `langchain.llms`,
> `langchain.chat_models`, `initialize_agent`, `AgentType`, `langchain.vectorstores`, and `RetrievalQA` —
> all removed or relocated in LangChain 1.x, while Modules 3–4 already import `langchain_classic`.
> Mixed-era imports across modules cause dependency conflicts in a single environment.

**Modern LangChain agent construction:**
- `langchain-openai` / provider packages; `init_chat_model` for one-line model swaps
- Defining tools with `@tool`: docstrings are the model's API documentation, not decoration
- Argument schemas with Pydantic; typed returns; error strings the model can actually recover from
- Binding tools, reading `tool_calls`, and running the loop with `create_agent`
- Step limits, timeouts, and recursion caps — bounding an agent is not optional
- Streaming intermediate steps so users see the agent thinking

**Traditional RAG vs. Agentic RAG:**
- Traditional: retrieve once → generate. Where and why it fails
- Agentic: retrieval as a *tool the model chooses to call*, possibly more than once
- Multi-tool agents: retriever + web search + finance/news tool, and how the model picks
- Cost consequence: an agentic RAG call can be 5–10× a plain RAG call. Measure it in the lab.

**Lab:**
- Migrate the legacy agent notebook to LangChain 1.x — students perform the migration as the exercise
- Build an agentic RAG assistant over the Microsoft earnings-call transcript with retriever + web search
- Compare traditional vs. agentic RAG on 20 questions: accuracy, tokens, latency, cost. Report a table.

---

## Module 3: LangGraph Core — State, Routing, Tools, Memory

**Why graphs:**
- The limits of linear chains and opaque agent executors: no branching, no resumption, no inspection
- LangChain vs. LangGraph: build fast vs. build reliable and long-running

**Core mechanics:**
- State as a `TypedDict`; reducers and `add_messages`
- Nodes as pure functions; edges as flow; `START` and `END`
- Conditional edges — routing on state, the foundation of every real agent
- Visualizing and debugging the compiled graph
- LLM inside a node; then tools inside a node with `ToolNode` and `tools_condition`
- Memory: `MemorySaver`, `thread_id`, and what a checkpointer actually persists
- **Durable state** — swapping to a SQLite/Postgres checkpointer, because `MemorySaver` dies with the process

**Worked examples (from `7.LangGraph_Part1`):**
Basic graph → conditional edges → LLM node → tool-using agent (Tavily) → agent with memory → RAG agent

**Lab:**
- Build a conditional-routing graph from a written spec, then extend it with a second branch
- Wikipedia research agent with tools and a step cap (existing lab exercise, extended)
- Add a checkpointer; prove multi-turn recall; then prove isolation across two `thread_id`s
- Swap `MemorySaver` for a SQLite checkpointer and resume a conversation after a kernel restart

---

## Module 4: LangGraph Advanced — Self-Correction, SQL, Human-in-the-Loop

**Self-correcting agents:**
- **Corrective RAG** — grade retrieved documents, rewrite the query, retrieve again, then answer
- Why a validation node between retrieval and generation is the highest-ROI change in most RAG systems
- **Reflection agents** — generate → critique → revise, and setting a stopping condition so it terminates
- Cost/quality tradeoff: reflection multiplies calls. When it earns its keep, and when it does not.

**Agents over structured data:**
- SQL agent with `SQLDatabaseToolkit`: list tables → get schema → generate query → execute
- Why schema-first prevents hallucinated column names
- **Read-only credentials and query validation** — an LLM writing SQL against a writable connection is a
  production incident waiting to happen

**Human-in-the-Loop:**
- `interrupt()` as a durable pause; why HITL requires a checkpointer
- Approval gates before irreversible actions: send, pay, delete, deploy
- Resuming with human input; approve / edit / reject paths
- Designing *which* steps deserve a gate — gate everything and nobody uses it

**Multi-tool agent case study:** the clinical decision-support agent, dissected end to end

**Lab:**
- Build Corrective RAG and measure it against plain RAG on a 30-question set with deliberately noisy docs
- Build a SQL agent on the provided SQLite DB with an approval gate on any non-`SELECT` statement
- Add HITL to your Module 2 agent; demonstrate approve, edit, and reject paths surviving a restart

---

## Module 5: Multi-Agent Systems — AG2 and CrewAI

**Multi-agent theory first:**
- When multiple agents genuinely beat one agent with more tools — and when they are just latency
- Roles, handoffs, termination conditions, and the runaway-conversation failure mode
- Cost multiplication: N agents × M turns. Budget before you build.

**AG2 (AutoGen 2):**
- The Microsoft AutoGen → AG2 fork and what it means for your dependency choice
- `ConversableAgent`, `LLMConfig`, two-agent conversation, termination messages
- Human-in-the-loop modes (`NEVER` / `TERMINATE` / `ALWAYS`)
- Sequential multi-agent chats with `initiate_chats` and context carry-over
- Case study: consumer-lending prescreening — details agent → products agent → documents agent → customer proxy

**CrewAI** *(the module the intro deck promises and the folder is missing — build this)*:
- Role–goal–backstory agent definition; tasks; sequential vs. hierarchical process
- Crew composition: researcher → writer → reviewer
- AG2 vs. CrewAI vs. LangGraph: conversation-driven vs. role-driven vs. state-machine-driven.
  **Deliverable: a one-page selection guide each student writes themselves.**

**Lab:**
- Reproduce the travel-planner crew in both AG2 and CrewAI; compare code volume, control, and token cost
- Build a 3-role crew for a domain of the student's choice with an explicit termination condition
- Break it: force a runaway loop, then bound it with max turns and a termination message

---

## Module 6: No-Code Agents with n8n

> Schedule Modules 6, 7, and the n8n half of Module 8 **consecutively** — n8n Cloud's free trial is
> time-limited. Alternatively, self-host n8n via Docker on a classroom machine (recommended for institutes).

**n8n as an agentic platform:**
- Where no-code wins: integrations, scheduling, ops ownership, non-developer maintainers
- Where it loses: version control, testing, complex state, code review. Be honest about both.
- Nodes, triggers, credentials, and the execution model
- The AI Agent node: model, memory, and tools in a visual graph

**Build-alongs (from `4.n8n_Agents`):**
- Email smart-response agent (Gmail trigger → LLM → reply)
- Cold-email marketing agent
- Interactive Telegram tech-news agent

**Operational reality:**
- Credentials and OAuth scoping — grant the narrowest scope that works
- Error branches, retries, and what happens at 3 a.m. when a node fails
- Exporting workflow JSON into Git as the only real version control you get

**Lab:**
- Import, run, and *modify* all three provided workflows — modification, not import, is the exercise
- Build one original agent from a business brief and export the JSON to the course repo
- Document one failure mode you introduced and the error branch that catches it

---

## Module 7: Advanced n8n — RAG, Webhooks & Data Agents

**RAG inside n8n:**
- Google Drive ingestion → chunking → embeddings → Supabase vector store
- Provisioning pgvector in Supabase: SQL setup, project URL, service-role key, table creation
- Retrieval node wired into an agent; the Ayurvedic-guru knowledge assistant as the worked example

**Integration agents:**
- Webhook-triggered agents: the door you just opened to the public internet
- LinkedIn lead generation with and without a SERP API
- Web-scraping agents — and the legal/ToS conversation that must accompany them
- Chaining workflows; sub-workflows as reusable functions

**Deployment:**
- n8n Cloud vs. self-hosted Docker; environment variables; backups
- Cost model: execution-based pricing vs. token cost

**Lab:**
- Build the Supabase RAG workflow end to end over a document set you supply
- Build a webhook agent, then **secure it** — auth header, payload validation, rate limit
- Take one Module 6 workflow to "handover quality": documented, error-handled, JSON in Git

---

## Module 8: Model Context Protocol (MCP)

**The problem MCP solves:**
- The aggregator intuition (MakeMyTrip → many hotels) and why bespoke API integration does not scale
- N×M integrations vs. N+M: the actual argument for a protocol
- APIs vs. MCP: who writes the adapter, and who owns the schema

**Mechanics:**
- Hosts, clients, and servers; tools, resources, and prompts
- Transports: stdio for local, HTTP/SSE for remote
- Discovery — how a host learns what a server can do

**Practice:**
- Case study 1: MCP servers in Claude Desktop — config, connection, first tool call
- Case study 2: n8n as MCP host and n8n as MCP server
- Writing a minimal MCP server exposing one tool over your own data

**The trust boundary — do not skip this:**
- Installing an MCP server grants a model access to your machine and data
- Server-provided tool descriptions are untrusted input that enters your model's context
- Permission scoping, approval prompts, and auditing what a server actually did
- MCP is young: adoption risk, and how to avoid coupling your architecture to it

**Lab:**
- Connect Claude Desktop to a filesystem MCP server; complete a task; read the audit trail
- Write and register an MCP server exposing one tool over a dataset you own
- Wire an MCP tool into an n8n agent
- **Threat exercise:** write a tool description containing an injected instruction; observe whether the
  host model follows it; document the mitigation

---

## Module 9: Agent Evaluation, Tracing & Cost Control

> **New module. This is the largest gap in the source material and the biggest differentiator for
> graduates.** Anyone can demo an agent. Almost nobody can prove one works.

**Why agent evaluation is harder than model evaluation:**
- Non-deterministic paths: the same input can produce different valid trajectories
- Three distinct things to measure: final answer, **trajectory**, and cost/latency
- Failure taxonomy: wrong tool, right tool with wrong arguments, infinite loop, premature stop,
  hallucinated tool output, silent partial failure

**Building the eval set:**
- 30–50 real tasks with expected outcomes and acceptable tool sequences
- Deterministic checks first: did it call the tool, did it terminate, is the output schema-valid
- LLM-as-judge for answer quality, with a rubric — and validating the judge against human labels
- Trajectory scoring: exact-match, subset-match, and order-insensitive tool-sequence checks
- Regression testing: the eval suite runs in CI on every prompt change

**Observability with LangSmith:**
- Tracing runs; reading a trace to find where an agent went wrong
- Datasets and evaluators; comparing two agent versions on the same set
- Annotation queues for human review at scale

**Cost and latency engineering:**
- Token accounting per run; the cost of reflection and multi-agent loops
- Model routing: cheap model first, escalate on failure
- Caching: exact and semantic
- Hard spend caps and per-run step budgets

**Lab:**
- Build a 40-task eval set for your Module 4 agent with expected trajectories
- Wire LangSmith; run the suite; produce a baseline table of accuracy, tool-choice accuracy, cost, p95 latency
- Make one improvement and **prove it with numbers**; a documented honest regression scores full marks
- Add model routing and report the cost delta at equal quality

---

## Module 10: Agent Security & Deployment

> **New module.** Every system built in Modules 2–8 is exploitable as delivered. The n8n email and
> Telegram agents, the RAG agents, and the MCP hosts are all injection surfaces by construction.

**Prompt injection:**
- Direct injection vs. **indirect injection** — the payload arriving inside a retrieved document,
  an incoming email, a scraped page, or a tool description
- Live demonstration against the Module 6 email agent and the Module 7 RAG workflow
- Why input filtering alone cannot fix it — the lethal trifecta: private data + untrusted content +
  external communication
- Mitigations that actually help: least-privilege tools, human gates on irreversible actions,
  separating untrusted content from instructions, output filtering, and dual-LLM patterns

**The wider surface:**
- OWASP Top 10 for LLM Applications, walked through against this course's own builds
- Excessive agency: what a compromised agent can reach with the credentials you gave it
- Sandboxing code-executing agents; read-only DB credentials; scoped OAuth
- Secrets handling; PII redaction before logging and tracing
- Supply chain: unvetted MCP servers, community n8n nodes, unpinned dependencies

**Deployment:**
- Serving a LangGraph agent behind FastAPI: streaming, async, timeouts
- Durable checkpointers for real persistence; resuming interrupted runs
- Background execution for long-running agents; queues and idempotency
- Rate limits, auth, and a spend cap that fails closed
- Containerization and a health check; logging that survives an incident review

**Lab:**
- Serve your capstone agent behind a streaming FastAPI endpoint with auth, rate limits, and a spend cap
- **Red-team a classmate's agent:** plant an indirect injection in a document their RAG will retrieve
  or an email their n8n agent will read
- Fix every finding on your own system and prove each fix with a test in your Module 9 suite

---

## Module 11: Capstone Project

**Started after Module 4, reviewed in Modules 7 and 9, defended in Module 11.**

Choose one:

- **Workflow agent** — a LangGraph agent with real tools, durable state, and a human approval gate
- **Multi-agent operation** — an AG2 or CrewAI team producing a reviewed, shippable artifact
- **Automation product** — an n8n agent solving a real business process, handover-quality
- **MCP integration** — an MCP server plus host exposing a genuine data source safely
- **Your own** — instructor-approved, same bar

**Every capstone must ship:**

| Requirement | Evidence |
|---|---|
| A real user problem | One-page problem statement naming an actual user |
| Working system, runs from a clean clone | Repository + README with pinned dependencies |
| Bounded agency | Step caps, timeouts, and an approval gate on every irreversible action |
| Eval set with baseline and measured improvement | 30+ tasks; accuracy, tool-choice accuracy, and a regression run |
| Cost and latency measured | Cost per run, p95 latency, and the spend cap in code |
| Traced | LangSmith project link or exported traces |
| Security review | Injection test results, permission scoping, and the fixes |
| Honest failure analysis | What broke, what you would do differently |

**Defense:** 15-minute demo + Q&A, including "show me the number that proves this claim,"
"open the file where you bound the agent," and "inject this string and show me what happens."

---

## Environment & Delivery Prerequisites

**Blocking fixes to the existing material — complete these before the first cohort:**

1. **Rewrite `2.LangChain_AI_Agents/Lang_Chain_AI_Agents.ipynb`** to LangChain 1.x. It currently imports
   `langchain.llms`, `langchain.chat_models`, `initialize_agent`, `AgentType`, `langchain.embeddings`,
   `langchain.vectorstores`, and `RetrievalQA` — removed or relocated. It will fail in cell 1 on a
   current install, and it conflicts with the `langchain_classic` imports in Modules 3–4.
2. **Add the missing `requirements.txt`.** Both LangGraph notebooks run `!pip install -r requirements.txt`
   and no such file exists anywhere in the folder. One pinned file per module, resolved and tested.
3. **De-Colab the notebooks.** Every notebook uses `from google.colab import userdata`. Replace with
   `os.getenv()` plus a `.env` fallback so local Jupyter and online students are not blocked.
4. **Resolve the CrewAI promise.** The intro deck lists CrewAI in "Course Contents"; no module exists.
   Build Module 5's CrewAI half or remove the slide.
5. **Clean the distribution.** Delete `LangGraph_Part2_v2.2 - Original(1).ipynb`; drop the `- Original`
   suffixes; strip saved outputs from notebooks before handout; ship starter and solution variants.
6. **Confirm licensing.** The decks carry a third-party author name and contact numbers on every slide.
   Verify redistribution rights before paid delivery, or rebuild the slides against this outline.

**Dependency policy:**

| Group | Constraint |
|---|---|
| Core | `langchain>=1.0,<2`, `langgraph>=1.0,<2`, `langchain-openai`, `langchain-core` |
| Legacy interop | `langchain-classic` — only where a module genuinely needs a moved API |
| Retrieval | `langchain-chroma` or `faiss-cpu`, `langchain-text-splitters`, `pypdf` |
| Multi-agent | `ag2`, `crewai` — **separate venv**; their transitive pins fight the core group |
| Tooling | `langsmith`, `tavily-python`, `gradio`, `fastapi`, `uvicorn`, `python-dotenv` |

Resolve once, freeze the exact versions into per-module `requirements.txt`, and re-test at the start of
every cohort. Pin, do not float — a mid-term breaking release costs a session.

**Accounts required (7).** Provision *before* day one, not during a lab:

| Service | Used in | Classroom strategy |
|---|---|---|
| OpenAI (or Bedrock/Anthropic) | 2–5, 9–11 | Institute-issued keys with per-student spend caps |
| Tavily | 3, 4 | Free tier is sufficient |
| LangSmith | 4, 9 | One shared org so the instructor can review student traces |
| Supabase | 7 | Free tier; pre-create projects to save 20 minutes |
| Gmail (OAuth) | 6 | **Shared lab account** — never students' personal inboxes |
| Telegram | 6 | Bot tokens issued by the instructor |
| SERP API | 7 | Free tier; one key per bench if quota is tight |

---

## Classroom vs. Online Delivery

**Classroom:**
- Pre-imaged environment (Docker image or a pre-built venv on lab machines). Never `pip install` live.
- Self-host n8n in Docker on the classroom network — avoids the trial clock and 30 simultaneous signups.
- **Offline fallback:** institute Wi-Fi plus 30 students hitting one API tier means rate limits.
  Keep an Ollama local model path and cached notebook outputs for every demo.
- Bench pairing for Modules 6–7 halves the credential-setup time.
- Red-teaming (Module 10) works best in person — run it as a live exercise across benches.

**Online:**
- **Pre-record every credential flow** — n8n OAuth, Supabase setup, Claude Desktop MCP config. These are
  screen-share hostile and consume a third of a live session.
- Ship starter/solution notebook pairs; breakout rooms for the lab half; instructor drops into rooms.
- One shared LangSmith project so labs can be graded from traces asynchronously.
- Modules 6–7 (n8n) are the highest-risk online sessions — allocate a buffer session for setup issues.
- Capstone defenses recorded; peer red-teaming assigned as async homework with a written report.

---

## Assessment

| Component | Weight |
|---|---|
| Weekly labs (10 graded) | 35% |
| Mid-course build — LangGraph agent with HITL (Module 4) | 15% |
| Capstone project | 30% |
| Quizzes (10 min, start of each module) | 10% |
| Peer red-teaming and code-review quality | 10% |

**Lab rubric:** runs from a clean clone (20%) · correctness (20%) · **bounded agency — step caps, timeouts,
approval gates (15%)** · measurement with an honest baseline (25%) · analysis (10%) · no leaked secrets (10%).

> A lab reporting an honest negative result with clean methodology scores higher than one claiming a win
> it cannot demonstrate. Say this in Module 1 and enforce it from Module 9.

---

## AI-Use Policy

- **Labs and projects:** AI assistance allowed and encouraged; disclose in `AI_USE.md`
- **Quizzes:** closed-book, no AI
- **All code:** you must be able to explain and modify any line under live questioning
- **Evaluation numbers:** never fabricated — this is misconduct, not a style issue

Enforcement is the oral defense, announced in Module 1 and applied from Module 4.

---

## Compute & Budget

| Modules | Requirement |
|---|---|
| 1–5 | Any laptop, 8 GB RAM; hosted APIs; Ollama for the offline fallback |
| 6–8 | Browser plus Docker for self-hosted n8n; Claude Desktop for MCP |
| 9–11 | API credits; a small VM or cloud free tier for FastAPI deployment |

**Budget:** roughly **₹2,000–4,000 (US $25–50) per student** in API credits across the term — higher than a
plain GenAI course because agent loops, reflection, and multi-agent chats multiply calls. Module 1 installs
the cost-logging wrapper before students can burn credits accidentally; Module 9 makes cost a graded metric.

---

## What Changed From the Source Material

| Change | Reason |
|---|---|
| **Added Module 9 (Evaluation)** and required numbers in every later lab | The largest gap; the source teaches tracing but never evaluation |
| **Added Module 10 (Security & Deployment)** | Every email, Telegram, RAG, and MCP build in the source is injection-exposed as delivered |
| **Added Module 11 (Capstone)** with a shipping checklist | Source assessment is two Lovable app assignments — insufficient for an institute |
| **Rewrote Module 2 to LangChain 1.x** | Legacy imports are removed upstream and conflict with Modules 3–4 |
| **Added CrewAI to Module 5** | Promised on the intro deck's contents slide; missing from the material |
| **Added agent design patterns to Module 1** | Frameworks change; the routing/orchestrator/evaluator taxonomy transfers |
| **Added a hand-written ReAct loop lab** | Makes every later framework recognizable instead of magical |
| **Cut the LLM/prompt-engineering recap to 20 minutes** | ~35% of the source LangChain deck re-teaches the prerequisite course |
| **Added durable checkpointers and bounded agency throughout** | `MemorySaver` and unbounded loops are demo-grade, not production-grade |
| **Added the accounts, offline-fallback, and n8n-trial plan** | These are what actually derail live sessions, in classroom and online alike |
