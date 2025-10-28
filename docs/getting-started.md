# Getting Started

This guide walks through the minimum steps required to bootstrap a development
environment and run the repository scaffolding checks. The stack is designed
around conda/mamba so that core chemistry packages (RDKit, OpenMM, OpenFF) work
reliably across platforms.

## 1. Create the Conda Environment

```bash
mamba env create -f env/environment.yml
conda activate moml
```

The environment ships with PyTorch, PyTorch Geometric, RDKit, OpenMM, OpenFF,
DVC, Hydra, and Weights & Biases. GPU support depends on your local CUDA
configuration.

## 2. Install the Package in Editable Mode

```bash
pip install -e .[dev]
```

Editable installs ensure local changes to `src/moml/` are immediately available
in your Python interpreter. The `dev` extra adds linting, typing, and testing
packages.

## 3. Configure Pre-Commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

Pre-commit enforces formatting (Black, isort), linting (Ruff), typing (mypy),
YAML validation, and package metadata expectations before changes leave your
machine.

## 4. Authenticate Optional Services

- **Weights & Biases (wandb):** Run `wandb login` with your API key to capture
  experiment metadata.
- **DVC:** Configure your remote (e.g., `dvc remote add --default storage s3://…`)
  before pushing large artifacts.

These services are optional until you introduce datasets or training runs, but
setting them up early prevents surprises later.

## 5. Run Smoke Tests

```bash
pytest
```

The default test suite only checks that the package imports. Add unit and
integration tests as you implement pipelines, models, and simulators.

## 6. Explore the CLI

```bash
moml --help
```

The CLI is powered by [Typer](https://typer.tiangolo.com/). Future milestones
will add subcommands for data ingestion, training, force-field assembly, and MD
execution.

## Next Steps

- Draft Hydra configs under `configs/` to describe your data and training jobs.
- Add DVC stage files for reproducible data preparation.
- Extend `src/moml/` with concrete implementations of data loaders, MGNN
  modules, MD assembly utilities, and LSTM trainers.
