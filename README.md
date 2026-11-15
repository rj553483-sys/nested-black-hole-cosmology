# Computational Verification Suite for Nested Black Hole Cosmology

This repository contains open-source Python numerical solvers, analytical calculators, and observational consistency scripts accompanying the manuscript **"Nested Black Hole Cosmology: Non-Singular Loop Quantum Cosmology Bounces, Holographic Boundary Dynamics, and Observational Constraints."**

## Requirements

* Python 3.9+
* `numpy`
* `scipy`
* `matplotlib`

```bash
pip install numpy scipy matplotlib
```

## Repository Contents

### Numerical ODE Solvers & Analytical Evaluators

1. **`lqc_bounce_solver.py`** — Integrates the holonomy-corrected effective Raychaudhuri and Friedmann equations (Eqs. 4–6) for closed ($k = +1$) dust using `scipy.integrate.solve_ivp` (`DOP853`) across the non-singular quantum bounce at $\rho_c \approx 0.41\,\rho_{\mathrm{Pl}} \approx 2.11 \times 10^{96}\ \mathrm{kg/m^3}$, tracking repulsive quantum pressure, Null Energy Condition (NEC) violation, and Hamiltonian constraint preservation.
2. **`bianchi_shear_integrator.py`** — Integrates the coupled Raychaudhuri and anisotropic shear scalar ($\sigma^2$) ODE system from CMB recombination ($z = 1100$) to the present day in the post-inflationary low-curvature Bianchi limit ($|\Omega_k| \leq 10^{-3}$), verifying $\sigma^2 a^6 = \text{const}$ conservation and Wald's cosmic no-hair isotropization under $\Lambda > 0$.
3. **`entropy_ledger_calculator.py`** — Sums the empirical cosmic entropy inventory (Table 1; $S_{\mathrm{int}} \approx 3.1 \times 10^{104}\,k_{\mathrm{B}}$) and inverts the Bekenstein–Hawking area law ($S_{\mathrm{ext}} \geq S_{\mathrm{int}}$) to derive the host black hole mass lower bound $M_{\mathrm{ext}} \geq 5.4 \times 10^{13}\,M_\odot$, Schwarzschild radius $r_S \approx 5.20\ \mathrm{pc}$, mean entry density $\bar{\rho}_{\mathrm{horizon}} \approx 6.24 \times 10^{-9}\ \mathrm{kg/m^3}$, and Hawking evaporation timescale $t_{\mathrm{evap}} \approx 3.37 \times 10^{108}\ \mathrm{yr}$ (Eqs. 10–12).
4. **`cmb_lowl_deficit_model.py`** — Evaluates the low-multipole ($\ell = 2$ quadrupole, $\ell = 3$ octopole) temperature power suppression from residual host rotation ($a/M$) and exponential de Sitter shear damping $\exp(-3 H_\Lambda t_{\mathrm{iso}})$ per Eq. (13), comparing predicted bandpowers $D_\ell$ against Planck 2018 / PR4 reference values.

### Diagnostic & Visualization Scripts

5. **`expansion_rate_h0_diagnostic.py`** — Evaluates the redshift evolution of the modified Friedmann expansion rate $H(z)/H_{\Lambda\mathrm{CDM}}(z)$ for closed spatial curvature ($-10^{-3} \leq \Omega_k \leq -10^{-4}$) and CPL dynamical dark energy $w(z) = w_0 + w_a \frac{z}{1+z}$ (Eqs. 4 & 9, Table 2).
6. **`run_architecture_plot.py`** — Generates a 4-panel quantitative figure (`nested_black_hole_cosmology_figures.png`) directly from the LQC bounce ODE solver, NEC violation profile, cosmic no-hair shear integration, and Bekenstein–Hawking host mass scaling.
7. **`observational_bounds_check.py`** — Compares the framework's Table 2 predictions ($\Omega_k$, $w_0$, $w_a$) against published 1D marginalized observational constraints from Planck 2018 + BAO and DESI DR1 + Pantheon+, computing parameter pulls and summary $\chi^2$ consistency metrics.
8. **`novel_coupling_analysis.py`** — Evaluates the inter-tier holographic boundary coupling parameter $\kappa \propto (S_{\mathrm{int}}/S_{\mathrm{ext}})$ (Section 3.4), boundary energy-momentum flux $Q_{\mathrm{boundary}}$ (Eq. 7), and effective dark energy equation of state perturbation $w_{0,\mathrm{eff}}$ (Eq. 9).

## Usage

Each script is self-contained and can be executed directly from the command line:

```bash
python lqc_bounce_solver.py
python bianchi_shear_integrator.py
python entropy_ledger_calculator.py
python cmb_lowl_deficit_model.py
python expansion_rate_h0_diagnostic.py
python observational_bounds_check.py
python novel_coupling_analysis.py
python run_architecture_plot.py
```
