import numpy as np

def run_h0_diagnostic():
    print("=== EXPLORATORY DIAGNOSTIC: RUNNING H0 ACROSS BOUNDARY HORIZONS ===")
    z_list = [0.0, 0.5, 1.0, 1.5, 2.0]
    for z in z_list:
        ratio = 1.0 + 0.002 * (z**2)
        print(f"  Redshift z = {z:.2f} | Effective Local H(z)/H0_ratio = {ratio:.4f}")

if __name__ == "__main__":
    run_h0_diagnostic()
