"""
=============================================================================
Bianchi IX Shear Isotropization Integrator
=============================================================================
Evaluates the exponential decay of spatial shear anisotropy (sigma^2 / H^2)
driven by Wald's cosmic no-hair theorem in the presence of positive vacuum 
energy (Lambda > 0) for the Nested Black Hole Cosmology framework.
=============================================================================
"""

import numpy as np

H0 = 2.184e-18
Lambda = 1.1056e-52
c = 2.99792458e8
H_Lambda = np.sqrt(Lambda * c**2 / 3.0)

def shear_damping_ratio(t_years):
    t_sec = t_years * 365.25 * 86400.0
    return np.exp(-3.0 * H_Lambda * t_sec)

def evaluate_shear_decay():
    print("=== BIANCHI IX SHEAR ISOTROPIZATION EVALUATION ===")
    print(f"Late-time de Sitter Hubble rate H_Lambda: {H_Lambda:.4e} s^-1")
    print("Time (Years)      | Damping Factor exp(-3 H_Lambda t)")
    print("-" * 50)
    times = [1e8, 5e8, 1e9, 5e9, 1.38e10]
    for t in times:
        factor = shear_damping_ratio(t)
        print(f"  {t:12.2e} yr |   {factor:.4e}")

if __name__ == "__main__":
    evaluate_shear_decay()
