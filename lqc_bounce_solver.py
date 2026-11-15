"""
=============================================================================
Loop Quantum Cosmology (LQC) Effective Bounce ODE Solver
=============================================================================
Numerically integrates the holonomy-corrected effective Raychaudhuri and
Friedmann equations (Eqs. 4-6) for closed (k = +1) pressureless dust across
the non-singular quantum bounce at critical density rho_c ~ 0.41 rho_Pl.
Tracks scale factor a(t), Hubble parameter H(t), effective quantum pressure,
Null Energy Condition (NEC) violation, and Hamiltonian constraint accuracy.
=============================================================================
"""

import numpy as np
from scipy.integrate import solve_ivp

# CODATA 2018 Physical Constants (SI Units)
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
hbar = 1.054571817e-34   # Reduced Planck constant (J s)
c = 2.99792458e8         # Speed of light (m/s)
gamma = 0.237538         # Barbero-Immirzi parameter (LQG state counting)
Lambda = 1.1056e-52      # Cosmological constant (m^-2)

# Planck Density & Critical LQC Bounce Density (Eq. 5)
rho_Pl = c**5 / (hbar * G**2)
rho_c = (np.sqrt(3.0) * c**5) / (32.0 * np.pi**2 * (gamma**3) * (G**2) * hbar)
rho_c_in_rho_Pl = rho_c / rho_Pl

# Closed FLRW Spatial Curvature Parameter (k = +1, physical radius scale at bounce)
K_CURV = 1.0
A_MIN = 1.0e-26  # Physical curvature radius at bounce (m), ensuring k*c^2/a^2 << G*rho_c

def effective_lqc_fluid(rho):
    """
    Computes effective LQC density and repulsive quantum pressure for dust (P_class = 0):
    rho_eff = rho * (1 - rho / rho_c)
    P_eff   = - (rho^2 / rho_c) * c^2   [Repulsive negative pressure driving the bounce]
    NEC sum = rho_eff * c^2 + P_eff = rho * c^2 * (1 - 2 * rho / rho_c)
    """
    rho_eff = rho * (1.0 - rho / rho_c)
    p_eff = -(rho**2 / rho_c) * (c**2)
    nec_sum = rho_eff * (c**2) + p_eff
    return rho_eff, p_eff, nec_sum

def lqc_raychaudhuri_ode(t, y):
    """
    Coupled ODE system for closed (k = +1) LQC dust universe:
    y[0] = a(t)     (physical curvature scale factor in meters)
    y[1] = da/dt    (m/s)
    """
    a, adot = y
    rho = rho_c * ((A_MIN / a)**3)
    H = adot / a

    # LQC-modified Raychaudhuri equation for closed dust + Lambda:
    # dH/dt = -4*pi*G*rho*(1 - 2*rho/rho_c) + k*c^2 / a^2
    dot_H = -4.0 * np.pi * G * rho * (1.0 - 2.0 * (rho / rho_c)) + (K_CURV * (c**2) / (a**2))
    addot = a * ((H**2) + dot_H)
    return [adot, addot]

def run_lqc_bounce_solver():
    print("=== LOOP QUANTUM COSMOLOGY (LQC) EFFECTIVE BOUNCE ODE SOLVER ===")
    print(f"Planck Density (rho_Pl)        : {rho_Pl:.4e} kg/m^3")
    print(f"Critical Bounce Density (rho_c): {rho_c:.4e} kg/m^3 ({rho_c_in_rho_Pl:.4f} rho_Pl)")
    print("-" * 104)

    # Exact bounce density where H = 0 (accounting for tiny k = +1 curvature term at a = A_MIN)
    coeff_b = (8.0 * np.pi * G / 3.0)
    curv_term = (K_CURV * (c**2) / (A_MIN**2)) - (Lambda * (c**2) / 3.0)
    discriminant = max(0.0, 1.0 - (4.0 * curv_term) / (coeff_b * rho_c))
    rho_bounce = 0.5 * rho_c * (1.0 + np.sqrt(discriminant))

    # Rescale A_MIN slightly so rho(A_MIN) == rho_bounce at t = 0, da/dt = 0
    a_bounce = A_MIN * ((rho_c / rho_bounce)**(1.0 / 3.0))
    y_bounce = [a_bounce, 0.0]

    # Characteristic Planckian bounce timescale ~ 1 / sqrt(G * rho_c) ~ 1e-43 s
    t_max = 5.0e-43
    t_neg = np.linspace(0.0, -t_max, 150)
    t_pos = np.linspace(0.0, t_max, 150)

    sol_neg = solve_ivp(lqc_raychaudhuri_ode, (0.0, -t_max), y_bounce, t_eval=t_neg, method='DOP853', rtol=1e-12, atol=1e-38)
    sol_pos = solve_ivp(lqc_raychaudhuri_ode, (0.0, t_max), y_bounce, t_eval=t_pos, method='DOP853', rtol=1e-12, atol=1e-38)

    # Stitch contracting (t < 0) and expanding (t > 0) trajectories
    t_full = np.concatenate((sol_neg.t[::-1][:-1], sol_pos.t))
    a_full = np.concatenate((sol_neg.y[0][::-1][:-1], sol_pos.y[0]))
    adot_full = np.concatenate((sol_neg.y[1][::-1][:-1], sol_pos.y[1]))

    print(f"{'Time (s)':<11} | {'a / a_bounce':<13} | {'Hubble H (s^-1)':<15} | {'P_eff (Pa)':<14} | {'NEC Sum (Pa)':<14} | {'Ham. Err'}")
    print("-" * 104)

    for i in np.linspace(0, len(t_full) - 1, 9, dtype=int):
        t_val = t_full[i]
        a_val = a_full[i]
        H_num = adot_full[i] / a_val
        rho_val = rho_c * ((A_MIN / a_val)**3)
        _, p_eff, nec_sum = effective_lqc_fluid(rho_val)

        # Verify Equation (4): H^2 = (8*pi*G/3)*rho*(1 - rho/rho_c) + Lambda*c^2/3 - k*c^2/a^2
        H2_eq4 = (8.0 * np.pi * G / 3.0) * rho_val * (1.0 - rho_val / rho_c) + (Lambda * (c**2) / 3.0) - (K_CURV * (c**2) / (a_val**2))
        scale = max(abs(H_num**2), (8.0 * np.pi * G / 3.0) * rho_c * 1e-12)
        ham_err = abs((H_num**2) - H2_eq4) / scale

        print(f"{t_val:11.2e} | {a_val/a_bounce:13.6f} | {H_num:15.4e} | {p_eff:14.4e} | {nec_sum:14.4e} | {ham_err:.2e}")

    print("=" * 104)

if __name__ == "__main__":
    run_lqc_bounce_solver()
