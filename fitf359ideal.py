# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:20:23 2023

@author: gabri
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker


def linear_func1(x, a, b, d):
    return a * x ** b+d


def plot_data(ax, x, y, title, legenda, xlabel, ylabel, fit_func=None, x_err=None, y_err=None, color='blue'):
    if x_err is not None:
        ax.errorbar(x, y, xerr=x_err, fmt='none', ecolor='black')
    if y_err is not None:
        ax.errorbar(x, y, yerr=y_err, fmt='none', ecolor='black')
    
    ax.scatter(x, y, s=5, color=color)
    
    if fit_func is not None:
        popt, pcov = curve_fit(fit_func, x, y, sigma=y_err, absolute_sigma=True)
        x_fit = np.linspace(0, 15, 10000)
        y_fit = fit_func(x_fit, *popt)
        ax.plot(x_fit, y_fit, color=color, linestyle='-', label=legenda)


        print('Optimized Parameters:')
        print('a =', popt[0], '+/-', np.sqrt(pcov[0, 0]))
        print('b =', popt[1], '+/-', np.sqrt(pcov[1, 1]))
        print('d =', popt[2], '+/-', np.sqrt(pcov[2, 2]))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.set_xlim(0)
    ax.set_ylim(200)
    plt.xlim(right=15)
    plt.ylim(top=1780)
    ax.legend()
    ax.grid(True)

#Artigo recente com valores para modelo e comparação
def artigo(ax):
    v = np.array([10, 20, 40, 60, 80, 100, 120], dtype=float)
    i = np.array([236, 324, 464, 577, 676, 763, 844], dtype=float)
    r = np.array([42.4, 61.7, 86.2, 104, 118, 131, 142], dtype=float)
    t = np.array([960, 1313, 1735, 2029, 2259, 2461, 2633], dtype=float)
    
    for a in range(len(t)):
        t[a]=t[a]/2633

    fig1 = plot_data(ax, v, t, 'Ideal Values','Ideal Values', 'Voltage', 'Current', fit_func=linear_func, color='black')
    return fig1


def lamp1(ax):
    #Lampada 1 - Valores Normalizados
    t0 = 298
    r0 = 1.95
    x=np.array([0.1695, 0.415, 0.785, 1.389, 0.998, 1.482, 2.0315, 2.551, 3.089, 3.973, 4.5765, 5.118, 6.095, 6.52, 7.02, 8, 8.69, 9.05, 9.96, 11.06, 12.06, 14.07])
    y=np.array([71, 108.95, 147.2, 203.3, 167, 212.5, 255.4, 299.45, 333.87, 384.1, 417.1, 448.07, 497.5, 519.85, 548.75, 591.9, 625, 640, 675, 720, 755, 825])
    
    t=[t0, 518.5, 684.9, 840.6, 752.5, 855.0, 953.3, 1008.9, 1080.2, 1184.6, 1243.8, 1285.9, 1362.6, 1389.3, 1412.2, 1477.9, 1512.9, 1534.2, 1589.2, 1642.9, 1696.9, 1791.4]
    

    r=[r0]
    for i in range(len(x)):
        r.append((x[i]/y[i])*(10**3))
    #for a in range(len(x)):
        #x[a]=x[a]/x[-1] 
   
    x1=np.array([0, 0.415, 0.785, 1.389, 0.998, 1.482, 2.0315, 2.551, 3.089, 3.973, 4.5765, 5.118, 6.095, 6.52, 7.02, 8, 8.69, 9.05, 9.96, 11.06, 12.06, 14.07])
    fig = plot_data(ax, x1, t, 'Lâmpada 1', 'Lâmpada 1', 'Voltagem (V)', 'Corrente (mA)', fit_func=linear_func1, color='red')
    return fig

def lamp2(ax):
    t0 = 299
    r0 = 2
    x=np.array([ 0.715, 1.029, 1.457, 2.027,  2.591, 2.928, 4.041, 4.522, 5.053, 6.05, 6.54, 7.04, 8.06, 9.24, 10.03, 11.02, 12, 13.88])
    y=np.array([166.2, 194.9, 231.65, 275.6, 315, 341.1, 403.7, 431.2, 458.7, 515, 540, 560, 615, 660, 690, 725, 760, 830])
    
    t=[t0]
    for i in range(len(x)):
        t.append((t0*((x[i]*(10**3))/(y[i]*r0))**(0.8271)))
  
    r=[r0]
    for i in range(len(x)):
        r.append((x[i]/y[i])*(10**3))
    #for a in range(len(x)):
        #x[a]=x[a]/x[-1] 
    x1=np.array([0, 0.715, 1.029, 1.457, 2.027,  2.591, 2.928, 4.041, 4.522, 5.053, 6.05, 6.54, 7.04, 8.06, 9.24, 10.03, 11.02, 12, 13.88])
    fig = plot_data(ax, x1, t, 'Lâmpada 2', 'Lâmpada 2', 'Voltagem (V)', 'Corrente (mA)', fit_func=linear_func1, color='green')
    return fig
  
def lamp3(ax):
    t0 = 299
    r0 = 2.4
    x=np.array([ 0.7204999999999999, 1.092, 1.569, 2.025, 3.032, 2.5355, 4.073, 4.498, 5.056, 6.03, 6.54, 7.01, 8.01, 8.71, 9.254999999999999, 10.16, 11.06, 12.05, 14.04])
    y=np.array([217.75, 250.3, 281.85, 307.0, 362.1, 336.4, 410.15, 429.55, 454.2, 496.09999999999997, 517.75, 535.5, 571.55, 591.55, 620.0, 650.0, 675.0, 710.0, 760.0])
    
    t=[t0]
    for i in range(len(x)):
        t.append((t0*((x[i]*(10**3))/(y[i]*r0))**(0.8271)))
 
    r=[r0]
    for i in range(len(x)):
        r.append((x[i]/y[i])*(10**3))
    #for a in range(len(x)):
        #x[a]=x[a]/x[-1] 
    x1=np.array([0, 0.7204999999999999, 1.092, 1.569, 2.025, 3.032, 2.5355, 4.073, 4.498, 5.056, 6.03, 6.54, 7.01, 8.01, 8.71, 9.254999999999999, 10.16, 11.06, 12.05, 14.04])
    fig = plot_data(ax, x1, t, 'Comportamento (V, R)', 'Lâmpada 3', 'Voltagem (V)', 'Resistência (ohm)', fit_func=linear_func1, color='blue')
    return fig

# Create figure and axes
fig, ax = plt.subplots()

# Call lamp1(), lamp2(), and lamp3() with the axes object as an argument
lamp1(ax)
#lamp2(ax)
#lamp3(ax)
#artigo(ax)
# Add a legend
plt.legend()

# Display the plot
dpi = 300
#plt.savefig('VxT.png', dpi=dpi, bbox_inches='tight')
plt.plot()
