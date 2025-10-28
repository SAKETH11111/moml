# MoML-CA Documentation

Welcome to the living specification for MoML-CA. This site complements the
repository structure by capturing design decisions, implementation notes, and
research context.

## Contents

- **Architecture Overview:** High-level system diagrams, dependency graphs, and
  interface contracts.
- **Configuration Registry:** Guidelines for extending Hydra configurations
  located in `configs/`.
- **Data Sources:** Provenance, governance, and transformation steps for each
  dataset.
- **Model Zoo:** Summaries of baseline and experimental architectures.
- **Simulation Playbook:** Recipes for integrating physics-based or agent-based
  simulations into ML pipelines.
- **Operations Cookbook:** Deployment strategies, observability hooks, and
  reproducibility workflows.
- **Roadmap:** See [roadmap.md](roadmap.md) for milestone planning and ownership.

## Getting Started

1. Install project dependencies (see the [README](../README.md)).
2. To work on documentation locally:
   ```bash
   poetry install --extras "docs"
   poetry run mkdocs serve
   ```
3. Draft new pages under `docs/` and update navigation in `mkdocs.yml` once it is
   introduced.

## Style Guide

- Use [MyST Markdown](https://myst-parser.readthedocs.io/) syntax when advanced
  directives are needed. Even though MyST is not enabled yet, structuring
  content with this standard makes future migrations easier.
- Keep sections concise. Factor out deep dives into dedicated pages linked from
  summaries.
- Include diagrams when they add clarity. We recommend storing source files in
  `docs/assets/` and exporting SVG for version control friendliness.

Have ideas for improving the docs? Open an issue or share your proposal in the
community discussion channels.
