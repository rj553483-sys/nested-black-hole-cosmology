"""
=============================================================================
Interior FLRW Architecture & Boundary Conditions Plot Generator
=============================================================================
Generates publication-quality schematic diagnostic visualizations of the nested 
black hole interior FLRW architecture, host Schwarzschild boundaries, LQC bounce 
throat, and cosmological expansion parameters.
=============================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_architecture_plot(output_path="/workspace/scratch/nested_black_hole_cosmology_architecture.png"):
    plt.rcParams.update({'mathtext.fontset': 'cm'})
    fig, ax = plt.subplots(figsize=(13, 10), facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.text(0.5, 0.96, "Nested Black Hole Cosmology: Interior FLRW Architecture & Boundary Conditions",
            color='#000000', fontsize=14, fontweight='bold', ha='center', va='top')
    
    bbox_blue = dict(boxstyle='round,pad=0.9', facecolor='#F0F8FF', edgecolor='#0066CC', linewidth=2.0)
    ax.text(0.04, 0.88, 
            '1. PARENT HOST SPACETIME (Schwarzschild Exterior)\n'
            '• Host Mass Lower Bound: $M_{\\mathrm{ext}} \\geq 5.4 \\times 10^{13} \\, M_\\odot$\n'
            '• Schwarzschild Horizon Radius: $r_S = \\frac{2GM_{\\mathrm{ext}}}{c^2} \\approx 5.20 \\text{ pc}$\n'
            '• Mean Entry Density: $\\bar{\\rho}_{\\mathrm{horizon}} \\approx 6.24 \\times 10^{-9} \\text{ kg/m}^3$\n'
            '• Horizon Stability: $t_{\\mathrm{evap}} \\approx 3.37 \\times 10^{108} \\text{ yr} \\gg t_{\\mathrm{universe}}$',
            color='#1A1A1A', fontsize=10.5, ha='left', va='top', bbox=bbox_blue, linespacing=1.6)
            
    bbox_pink = dict(boxstyle='round,pad=0.9', facecolor='#FFF0F5', edgecolor='#CC0055', linewidth=2.0)
    ax.text(0.52, 0.88, 
            '2. BOUNDARY JUNCTION HYPERSURFACE (\\Sigma)\n'
            '• Metric Matching: Darmois--Israel \\& Barrab\\`es--Israel\n'
            '• Vanishing Surface Stress: $S_{ij} \\equiv 0$ (Smooth Match)\n'
            '• Holographic Intake: $\\nabla_\\mu T_{\\mathrm{boundary}}^{\\mu\\nu} = \\kappa \\left( \\frac{\\dot{M}_{\\mathrm{ext}}}{V_{\\mathrm{int}}} \\right) n^\\nu$\n'
            '• Holographic Bound: $S_{\\mathrm{int}} \\leq S_{\\mathrm{ext}} \\sim 3.1 \\times 10^{104} \\, k_{\\mathrm{B}}$',
            color='#1A1A1A', fontsize=10.5, ha='left', va='top', bbox=bbox_pink, linespacing=1.6)
            
    bbox_yellow = dict(boxstyle='round,pad=0.9', facecolor='#FFFFF0', edgecolor='#D48800', linewidth=2.0)
    ax.text(0.04, 0.42, 
            '3. LQC QUANTUM BOUNCE THROAT ($a_{\\mathrm{min}} > 0$)\n'
            '• Holonomy Friedmann: $H^2 = \\frac{8\\pi G}{3}\\rho \\left(1 - \\frac{\\rho}{\\rho_c}\\right)$\n'
            '• Critical Density: $\\rho_c \\approx 0.41 \\, \\rho_{\\text{Pl}} \\approx 2.11 \\times 10^{96} \\text{ kg/m}^3$\n'
            '• Repulsive Quantum Pressure: $P_{\\mathrm{quantum}} = -\\rho c^2 \\left(1 - \\frac{2\\rho}{\\rho_c}\\right)$\n'
            '• Singularity Avoidance: $P_{\\mathrm{eff}} + \\rho_{\\mathrm{eff}} c^2 < 0$ (NEC Violation)',
            color='#1A1A1A', fontsize=10.5, ha='left', va='top', bbox=bbox_yellow, linespacing=1.6)
            
    bbox_green = dict(boxstyle='round,pad=0.9', facecolor='#F0FFF0', edgecolor='#008855', linewidth=2.0)
    ax.text(0.52, 0.42, 
            '4. EXPANDING FLRW INTERIOR COSMOS\n'
            '• Inflation Expansion: $e^{3N} \\geq 10^{78}$ ($N \\geq 60$ e-folds)\n'
            '• Observable Patch Scale: $r_{\\mathrm{obs}} \\approx 14.3 \\text{ Gpc} \\gg r_S$\n'
            '• Spatial Curvature: Closed geometry ($-10^{-3} \\leq \\Omega_k \\leq -10^{-4}$)\n'
            '• Low-$\\ell$ CMB Deficit: $\\frac{\\Delta C_\\ell}{C_\\ell} = -\\alpha_\\ell \\left(\\frac{a}{M}\\right)^2 e^{-3 H_\\Lambda t_{\mathrm{iso}}}$',
            color='#1A1A1A', fontsize=10.5, ha='left', va='top', bbox=bbox_green, linespacing=1.6)
            
    ax.axis('off')
    plt.savefig(output_path, dpi=300, facecolor='#FFFFFF', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    generate_architecture_plot()
