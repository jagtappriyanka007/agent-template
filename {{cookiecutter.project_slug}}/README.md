# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

```bash
uv venv --python {{ cookiecutter.python_version }}
uv sync
uv run --python {{ cookiecutter.python_version }} uvicorn app.main:app --app-dir src --reload --port 8000
```

## Test

```bash
uv run --python {{ cookiecutter.python_version }} pytest -q
```

## Build Cython

```bash
uv run --python {{ cookiecutter.python_version }} python setup.py build_ext --inplace
```

## Docker

```bash
docker compose up --build
```
