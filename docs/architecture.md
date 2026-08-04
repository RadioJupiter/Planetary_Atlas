\# Architecture Overview



Planetary\_Atlas is organized into three main layers:



\## 1. Core Physics Layer — `atlas/`

Contains the scientific logic and disk‑physics models.



\### Key Module: `disk\_atlas.py`

\- Loads disk data

\- Computes physics tables

\- Provides analysis helpers



\---



\## 2. Analysis Tools — `tools/`

Small, focused utilities that operate on a `DiskAtlas` instance.



\### `planet\_finder.py`

Ranks radii by planet‑like signatures.



\### `hydro\_planner.py`

Creates a prioritized list of radii for hydro simulations.



\---



\## 3. Documentation — `docs/`

Human‑readable guides, API references, and notebooks.



\### Includes:

\- `overview.md`

\- `api.md`

\- `Quickstart.ipynb`

\- `architecture.md` (this file)



\---



\## Data Flow





1\. Load disk physics  

2\. Identify planet candidates  

3\. Build hydro simulation plan  

4\. Export or visualize results



\---



\## Design Goals

\- Clear separation between physics and tools

\- Minimal dependencies

\- Easy to extend with new analysis modules



