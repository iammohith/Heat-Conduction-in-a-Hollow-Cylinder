# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:35:28 2020

@author: Mohith Sai
"""
""" Let us consider heat tranfer through a hollow pipe with
fluid flow inside. Heat is assumed to flow only radially.
A hollow cylinder with length L and Ti & To be the 
inside and outside temperatures of hollow cylinder
Ri and Ro be the inside and outside radius of hollow cylinder with heat generation Qg
the temperature distributuion over a hollow cylinder is given by
T(r) = Qg/4*k*(Ro**2-R**2) + (ln(r/Ro)/ln(Ro/Ri)*(Qg/4*k(Ro**2-Ri**2)+To-Ti)) + Ti"""

import numpy as np
import matplotlib.pyplot as plt

Ti = 100 #inside pipe temperature units must be in degC
To = 20 #outside pipe temperature units must be in degC
Ri = 0.5 #inside radius of pipe units must be in meters
Ro = 1 #outside radius of pipe units must be in meters
Qg = 100 #heat generation the units must be W/m**3
K = 10 #thermal conductivity of the material
n = 20 #the number of points
r = np.linspace(Ri,Ro,n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
const = Qg/4*K
for i in range(n):
    T[i] = const*((Ro**2) - (r[i]**2)) + (np.log(r[i]/Ri)/np.log(Ro/Ri))*((const*((Ro**2) - (Ri**2))) + To - Ti) + To
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
print("The temperatures are:",T)
