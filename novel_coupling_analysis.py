import numpy as np

def run_coupling_analysis():
    print("=== EXPLORATORY DIAGNOSTIC: NOVEL BOUNDARY COUPLING TERM DYNAMICS ===")
    print("Entropy Scale Ratio S_ext/S_int | Effective Coupling Parameter kappa")
    print("-" * 69)
    for ratio in [1.0, 10.0, 100.0, 1000.0]:
        kappa = 1e-3 / ratio
        print(f"               {ratio:5.1f}               |           {kappa:.4e}")

if __name__ == "__main__":
    run_coupling_analysis()
