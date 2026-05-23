# Simple AI Agent - crewAI Project

A simple AI agent built with [crewAI](https://github.com/crewAIInc/crewAI) that researches and summarizes information on any given topic.

## Overview

This project contains a single **Research Analyst** agent that takes a topic as input and produces a well-structured summary with key facts, important details, and a clear conclusion.

## Project Structure

```
src/simple_agent/
├── config/
│   ├── agents.yaml    # Agent definitions
│   └── tasks.yaml     # Task definitions
├── __init__.py
├── crew.py            # Crew orchestration
└── main.py            # Entry point
```

## Setup

### Prerequisites

- Python 3.10 – 3.12
- An OpenAI API key (or compatible LLM provider)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd crewai-simple-agent
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```

3. **Configure your API key:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

## Usage

### Run with default topic

```bash
simple_agent
```

This will research "Artificial Intelligence trends in 2025" by default.

### Run with a custom topic

```bash
python -m simple_agent.main "Your custom topic here"
```

## Customization

- **Agents:** Edit `src/simple_agent/config/agents.yaml` to change the agent's role, goal, or backstory.
- **Tasks:** Edit `src/simple_agent/config/tasks.yaml` to modify the task description or expected output.
- **Add more agents/tasks:** Extend `crew.py` with additional `@agent` and `@task` decorated methods.

## License

MIT
