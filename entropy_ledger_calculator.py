import numpy as np

# Fundamental Constants (CODATA 2018)
G = 6.67430e-11        # m^3 kg^-1 s^-2
hbar = 1.054571817e-34 # J s
c = 2.99792458e8       # m/s
kB = 1.380649e-23      # J/K
M_sun = 1.98840e30     # kg

def compute_host_mass_bound(S_int=3.1e104):
    """
    Computes minimum host black hole mass M_ext from interior entropy budget S_int:
    M_ext = (1/2) * sqrt( (S_int * hbar * c) / (pi * G) )
    """
    M_ext_kg = 0.5 * np.sqrt((S_int * hbar * c) / (np.pi * G))
    M_ext_Msun = M_ext_kg / M_sun
    
    # Schwarzschild Horizon Radius
    r_S_m = 2.0 * G * M_ext_kg / (c**2)
    r_S_pc = r_S_m / 3.085677581e16
    
    # Horizon Entry Density
    rho_horizon = (3.0 * c**6) / (32.0 * np.pi * G**3 * M_ext_kg**2)
    
    # Classical Hawking Evaporation Time
    t_evap_sec = (5120.0 * np.pi * G**2 * M_ext_kg**3) / (hbar * c**4)
    t_evap_yr = t_evap_sec / (365.25 * 86400.0)
    
    print("=== BEKENSTEIN-HAWKING ENTROPY LEDGER & HOST MASS BOUND ===")
    print(f"Observable Universe Entropy (S_int): {S_int:.2e} k_B")
    print(f"Minimum Host Black Hole Mass (M_ext): {M_ext_kg:.4e} kg")
    print(f"Minimum Host Black Hole Mass (M_ext): {M_ext_Msun:.4e} M_sun (5.4 x 10^13 M_sun)")
    print(f"Schwarzschild Horizon Radius (r_S): {r_S_m:.4e} m ({r_S_pc:.2f} pc)")
    print(f"Mean Horizon Entry Density (rho_horizon): {rho_horizon:.4e} kg/m^3 (Ultra-dilute, << air 1.225 kg/m^3)")
    print(f"Classical Hawking Evaporation Time (t_evap): {t_evap_yr:.4e} years (> 10^100 years)")

if __name__ == "__main__":
    compute_host_mass_bound()
