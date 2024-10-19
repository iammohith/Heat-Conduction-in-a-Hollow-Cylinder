# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:55:55 2020

@author: Mohith Sai
"""
# Heat Transfer in a Hollow Cylinder

"""
This script simulates the temperature distribution through a hollow pipe with fluid flowing inside.
The heat transfer is assumed to flow only radially.
The parameters considered are:
- Length of the cylinder (L) [not used in calculations here]
- Inside temperature (Ti)
- Outside temperature (To)
- Inside radius (Ri)
- Outside radius (Ro)

The temperature distribution over the hollow cylinder is calculated using the equation:
T(r) = (ln(r/Ri)/ln(Ro/Ri))*(To - Ti) + Ti
where:
- r is the radial distance from the center of the cylinder.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define temperatures and dimensions
Ti = 100  # Inside pipe temperature (°C)
To = 35   # Outside pipe temperature (°C)
Ri = 0.5  # Inside radius of the pipe (m)
Ro = 1    # Outside radius of the pipe (m)

# Number of discrete points to calculate temperature
n = 20  
r = np.linspace(Ri, Ro, n)  # Linearly spaced points from Ri to Ro
T = np.ones(n)  # Preallocate array for temperature values

# Calculate temperature distribution
for i in range(n):
    T[i] = ((np.log(r[i] / Ri) / np.log(Ro / Ri)) * (To - Ti)) + Ti

# Visualization of temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Hollow Cylinder')
plt.grid()  # Add grid for better readability
plt.show()  # Display the plot

# Print calculated temperatures for each radial distance
print("The temperatures at various distances are:", T)
