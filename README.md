<div align="center">

# 🤖 Strands Agents Workshop

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/bedrock/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[![CI](https://github.com/christiangfv/strands-agents-workshop/actions/workflows/ci.yml/badge.svg)](https://github.com/christiangfv/strands-agents-workshop/actions)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-christiangfv-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/christiangfv)
[![GitHub](https://img.shields.io/badge/GitHub-christiangfv-181717?style=flat&logo=github)](https://github.com/christiangfv)

**A progressive, hands-on workshop to master intelligent agents with the [Strands](https://github.com/strands-agents/sdk-python) framework.**  
*From zero to production-ready Planner-Executor architecture — step by step.*

[🚀 Quick Start](#-quick-start) • [📚 Workshop Levels](#-workshop-structure) • [🏗️ Architecture](#️-architecture) • [🤝 Contributing](CONTRIBUTING.md)

---

</div>

## 🌟 What is this?

**Strands Agents Workshop** is a practical, progressive course for building intelligent agents using the [Strands SDK](https://github.com/strands-agents/sdk-python). You'll go from a simple conversational agent to a full **Planner-Executor** architecture — the same pattern used in production AI systems.

> Built from real-world experience developing AI agents for fraud detection and financial automation at scale using **AWS Bedrock + Strands**.

### 🎯 Who is this for?

| Audience | Why it matters |
|----------|---------------|
| 👨‍💻 **Backend Developers** | Learn to add AI reasoning to your services |
| 🎓 **ML/AI Students** | Understand real-world agent architectures |
| 🏗️ **Solution Architects** | Evaluate agent patterns for production |
| 🤖 **AI Enthusiasts** | Experiment with LLMs + tools hands-on |

---

## 📚 Workshop Structure

> Each level builds on the previous. You can start from any level, but the progression is designed to be linear.

### 🟢 Level 01 — [Simple Agent](./01-agente-simple/)
**Core Foundations**
- Conversational agent with zero tools
- Basic Strands SDK API
- LiteLLM / OpenRouter integration

```bash
cd 01-agente-simple && python agent.py
```

---

### 🟡 Level 02 — [Agent with Tools](./02-agente-actual/)
**First Tool Integration**
- Single functional tool
- Basic Planner-Executor pattern
- Custom logging

```bash
cd 02-agente-actual && python agent.py
```

---

### 🟠 Level 03 — [Multi-Tool Agent](./03-agente-multi-tools/)
**Modular Architecture**

5 specialized tools:
| Tool | Description |
|------|-------------|
| 🌤️ Weather | Real-time weather via external API |
| 🔢 Calculator | Mathematical expressions |
| 🐾 Pokémon | PokéAPI integration |
| 😄 Jokes | Random joke generator |
| 🌐 Translator | Multi-language translation |

```bash
cd 03-agente-multi-tools && python agent.py
```

---

### 🔴 Level 04 — [Planner-Executor Agent](./04-agente-planner-executor/)
**Production-Ready Architecture**
- Full Planner-Executor coordination
- Structured JSON task planning
- All Level 03 tools included
- `plan [task]` command for complex goals

```bash
cd 04-agente-planner-executor && python agent.py

# Example: complex task planning
> plan organize a team meeting with weather and availability checks
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- [OpenRouter API Key](https://openrouter.ai) (free) **or** AWS credentials for Bedrock

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/christiangfv/strands-agents-workshop.git
cd strands-agents-workshop

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Configure environment
cp .env.example .env
# Edit .env with your API key
```

### Environment Variables

```env
# Option A: OpenRouter (recommended for workshop)
OPENROUTER_API_KEY=your_key_here

# Option B: AWS Bedrock (production-grade)
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
```

### Verify Installation

```bash
python -c "import strands; print('✅ Strands ready')"
pytest  # run test suite
```

---

## 🏗️ Architecture

```
strands-agents-workshop/
├── 01-agente-simple/           # 🟢 Level 1 — Basics
│   └── agent.py
├── 02-agente-actual/           # 🟡 Level 2 — First tools
│   ├── agent.py
│   └── tools.py
├── 03-agente-multi-tools/      # 🟠 Level 3 — Multi-tool
│   ├── agent.py
│   └── tools.py
├── 04-agente-planner-executor/ # 🔴 Level 4 — Advanced
│   ├── agent.py
│   └── tools.py
├── strands_workshop/           # Shared library
│   ├── agents.py
│   └── tools.py
├── pyproject.toml              # Modern Python packaging
├── requirements.txt
└── README.md
```

### Design Principles

| Principle | Description |
|-----------|-------------|
| 📈 **Progressive Complexity** | Each level builds on the previous |
| 🔧 **Separation of Concerns** | Tools isolated from agent logic |
| 🧪 **Tests Included** | Critical coverage in each level |
| 🚀 **Production-Ready Patterns** | Planner-Executor used in real systems |

---

## 🔄 Planner-Executor Pattern

The Level 4 agent implements the **Planner-Executor** pattern — a production architecture where:

```
User Request
     │
     ▼
 ┌─────────┐    JSON Plan    ┌──────────────┐
 │ Planner │ ─────────────► │   Executor   │
 │  (LLM)  │                │  (Tools +    │
 └─────────┘                │   LLM loop)  │
                             └──────────────┘
                                    │
                              Final Response
```

1. **Planner**: LLM receives the task and generates a structured JSON plan
2. **Executor**: Steps are executed sequentially using available tools
3. **Feedback loop**: Results from each step inform the next

> This is the same pattern used in production fraud detection systems with AWS Bedrock.

---

## 🧪 Testing

```bash
# Run full test suite
pytest

# With coverage report
pytest --cov=strands_workshop --cov-report=html

# Specific level
pytest tests/test_01_agente_simple/
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
git checkout -b feature/new-tool
git commit -m "feat: add new tool"
git push origin feature/new-tool
# Open a Pull Request
```

---

## 👤 About the Author

**Christian Fuentes** — AI/ML Engineer building production AI agents.

Currently developing fraud detection agents using **AWS Bedrock + Strands SDK** at [Radar](https://radar.cl) — the same patterns taught in this workshop.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/christiangfv)
[![GitHub](https://img.shields.io/badge/GitHub-@christiangfv-181717?style=flat&logo=github)](https://github.com/christiangfv)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Strands SDK](https://github.com/strands-agents/sdk-python) — the agent framework
- [OpenRouter](https://openrouter.ai) — multi-model API access
- [AWS Bedrock](https://aws.amazon.com/bedrock/) — production LLM infrastructure

---

<div align="center">

**⭐ If this helped you, star it on GitHub!**

*Tags: `ai-agents` `strands` `planner-executor` `aws-bedrock` `llm` `python` `workshop` `tutorial`*

</div>
