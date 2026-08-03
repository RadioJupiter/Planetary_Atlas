import os
import numpy as np
from .disk_atlas import DiskAtlas

def load_atlas():
    # Path to this folder
    here = os.path.dirname(__file__)
    data_path = os.path.join(here, "atlas_data.npz")

    data = np.load(data_path)

    atlas = DiskAtlas(
        data["r_vals"],
        data["scores"],
        data["compression"],
        data["stability"],
        data["v_drift"],
        data["planet_forces"],
        data["pressure"],
        data["sigma"],
        data["curvature"],
        data["ring_width"],
        data["survival"],
        data["gap_mass"],
        data["planet_mass_inversion"],
        data["brightness"],
        data["alpha"],
	data["nu"]

    )

    return atlas
