
# 🤖 Chainlit HelloWorld with OpenAI Agents SDK Exploration

This repository contains a simple **Chainlit chatbot** (HelloWorld app) that I built while exploring advanced agent orchestration frameworks like **OpenAI Swarm**, **OpenAI Agents SDK**, and **Anthropic's multi-agent design patterns**.

---

## 🚀 Features

- ✅ Built using [Chainlit](https://www.chainlit.io/)
- 🧠 Understands and explains basic user queries
- 💬 Real-time, interactive chat interface using Python
- 🔄 Async handling for smooth user experience
- 🔗 Conceptually integrates OpenAI Agents SDK patterns like:
  - Prompt Chaining
  - Routing & Handoffs
  - Orchestrator–Worker pattern

---

## 📚 What I Learned

### 🧩 Chainlit Framework
- Python-first framework to build conversational UI rapidly
- Rich UI elements (text, forms, buttons, file uploads)
- Async support, middleware hooks, and state management

### 🧠 OpenAI’s Swarm
- Lightweight orchestration framework for multi-agent systems
- Agents + Handoffs = Scalable, dynamic control transfer

### ⚙️ OpenAI Agents SDK
- Production evolution of Swarm
- Enables orchestrating workflows across multiple intelligent agents
- Supports evaluator-optimizer patterns for agent collaboration

### 💡 Anthropic Agent Design Patterns
- Prompt Chaining
- Routing
- Parallelization
- Orchestrator-Worker
- Evaluator-Optimizer

---

## 🛠️ How to Run

```bash
# Initialize project with UV
uv init helloworld

cd helloworld

# Create and activate virtual environment
uv venv

# On MacOS activate venv like this:
source .venv/bin/activate

# Create a .gitignore file at project root with this content:
# .venv

# Install Chainlit using UV package manager
uv add chainlit

# Delete default main.py file created by uv init
rm main.py

# Create a new chatbot.py file for your chatbot code
touch chatbot.py


# Run Chainlit server
uv run chainlit chatbot.py

````

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🤔 Sample Q\&A

**Q:** What is Chainlit used for?
**A:** It helps developers build UI for conversational AI apps quickly using Python.

**Q:** What is a handoff in OpenAI Swarm?
**A:** It allows one agent to transfer control to another agent based on context.

**Q:** How does the Agents SDK relate to Swarm?
**A:** It’s a production-ready evolution that builds upon Swarm's foundational principles.

**Q:** Can I use multiple agents with Chainlit?
**A:** Conceptually yes — by integrating logic in Python, routing and orchestration patterns can be simulated.

---

## 🧑‍💻 Author

**Hadiqa Gohar**
🌐 [LinkedIn](https://pk.linkedin.com/in/hadiqa-gohar-b64778300)
📧 [tasleemhadiqa76@gmail.com](mailto:tasleemhadiqa76@gmail.com)



> 🔁 Replace `https://github.com/HadiqaGohar` and GitHub URL above with your actual usernames and links.
