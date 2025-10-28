# Contributing to MoML-CA

Thank you for your interest in improving MoML-CA! This document captures the
processes and conventions that keep the project healthy and collaborative.

## Table of Contents

1. [Project Principles](#project-principles)
2. [Ways to Contribute](#ways-to-contribute)
3. [Development Workflow](#development-workflow)
4. [Coding Standards](#coding-standards)
5. [Documentation Expectations](#documentation-expectations)
6. [Communication Channels](#communication-channels)

## Project Principles

- **Scientific Rigor:** Reproducibility and traceability are top priorities.
- **Inclusive Collaboration:** Diverse perspectives produce better tooling and
  science. See the [Code of Conduct](CODE_OF_CONDUCT.md).
- **Automation-first:** Prefer declarative configs, infrastructure-as-code, and
  automated validation over manual steps.
- **Safety:** Treat production experiments and sensitive research data with care.

## Ways to Contribute

- **Bug Reports:** Open an issue with clear reproduction steps, observed vs.
  expected behavior, and environment details.
- **Feature Proposals:** Share motivation, high-level design, acceptance
  criteria, and potential alternatives.
- **Documentation Improvements:** Submit fixes or clarifications for docs,
  READMEs, notebooks, or inline references.
- **Infrastructure Enhancements:** Improve automation, developer experience, or
  reproducibility pipelines.

## Development Workflow

1. **Sync main & your dev branch**
   ```bash
   git checkout main
   git pull
   git checkout dev/<your-name>
   git pull
   ```
2. **Create a feature branch**
   ```bash
   git checkout -b feature/<your-name>/<ticket-or-topic>
   ```
3. **Install dependencies** via Poetry (including extras for your workflow). The
   default setup installs development tooling:
   ```bash
   poetry install --extras "dev simulation docs"
   ```
4. **Implement the change**. Keep commits focused and reference issues when
   possible.
5. **Run quality gates locally** before opening a PR:
   ```bash
   make lint
   make test
   ```
6. **Open a pull request** against your dev branch. Ensure the PR template is
   completed. After review, a maintainer will merge upstream.
7. **Keep branches up-to-date** with `git fetch` and `git merge --ff-only` where
   possible. Rebase only if you are confident there will be no disruption to
   shared branches.

## Coding Standards

- **Language Versions:** Python `>=3.10`.
- **Formatting & Linting:** We use [Ruff](https://docs.astral.sh/ruff/) as the
  primary linter/formatter and [mypy](https://mypy-lang.org/) for static typing.
  - `make lint` runs both tools.
  - Enable `pre-commit` locally with `poetry run pre-commit install`.
- **Testing:** Unit tests live under `tests/unit`, integration tests under
  `tests/integration`. Provide fixtures under `tests/fixtures` where practical.
- **Type Hints:** Public APIs should be fully typed. Use `typing_extensions`
  helpers when targeting multiple Python versions.
- **Configuration:** Use `configs/` to register Hydra-style components. Keep
  secrets out of version control.

## Documentation Expectations

- Update `docs/` when introducing new modules, configurations, or workflows.
- Provide docstrings for public functions, classes, and modules. Prefer
  [Google-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
  docstrings.
- When adding notebooks, include a brief README describing the purpose,
  dependencies, and data sources.

## Communication Channels

- **Issues:** GitHub Issues for bugs and feature requests.
- **Discussions:** Use GitHub Discussions (or the team's designated workspace)
  for design proposals and strategy conversations.
- **Security:** Report potential security or compliance issues privately to the
  maintainers before filing a public issue.

Adhering to this guide helps us build reliable tooling and iterate quickly.
Thanks for contributing!
