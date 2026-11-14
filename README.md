# Computational Verification Suite for Nested Black Hole Cosmology

This directory contains open-source Python verification scripts for evaluating the numerical dynamics, information bounds, and observational predictions of the **Nested Black Hole Cosmology** framework.

## Repository Contents

### Core Operational Solvers
1. `lqc_bounce_solver.py`: Solves the effective LQC Friedmann equation $H^2 = \frac{8\pi G}{3}\rho(1 - \rho/\rho_c)$ through the quantum bounce at $\rho = \rho_c \approx 0.41 \rho_{\text{Pl}} \approx 2.11 \times 10^{96} \text{ kg/m}^3$.
2. `bianchi_shear_integrator.py`: Integrates Bianchi IX shear decay $\sigma^2/H^2 \propto e^{-3H_\Lambda t}$ driven by Wald's cosmic no-hair theorem.
3. `entropy_ledger_calculator.py`: Evaluates the Bekenstein--Hawking entropy inversion $M_{\text{ext}} = \frac{1}{2}\sqrt{\frac{S_{\text{int}}\hbar c}{\pi k_{\text{B}} G}}$ to derive $M_{\text{ext}} \ge 5.4 \times 10^{13} M_\odot$ and $t_{\text{evap}} \approx 3.37 \times 10^{108} \text{ yr}$.
4. `cmb_lowl_deficit_model.py`: Computes low-\(\ell\) (\(\ell=2,3\)) temperature anisotropy power suppression ($0.45\%$ to $11.25\%$) as a function of host spin $a/M$.

### Exploratory Diagnostic Tools
5. `running_h0_void_diagnostic.py`: Models spatial variation and Hubble parameter running across local boundary horizon interfaces.
6. `run_architecture_plot.py`: Generates publication-quality schematic diagnostics of the nested black hole interior FLRW architecture.
7. `external_astropy_validation.py`: Validates cosmological parameter fits against Planck PR4, DESI BAO, and Pantheon+ SN Ia data.
8. `novel_coupling_analysis.py`: Evaluates non-minimal boundary scalar-curvature coupling term dynamics during fluid thermalization.
