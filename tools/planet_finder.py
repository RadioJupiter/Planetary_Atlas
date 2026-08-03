# planet_finder.py
import numpy as np
import pandas as pd

def find_planet_candidates(atlas, max_candidates=5):
    """
    Use DiskAtlas physics to identify likely planet locations.
    """
    df = atlas.candidate_table().copy()

    # Simple planet-likeness score
    df["planet_score"] = (
        0.4 * df["planet_forces"] +
        0.3 * df["gap_mass"] +
        0.2 * df["planet_mass_inversion"] +
        0.1 * df["compression"]
    )

    df_sorted = df.sort_values("planet_score", ascending=False)

    return df_sorted.head(max_candidates)[
        ["radius_AU", "planet_score", "planet_forces",
         "gap_mass", "planet_mass_inversion", "compression"]
    ]
