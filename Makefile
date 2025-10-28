POETRY ?= poetry

.PHONY: all clean help setup lint format test docs export-requirements

all: setup lint test

clean:
	rm -rf site/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

help:
	@printf "Available targets:\n"
	@printf "  all                  Run setup, lint, and test\n"
	@printf "  clean                Remove build artifacts and caches\n"
	@printf "  setup                Install dependencies with Poetry (including extras)\n"
	@printf "  lint                 Run static analysis (ruff + mypy)\n"
	@printf "  format               Format code using ruff\n"
	@printf "  test                 Run the pytest suite\n"
	@printf "  docs                 Build the documentation site\n"
	@printf "  export-requirements  Export pip-style requirements.txt\n"

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
	$(POETRY) export --without-hashes -f requirements.txt -o requirements.txt
