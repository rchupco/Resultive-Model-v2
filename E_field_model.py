import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # m^3 kg^-1 s^-2
c = 3e8  # m/s
mu_0 = 4e-7 * np.pi  # H/m
M_sun = 1.989e30  # kg
day_to_s = 86400  # s
M = 9e8 * M_sun  # 3C 273 mass
M_core = 0.1 * M  # Approximate core mass
r = 2 * G * M / c**2  # Schwarzschild radius
T = 108 * day_to_s  # Oscillation period (s)
alpha = 0.1  # Modulation amplitude
k = 1e-10  # Proportionality constant (adjust based on volume)

# Time array
t = np.linspace(0, 2 * T, 200)  # 2 periods

# Field energy model
B_0 = (G * M * M_core / (r * c**2))  # Base field strength (simplified)
B_t = B_0 * (1 + alpha * np.sin(2 * np.pi * t / T))
u_B = B_t**2 / (2 * mu_0)
V = k * r**3  # Approximate volume
E_field = u_B * V
E_field_perceived = E_field * (1 - 0.5 * 0.5)  # Clarity damping at GM/rc^2 = 0.5

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t / day_to_s, E_field_perceived / 1e30, label='Perceived E_field (x10^30 J)')
plt.xlabel('Time (days)')
plt.ylabel('Perceived Energy (x10^30 J)')
plt.title('E_field(t) for 3C 273')
plt.grid(True)
plt.legend()
plt.savefig('E_field_model.png')