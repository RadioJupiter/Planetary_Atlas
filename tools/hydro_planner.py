# hydro_planner.py
import pandas as pd
import numpy as np

def make_hydro_plan(atlas, max_targets=10):
    """
    Build a prioritized list of radii for hydro simulations.
    """
    cand = atlas.candidate_table().copy()
    zones = atlas.missing_physics_table().copy()

    # Priority score: strong physics + planet-like features
    cand["priority_score"] = (
        0.3 * cand["compression"] +
        0.3 * cand["pressure"] +
        0.2 * cand["stability"] +
        0.2 * cand["planet_forces"]
    )

    cand_sorted = cand.sort_values("priority_score", ascending=False)

    top = cand_sorted.head(max_targets).copy()

    # Tag reasons
    reasons = []
    for _, row in top.iterrows():
        r = row["radius_AU"]
        tags = []

        if row["planet_forces"] > 0.7:
            tags.append("planet-like forces")
        if row["gap_mass"] > 0.7:
            tags.append("gap structure")
        if row["pressure"] > 0.7:
            tags.append("pressure bump")
        if row["stability"] > 0.7:
            tags.append("stable ring zone")

        reasons.append(", ".join(tags) if tags else "general ring candidate")

    top["reason"] = reasons

    return top[["radius_AU", "priority_score", "reason"]]
