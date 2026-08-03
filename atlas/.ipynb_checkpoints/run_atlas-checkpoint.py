import numpy as np
import pandas as pd
from atlas.disk_atlas import DiskAtlas

# TODO: replace these with your real arrays from the notebook
r_vals = np.array([...])
scores = np.array([...])
compression = np.array([...])
stability = np.array([...])
v_drift = np.array([...])
planet_forces = np.array([...])
pressure = np.array([...])
sigma = np.array([...])
curvature = np.array([...])
ring_width = np.array([...])
survival = np.array([...])
gap_mass = np.array([...])
planet_mass_inversion = np.array([...])
brightness = np.array([...])
alpha = 0.001
nu = 1e-3

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

print("Hidden planet candidates:")
print(atlas.candidate_table())

print("\nMissing physics zones:")
print(atlas.missing_physics_table())

print("\nDisk classification:")
print(atlas.classify())
