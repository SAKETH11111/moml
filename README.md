# MoML-CA

MoML-CA (Molecular Machine Learning for Chemical Automation) is an open research
platform for building end-to-end molecular modeling pipelines that unify data
engineering, representation learning, simulation, and automated decision making.
The initial release lays the groundwork for collaborative development across
scientists, engineers, and product teams who work on chemistry-aware machine
learning systems.

> **Status:** Repository bootstrap. The scaffolding included here establishes
> shared conventions, infrastructure, and tooling so contributors can focus on
> high-impact features from day one.

## Vision & Roadmap

| Phase | Focus | Highlights |
| ----- | ----- | ---------- |
| 0. Foundations | Repository & infrastructure | Project scaffolding, packaging, CI hooks, documentation baseline |
| 1. Data Backbone | Unified data ingestion | Configurable pipelines, feature stores, quality gates |
| 2. Modeling Core | Molecular learning workflows | GNN architectures, pre-training, uncertainty estimation |
| 3. Simulation Loop | Physics-informed integration | Hybrid ML/simulation pipelines, calibration, scenario generation |
| 4. Automation | Continuous experimentation | Experiment tracking, orchestration, feedback-driven optimization |

A detailed backlog is captured in the roadmap within [`docs/`](docs/) and is
refined via collaborative planning sessions. Contributions that align with the
vision above are welcome through pull requests (see [Contributing](#contributing)).

## Repository Layout

```
moml-ca/
├── configs/                  # Hydra-style config templates and registries
│   ├── base.yaml
│   ├── data/
│   ├── model/
│   ├── pipeline/
│   └── simulation/
├── data/                     # External datasets (ignored by git)
├── docs/                     # Markdown documentation and specs
├── momlca/                   # Python package root
│   ├── cli/
│   ├── config/
│   ├── data_pipeline/
│   ├── evaluation/
│   ├── featurizers/
│   ├── models/
│   ├── pipelines/
│   ├── simulation/
│   ├── training/
│   └── utils/
├── notebooks/                # Exploratory analysis and prototypes
└── tests/
    ├── fixtures/
    ├── integration/
    └── unit/
```

Each subpackage ships with placeholders and docstrings so that new modules can
be implemented incrementally without fighting import order or packaging issues.

## Tooling Overview

- **Python Packaging:** Managed with [Poetry](https://python-poetry.org/). Core
  dependencies include `numpy`, `pandas`, `torch`, `torch-geometric`, and
  `rdkit-pypi`. Optional feature sets are exposed as extras (`simulation`,
  `docs`, `dev`).
- **Environment Snapshots:** `environment.yml` documents a conda-based runtime
  that mirrors the Poetry configuration. Update both when introducing new
  dependencies.
- **Docker:** GPU-ready image built from the official NVIDIA CUDA runtime with
  Poetry pre-installed for reproducible deployments.
- **Make Targets:** Quality-of-life wrappers around installation, linting,
  testing, and documentation workflows (see [Makefile](Makefile)).
- **Continuous Integration:** GitHub Actions workflow for linting and testing on
  pushes and pull requests (see [ci.yml](.github/workflows/ci.yml)).

## Getting Started

### 1. Clone & Branch Strategy

```bash
git clone git@github.com:<org>/moml-ca.git
cd moml-ca
# Create a feature branch based on your personal dev branch
# e.g., main -> dev/<your-name> -> feature/<your-name>/<ticket>
```

> Branch protection rules guard `main` and team-maintained dev branches. Please
> open pull requests against your dev branch first, then merge upstream once the
> review is complete.

### 2. Install Dependencies (Poetry)

```bash
# Install Poetry if you have not already
curl -sSL https://install.python-poetry.org | python3 -

# Install core dependencies plus development toolchain
poetry install --extras "dev simulation docs"

# Optional: sync lockfile updates across formats
make setup
```

#### Optional Extras

| Extra | Includes | Purpose |
| ----- | -------- | ------- |
| `simulation` | `simpy`, `scipy` | Experimental simulation loops |
| `docs` | `mkdocs`, `mkdocs-material`, `mkdocstrings-python` | Documentation site |
| `dev` | `pytest`, `pytest-cov`, `ruff`, `mypy`, `pre-commit` | Local quality checks |

### 3. Quick Commands

```bash
make lint                 # ruff + mypy
make test                 # pytest suite (unit & integration)
make docs                 # Build static docs to site/
make export-requirements  # Regenerate requirements.txt from Poetry
```

The [`requirements.txt`](requirements.txt) export supports lightweight
installations where Poetry is unavailable. Regenerate it after dependency
updates with `poetry export --without-hashes -f requirements.txt > requirements.txt`.

### 4. Docker Workflow

```bash
# Build the CUDA-enabled image
docker build -t ghcr.io/<org>/moml-ca:dev .

# Run interactively with GPU access
docker run --gpus all -it --rm \
  -v $(pwd):/workspace \
  ghcr.io/<org>/moml-ca:dev bash
```

See the [Dockerfile](Dockerfile) for customization hints and the
[`environment.yml`](environment.yml) for a matching conda spec.

## Contributing

Community contributions are welcome! Please review
[CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md)
before submitting a pull request. Automated linting and type checks run in CI,
so ensure `make lint && make test` succeed locally.

## License

A project-wide license will be added before the first public release. Until
then, contributions fall under the repository's default copyright.
