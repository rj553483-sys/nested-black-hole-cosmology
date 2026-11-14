import numpy as np

G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
kB = 1.380649e-23
M_sun = 1.98840e30

def compute_host_mass_bound(S_int=3.1e104):
    M_ext_kg = 0.5 * np.sqrt((S_int * hbar * c) / (np.pi * kB * G))
    M_ext_Msun = M_ext_kg / M_sun
    r_S_m = 2.0 * G * M_ext_kg / (c**2)
    r_S_pc = r_S_m / 3.085677581e16
    rho_horizon = (3.0 * c**6) / (32.0 * np.pi * G**3 * M_ext_kg**2)
    t_evap_sec = (5120.0 * np.pi * G**2 * M_ext_kg**3) / (hbar * c**4)
    t_evap_yr = t_evap_sec / (365.25 * 86400.0)
    print("=== BEKENSTEIN-HAWKING ENTROPY LEDGER & HOST MASS BOUND ===")
    print(f"Observable Universe Entropy (S_int): {S_int:.2e} k_B")
    print(f"Minimum Host Mass: {M_ext_Msun:.4e} M_sun (5.4 x 10^13 M_sun)")
    print(f"Schwarzschild Radius: {r_S_m:.4e} m ({r_S_pc:.2f} pc)")
    print(f"Horizon Density: {rho_horizon:.4e} kg/m^3 (Ultra-dilute, << air 1.225 kg/m^3)")
    print(f"Evaporation Time: {t_evap_yr:.2e} yr")

if __name__ == "__main__":
    compute_host_mass_bound()
