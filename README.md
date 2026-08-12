# Coding Agents

A modular Python project for dynamic AI agent orchestration, validation, and prompt-driven reasoning.

## Overview

This repository demonstrates a technical agent framework built with Python and integrated with Ollama via `langchain_ollama`.
It features:
- dynamic agent loading from `src/models/brain`
- runtime state management using typed state models
- an evaluation workflow with separate agent/judge nodes
- prompt-based task execution for programming and judge evaluation

## Key Concepts

- `src/utils/agent_starter.py` loads agents dynamically using Python import machinery.
- `src/utils/handle_agent.py` wraps runtime startup logic and error handling.
- `src/models/brain/agent.py` and `agent2.py` initialize Ollama-backed chat agents.
- `src/models/brain/test_agent.py` provides a lightweight mock agent for verification.
- `src/state/` stores strongly typed state definitions for answers, metrics, and constraints.
- `src/nodes/` contains node-level execution logic for `start_agent` and `start_judge`.

## Project Structure

- `main.py` — entry point for the application
- `requirement.txt` — project dependencies
- `src/` — application source code
  - `models/brain/` — agent definitions and provider bindings
  - `nodes/` — orchestrator nodes for starting agents and judges
  - `prompts/` — prompt templates and LLM instruction files
  - `state/` — typed state definitions and evaluation models
  - `utils/` — reusable startup, runtime, and agent helper code

## Installation

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirement.txt
```

## Usage

Run the main entry point:

```bash
python main.py
```

For quick verification, use:

```bash
python src/test_run.py
```

## Technical Highlights

- Clean modular design with clear separation of concerns
- Dynamic runtime agent import for flexible extension and testing
- Use of typed dictionaries and structured state for predictable data flow
- Integration-ready for Ollama models and prompt automation

## Notes

This repository is built to reflect engineering-level design and is well-suited for experimentation with AI-driven agent workflows.
