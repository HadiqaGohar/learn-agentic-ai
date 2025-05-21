
# ⚡ Python UV – The Ultimate Guide to the Fastest Python Package Manager

> 🚀 **UV** is the **blazing fast** Python package manager & virtual environment tool — designed to simplify, speed up, and streamline your development workflow.

---

## 📚 Official Documentation

🔗 [Explore the Docs](https://github.com/astral-sh/uv)  
🎥 [Watch: Python Setup Simplified – Full UV Tutorial](https://www.youtube.com/watch?v=example)

---

## 🎯 Why Use UV?

UV is built to be **fast**, **reliable**, and **developer-friendly**, replacing tools like `pip`, `virtualenv`, `pip-tools`, and `poetry` with one single CLI.

### ✨ Key Features:

- ⚡ Super-fast dependency resolution
- 📦 Simple CLI for managing projects & packages
- 🧪 Built-in virtual environments
- 📁 Clean project structure & initialization
- 🧰 Excellent for packaged applications (like PyPI CLI tools)

---

## 🐍 Python Cursor Rule

> **Always use UV as your package manager when working in Python.**  
> Avoid writing repetitive setup code – just use CLI commands where efficient!

---

## 🚀 Getting Started

### 1️⃣ Install `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
````

*or install using pipx:*

```bash
pipx install uv
```

---

### 2️⃣ Create a New Project

To start a new Python project with a **virtual environment** and proper structure:

```bash
uv init project_1
cd project_1
code .
```

This will create:

```
project_1/
├── .venv/           # Virtual environment
├── pyproject.toml   # Project metadata
└── src/             # Your source code folder
```

---

## 🧪 Working with Virtual Environments

UV **automatically creates and activates** a virtual environment in `.venv/`.

To manually activate it (if needed):

```bash
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

No need to use `venv` or `virtualenv` separately!

---

## 📦 Add Dependencies

To add dependencies (like `crewai` or even `uv` itself):

```bash
uv add crewai
uv add uv
```

To install a specific version:

```bash
uv add fastapi@0.110.0
```

---

## 📦 Create a Packaged CLI App

If you're planning to create a **packaged application**, such as a CLI tool or a project for PyPI:

```bash
uv init project_1
```

This sets up the right folder structure:

```
example-pkg/
├── src/example_pkg/
├── tests/
└── pyproject.toml
```

You can now publish, test, or build easily.

---

## 🧪 Running Scripts

You can run Python scripts easily within the project:

```bash
uv run src/main.py
```

Or define scripts inside your `pyproject.toml` and run them like:

```bash
uv run your-script-name
```

---

## 🔧 Useful CLI Commands

| Command            | Purpose                                 |
| ------------------ | --------------------------------------- |
| `uv init`          | Initialize a new Python project         |
| `uv add <package>` | Add and install packages                |
| `uv pip <command>` | Run pip commands within UV environment  |
| `uv venv`          | Create and manage virtual environments  |
| `uv run <script>`  | Run scripts or commands                 |
| `uv sync`          | Sync dependencies from `pyproject.toml` |

---

## 🧠 Tips

* 🔄 **Use `uv sync`** if you edit `pyproject.toml` manually.
* ✅ **Use `uv` instead of `pip`**, `venv`, and `requirements.txt` — it's faster and cleaner.
* 📁 **Keep all source code in `src/`** directory for best practices.

---

## ✅ Example Flow

```bash
uv init project_1
cd project_1
uv add typer rich
uv run src/main.py
```

Now you're ready to build and run a full CLI app!

---

## ✨ Conclusion

`uv` is the **future of Python development tooling** — combining speed, simplicity, and structure. Whether you're a beginner or a pro, it's your new best friend for building Python apps.

> 🚀 *Say goodbye to pip, virtualenv, poetry, and hello to UV!*

---

**Crafted with ❤️ by Hadiqa Gohar*
