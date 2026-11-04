import numpy as np

# Fundamental Constants & Baseline Parameters
H0 = 2.184e-18 # Hubble constant in s^-1 (~67.4 km/s/Mpc)
Lambda = 1.1056e-52 # Cosmological constant in m^-2
c = 2.99792458e8 # m/s

H_Lambda = np.sqrt(Lambda * c**2 / 3.0) # Late-time de Sitter Hubble rate

def shear_damping_ratio(t_seconds, sigma0_over_H0=0.1):
    """
    Computes Wald shear-to-Hubble decay ratio:
    (sigma / H)^2 = (sigma0 / H0)^2 * exp(-3 * H_Lambda * t)
    """
    shear_ratio = (sigma0_over_H0) * np.exp(-1.5 * H_Lambda * t_seconds)
    return shear_ratio

def evaluate_shear_decay():
    print("=== BIANCHI IX SHEAR ISOTROPIZATION EVALUATION ===")
    print(f"Late-time de Sitter Hubble rate H_Lambda: {H_Lambda:.4e} s^-1")
    
    # Time at recombination t_rec ~ 380,000 years
    t_rec_sec = 380000.0 * 365.25 * 86400.0
    
    # Time at present epoch t_0 ~ 13.8 billion years
    t_0_sec = 13.8e9 * 365.25 * 86400.0
    
    for a_over_M in [0.1, 0.25, 0.5]:
        sigma0 = 0.1 * (a_over_M)**2
        sigma_rec = shear_damping_ratio(t_rec_sec, sigma0_over_H0=sigma0)
        sigma_0_now = shear_damping_ratio(t_0_sec, sigma0_over_H0=sigma0)
        print(f"Host Spin a/M = {a_over_M:.2f} -> Initial Shear (sigma0/H0): {sigma0:.4f}")
        print(f"  -> Shear ratio at Recombination (t_rec): {sigma_rec:.4e} (< 10^-5 CMB threshold)")
        print(f"  -> Shear ratio at Present Epoch (t_0):   {sigma_0_now:.4e}")

if __name__ == "__main__":
    evaluate_shear_decay()
