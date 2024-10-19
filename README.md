# Heat Conduction in a Hollow Cylinder

This repository contains Python code for simulating heat conduction in a hollow cylinder with various boundary conditions and heat generation. The temperature distribution is calculated and visualized based on the governing heat conduction equations.

## Project Overview

This project investigates the thermal behavior of a hollow cylinder, characterized by 
its inner radius $R_i$, outer radius $R_o$, and length $L$, subjected to heat transfer and varying internal and external temperatures $T_i$ and $T_o$ respectively.
It considers radial heat flow and includes the effects of heat generation within the cylinder.

### Key Features
- Models heat conduction through a hollow cylinder with internal fluid flow.
- Calculates temperature distributions with and without heat generation.
- Visualizes temperature profiles using Python's `matplotlib` library.

## Formulas Used

### 1. **Temperature Distribution Without Heat Generation**

The temperature distribution in a hollow cylinder with no heat generation is given by:

$$
T(r) = \frac{\ln\left(\frac{r}{R_i}\right)}{\ln\left(\frac{R_o}{R_i}\right)} (T_o - T_i) + T_i
$$

Where:
- $T_i$ and $T_o$ are the temperatures at the inner and outer surfaces of the cylinder, respectively.
- $R_i$ and $R_o$ are the inner and outer radii of the cylinder, respectively.
- $T(r)$ is the temperature at a radius $r$ within the hollow cylinder.

### 2. **Temperature Distribution With Heat Generation**

When there is uniform heat generation $Q_g$ within the hollow cylinder, the temperature distribution can be expressed as:

$$
T(r) = \frac{Q_g}{4k} (R_o^2 - r^2) + \frac{\ln\left(\frac{r}{R_o}\right)}{\ln\left(\frac{R_o}{R_i}\right)}\left(\frac{Q_g}{4k}(R_o^2 - R_i^2) + T_o - T_i\right) + T_i
$$

Where:
- $Q_g$ is the rate of heat generation per unit volume.
- $k$ is the thermal conductivity of the material.
- $T(r)$ is the temperature at a radius $r$ within the hollow cylinder.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iammohith/Heat-Conduction-in-a-Hollow-Cylinder.git
