"""
=============================================================================
Nested Black Hole Cosmology: Multi-Panel Quantitative Figure Generator
=============================================================================
Generates a publication-ready 4-panel quantitative figure directly from the
framework's core equations and ODE integrations:
  (a) LQC Non-Singular Quantum Bounce Trajectory a(t) and Density rho(t)
  (b) Effective Quantum Pressure & Null Energy Condition (NEC) Violation
  (c) Post-Recombination Shear Isotropization (sigma/H) under Lambda > 0
  (d) Host Black Hole Mass & Horizon Density Scaling vs. Interior Entropy
=============================================================================
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# CODATA 2018 / Planck 2018 Constants (SI Units)
G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
kB = 1.380649e-23
M_sun = 1.98840e30
gamma = 0.237538
H0 = 2.184e-18
Omega_m0, Omega_L0 = 0.315, 0.685
Lambda = 3.0 * Omega_L0 * (H0**2) / (c**2)
rho_c = (np.sqrt(3.0) * c**5) / (32.0 * np.pi**2 * (gamma**3) * (G**2) * hbar)

def integrate_bounce():
    """Integrates dimensionless a(t) across the LQC bounce at t = 0."""
    def ode(t, y):
        a, adot = y
        rho = rho_c / (a**3)
        H = adot / a
        dot_H = -4.0 * np.pi * G * rho * (1.0 - 2.0 * rho / rho_c)
        return [adot, a * (H**2 + dot_H)]

    t_max = 4.0e-43
    sol_neg = solve_ivp(ode, (0.0, -t_max), [1.0, 0.0], t_eval=np.linspace(0, -t_max, 200), method="DOP853", rtol=1e-11, atol=1e-13)
    sol_pos = solve_ivp(ode, (0.0, t_max), [1.0, 0.0], t_eval=np.linspace(0, t_max, 200), method="DOP853", rtol=1e-11, atol=1e-13)

    t = np.concatenate((sol_neg.t[::-1][:-1], sol_pos.t)) * 1e43  # in units of 10^-43 s
    a = np.concatenate((sol_neg.y[0][::-1][:-1], sol_pos.y[0]))
    rho_ratio = 1.0 / (a**3)
    return t, a, rho_ratio

def integrate_shear():
    """Integrates shear-to-Hubble ratio sigma/H from recombination to today."""
    rho_crit0 = 3.0 * (H0**2) / (8.0 * np.pi * G)
    rho_m0 = Omega_m0 * rho_crit0

    def ode(t, y):
        a, adot, sig_sq = y
        H = adot / a
        rho_m = rho_m0 / (a**3)
        addot = a * (-(4.0 * np.pi * G / 3.0) * rho_m - (2.0 / 3.0) * sig_sq + (Lambda * c**2 / 3.0))
        return [adot, addot, -6.0 * H * sig_sq]

    a_init = 1.0 / 1101.0
    sig_H_init = 5.0e-6
    H_init = np.sqrt(((8.0 * np.pi * G / 3.0) * (rho_m0 / a_init**3) + Lambda * c**2 / 3.0) / (1.0 - sig_H_init**2 / 3.0))
    y0 = [a_init, H_init * a_init, (sig_H_init * H_init)**2]

    t_start = 3.8e5 * 365.25 * 86400.0
    t_end = 1.38e10 * 365.25 * 86400.0
    sol = solve_ivp(ode, (t_start, t_end), y0, t_eval=np.linspace(t_start, t_end, 300), method="DOP853", rtol=1e-11, atol=1e-45)

    t_gyr = sol.t / (365.25 * 86400.0 * 1e9)
    H = sol.y[1] / sol.y[0]
    sig_over_H = np.sqrt(np.maximum(0.0, sol.y[2])) / H
    return t_gyr, sig_over_H

def generate_architecture_plot(output_path="run_architecture_plot.png"):
    plt.rcParams.update({"mathtext.fontset": "cm", "font.size": 10})
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), dpi=300)
    fig.patch.set_facecolor("white")

    # Panel (a): LQC Quantum Bounce
    t_b, a_b, rho_r = integrate_bounce()
    ax1 = axes[0, 0]
    ax1_twin = ax1.twinx()
    l1, = ax1.plot(t_b, a_b, color="#0055AA", lw=2.2, label=r"Scale Factor $a(t)/a_{\mathrm{min}}$")
    l2, = ax1_twin.plot(t_b, rho_r, color="#CC3311", lw=2.0, ls="--", label=r"Density $\rho(t)/\rho_c$")
    ax1.axvline(0, color="gray", ls=":", lw=1.0)
    ax1.set_title("(a) LQC Non-Singular Quantum Bounce", fontweight="bold")
    ax1.set_xlabel(r"Proper Time $t$ ($10^{-43}\ \mathrm{s}$)")
    ax1.set_ylabel(r"Normalized Scale Factor $a / a_{\mathrm{min}}$", color="#0055AA")
    ax1_twin.set_ylabel(r"Normalized Density $\rho / \rho_c$", color="#CC3311")
    ax1.legend([l1, l2], [l1.get_label(), l2.get_label()], loc="upper center", frameon=True, fontsize=8.5)
    ax1.grid(True, alpha=0.25)

    # Panel (b): NEC Violation & Quantum Pressure
    rho_grid = np.linspace(0.0, 1.0, 300)
    nec_norm = rho_grid * (1.0 - 2.0 * rho_grid)
    p_eff_norm = -(rho_grid**2)
    ax2 = axes[0, 1]
    ax2.plot(rho_grid, nec_norm, color="#008855", lw=2.2, label=r"$(\rho_{\mathrm{eff}}c^2 + P_{\mathrm{eff}})/(\rho_c c^2)$")
    ax2.plot(rho_grid, p_eff_norm, color="#AA4499", lw=2.0, ls="--", label=r"$P_{\mathrm{eff}}/(\rho_c c^2)$")
    ax2.axhline(0, color="black", lw=1.0)
    ax2.axvspan(0.5, 1.0, color="#FFEEEE", alpha=0.7, label=r"NEC Violated ($\rho > 0.5\rho_c$)")
    ax2.set_title("(b) Quantum Pressure & NEC Violation", fontweight="bold")
    ax2.set_xlabel(r"Normalized Energy Density $\rho / \rho_c$")
    ax2.set_ylabel(r"Normalized Pressure / Energy Density")
    ax2.legend(loc="lower left", frameon=True, fontsize=8.5)
    ax2.grid(True, alpha=0.25)

    # Panel (c): Wald Shear Isotropization
    t_gyr, sig_H = integrate_shear()
    ax3 = axes[1, 0]
    ax3.semilogy(t_gyr, sig_H, color="#D47700", lw=2.2, label=r"Integrated $\sigma(t)/H(t)$")
    ax3.axhline(1e-5, color="#CC3311", ls="--", lw=1.2, label=r"CMB Isotropy Bound ($10^{-5}$)")
    ax3.set_title(r"(c) Cosmic No-Hair Shear Decay ($\Lambda > 0$)", fontweight="bold")
    ax3.set_xlabel("Cosmic Time (Gyr)")
    ax3.set_ylabel(r"Dimensionless Shear Anisotropy $\sigma / H$")
    ax3.legend(loc="upper right", frameon=True, fontsize=8.5)
    ax3.grid(True, which="both", alpha=0.25)

    # Panel (d): Host Mass & Horizon Density Scaling
    S_grid = np.logspace(102, 106, 200)
    M_grid_kg = 0.5 * np.sqrt((S_grid * hbar * c) / (np.pi * kB * G))
    M_grid_Msun = M_grid_kg / M_sun
    rho_h_grid = (3.0 * c**6) / (32.0 * np.pi * (G**3) * (M_grid_kg**2))
    ax4 = axes[1, 1]
    ax4_twin = ax4.twinx()
    l3, = ax4.loglog(S_grid, M_grid_Msun, color="#0055AA", lw=2.2, label=r"Min Host Mass $M_{\mathrm{ext}}\ (M_\odot)$")
    l4, = ax4_twin.loglog(S_grid, rho_h_grid, color="#008855", lw=2.0, ls="--", label=r"Horizon Density $\bar{\rho}_{\mathrm{horizon}}\ (\mathrm{kg/m^3})$")
    ax4.axvline(3.1e104, color="gray", ls=":", lw=1.2)
    ax4.set_title("(d) Bekenstein-Hawking Host Mass Bound", fontweight="bold")
    ax4.set_xlabel(r"Interior Entropy Ledger $S_{\mathrm{int}}\ (k_{\mathrm{B}})$")
    ax4.set_ylabel(r"Host Mass Bound $M_{\mathrm{ext}}\ (M_\odot)$", color="#0055AA")
    ax4_twin.set_ylabel(r"Mean Entry Density ($\mathrm{kg/m^3}$)", color="#008855")
    ax4.legend([l3, l4], [l3.get_label(), l4.get_label()], loc="center left", frameon=True, fontsize=8.5)
    ax4.grid(True, which="both", alpha=0.25)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved publication figure to {output_path}")

if __name__ == "__main__":
    generate_architecture_plot()
