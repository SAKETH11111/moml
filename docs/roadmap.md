# MoML-CA Roadmap

This roadmap outlines the evolving milestones for MoML-CA. It expands on the
high-level phases described in the [project README](../README.md).

## Phase 0 — Foundations

- [x] Repository bootstrap (tooling, packaging, docs skeleton).
- [ ] Define coding conventions and review guidelines.
- [ ] Establish continuous integration and release pipelines.

## Phase 1 — Data Backbone

- [ ] Data catalog structure in `configs/data/` with validation schemas.
- [ ] Sample ETL pipeline covering molecule ingestion and cleaning.
- [ ] Feature store integration for experiment reproducibility.

## Phase 2 — Modeling Core

- [ ] Baseline graph neural network models with training scripts.
- [ ] Evaluation suite covering regression/classification metrics.
- [ ] Model registry for experiment tracking.

## Phase 3 — Simulation Loop

- [ ] Simulation adapters interfacing with physics-based engines.
- [ ] Calibration routines aligning simulation outputs with empirical data.
- [ ] Scenario generation and stress testing workflows.

## Phase 4 — Automation

- [ ] Experiment orchestration templates.
- [ ] Observability stack (logging, tracing, experiment dashboards).
- [ ] Continuous deployment strategy for model & simulation releases.

> _Have suggestions or want to take ownership of a roadmap item? Open an issue
> or start a discussion thread so we can collaborate on priorities and scope._
