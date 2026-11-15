"""
=============================================================================
CMB Low-Multipole Power Deficit & Planck Bandpower Evaluator
=============================================================================
Evaluates the low-multipole (l=2 quadrupole, l=3 octopole) temperature power
suppression from residual host rotation (a/M) and de Sitter shear damping
exp(-3 * H_Lambda * t_iso) per Eq. (13), comparing predicted bandpowers D_l
against Planck 2018 / PR4 best-fit LCDM and observed low-l values.
=============================================================================
"""

import numpy as np

# Physical Constants & Cosmological Parameters
Lambda = 1.1056e-52    # Cosmological constant (m^-2)
c = 2.99792458e8       # Speed of light (m/s)
H_Lambda = np.sqrt(Lambda * c**2 / 3.0)

# Planck 2018 / PR4 Reference Low-l Temperature Bandpowers D_l = l(l+1)C_l/(2*pi) [uK^2]
D2_LCDM, D2_OBS = 1016.0, 226.0   # Quadrupole (l=2)
D3_LCDM, D3_OBS = 960.0,  490.0   # Octopole (l=3)

def compute_damping_factor(t_iso_years):
    """Calculates exponential shear isotropization damping exp(-3 * H_Lambda * t_iso)."""
    t_sec = t_iso_years * 365.25 * 86400.0
    return np.exp(-3.0 * H_Lambda * t_sec)

def run_cmb_deficit_evaluation():
    print("=== CMB LOW-MULTIPOLE POWER DEFICIT & BANDPOWER EVALUATOR ===")
    print(f"Asymptotic de Sitter Hubble Rate (H_Lambda): {H_Lambda:.4e} s^-1")
    print(f"Planck Reference Quadrupole (l=2): LCDM = {D2_LCDM:.1f} uK^2 | Observed = {D2_OBS:.1f} uK^2")
    print(f"Planck Reference Octopole   (l=3): LCDM = {D3_LCDM:.1f} uK^2 | Observed = {D3_OBS:.1f} uK^2")
    print("-" * 102)

    a_over_M_list = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50]
    t_iso_gyr = 1.0
    damping = compute_damping_factor(t_iso_gyr * 1e9)

    # Phenomenological multipole shear-coupling coefficients
    alpha2 = 0.45
    alpha3 = 0.28

    print(f"{'Host a/M':<9} | {'dC2/C2 (%)':<11} | {'Pred D2 (uK^2)':<15} | {'dC3/C3 (%)':<11} | {'Pred D3 (uK^2)':<15} | {'Regime'}")
    print("-" * 102)

    for a_M in a_over_M_list:
        frac2 = -alpha2 * (a_M**2) * damping
        frac3 = -alpha3 * (a_M**2) * damping
        pred_D2 = D2_LCDM * (1.0 + frac2)
        pred_D3 = D3_LCDM * (1.0 + frac3)
        note = "Linear perturbative" if a_M <= 0.10 else "2nd-order extrapolation"
        print(f"{a_M:9.2f} | {frac2*100:10.3f}% | {pred_D2:15.1f} | {frac3*100:10.3f}% | {pred_D3:15.1f} | {note}")

    print("=" * 102)

if __name__ == "__main__":
    run_cmb_deficit_evaluation()
