
import numpy as np
import pickle # for loading pickled test data
import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit
from scipy.stats import linregress

path =r'C:\Users\gabri\OneDrive\Área de Trabalho\Amostras - Raman e PL\Medusa 2'
file_name = 'aaa'+'.txt'
full_path = os.path.join(path,file_name)
data= pd.read_csv(full_path, sep="\t", header = None)
print(data)

def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)

def lorentzian(x, amplitude, x0, gamma):
    return (amplitude * (gamma**2)) / ((x - x0)**2 + gamma**2)

x=data[0]
y=data[1]

# Chute inicial para os parâmetros da gaussiana
initial_guess = [1.0, 3.0, 1.0]

# Ajuste da curva gaussiana aos dados
optimized_parameters, _ = curve_fit(gaussian, x, y, p0=initial_guess)

# Gerar pontos da curva gaussiana com os parâmetros ajustados
x_curve = np.linspace(200, 230, 1000)
y_curve = gaussian(x_curve, *optimized_parameters)

# Plotar os dados e a curva gaussiana ajustada
plt.scatter(x, y)
plt.plot(x_curve, y_curve, markersize=1)
plt.show()
