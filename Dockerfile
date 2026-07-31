# syntax=docker/dockerfile:1
FROM python:3.13-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app

RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --no-dev --no-install-project
COPY src ./src
RUN uv sync --no-dev

FROM python:3.13-slim AS runtime

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_ENV=production
WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --chown=app:app src ./src

USER app
EXPOSE 8000
CMD ["uvicorn", "ai_commerce_os.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
