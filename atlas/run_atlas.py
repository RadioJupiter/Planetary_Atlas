import numpy as np
import pandas as pd
from disk_atlas import DiskAtlas


# ============================
# LOAD DATA FROM FILE
# ============================

data = np.load("atlas_data.npz")

r_vals = data["r_vals"]
scores = data["scores"]
compression = data["compression"]
stability = data["stability"]
v_drift = data["v_drift"]
planet_forces = data["planet_forces"]
pressure = data["pressure"]
sigma = data["sigma"]
curvature = data["curvature"]
ring_width = data["ring_width"]
survival = data["survival"]
gap_mass = data["gap_mass"]
planet_mass_inversion = data["planet_mass_inversion"]
brightness = data["brightness"]

alpha = float(data["alpha"])
nu = float(data["nu"])

# ============================
# CREATE ATLAS INSTANCE
# ============================

atlas = DiskAtlas(
    r_vals,
    scores,
    compression,
    stability,
    v_drift,
    planet_forces,
    pressure,
    sigma,
    curvature,
    ring_width,
    survival,
    gap_mass,
    planet_mass_inversion,
    brightness,
    alpha,
    nu
)

# ============================
# RUN BASIC TESTS
# ============================

print("Hidden planet candidates:")
print(atlas.candidate_table())

print("\nMissing physics zones:")
print(atlas.missing_physics_table())

print("\nDisk classification:")
print(atlas.classify())
