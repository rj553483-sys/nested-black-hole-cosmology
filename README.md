# Computational Evaluation Pipeline: Nested Black Hole Cosmology

This directory contains open-source Python verification scripts for evaluating the numerical dynamics, information bounds, and observational predictions of the **Nested Black Hole Cosmology** framework.

## Repository Contents

- `lqc_bounce_solver.py`: Evaluates the Loop Quantum Cosmology (LQC) holonomy-corrected effective Friedmann equation ($H^2$), computes the critical bounce density ($\rho_c \approx 0.41 \rho_{\text{Pl}} \approx 2.11 \times 10^{96} \text{ kg/m}^3$), and verifies Null Energy Condition (NEC) violation at the bounce.
- `bianchi_shear_integrator.py`: Solves Wald shear-to-Hubble decay ($\sigma^2/H^2 \propto e^{-3 H_\Lambda t}$) across expansion epochs to confirm shear damping below the CMB threshold ($\sigma_{\text{rec}}/H_{\text{rec}} < 10^{-5}$).
- `entropy_ledger_calculator.py`: Evaluates the Bekenstein-Hawking area entropy inversion $M_{\text{ext}} = \frac{1}{2}\sqrt{\frac{S_{\text{int}}\hbar c}{\pi k_{\text{B}} G}}$, deriving the minimum host black hole mass ($M_{\text{ext}} \ge 5.4 \times 10^{13} \, M_\odot$) from the empirical universe entropy ledger ($S_{\text{int}} \sim 3.1 \times 10^{104} k_{\text{B}}$).
- `cmb_lowl_deficit_model.py`: Calculates low-multipole ($\ell=2,3$) CMB temperature anisotropy power suppression ($\Delta C_\ell / C_\ell$) as a function of dimensionless host spin $a/M$.

## Installation & Environment Setup

These scripts require Python 3.8+ and standard Numerical Python (`numpy`):

```bash
python3 -m venv env
source env/bin/activate
pip install numpy
```

## Running Verification Scripts

Run each verification script directly from the command line:

```bash
python3 lqc_bounce_solver.py
python3 bianchi_shear_integrator.py
python3 entropy_ledger_calculator.py
python3 cmb_lowl_deficit_model.py
```

## Double-Anonymous Peer Review Compliance

All scripts and documentation in this repository have been anonymized for double-anonymous peer review. Author identities, institutional affiliations, and local environment tags have been omitted.
