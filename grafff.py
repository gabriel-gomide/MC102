import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker

#Opções de fitagem
def expo(x, a, b, c):
    return a * np.exp(-b * x) + c

def poly4(x, a, b, c, d, e):
    return a*(x**4) +b*(x**3)+c*(x**2)+d*(x)+e

def linear_func(x, a, b):
    return a * x + b
    
def loga(x, a, b):
    return a*np.log(x)+b
    
    

#Função para plot
def plotagem(x, y, titulo, eixox, eixoy, fitagem=None, xerr=None, yerr=None):
    #Criando imagem e eixos
    fig, ax=plt.subplots()
    plt.scatter(x, y)
    
    #Se tem erro, isso ativa
    if xerr is not None:
        plt.errorbar(x, y, xerr=xerr, fmt='none', ecolor='black')
    if yerr is not None:
        plt.errorbar(x, y, yerr=yerr, fmt='none', ecolor='black')
    if fitagem is not None:    
    #Fitando os dados    
        popt, pcov = curve_fit(fitagem, x, y, sigma=yerr, absolute_sigma=True)
        xfit = np.linspace(0, 30, 200)
        yfit = fitagem(xfit, *popt)
        plt.plot(xfit, yfit, 'r-', label='Fit')
    
    #Selecionando os parametro que vão ser exibidos
        if fitagem==linear_func or fitagem==loga:
            print('Optimized Parameters:')
            print('a =', popt[0], '+/-', np.sqrt(pcov[0, 0]))
            print('b =', popt[1], '+/-', np.sqrt(pcov[1, 1]))
    
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
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.set_xlim(0)
    ax.set_ylim(0)
    plt.xlim(right=30)
    plt.ylim(top=1200)
    plt.legend()
    plt.grid(True)
    return plt.show()


titulo = 'Corrente por voltagem - Lâmpada 1'
eixox= 'Voltagem (V)'
eixoy= 'Corrente (mA)'
x=np.array([4.5605, 5.78225, 6.3625, 7.635, 11.01, 13.00,15.94, 17.99, 18.22, 19.52, 20.20, 21.66, 25.22])
y=np.array([429.4, 491.775, 520.5, 577.4, 710.0, 780.0, 880.0, 940.0, 945.0, 980.0, 1000, 1040, 1011.5  ])
xerr=np.array([0.021, 0.023, 0.024, 0.026, 0.032, 0.035, 0.040, 0.044, 0.044, 0.046, 0.047, 0.05, 0.056])
yerr = np.array([1.257, 1.43, 1.52, 1.684, 2.067, 2.269, 2.558, 2.731, 2.745, 2.846, 2.904, 3.02, 3.236])

plotagem(x, y, titulo, eixox, eixoy, fitagem=loga, xerr=xerr, yerr=yerr)
