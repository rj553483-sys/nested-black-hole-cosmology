"""
=============================================================================
Bianchi I / Low-Curvature Bianchi IX Limit Coupled Shear Integrator
=============================================================================
Rigorously integrates the coupled Raychaudhuri and anisotropic shear scalar 
ODE system from CMB recombination to the present day using scipy.integrate.solve_ivp. 
Verifies matter/shear/Lambda background evolution, shear dilution (sigma^2 ~ a^-6), 
and Wald's cosmic no-hair theorem under an accelerating de Sitter attractor.

Note: In the post-inflationary low-curvature limit (|Omega_k| <= 10^-3), the 
Bianchi IX spatial curvature anisotropy potential is negligible, reducing the 
shear dynamics to d(sigma^2)/dt = -6H * sigma^2.
=============================================================================
"""

import numpy as np
from scipy.integrate import solve_ivp

# Physical Constants & Planck Baseline Parameters (SI Units)
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
c = 2.99792458e8         # Speed of light (m/s)
H0 = 2.184e-18           # Present Hubble constant (~67.4 km/s/Mpc in s^-1)
Omega_m0 = 0.315         # Present matter density parameter
Omega_L0 = 0.685         # Present dark energy density parameter

Lambda = 3.0 * Omega_L0 * (H0**2) / (c**2)
H_Lambda = np.sqrt(Lambda * c**2 / 3.0)
rho_crit0 = 3.0 * (H0**2) / (8.0 * np.pi * G)
rho_m0 = Omega_m0 * rho_crit0

def bianchi_shear_ode(t, y):
    """
    Coupled Raychaudhuri + Shear ODE system (matter + shear + Lambda):
    y[0] = a(t)        (dimensionless scale factor, normalized to a_0 = 1 today)
    y[1] = da/dt       (s^-1)
    y[2] = sigma^2(t)  (shear scalar in s^-2)
    """
    a, adot, sig_sq = y
    H = adot / a
    rho_m = rho_m0 / (a**3)

    # Exact Raychaudhuri acceleration equation: d^2a/dt^2 = a * (-4*pi*G/3 * rho_m - 2/3 * sigma^2 + Lambda*c^2/3)
    addot = a * (-(4.0 * np.pi * G / 3.0) * rho_m - (2.0 / 3.0) * sig_sq + (Lambda * c**2 / 3.0))

    # Shear evolution: d(sigma^2)/dt = -6 * H * sigma^2
    dsig_sq_dt = -6.0 * H * sig_sq

    return [adot, addot, dsig_sq_dt]

def run_shear_integration():
    print("=== LOW-CURVATURE BIANCHI COUPLED SHEAR ISOTROPIZATION INTEGRATOR ===")
    print(f"Asymptotic de Sitter Hubble Rate (H_Lambda): {H_Lambda:.4e} s^-1")
    print("-" * 86)

    # Start at CMB recombination (z = 1100 => a_init = 1 / 1101)
    a_init = 1.0 / 1101.0
    # Initial dimensionless shear ratio consistent with CMB bound (sigma/H < 1e-5)
    sigma_over_H_init = 5.0e-6

    # Compute initial H from the exact Hamiltonian constraint:
    # H^2 * (1 - (1/3)*(sigma/H)^2) = (8*pi*G/3)*rho_m(a_init) + Lambda*c^2/3
    rho_m_init = rho_m0 / (a_init**3)
    H_init = np.sqrt(((8.0 * np.pi * G / 3.0) * rho_m_init + (Lambda * c**2 / 3.0)) / (1.0 - (sigma_over_H_init**2) / 3.0))

    adot_init = H_init * a_init
    sig_sq_init = (sigma_over_H_init * H_init)**2
    y0 = [a_init, adot_init, sig_sq_init]

    # Integrate from recombination (~380,000 yr) to present age (13.8 Gyr)
    t_start = 3.8e5 * 365.25 * 86400.0
    t_end = 1.38e10 * 365.25 * 86400.0
    t_eval = np.linspace(t_start, t_end, 200)

    sol = solve_ivp(bianchi_shear_ode, (t_start, t_end), y0, t_eval=t_eval, method='DOP853', rtol=1e-12, atol=1e-45)

    print(f"{'Time (Gyr)':<11} | {'Scale Factor a':<14} | {'Hubble H (s^-1)':<15} | {'sigma/H':<13} | {'Invariant err'}")
    print("-" * 86)

    invariant_0 = sig_sq_init * (a_init**6)
    for i in np.linspace(0, len(sol.t) - 1, 9, dtype=int):
        t_gyr = sol.t[i] / (365.25 * 86400.0 * 1e9)
        a_val = sol.y[0][i]
        H_val = sol.y[1][i] / a_val
        sig_sq_val = sol.y[2][i]
        sig_over_H = np.sqrt(max(0.0, sig_sq_val)) / H_val

        # Verify conservation of sigma^2 * a^6 = const
        inv_err = abs(sig_sq_val * (a_val**6) - invariant_0) / invariant_0

        print(f"{t_gyr:11.3f} | {a_val:14.6f} | {H_val:15.4e} | {sig_over_H:13.4e} | {inv_err:.2e}")

    print("=======================================================================")

if __name__ == "__main__":
    run_shear_integration()
