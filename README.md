# hello-python-311

Minimal Python 3.11 project that says "Hello, World!" with **pytest**, **ruff**, and **pylint** configured via `pyproject.toml`.

## Getting Started

```bash
# 1) Install uv if not installed
pip install uv

# 2) Create & activate environment with Python 3.11
uv venv --python=3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3) Install dev dependencies
uv pip install -e ".[dev]"

# 4) Run tests
uv run pytest

# 5) Lint & format
uv run ruff check .
uv run ruff format .
uv run pylint hello_app

# 6) Run
uv run python -m hello_app
# or
uv run hello-app
```
