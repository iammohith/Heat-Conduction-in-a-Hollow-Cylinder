# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:35:28 2020

@author: Mohith Sai
"""
# Heat Transfer in a Hollow Cylinder with Heat Generation

"""
This script simulates the temperature distribution through a hollow pipe with fluid flowing inside.
Heat transfer is assumed to flow only radially. The parameters considered are:
- Inside temperature (Ti)
- Outside temperature (To)
- Inside radius (Ri)
- Outside radius (Ro)
- Heat generation rate (Qg)
- Thermal conductivity (K)

The temperature distribution over the hollow cylinder is calculated using the equation:
T(r) = Qg/4*k*(Ro**2 - r**2) + (ln(r/Ro)/ln(Ro/Ri)) * (Qg/4*k*(Ro**2 - Ri**2) + To - Ti) + Ti
where:
- r is the radial distance from the center of the cylinder.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define temperatures and dimensions
Ti = 100  # Inside pipe temperature (°C)
To = 20   # Outside pipe temperature (°C)
Ri = 0.5  # Inside radius of the pipe (m)
Ro = 1    # Outside radius of the pipe (m)
Qg = 100  # Heat generation rate (W/m³)
K = 10    # Thermal conductivity of the material (W/m·K)

# Number of discrete points to calculate temperature
n = 20  
r = np.linspace(Ri, Ro, n)  # Linearly spaced points from Ri to Ro
T = np.ones(n)  # Preallocate array for temperature values

# Calculate temperature distribution
const = Qg / (4 * K)  # Constant term for temperature distribution calculation
for i in range(n):
    T[i] = (const * (Ro**2 - r[i]**2) +
             (np.log(r[i] / Ri) / np.log(Ro / Ri)) * 
             (const * (Ro**2 - Ri**2) + To - Ti) + Ti)

# Visualization of temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Hollow Cylinder with Heat Generation')
plt.grid()  # Add grid for better readability
plt.show()  # Display the plot

# Print calculated temperatures for each radial distance
print("The temperatures at various distances are:", T)
