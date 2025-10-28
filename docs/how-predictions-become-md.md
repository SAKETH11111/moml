# How Predictions Become MD

This document explains how directional, hierarchical MGNN predictions transform
into molecular dynamics (MD) simulations and long-horizon forecasts inside
MoML. It mirrors the single-path roadmap defined for the MIT THINK project.

## 1. Data Foundations

1. **PFAS Universe:** Curate canonical PFAS lists from OECD and EPA CompTox,
   sanitize them with RDKit, and generate low-energy conformers.
2. **Baseline Force Field:** Parameterize each molecule with OpenFF Sage to
   obtain reliable starting charges and Lennard-Jones values.
3. **Delta Labels:** Produce high-fidelity targets for partial charges and LJ
   parameters via RESP/Evaluator workflows. These labels drive supervised MGNN
   training.
4. **Auxiliary Physics:** Pull a targeted subset of SPICE fragments to regularize
   the model near relevant chemical space.
5. **Environmental Signals:** Aggregate plant data (pH, flow, temperature, etc.)
   for LSTM conditioning.

Outputs are stored as PyTorch Geometric graphs, tabular manifests, and DVC
artifacts so every experiment is traceable.

## 2. Directional, Hierarchical MGNN

1. **Inputs:** Graphs encode atom and bond features, baseline force-field
   parameters, and directional geometry via DimeNet++ style bases.
2. **Hierarchy:** ASAPooling coarsens the graph into functional supernodes; a
   U-Net skip architecture brings information back to the atom scale.
3. **Outputs:** A unified head predicts `Δq`, `Δσ`, and `Δε` per atom while
   enforcing charge neutrality and positive-definite LJ terms.
4. **Regularization:** Lightweight energy/force consistency on small fragments
   keeps deltas physically meaningful.

The trained MGNN yields delta parameters that update baseline OpenFF assignments
without diverging from chemical intuition.

## 3. Force-Field Assembly & OpenMM Simulation

1. **Delta Application:** Convert MGNN outputs into OpenFF patches or directly
   modify an OpenMM `System`.
2. **System Builder:** Construct solvated PFAS boxes or surface interactions,
   following OpenMM best practices (PME, Langevin integrators, constrained bonds).
3. **Execution:** Run smoke tests followed by production trajectories while
   logging metadata through WandB and DVC.
4. **Post-Processing:** Use MDAnalysis/MDTraj to compute observables such as
   RMSD, RDFs, adsorption metrics, and energy components.

## 4. LSTM Forecasting

1. **Windowed Features:** Transform MD observables and environmental covariates
   into sequences.
2. **Model:** A two-layer LSTM with LayerNorm predicts future dynamics across
   multiple horizons.
3. **Feedback:** Divergent forecasts trigger data/model refresh cycles, closing
   the MGNN → MD → LSTM loop.

## 5. End-to-End Flow

```
Data curation → Baseline OpenFF tagging → Δ-label generation →
Directional MGNN training → Force-field patching → OpenMM MD →
MD feature extraction → LSTM forecasting → Feedback into data/model queues
```

This blueprint keeps the repository laser focused: every new component either
improves data fidelity, strengthens MGNN predictions, stabilizes MD, or extends
forecast horizons. Subsequent documentation will dig deeper into individual
modules, but this narrative serves as the anchor for contributors today.
