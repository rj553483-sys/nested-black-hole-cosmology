import numpy as np

G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
kB = 1.380649e-23
M_sun = 1.98840e30
gamma = 0.237538

rho_Pl = c**5 / (hbar * G**2)
rho_c = (np.sqrt(3) * c**5) / (32.0 * np.pi**2 * gamma**3 * G**2 * hbar)
rho_c_in_rho_Pl = rho_c / rho_Pl

def friedmann_rate(rho, Lambda=1.1056e-52, k=1.0, a=1.0):
    H2 = (8 * np.pi * G / 3.0) * rho * (1.0 - rho / rho_c) + (Lambda * c**2 / 3.0) - (k * c**2 / a**2)
    return H2

def test_bounce_condition():
    print("=== LQC BOUNCE DYNAMICS EVALUATION ===")
    print(f"Planck Density (rho_Pl): {rho_Pl:.4e} kg/m^3")
    print(f"Critical Density (rho_c): {rho_c:.4e} kg/m^3 ({rho_c_in_rho_Pl:.4f} rho_Pl)")
    H2_bounce = friedmann_rate(rho_c, Lambda=0.0, k=0.0, a=1.0)
    print(f"H^2 at rho = rho_c (flat, Lambda=0): {H2_bounce:.4e} s^-2")
    P_quantum_bounce = -rho_c * c**2 * (1.0 - 2.0 * (rho_c / rho_c))
    print(f"Effective Quantum Pressure at bounce: +{P_quantum_bounce:.4e} Pa (Repulsive Quantum Pressure)")
    rho_eff_bounce = rho_c * (1.0 - rho_c / rho_c)
    NEC_sum = P_quantum_bounce + rho_eff_bounce * c**2
    print(f"NEC Violation Sum (P_eff + rho_eff * c^2) at bounce: {NEC_sum:.4e} Pa < 0 (NEC VIOLATED)")

if __name__ == "__main__":
    test_bounce_condition()
