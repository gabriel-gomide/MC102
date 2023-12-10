import numpy as np
import pickle # for loading pickled test data
import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy.signal import find_peaks

def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)

#Selecionando o arquivo
path =r'C:\Users\gabri\OneDrive\Área de Trabalho\Amostras - Raman e PL\Medusa 2'
file_name = 'aaa'+'.txt'
full_path = os.path.join(path,file_name)
data= pd.read_csv(full_path, sep="\t", header = None)

#Pegando os dados de interesse e tirando o ruído de fundo
#Y vai de 1 a 100
x=data[0]
y=data[54]
y=y-min(y)
plt.plot(x, y, '.', markersize=1)
print(x[330])
#%%
peaks,_ = find_peaks(y, height=300)
chu_amplitude=[]
chu_media=[]
for i in range(len(peaks)):
    chu_media.append(x[peaks[i]])
    chu_amplitude.append(y[peaks[i]])
plt.plot(x, y,  '.', markersize=1)
plt.plot(chu_media, chu_amplitude, '.')
print(chu_amplitude)
#%%

plt.scatter(x, y, s=1.)
initial_guess=[]
for i in range(len(chu_media)):
    M = chu_media[i]
    A = chu_amplitude[i]
    M=int(M)
    A=int(A)
    initial_guess.append(A)
    initial_guess.append(M)
    initial_guess.append(2)

    # Ajuste da curva gaussiana aos dados
    optimized_parameters, _ = curve_fit(gaussian, x, y, p0=(A, M, 2))

    # Gerar pontos da curva gaussiana com os parâmetros ajustados
    x_curve = np.linspace(M-5, M+5, A)
    y_curve = gaussian(x_curve, *optimized_parameters)

    # Plotar os dados e a curva gaussiana ajustada

    plt.plot(x_curve, y_curve, 'r', markersize=1)
    print("Parâmetros otimizados:")
    print("Amplitude:", optimized_parameters[0])
    print("Média:", optimized_parameters[1])
    print("Desvio padrão:", optimized_parameters[2])


#%%
x=x[332:380]
y=y[332:380]
plt.scatter(x, y, s=1.)
# Ajuste da curva gaussiana aos dados
optimized_parameters, _ = curve_fit(gaussian, x, y, p0=(200, 257, 2))

    # Gerar pontos da curva gaussiana com os parâmetros ajustados
x_curve = np.linspace(255, 270, 200)
y_curve = gaussian(x_curve, *optimized_parameters)

    # Plotar os dados e a curva gaussiana ajustada

plt.plot(x_curve, y_curve, 'r', markersize=1)
print("Parâmetros otimizados:")
print("Amplitude:", optimized_parameters[0])
print("Média:", optimized_parameters[1])
print("Desvio padrão:", optimized_parameters[2])

plt.xlim(left=200, right=400)
plt.show()

