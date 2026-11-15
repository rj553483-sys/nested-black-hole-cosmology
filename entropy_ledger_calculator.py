"""
=============================================================================
Bekenstein-Hawking Entropy Ledger & Host Mass Bound Calculator
=============================================================================
Sums the empirical cosmic entropy inventory (Egan & Lineweaver 2010, Table 1)
and inverts the Bekenstein-Hawking area law (S_ext >= S_int) to derive the
minimum host black hole mass bound M_ext, Schwarzschild radius r_S, mean
horizon entry density, and Hawking evaporation timescale.
=============================================================================
"""

import numpy as np

# CODATA 2018 / IAU Physical Constants (SI Units)
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
hbar = 1.054571817e-34   # Reduced Planck constant (J s)
c = 2.99792458e8         # Speed of light (m/s)
kB = 1.380649e-23        # Boltzmann constant (J/K)
M_sun = 1.98840e30       # Solar mass (kg)
PC_IN_M = 3.085677581e16 # Parsec in meters
YR_IN_S = 365.25 * 86400.0

# Empirical Cosmic Entropy Inventory (Table 1, in units of k_B)
ENTROPY_LEDGER_KB = {
    "Supermassive Black Holes (SMBHs)": 3.1e104,
    "Stellar-Mass Black Holes (2.5-15 M_sun)": 5.0e97,
    "Cosmic Microwave Background (CMB)": 5.4e89,
    "Relic Neutrinos (CNB)": 5.2e89,
    "Dark Matter & Interstellar Medium": 1.0e88,
    "Stars & Baryonic Matter": 1.0e81,
}

def evaluate_host_bounds(S_int_kB):
    """Inverts S_ext = 4*pi*k_B*G*M^2 / (hbar*c) >= S_int to compute host scales."""
    M_ext_kg = 0.5 * np.sqrt((S_int_kB * hbar * c) / (np.pi * kB * G))
    M_ext_Msun = M_ext_kg / M_sun
    r_S_m = 2.0 * G * M_ext_kg / (c**2)
    r_S_pc = r_S_m / PC_IN_M
    rho_horizon = (3.0 * c**6) / (32.0 * np.pi * (G**3) * (M_ext_kg**2))
    t_evap_yr = (5120.0 * np.pi * (G**2) * (M_ext_kg**3)) / (hbar * (c**4) * YR_IN_S)
    return M_ext_Msun, r_S_m, r_S_pc, rho_horizon, t_evap_yr

def run_entropy_ledger():
    S_total = sum(ENTROPY_LEDGER_KB.values())

    print("=== EMPIRICAL COSMIC ENTROPY LEDGER (TABLE 1) ===")
    for component, val in ENTROPY_LEDGER_KB.items():
        share = (val / S_total) * 100.0
        print(f"  {component:<42}: {val:.2e} k_B ({share:.4g}%)")
    print("-" * 78)
    print(f"  Total Observable Matter/BH Entropy (S_int)  : {S_total:.4e} k_B")
    print("=" * 78)

    M_ext, r_S_m, r_S_pc, rho_h, t_evap = evaluate_host_bounds(S_total)
    print("\n=== DERIVED HOST BLACK HOLE LOWER BOUNDS ===")
    print(f"  Minimum Host Mass (M_ext)      : {M_ext:.4e} M_sun")
    print(f"  Schwarzschild Radius (r_S)     : {r_S_m:.4e} m ({r_S_pc:.2f} pc)")
    print(f"  Mean Horizon Entry Density     : {rho_h:.4e} kg/m^3 (vs. air 1.225 kg/m^3)")
    print(f"  Hawking Evaporation Timescale  : {t_evap:.4e} yr")
    print("=" * 78)

if __name__ == "__main__":
    run_entropy_ledger()
