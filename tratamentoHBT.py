import numpy as np
import pickle # for loading pickled test data
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy.signal import find_peaks

def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)

#Selecionando o arquivos
path =r'C:\Users\gabri\OneDrive\Área de Trabalho\Livros e materiais\IC Infor quanti\Histogramas HBT'
file_name = 'Results_Histogram_2023-09-14T16_06_27'+'.csv'
full_path = os.path.join(path,file_name)
column_names = ["BinCenter (ps)", "Histo01", "Histo02", "Histo03", "Histo04"]
data= pd.read_csv(full_path, delimiter=';', header = None, names=column_names, skiprows=1)


bin_centers = data['BinCenter (ps)']
bin_centers = bin_centers/1000
bin_centers2 = -bin_centers

histo01 = data['Histo01']
histo02 = data['Histo02']

infinito = len(histo01) -1
norma = (histo01[infinito]+histo02[infinito] + histo01[infinito-1]+histo02[infinito-1] + histo01[infinito-2]+histo02[infinito-2])/6
print(norma)
histo01 = histo01/norma
histo02 = histo02/norma


fig, ax=plt.subplots()
plt.plot(bin_centers, histo01, 'b.',  bin_centers2, histo02, 'b.', markersize=1)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_ylim(0)
plt.xlabel('Delay (ns)')
plt.ylabel('Contagens de coincidências')
plt.legend()
plt.grid(True)
dpi = 300
plt.savefig('eletrolum.png', dpi=dpi, bbox_inches='tight')


