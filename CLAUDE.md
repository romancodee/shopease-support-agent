# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

Two virtual environments exist: `.venv` (base) and `adk-env` (ADK-specific). Use `adk-env` for running ADK commands.

```powershell
# Activate the ADK environment
.\adk-env\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

The `.env` file (gitignored) must contain `GROQ_API_KEY` for the Groq LLM backend.

## Running the Agents

Google ADK agents are launched via the `adk` CLI. The entry point ADK discovers is the `root_agent` variable exported from a package's `__init__.py`.

```powershell
# Launch the web UI (opens browser at http://localhost:8000)
adk web

# Run a specific agent package in CLI mode
adk run ecom_support
adk run my_agent
```

## Running Tests

```powershell
pytest
pytest tests/test_specific.py  # run a single test file
pytest -k "test_name"          # run a single test by name
```

## Architecture

This repo contains two independent ADK agent packages:

### `my_agent/` — Simple standalone agent
A single `root_agent` using Groq's `llama-3.3-70b-versatile` via LiteLLM. Serves as a minimal reference implementation.

### `ecom_support/` — Multi-agent e-commerce support system
A hierarchical multi-agent system for "ShopEase" customer support. The architecture is:

```
ecom_support/agent.py       ← root_agent (triage_agent "Sana")
    ├── sub_agents/order_agent.py       → tools/order_tools.py
    ├── sub_agents/return_agent.py      → tools/returns_tools.py
    ├── sub_agents/delivery_agent.py    → tools/delivery_tools.py
    ├── sub_agents/payment_agent.py     → tools/payment_tools.py
    └── sub_agents/escalation_agent.py  (tool defined inline)
```

**Routing**: The `triage_agent` reads user intent and delegates to the appropriate sub-agent. Sub-agents are passed as the `sub_agents=[]` list on the root `Agent`.

**Tools**: Each sub-agent has a dedicated tool file under `ecom_support/tools/`. All tools currently use in-memory fake data (Python dicts) — no real database. Tool functions are plain Python functions passed in `tools=[]` on each `Agent`. The escalation agent defines its tool (`create_escalation_ticket`) inline in its own file rather than in the tools directory.

**Model**: All agents use `LiteLlm(model="groq/llama-3.3-70b-versatile")`. LiteLLM acts as the bridge between Google ADK and the Groq API.

**Language**: Agent `instruction` strings and some tool responses are written in Roman Urdu (Hindustani). This is intentional — the support persona "Sana" is designed to communicate with Urdu-speaking customers.

## Adding a New Sub-agent

1. Create `ecom_support/tools/your_tools.py` with plain Python tool functions.
2. Create `ecom_support/sub_agents/your_agent.py` importing those tools and defining an `Agent` instance.
3. Import and add the agent to `sub_agents=[]` in `ecom_support/agent.py`.
4. Update the triage instruction in `ecom_support/agent.py` to describe when to route to the new agent.
