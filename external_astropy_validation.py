"""
=============================================================================
Observational Parameter Bounds Consistency Check
=============================================================================
Compares the Nested Black Hole Cosmology predictions (Table 2: spatial curvature
Omega_k and dynamical dark energy parameters w0, wa) against published 1D
marginalized constraints from Planck 2018/PR4 + BAO and DESI DR1/DR2 + Pantheon+.
Calculates parameter pulls and summary chi-squared consistency metrics.
=============================================================================
"""

import numpy as np

# Published Observational 1D Constraints vs. Representative Model Predictions (Table 2)
OBSERVATIONAL_CONSTRAINTS = {
    "Planck + BAO (Spatial Curvature Omega_k)": {
        "Observed_Val": 0.0007,      # Planck 2018 + BAO baseline (arXiv:1807.06209)
        "Obs_Error": 0.0019,
        "Model_Val": -0.0005,        # Midpoint of Table 2 prediction: -1e-3 <= Omega_k <= -1e-4
    },
    "DESI DR1 + Pantheon+ (Dark Energy w0)": {
        "Observed_Val": -0.827,      # DESI 2024 VI + Pantheon+ CPL fit (arXiv:2404.03002)
        "Obs_Error": 0.063,
        "Model_Val": -0.950,         # Representative Table 2 prediction: w0 > -1
    },
    "DESI DR1 + Pantheon+ (Dark Energy wa)": {
        "Observed_Val": -0.75,       # DESI 2024 VI + Pantheon+ CPL fit (arXiv:2404.03002)
        "Obs_Error": 0.27,
        "Model_Val": -0.20,          # Representative Table 2 prediction: wa < 0
    },
}

def run_bounds_consistency_check():
    print("=== OBSERVATIONAL PARAMETER BOUNDS CONSISTENCY CHECK ===")
    print("Comparing Table 2 Predictions against Published Planck & DESI + Pantheon+ Constraints")
    print("-" * 102)
    print(f"{'Observable Constraint':<42} | {'Published ± 1σ':<18} | {'Model Val':<11} | {'Pull':<8} | {'chi^2'}")
    print("-" * 102)

    total_chi2 = 0.0
    dof = len(OBSERVATIONAL_CONSTRAINTS)

    for label, entry in OBSERVATIONAL_CONSTRAINTS.items():
        obs = entry["Observed_Val"]
        err = entry["Obs_Error"]
        mod = entry["Model_Val"]

        pull = (mod - obs) / err
        chi2 = pull**2
        total_chi2 += chi2

        print(f"{label:<42} | {obs:+.4f} ± {err:.4f}   | {mod:+.4f}     | {pull:+.2f}σ   | {chi2:.4f}")

    reduced_chi2 = total_chi2 / dof
    print("-" * 102)
    print(f"  Summary Chi-Squared (chi^2)          : {total_chi2:.4f} (DOF = {dof})")
    print(f"  Reduced Chi-Squared (chi^2 / DOF)    : {reduced_chi2:.4f}")
    print("  Note: Evaluates 1D marginalized published bounds; full covariance MCMC is external.")
    print("=" * 102)

if __name__ == "__main__":
    run_bounds_consistency_check()
