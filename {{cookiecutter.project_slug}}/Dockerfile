FROM python:{{ cookiecutter.python_version }}-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml setup.py ./
RUN pip install --upgrade pip && pip install .

COPY src ./src
RUN python setup.py build_ext --inplace

FROM python:{{ cookiecutter.python_version }}-slim AS runtime

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

RUN useradd -m appuser

COPY --from=builder /usr/local/lib/python{{ cookiecutter.python_version }} /usr/local/lib/python{{ cookiecutter.python_version }}
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src
COPY .env.example ./.env.example

USER appuser
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
