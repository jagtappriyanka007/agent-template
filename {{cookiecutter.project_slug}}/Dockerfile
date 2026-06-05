# ---------- BUILD STAGE ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files FIRST (important fix ✅)
COPY pyproject.toml setup.py ./
COPY src ./src

# Install dependencies
RUN pip install --upgrade pip && pip install .

# Build C extensions (if any)
RUN python setup.py build_ext --inplace


# ---------- RUNTIME STAGE ----------
FROM python:3.11-slim AS runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Create non-root user
RUN useradd -m appuser

# Copy only required runtime artifacts
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

# Copy env example (optional)
COPY .env.example ./.env.example

# Switch to non-root user
USER appuser

EXPOSE 8000

# ✅ Updated module path (check this!!)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
