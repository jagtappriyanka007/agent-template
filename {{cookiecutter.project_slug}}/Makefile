UV ?= uv
PYTHON ?= {{ cookiecutter.python_version }}
IMAGE ?= {{ cookiecutter.project_slug }}:latest

.PHONY: help venv sync test test-verbose run build-cython docker-build docker-run docker-up docker-down clean

help:
	@echo "Available targets:"
	@echo "  make venv           - Create virtual environment with uv"
	@echo "  make sync           - Sync dependencies from pyproject.toml"
	@echo "  make test           - Run pytest"
	@echo "  make test-verbose   - Run pytest with verbose output"
	@echo "  make run            - Start FastAPI app in reload mode"
	@echo "  make build-cython   - Build Cython extensions in place"
	@echo "  make docker-build   - Build Docker image"
	@echo "  make docker-run     - Run Docker container locally"
	@echo "  make docker-up      - Start services with docker compose"
	@echo "  make docker-down    - Stop services with docker compose"
	@echo "  make clean          - Remove build/test artifacts"

venv:
	$(UV) venv --python $(PYTHON)

sync:
	$(UV) sync

test:
	$(UV) run --python $(PYTHON) pytest -q

test-verbose:
	$(UV) run --python $(PYTHON) pytest -vv

run:
	$(UV) run --python $(PYTHON) uvicorn app.main:app --app-dir src --reload --port 8000

build-cython:
	$(UV) run --python $(PYTHON) python setup.py build_ext --inplace

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run --rm -p 8000:8000 --env-file .env $(IMAGE)

docker-up:
	docker compose up --build

docker-down:
	docker compose down

clean:
	$(UV) run --python $(PYTHON) python -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['.pytest_cache','build','dist']]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('src').rglob('__pycache__') if p.is_dir()]; [f.unlink() for f in pathlib.Path('src').rglob('*.so') if f.is_file()]; [f.unlink() for f in pathlib.Path('src').rglob('*.pyd') if f.is_file()]; [f.unlink() for f in pathlib.Path('src').rglob('*.c') if f.is_file()]"
