POETRY ?= poetry

.PHONY: help setup lint format test docs export-requirements

help:
	@echo "Available targets:"
	@echo "  setup                Install dependencies with Poetry (including extras)"
	@echo "  lint                 Run static analysis (ruff + mypy)"
	@echo "  format               Format code using ruff"
	@echo "  test                 Run the pytest suite"
	@echo "  docs                 Build the documentation site"
	@echo "  export-requirements  Export pip-style requirements.txt"

setup:
	$(POETRY) install --sync --extras "dev docs simulation"

lint:
	$(POETRY) run ruff check momlca tests
	$(POETRY) run mypy momlca

format:
	$(POETRY) run ruff format momlca tests

test:
	$(POETRY) run pytest

docs:
	$(POETRY) run mkdocs build --site-dir site

export-requirements:
	$(POETRY) export --without-hashes -f requirements.txt > requirements.txt
