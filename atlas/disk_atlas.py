import numpy as np
import pandas as pd

class DiskAtlas:
    """
    DiskAtlas: Pure-conditions model for predicting ring formation,
    identifying hidden planets, and mapping disk structure.

    This model uses precomputed physical arrays from atlas_data.npz:
    - compression
    - stability
    - v_drift
    - planet_forces
    - pressure
    - sigma
    - curvature
    - ring_width
    - survival
    - gap_mass
    - planet_mass_inversion
    - brightness
    - alpha(r)
    - nu(r)

    Candidate radii are detected using local maxima in each physical array.
    """

    def __init__(
        self,
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
    ):
        self.r_vals = r_vals
        self.scores = scores
        self.compression = compression
        self.stability = stability
        self.v_drift = v_drift
        self.planet_forces = planet_forces
        self.pressure = pressure
        self.sigma = sigma
        self.curvature = curvature
        self.ring_width = ring_width
        self.survival = survival
        self.gap_mass = gap_mass
        self.planet_mass_inversion = planet_mass_inversion
        self.brightness = brightness
        self.alpha = alpha
        self.nu = nu

        # Build candidate radii immediately
        self.candidates = self._find_candidate_radii()

    # ------------------------------------------------------------
    # INTERNAL: Local maxima detection
    # ------------------------------------------------------------

    def _local_maxima(self, arr):
        """Return radii where arr has local maxima."""
        peaks = []
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                peaks.append(self.r_vals[i])
        return np.array(peaks)

    def _find_candidate_radii(self):
        """Combine local maxima from all physical arrays."""
        peak_sets = [
            self._local_maxima(self.compression),
            self._local_maxima(self.stability),
            self._local_maxima(self.planet_forces),
            self._local_maxima(self.pressure),
            self._local_maxima(self.sigma),
            self._local_maxima(self.curvature),
            self._local_maxima(self.survival),
            self._local_maxima(self.gap_mass),
            self._local_maxima(self.planet_mass_inversion),
            self._local_maxima(self.brightness),
        ]

        all_peaks = np.concatenate(peak_sets)
        all_peaks = np.unique(np.round(all_peaks, 2))
        return np.sort(all_peaks)

    # ------------------------------------------------------------
    # PUBLIC: Candidate table
    # ------------------------------------------------------------

    def candidate_table(self):
        """Return a table of candidate radii with physical conditions."""
        rows = []
        for r in self.candidates:
            idx = np.argmin(np.abs(self.r_vals - r))
            rows.append({
                "radius_AU": r,
                "compression": self.compression[idx],
                "stability": self.stability[idx],
                "v_drift": self.v_drift[idx],
                "planet_forces": self.planet_forces[idx],
                "pressure": self.pressure[idx],
                "sigma": self.sigma[idx],
                "curvature": self.curvature[idx],
                "ring_width": self.ring_width[idx],
                "survival": self.survival[idx],
                "gap_mass": self.gap_mass[idx],
                "planet_mass_inversion": self.planet_mass_inversion[idx],
                "brightness": self.brightness[idx],
            })

        return pd.DataFrame(rows)

    # ------------------------------------------------------------
    # PUBLIC: Missing physics table
    # ------------------------------------------------------------

    def missing_physics_table(self):
        """
        Identify key physics zones:
        - snowline (temperature drop)
        - dead zone (viscosity jump)
        - drift trap (v_drift minimum)
        - pressure bump (pressure maximum)
        - gap edges (planet_mass_inversion peaks)
        """

        # Snowline: alpha/nu transition
        snow_idx = np.argmin(np.abs(self.alpha - np.median(self.alpha)))
        snowline = self.r_vals[snow_idx]

        # Dead zone: alpha minimum
        dead_idx = np.argmin(self.alpha)
        dead_zone = self.r_vals[dead_idx]

        # Drift trap: v_drift minimum
        drift_idx = np.argmin(self.v_drift)
        drift_trap = self.r_vals[drift_idx]

        # Pressure bump: pressure maximum
        pb_idx = np.argmax(self.pressure)
        pressure_bump = self.r_vals[pb_idx]

        # Gap edges: planet_mass_inversion peaks
        gap_edges = self._local_maxima(self.planet_mass_inversion)

        return pd.DataFrame({
            "zone": ["snowline", "dead_zone", "drift_trap", "pressure_bump", "gap_edges"],
            "radius_AU": [
                snowline,
                dead_zone,
                drift_trap,
                pressure_bump,
                list(gap_edges)
            ]
        })

    # ------------------------------------------------------------
    # PUBLIC: Disk classification
    # ------------------------------------------------------------

    def classify(self):
        """
        Classify disk based on physical conditions.
        """

        num_candidates = len(self.candidates)

        # Strength indicators
        strong_pressure = np.max(self.pressure)
        strong_planet_forces = np.max(self.planet_forces)
        strong_gap_mass = np.max(self.gap_mass)

        if strong_planet_forces > 0.8 and strong_gap_mass > 0.8:
            return "Planet-dominated disk"

        if strong_pressure > 0.8 and num_candidates > 5:
            return "Pressure-structured disk"

        if num_candidates < 3:
            return "Weakly-structured disk"

        return "Mixed-physics disk"
