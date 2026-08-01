UV ?= uv

.PHONY: lint format test check

lint:
	$(UV) run ruff check .
	$(UV) run ruff format --check .
	$(UV) run mypy src tests

format:
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

test:
	$(UV) run pytest

check: lint test
