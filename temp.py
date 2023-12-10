# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
'''
# Input data
x = [0.000050, 0.000341, 0.000764, 0.01080, 0.01454, 0.01908, 0.3863, 0.4213, 0.4355, 0.08995, 0.1039, 0.1192, 0.1357, 0.2169, 0.2410]
y = [6.9, 32.7, 55.5, 298.5, 361.5, 430.2, 2649, 2792, 2850, 1117, 1216, 1318, 1423, 1873, 1993]

# Plot scatter plot of input data
plt.scatter(x, y)

# Fit data with a polynomial function of degree 3
#z = np.polyfit(x, y, 3)
#p = np.poly1d(z)

# Plot fitted polynomial function
#xp = np.linspace(min(x), max(x), 100)
#plt.plot(xp, p(xp), 'r-')

# Add plot title and labels
plt.title("Voltagem x Corrente - Hipotese")
plt.xlabel("Voltagem")
plt.ylabel("Corrente")

# Show plot
plt.show()

x = [0.000050, 0.000341, 0.000764, 0.01080, 0.01454, 0.01908, 0.3863, 0.4213, 0.4355, 0.08995, 0.1039, 0.1192, 0.1357, 0.2169, 0.2410]
y = [7.24, 10.43, 13.76, 36.20, 40.23, 44.34, 146, 150.9, 152.8, 80.52, 85.41, 90.41, 95.39, 115.83, 120.9]

plt.scatter(x, y)

plt.title("Voltagem x Resistência - Hipotese")
plt.xlabel("Voltagem")
plt.ylabel("Resistência")
plt.show()'''

x = [0.000050, 0.000341, 0.000764, 0.01080, 0.01454, 0.01908, 0.3863, 0.4213, 0.4355, 0.08995, 0.1039, 0.1192, 0.1357, 0.2169, 0.2410]
y = [300, 400, 500, 1100, 1200, 1300, 3400, 3500, 3540, 2100, 2200, 2300, 2400, 2800, 2900]

plt.scatter(x, y)

plt.title("Voltagem x Temperatura - Hipotese")
plt.xlabel("Voltagem")
plt.ylabel("Temperatura")
plt.show()

t=300
r=7.247
R=70
T=t*(R/r)**0.8271
print(T)
