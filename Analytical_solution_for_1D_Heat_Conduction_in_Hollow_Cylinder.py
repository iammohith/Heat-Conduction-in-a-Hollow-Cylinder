# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:55:55 2020

@author: Mohith Sai
"""
""" Let us consider heat tranfer through a hollow pipe with
fluid flow inside. Heat is assumed to flow only radially.
A hollow cylinder with length L and Ti & To be the 
inside and outside temperatures of hollow cylinder
Ri and Ro be the inside and outside radius of hollow cylinder
the temperature distributuion over a hollow cylinder is given by
T(r) = (ln(r/Ri)/ln(Ro/Ri))*(To-Ti) + Ti"""

import numpy as np
import matplotlib.pyplot as plt

Ti = 100 #inside pipe temperature units must be in degC
To = 35 #outside pipe temperature units must be in degC
Ri = 0.5 #inside radius of pipe units must be in meters
Ro = 1 #outside radius of pipe units must be in meters
n = 20 #the number of points
r = np.linspace(Ri,Ro,n) #linearlyspaced points
T = np.ones(n) #preallocating array of ones for temperature
for i in range(0,n):
    T[i] = ((np.log(r[i]/Ri)/np.log(Ro/Ri))*(To-Ti)) + Ti
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Graph')
print("The temperatures are:",T)