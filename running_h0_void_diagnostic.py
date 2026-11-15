"""
=============================================================================
Modified Friedmann Expansion Rate H(z) & CPL Dark Energy Diagnostic
=============================================================================
Evaluates the redshift evolution of the Hubble expansion parameter H(z)
in the Nested Black Hole Cosmology framework relative to flat LCDM,
incorporating closed spatial curvature (Omega_k in [-1e-3, -1e-4]) and
holographically induced CPL dynamical dark energy w(z) = w0 + wa * z/(1+z)
(Eqs. 4 & 9, Table 2).
=============================================================================
"""

import numpy as np

# Planck 2018 Baseline Parameters
H0_KM_S_MPC = 67.4       # Present Hubble constant (km / s / Mpc)
OMEGA_M0 = 0.315         # Present matter density parameter

def e_lcdm(z):
    """Dimensionless Hubble rate E(z) = H(z)/H0 for flat LCDM (Omega_k = 0, w = -1)."""
    omega_l0 = 1.0 - OMEGA_M0
    return np.sqrt(OMEGA_M0 * ((1.0 + z)**3) + omega_l0)

def e_nested_bh(z, omega_k0=-0.0005, w0=-0.95, wa=-0.20):
    """
    Dimensionless Hubble rate E(z) = H(z)/H0 for closed Nested BH Cosmology
    with CPL dynamical dark energy w(z) = w0 + wa * z / (1 + z) (Eq. 9).
    """
    omega_de0 = 1.0 - OMEGA_M0 - omega_k0
    de_evolution = ((1.0 + z)**(3.0 * (1.0 + w0 + wa))) * np.exp(-3.0 * wa * z / (1.0 + z))
    return np.sqrt(
        OMEGA_M0 * ((1.0 + z)**3)
        + omega_k0 * ((1.0 + z)**2)
        + omega_de0 * de_evolution
    )

def run_expansion_diagnostic():
    print("=== MODIFIED FRIEDMANN EXPANSION RATE H(z) DIAGNOSTIC ===")
    print("Model Parameters: Omega_k = -5.0e-4 | w0 = -0.95 | wa = -0.20 (Table 2)")
    print("-" * 82)
    print(f"{'Redshift z':<12} | {'H_LCDM (km/s/Mpc)':<19} | {'H_Nested (km/s/Mpc)':<21} | {'Ratio H_Nested/H_LCDM'}")
    print("-" * 82)

    z_list = [0.0, 0.25, 0.50, 1.00, 1.50, 2.00]
    for z in z_list:
        h_std = H0_KM_S_MPC * e_lcdm(z)
        h_mod = H0_KM_S_MPC * e_nested_bh(z)
        ratio = h_mod / h_std
        print(f"{z:12.2f} | {h_std:19.3f} | {h_mod:21.3f} | {ratio:21.6f}")

    print("=" * 82)

if __name__ == "__main__":
    run_expansion_diagnostic()
