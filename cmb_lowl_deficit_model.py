import numpy as np

def compute_cmb_power_deficit(a_over_M_list=[0.1, 0.2, 0.3, 0.4, 0.5]):
    alpha2 = 0.45
    alpha3 = 0.28
    print("=== CMB LOW-MULTIPOLE POWER DEFICIT MODELING ===")
    print("Host Spin (a/M) | Quadrupole Deficit (l=2) | Octopole Deficit (l=3) | Regime Note")
    print("-" * 95)
    for a_M in a_over_M_list:
        deficit2 = -alpha2 * (a_M)**2 * 100.0
        deficit3 = -alpha3 * (a_M)**2 * 100.0
        note = "[Linear perturbative regime]" if a_M <= 0.1 else "[Note: a/M > 0.1 represents secondary-order extrapolation beyond linear regime]"
        print(f"   a/M = {a_M:.2f}     |      {deficit2:6.2f}%              |      {deficit3:6.2f}%             | {note}")

if __name__ == "__main__":
    compute_cmb_power_deficit()
