import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker

#Opções de fitagem
    
def loga(x, a, b, c):
    return a*np.log(x)+b*x+c
def linear_func(x, a, b):
    return a * x**b
def poli(x, a, b, c, d, e):
    return a+b*x+c*x*x+d*x*x*x+e*x*x*x*x
#Função para plot
def plotagem(x, y, titulo, eixox, eixoy, fitagem=None, xerr=None, yerr=None):
    #Criando imagem e eixos
    fig, ax=plt.subplots()
    plt.scatter(x, y, s=5.)
    
    #Se tem erro, isso ativa
    if xerr is not None:
        plt.errorbar(x, y, xerr=xerr, fmt='none', ecolor='black')
    if yerr is not None:
        plt.errorbar(x, y, yerr=yerr, fmt='none', ecolor='black')
    if fitagem is not None:    
    #Fitando os dados    
        popt, pcov = curve_fit(fitagem, x, y, sigma=yerr, absolute_sigma=True)
        xfit = np.linspace(0, 15, 100000)
        yfit = fitagem(xfit, *popt)
        plt.plot(xfit, yfit, 'r-', label='Fit')
    
    #Selecionando os parametro que vão ser exibidos
        if  fitagem==loga or fitagem==linear_func:
            print('Optimized Parameters:')
            print('a =', popt[0], '+/-', np.sqrt(pcov[0, 0]))
            print('b =', popt[1], '+/-', np.sqrt(pcov[1, 1]))
            #print('c =', popt[2], '+/-', np.sqrt(pcov[2, 2]))
        else:
            print('Optimized Parameters:')
            print('a =', popt[0], '+/-', np.sqrt(pcov[0, 0]))
            print('b =', popt[1], '+/-', np.sqrt(pcov[1, 1]))
            print('c =', popt[2], '+/-', np.sqrt(pcov[2, 2]))
            print('d =', popt[3], '+/-', np.sqrt(pcov[3, 3]))
            print('e =', popt[4], '+/-', np.sqrt(pcov[4, 4]))
    
    #Nomes e estetica
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.set_xlim(0)
    ax.set_ylim(0)
    #plt.xlim(right=4)
    #plt.ylim(top=300)
    plt.legend()
    plt.grid(True)
    return plt.show()

#Lampada III
'''
t0 = 298
r0 = 1.95

x=np.array([0.094, 0.1695, 0.415, 0.785, 1.389, 0.998, 1.482, 2.0315, 2.551, 3.089, 3.973, 4.5765, 5.118, 6.095, 6.52, 7.02, 8, 8.69, 9.05, 9.96, 11.06, 12.06, 14.07])
y=np.array([44.045, 71, 108.95, 147.2, 203.3, 167, 212.5, 255.4, 299.45, 333.87, 384.1, 417.1, 448.07, 497.5, 519.85, 548.75, 591.9, 625, 640, 675, 720, 755, 825])
xerr=np.array([0.015, 0.015, 0.015, 0.016, 0.016, 0.016, 0.017, 0.017, 0.018, 0.019, 0.02, 0.021, 0.022, 0.024, 0.024, 0.025, 0.027, 0.028, 0.029, 0.03, 0.032, 0.034, 0.037])

resistencia=[]
for i in range(len(x)):
    resistencia.append((x[i]/y[i])*(10**3))
#print(resistencia)

temperatura=[]
for i in range(len(x)):
    temperatura.append((t0*(resistencia[i]/r0)**(0.8271)))
#print(temperatura)
'''
#Lampada IV
'''
t0 = 299
r0 = 2
x=np.array([0.076, 0.154, 0.350, 0.715, 1.029, 1.457, 2.027,  2.591, 2.928, 4.041, 4.522, 5.053, 6.05, 6.54, 7.04, 8.06, 8.08, 9.24, 10.03, 11.02, 12, 13.88])
y=np.array([43.3, 81.15, 130.3, 166.2, 194.9, 231.65, 275.6, 315, 341.1, 403.7, 431.2, 458.7, 515, 540, 560, 615, 630, 660, 690, 725, 760, 830])
xerr=np.array([0.015, 0.015, 0.015, 0.015, 0.016, 0.017, 0.017, 0.018, 0.019, 0.02, 0.021, 0.022, 0.024, 0.024, 0.025, 0.027, 0.027, 0.029, 0.03, 0.032, 0.033, 0.037])

resistencia=[]
for i in range(len(x)):
    resistencia.append((x[i]/y[i])*(10**3))
#print(resistencia)

temperatura=[]
for i in range(len(x)):
    temperatura.append((t0*(resistencia[i]/r0)**(0.8271)))
#print(temperatura)
'''

#Lampada VI
t0 = 299
r0 = 2.4
x=np.array([0.0765, 0.155, 0.358, 0.7204999999999999, 1.092, 1.569, 2.025, 3.032, 2.5355, 4.073, 4.498, 5.056, 6.03, 6.54, 7.01, 8.01, 8.71, 9.254999999999999, 10.16, 11.06, 12.05, 14.04])
y=np.array([29.55666666666667, 82.1, 154.6, 217.75, 250.3, 281.85, 307.0, 362.1, 336.4, 410.15, 429.55, 454.2, 496.09999999999997, 517.75, 535.5, 571.55, 591.55, 620.0, 650.0, 675.0, 710.0, 760.0])
xerr=np.array([0.015, 0.015, 0.015, 0.015, 0.016, 0.017, 0.017, 0.019, 0.018, 0.021, 0.021, 0.022, 0.024, 0.024, 0.025, 0.027, 0.028, 0.029, 0.03, 0.032, 0.034, 0.037])

resistencia=[]
for i in range(len(x)):
    resistencia.append((x[i]/y[i])*(10**3))
#print(resistencia)

temperatura=[]
for i in range(len(x)):
    temperatura.append((t0*(resistencia[i]/r0)**(0.8271)))
#print(temperatura)


queres = input('')

if queres=='1':
    titulo = 'Corrente por voltagem - Lâmpada 3'
    eixox= 'Voltagem (V)'
    eixoy= 'Corrente (mA)'
    
    yerr = np.array([0.103, 0.254, 0.464, 0.646, 0.74, 0.831, 0.904, 1.063, 0.988, 1.201, 1.257, 1.329, 1.449, 1.512, 1.563, 1.667, 1.725, 1.807, 1.894, 1.966, 2.067, 2.211])

    plotagem(x, y, titulo, eixox, eixoy, fitagem=linear_func, xerr=xerr, yerr=yerr)

if queres=='2':
    titulo = 'Resistência por voltagem - Lâmpada 3'
    eixox= 'Voltagem (V)'
    eixoy= 'Resistência (ohm)'

    rerr=np.array([0.508, 0.183, 0.097, 0.07, 0.065, 0.063, 0.059, 0.058, 0.058, 0.059, 0.058, 0.058, 0.06, 0.059, 0.06, 0.062, 0.064, 0.064, 0.065, 0.067, 0.069, 0.073])
    yerr=rerr
  
    y=np.array(resistencia)
    plotagem(x, y, titulo, eixox, eixoy, fitagem=linear_func, xerr=xerr, yerr=yerr)

if queres=='3':
    titulo = 'Temperatura por voltagem - Lâmpada 3'
    eixox= 'Voltagem (V)'
    eixoy= 'Temperatura (K)'

    y=np.array(temperatura)
    yerr = np.array([51.7, 19.7, 10.3, 7.4, 7.1, 7.3, 7.3, 8.0, 7.7, 8.8, 9.0, 9.3, 9.9, 10.1, 10.4, 10.9, 11.3, 11.4, 11.8, 12.3, 12.6, 13.5])

    plotagem(x, y, titulo, eixox, eixoy, fitagem=linear_func, xerr=xerr, yerr=yerr)

    