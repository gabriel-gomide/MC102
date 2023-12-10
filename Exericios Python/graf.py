import numpy as np
import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Plot scatter plot of input data
plt.scatter(x, y)

# Fit data with a polynomial function of degree 3
z = np.polyfit(x, y, 3)
p = np.poly1d(z)

# Plot fitted polynomial function
xp = np.linspace(min(x), max(x), 100)
plt.plot(xp, p(xp), 'r-')

# Add plot title and labels
plt.title("Scatter plot of input data with polynomial fit")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show plot
plt.show()
