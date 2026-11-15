"""
=============================================================================
Holographic Boundary Flux & Effective Dark Energy Coupling Analysis
=============================================================================
Evaluates the inter-tier holographic boundary coupling parameter kappa
(scaling inversely with host horizon entropy ratio S_ext / S_int per Sec. 3.4)
and computes the resulting boundary energy-momentum flux Q_boundary (Eq. 7)
and effective dark energy equation of state perturbation w0_eff (Eq. 9).
=============================================================================
"""

import numpy as np

# CODATA 2018 / Planck 2018 Cosmological Parameters (SI Units)
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
c = 2.99792458e8         # Speed of light (m/s)
M_sun = 1.98840e30       # Solar mass (kg)
H0 = 2.184e-18           # Present Hubble rate (~67.4 km/s/Mpc in s^-1)
Omega_m0 = 0.315         # Present matter density fraction
Omega_L0 = 0.685         # Present vacuum energy density fraction

# Present critical energy density (J/m^3) and observable patch volume (m^3)
rho_crit0_energy = (3.0 * (H0**2) * (c**2)) / (8.0 * np.pi * G)
rho_de0_energy = Omega_L0 * rho_crit0_energy
R_obs_m = 14.3e9 * 3.085677581e16  # 14.3 Gpc observable patch radius in meters
V_int0 = (4.0 / 3.0) * np.pi * (R_obs_m**3)

def hubble_lcdm(z):
    """Background Hubble expansion rate H(z) in s^-1."""
    return H0 * np.sqrt(Omega_m0 * ((1.0 + z)**3) + Omega_L0)

def evaluate_boundary_coupling(S_ratio, kappa_0=1.0e-3, M_dot_Msun_per_yr=1.0e3):
    """
    Computes effective coupling kappa = kappa_0 * (S_int / S_ext) and the
    induced dark energy equation of state shift dw = w_eff(0) - (-1) at z = 0.
    """
    kappa = kappa_0 / S_ratio
    M_dot_kg_s = (M_dot_Msun_per_yr * M_sun) / (365.25 * 86400.0)

    # Boundary energy flux Q_boundary = kappa * c^2 * (M_dot / V_int) [J m^-3 s^-1]
    Q_boundary = kappa * (c**2) * (M_dot_kg_s / V_int0)

    # Continuity equation with boundary equilibration transfer (-Q_boundary):
    # drho_de/dt + 3H(1 + w_eff)rho_de = -Q_boundary  =>  w0_eff = -1 + Q_boundary / (3 * H0 * rho_de0)
    delta_w0 = abs(Q_boundary) / (3.0 * H0 * rho_de0_energy)
    w0_eff = -1.0 + delta_w0
    return kappa, Q_boundary, w0_eff

def run_coupling_analysis():
    print("=== HOLOGRAPHIC BOUNDARY FLUX & DARK ENERGY COUPLING ANALYSIS ===")
    print(f"Baseline Observable Volume (V_int) : {V_int0:.4e} m^3")
    print(f"Present Dark Energy Density        : {rho_de0_energy:.4e} J/m^3")
    print("-" * 88)
    print(f"{'Entropy Ratio (S_ext/S_int)':<27} | {'Coupling kappa':<15} | {'Flux Q (J/m^3/s)':<18} | {'Effective w0'}")
    print("-" * 88)

    for ratio in [1.0, 10.0, 100.0, 1000.0]:
        kappa, Q_flux, w0_eff = evaluate_boundary_coupling(ratio)
        print(f"{ratio:27.1f} | {kappa:15.4e} | {Q_flux:18.4e} | {w0_eff:+.6e}")

    print("=" * 88)

if __name__ == "__main__":
    run_coupling_analysis()
