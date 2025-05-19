import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # m^3 kg^-1 s^-2
c = 3e8  # m/s
M_universe = 1e53  # kg (approximate)
M_local = 1e50  # kg (approximate)
r_CMB = 1e26  # m (horizon at recombination)
r_SN = 1e24  # m (local scale)
lambda_CMB = 1e-3  # m (CMB wavelength)
lambda_target_CMB = 1e-6  # m (recombination scale)
H0_true = 70  # km/s/Mpc (assumed true value)

# Clarity calculation
f_cosmic_CMB = 0.5 * (G * M_universe) / (r_CMB * c**2)
clarity_CMB_cosmic = 1 - f_cosmic_CMB
f_cosmic_SN = 0.5 * (G * M_local) / (r_SN * c**2)
clarity_SN_cosmic = 1 - f_cosmic_SN
f_quantum_CMB = lambda_CMB / lambda_target_CMB
clarity_CMB_quantum = 1 / (1 + f_quantum_CMB)  # Dampened form

# Observed H0
H0_CMB = H0_true * clarity_CMB_cosmic * clarity_CMB_quantum
H0_SN = H0_true * clarity_SN_cosmic

print(f"H0_CMB (cosmic + quantum): {H0_CMB:.1f} km/s/Mpc")
print(f"H0_SN (cosmic): {H0_SN:.1f} km/s/Mpc")

# Plot clarity vs. redshift (simplified)
z = np.linspace(0, 1100, 100)
f_cosmic = 0.5 * (G * M_universe) / ((1 + z) * r_CMB * c**2)
clarity = 1 - f_cosmic
plt.plot(z, clarity, label='Clarity vs. Redshift')
plt.xlabel('Redshift (z)')
plt.ylabel('Clarity')
plt.title('Clarity Gradient Effect on H_0')
plt.legend()
plt.grid(True)
plt.savefig('clarity_gradient_H0.png')