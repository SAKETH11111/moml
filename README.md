# MoML

MoML (Molecular Modeling & Machine Learning) is a research-first framework for
building directional, hierarchical graph neural networks that drive molecular
dynamics simulations and long-horizon forecasters for PFAS analysis.

This repository currently contains the hardened project scaffolding described in
the MIT THINK proposal. The first milestone focuses on tooling, reproducibility,
and documentation so contributors can build out data, modeling, and simulation
workstreams with confidence.

## Repository Layout

```text
moml/
├── pyproject.toml
├── env/
│   └── environment.yml
├── configs/
│   ├── data/
│   ├── model/
│   ├── train/
│   ├── sim/
│   └── eval/
├── data/
├── docs/
├── scripts/
├── src/
│   └── moml/
│       ├── cli.py
│       ├── dataio/
│       ├── featurizers/
│       ├── ff/
│       ├── models/
│       ├── pipelines/
│       └── sim/
└── tests/
```

Each directory is a foundation for future milestones:

- **configs/** — Hydra configuration tree (data, model, training, simulation,
  evaluation).
- **data/** — DVC-tracked manifests; large blobs are never committed to git.
- **src/moml/** — Python package registered via `pyproject.toml`.
- **scripts/** — Thin wrappers that call into the Python package (currently a
  placeholder).
- **tests/** — Unit and integration tests (currently a placeholder import smoke
  test).

## Getting Started

Detailed setup instructions live in [`docs/getting-started.md`](docs/getting-started.md).
A high-level summary:

1. Create the conda environment described in `env/environment.yml` using mamba.
2. Install the package in editable mode with `pip install -e .` (inside the
   environment).
3. Enable the provided pre-commit hooks with `pre-commit install`.
4. Run `pytest` to verify the scaffolding.

## How Predictions Become MD

The systems view of the MGNN → MD → LSTM pipeline is documented in
[`docs/how-predictions-become-md.md`](docs/how-predictions-become-md.md). It
captures the end-to-end flow from curated PFAS data to simulation-ready force
fields and long-range behavioral forecasts.
