# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:48:59 2023

@author: maria carolina
"""

#imports
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import warnings
from scipy.optimize import differential_evolution
from scipy.signal import find_peaks
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.metrics import r2_score
from scipy.interpolate import splrep, BSpline
from scipy import sparse
from scipy.sparse.linalg import spsolve


def linear(x,a,b):
    return a*x+b

def retirar_background(signal, shift):
    valor = (signal[len(signal)-1]+signal[len(signal)-50])/2
    return intensity-valor

def retirar_background_afim(signal, shift):
    v=100
    valor1 = (signal[len(signal)-1]+signal[len(signal)-50])/2
    valor2 = (signal[v]+signal[v-5])/2
    x1=(shift[len(signal)-1]+shift[len(signal)-50])/2
    x2 = (shift[v]+shift[v-5])/2
    parameters, covariance = curve_fit(linear, (x2,x1),(valor2,valor1))
    
    return intensity-parameters[0]*shift-parameters[1]

def retirar_background_linear(shift,signal): 
    parameters, covariance = curve_fit(linear, shift[50::], signal[50::])
    # plt.plot(parameters[0]*shift+parameters[1])
    # plt.show()
    return  intensity-parameters[0]*shift-parameters[1]

# The next function calculates the modified z-scores of a diferentiated spectrum

def modified_z_score(ys):
    ysb = np.diff(ys) # Differentiated intensity values
    median_y = np.median(ysb) # Median of the intensity values
    median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ysb]) # median_absolute_deviation of the differentiated intensity values
    modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y for y in ysb] # median_absolute_deviationmodified z scores
    return modified_z_scores
    
# The next function calculates the average values around the point to be replaced.
def fixer(y,ma):
    threshold = 150 # binarization threshold
    spikes = abs(np.array(modified_z_score(y))) > threshold
    y_out = y.copy()
    for i in np.arange(len(spikes)):
        if spikes[i] != 0:
            w = np.arange(i-ma,i+1+ma)
            we = w[spikes[w] == 0]
            y_out[i] = np.mean(y[we])
    return y_out

def baseline_als(y, lam, p, niter=100):
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z


def gaussian1(x_array, amp1,cen1,sigma1):
    return amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x_array-cen1)/sigma1)**2)))

def gaussian2(x_array, amp1,cen1,sigma1, amp2,cen2,sigma2):
    return amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x_array-cen1)/sigma1)**2))) + \
            amp2*(1/(sigma2*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x_array-cen2)/sigma2)**2)))

def Lorentzian1(x, amp1, cen1, wid1):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) 

def Lorentzian2(x, amp1, cen1, wid1, amp2,cen2,wid2):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (amp2*wid2**2/((x-cen2)**2+wid2**2)) 

def Lorentzian3(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
                (amp3*wid3**2/((x-cen3)**2+wid3**2))
                
def Lorentzian4(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3, amp4,cen4,wid4):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
                (amp3*wid3**2/((x-cen3)**2+wid3**2)) +\
                    (amp4*wid4**2/((x-cen4)**2+wid4**2))

def Lorentzian5(x, amp1, cen1, wid1, amp2,cen2,wid2, amp3,cen3,wid3, amp4,cen4,wid4, amp5,cen5,wid5):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2)) +\
            (amp2*wid2**2/((x-cen2)**2+wid2**2)) +\
                (amp3*wid3**2/((x-cen3)**2+wid3**2)) +\
                    (amp4*wid4**2/((x-cen4)**2+wid4**2)) +\
                        (amp5*wid5**2/((x-cen5)**2+wid5**2))



# HORIBA SINGLE SPECTRUM

i=9

path =r'G:/Meu Drive/Mestrado Carol/2D/Measurements/AFOSR/Horiba/23_07_07/Flat_S{}'.format(i)
file_name = 's{}_sinx_raman_1s_10ac.txt'.format(i)
full_path = os.path.join(path,file_name)
data= pd.read_csv(full_path, sep="\t", header = 0)

shift=data.iloc[:,0]
intensity=data.iloc[:,1]

# Background and normalization

# Parameters for this case:
l = 10000000 # smoothness
p = 0.05 # asymmetry

# signal=retirar_background(shift,intensity)/(np.max(retirar_background(shift,intensity)))
# signal=retirar_background_afim(shift,intensity)/(np.max(retirar_background_afim(shift,intensity)))
# signal=retirar_background_linear(shift,intensity)/(np.max(retirar_background_linear(shift,intensity)))

intensity=intensity[50::]
shift = shift[50::]

despiked_spectrum = fixer(intensity,ma=10)
estimated_baselined = baseline_als(despiked_spectrum, l, p)
signal = (despiked_spectrum - estimated_baselined)/np.max(despiked_spectrum - estimated_baselined)


# # We compared the original mix spectrum and the estimated baseline:
# ax1.plot(shift[50::], despiked_spectrum, color = 'black', label = 'Mix spectrum with noise' )
# ax1.plot(shift[50::], estimated_baselined, color = 'red', label = 'Estimated baseline')
# ax1.set_title('Baseline estimation', fontsize = 15)
# ax1.set_xlabel('Wavelength', fontsize = 15)
# ax1.set_ylabel('Intensity',  fontsize = 15)
# ax1.legend()

# # We plot the mix spectrum after baseline subtraction
# ax2.plot(shift[50::], baselined_spectrum, color = 'black', label = 'Baselined spectrum with noise' )
# ax2.set_title('Baselined spectrum', fontsize = 15)
# ax2.set_xlabel('Wavelength', fontsize = 15)
# ax2.set_ylabel('Intensity',  fontsize = 15)
# plt.show()


# Find Peaks

peaks, _ = find_peaks(signal, height=0.08)
plt.plot(shift, signal, '.', label='data')
plt.plot(shift[peaks+50],signal[peaks+50], 'x', label='Peaks')
plt.show()

# Fit


if len(peaks)==1:
    chutes=(signal[peaks[0]+50],shift[peaks[0]+50],10)



    parameters, covariance = curve_fit(Lorentzian1, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    fit_y = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()



elif len(peaks)==2:
    chutes=(signal[peaks[0]+50],shift[peaks[0]+50],3,signal[peaks[1]+50],shift[peaks[1]+50],10)



    parameters, covariance = curve_fit(Lorentzian2, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    # fit_y1 = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    # plt.plot(shift, fit_y1, '-', label='Lorentzian 1')
    # fit_y2 = Lorentzian1(shift, parameters[3], parameters[4],parameters[5])
    # plt.plot(shift, fit_y2, '-', label='Lorentzian 2')
    fit_y = Lorentzian2(shift, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],parameters[5])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()
    




elif len(peaks)==3:
    chutes=(signal[peaks[0]+50],shift[peaks[0]+50],3,signal[peaks[1]+50],shift[peaks[1]+50],3,signal[peaks[2]+50],shift[peaks[2]],10)



    parameters, covariance = curve_fit(Lorentzian3, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    # fit_y1 = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    # plt.plot(shift, fit_y1, '-', label='Lorentzian 1')
    # fit_y2 = Lorentzian1(shift, parameters[3], parameters[4],parameters[5])
    # plt.plot(shift, fit_y2, '-', label='Lorentzian 2')
    # fit_y3 = Lorentzian1(shift, parameters[6],parameters[7],parameters[8])
    # plt.plot(shift, fit_y3, '-', label='Lorentzian 3')  
    fit_y = Lorentzian3(shift, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],parameters[5],parameters[6],parameters[7],parameters[8])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()


elif len(peaks)==4:
    chutes=(signal[peaks[0]+50],shift[peaks[0]+50],3,signal[peaks[1]+50],shift[peaks[1]+50],3,signal[peaks[2]+50],shift[peaks[2]+50],3,signal[peaks[3]+50],shift[peaks[3]+50],10)



    parameters, covariance = curve_fit(Lorentzian4, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    # fit_y1 = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    # plt.plot(shift, fit_y1, '-', label='Lorentzian 1')
    # fit_y2 = Lorentzian1(shift, parameters[3], parameters[4],parameters[5])
    # plt.plot(shift, fit_y2, '-', label='Lorentzian 2')
    # fit_y3 = Lorentzian1(shift, parameters[6],parameters[7],parameters[8])
    # plt.plot(shift, fit_y3, '-', label='Lorentzian 3')  
    fit_y = Lorentzian4(shift, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],parameters[5],parameters[6],parameters[7],parameters[8],parameters[9],parameters[10],parameters[11])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()


elif len(peaks)==5:
    chutes=(signal[peaks[0]+50],shift[peaks[0]+50],3,signal[peaks[1]+50],shift[peaks[1]+50],3,signal[peaks[2]+50],shift[peaks[2]+50],3,signal[peaks[3]+50],shift[peaks[3]+50],3,signal[peaks[4]+50],shift[peaks[4]+50],10)



    parameters, covariance = curve_fit(Lorentzian5, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    # fit_y1 = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    # plt.plot(shift, fit_y1, '-', label='Lorentzian 1')
    # fit_y2 = Lorentzian1(shift, parameters[3], parameters[4],parameters[5])
    # plt.plot(shift, fit_y2, '-', label='Lorentzian 2')
    # fit_y3 = Lorentzian1(shift, parameters[6],parameters[7],parameters[8])
    # plt.plot(shift, fit_y3, '-', label='Lorentzian 3')  
    fit_y = Lorentzian5(shift, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],parameters[5],parameters[6],parameters[7],parameters[8],parameters[9],parameters[10],parameters[11],parameters[12],parameters[13],parameters[14])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()


else:
    chutes=(0.5,130,3,0.5,250,3,0.5,260,3,0.5,520,10)



    parameters, covariance = curve_fit(Lorentzian4, shift, signal, p0 = chutes)
    plt.plot(shift, signal, '.', label='data')
    # fit_y1 = Lorentzian1(shift, parameters[0], parameters[1], parameters[2])
    # plt.plot(shift, fit_y1+1, '-', label='Lorentzian 1')
    # fit_y2 = Lorentzian1(shift, parameters[3], parameters[4],parameters[5])
    # plt.plot(shift, fit_y2+1, '-', label='Lorentzian 2')
    # fit_y3 = Lorentzian1(shift, parameters[6],parameters[7],parameters[8])
    # plt.plot(shift, fit_y3+1, '-', label='Lorentzian 3')
    # fit_y4 = Lorentzian1(shift, parameters[9],parameters[10],parameters[11])
    # plt.plot(shift, fit_y4+1, '-', label='Lorentzian 4')  
    fit_y = Lorentzian4(shift, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],parameters[5],parameters[6],parameters[7],parameters[8],parameters[9],parameters[10],parameters[11])
    plt.plot(shift, fit_y, '-', label='fit')


    plt.xlim()
    plt.legend()
    plt.xlabel('Raman Shift (cm $^{-1}$)')
    plt.ylabel('Intensity (a.u.)')
    plt.show()
   


