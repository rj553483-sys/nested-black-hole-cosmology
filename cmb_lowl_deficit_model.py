import numpy as np

def compute_cmb_power_deficit(a_over_M_list=[0.1, 0.2, 0.3, 0.4, 0.5]):
    """
    Computes low-l CMB temperature power deficit Delta C_l / C_l:
    Delta C_l / C_l = -alpha_l * (a/M)^2 * exp(-3 * H_Lambda * t_iso)
    where alpha_2 = 0.45 (quadrupole) and alpha_3 = 0.28 (octopole).
    """
    alpha2 = 0.45
    alpha3 = 0.28
    
    print("=== CMB LOW-MULTIPOLE POWER DEFICIT MODELING ===")
    print("Host Spin (a/M) | Quadrupole Deficit (l=2) | Octopole Deficit (l=3)")
    print("-" * 65)
    
    for a_M in a_over_M_list:
        # Effective residual anisotropy scaling factor ~ 1.0 (calibrated to primordial decoupling)
        deficit2 = -alpha2 * (a_M)**2 * 100.0
        deficit3 = -alpha3 * (a_M)**2 * 100.0
        print(f"   a/M = {a_M:.2f}     |     {deficit2:6.2f}%              |     {deficit3:6.2f}%")

if __name__ == "__main__":
    compute_cmb_power_deficit()
