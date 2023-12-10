#Medidas:
# Diferença de potencial em Volts;
# Corrente elétrica em miliAmpere;
# Resistência em Ohms.

#Funções auxiliares:
def media(lista):
    M = sum(lista)/len(lista)
    return M

def lista_media(medida):
    for i in range(len(medida)):
            im = media(medida[i])
            medida[i] = im
    return medida

#Incertezas fdps retangulares:   #u = a/2sqrt(3), onde "a" é a menor medida do visor
umA = 0.01/2*(3**(1/2))  
uV = 0.01/2*(3**(1/2))
uOhm = 0.01/2*(3**(1/2))


#Incertezas de calibração e combinadas:
#Amperímetro:
def cal_mA(LmA, n):
    listau = []
    listauc = []
    for i in range(len(LmA)):
       u = (0.005*LmA[i]+0.03)/(3**(1/2))
       listau.append(round(u,3))
       uc = (umA**2 +u**2)**(1/2)
       listauc.append(round(uc,3))
    X = listauc
    return X

#Voltímetro:
def cal_V(LV, n):
    listau = []
    listauc = []
    for i in range(len(LV)):
       u = (0.003*LV[i]+0.02)/(3**(1/2))
       listau.append(round(u,3))
       uc = (uV**2 +u**2)**(1/2)
       listauc.append(round(uc,3))
    X = listauc
    return X

#Ohmímetro:
def cal_ohm(LR): #Resistência em temperatura ambiente de cada lâmpada
    listau = []
    listauc = []
    for i in range(len(LR)):
       u = (0.005*LR[i]+0.02)/(3**(1/2))
       listau.append(round(u,3))
       uc = (uOhm**2 +u**2)**(1/2)
       listauc.append(round(uc,3))
    X = listauc
    return X


#Cálculo pontual da Resistência e temperatura:
#Cálculo da Resistência
def Rohm(mAm, Vm):
    listaR = []
    for i in range(len(mAm)):
        R = Vm[i]/(mAm[i]*0.001)
        listaR.append(round(R,6))
    return listaR

#Cálculo da Temperatura
def T(Rm,T0,RT0):
    listaT = []
    for i in range(len(Rm)):
        T = T0*(Rm[i]/RT0)**0.8271
        listaT.append(round(T,1))
    return listaT

#Incertezas propagadas:
#Incertezas pontuais da resistência de cada lâmpada
def IncResPont(Vm,mAm,ImA,IV,n):
    listauR = []
    for i in range(len(mAm)):
        uR = ((IV[i]/mAm[i])**2 + (Vm[i]*ImA[i]/((mAm[i])**2))**2)**0.5
        listauR.append(round(uR*1000,3))
    return listauR

#incertezaR1 = IncResPont(V1m, mA1m, incertezaL1mA, incertezaL1V, 1)

#Incertezas pontuais da resistência de cada lâmpada
def IncTempPont(Rm,IR, T0, RT0,IT0, IRT0, n):
    A = 0.8271
    listauT = []
    for i in range(len(Rm)):
        uT = ((((Rm[i]/RT0)**A)*IT0)**2 + ((A*(Rm[i])**(A-1)*T0/(RT0)**A)*IR[i])**2 + ((A*(RT0)**(-A-1))*T0*((Rm[i])**A)*IRT0)**2)**0.5
        listauT.append(round(uT,1))
    X = (f"Incertezas das temperaturas da lâmpada {n} em Kelvin: \n {listauT}")
    return X

#Dados iniciais da temperatura
T0 = [300, 298, 299, 299] #Lâmpadas I, III, IV e VI
IT0 = 1

RT0 = [1.55, 1.95, 2, 2.4]
IRT0= cal_ohm(RT0)





#Lâmpada I (1,5 - 1,6 ohms) (queimou)
mA1 = [[429.7, 429.3, 429.3, 429.3], [481.9, 491.8, 491.7, 491.7], [520.9, 521, 520.7, 519.4], [577.4], [710], [780], [880], [940], 
       [940, 950], [980], [1000], [1040], [1120, 1110]]

V1 = [[4.565, 4.558, 4.560, 4.559], [5.783, 5.782, 5.782, 5.782], [6.39, 6.37, 6.36, 6.35], 
      [7.64, 7.64, 7.63], [11.01], [13], [15.94], [17.99], [18.22], [19.52], [20.20], [21.66], [25.22]]

mA1m = lista_media(mA1)
#print(f"Corrente da lâmpada 1 em miliampere:\n {mA1m}")
incertezaL1mA = cal_mA(mA1m,1)
#print(f"Incerteza da corrente da lâmpada 1 em mA:\n {incertezaL1mA}")
V1m = lista_media(V1)
#print(f"Voltagem da lâmpada 1 em Volts:\n {V1m}")
incertezaL1V = cal_V(V1m,1)
#print(f"Incerteza da voltagem da lâmpada 1 em V:\n {incertezaL1V}")
R1 = Rohm(mA1m,V1m)
#print(f"Resistências da lâmpada 1 em Ohms:\n {R1}")
IR1 = IncResPont(V1m,mA1m,incertezaL1mA,incertezaL1V,1)
#print(f"Incertezas das Resistências da lâmpada 1 em Ohms:\n {IR1}")
RT01 = RT0[0]
IRT01 = IRT0[0]
T01 = T0[0]
T1 = T(R1,T01,RT01)
#print(f"Temperaturas da lâmpada 1 em Kelvin:\n {T1}")
IT1 = IncTempPont(R1, IR1, T01, RT01, IT0, IRT01, 1)
#print(IT1)






#Lâmpada III (1,7 - 1,8 ohms)
mA3 = [[44.045], [71], [108.95], [147.2], [203.3], [167], [212.5], [255.4],[299.45], [333.87], 
[384.1], [417.1], [448.07], [497.5], [519.85], [548.75], [591.9], [625], 
[640], [675], [720], [755], [825]]

V3 = [[0.094], [0.1695], [0.415], [0.785], [1.389], [0.998], [1.482], [2.0315], [2.551], 
[3.089], [3.973], [4.5765], [5.118], [6.095], [6.52], [7.02], [8], [8.69], 
[9.05], [9.96], [11.06], [12.06], [14.07]]

mA3m = lista_media(mA3)
#print(f"Corrente da lâmpada 3 em miliampere:\n {mA3m}")
incertezaL3mA = cal_mA(mA3m,3)
#print(f"Incerteza da corrente da lâmpada 3 em mA:\n {incertezaL3mA}")
V3m = lista_media(V3)
print(f"Voltagem da lâmpada 3 em Volts:\n {V3m}")
incertezaL3V = cal_V(V3m,3)
#print(f"Incerteza da voltagem da lâmpada 3 em V:\n {incertezaL3V}")
R3 = Rohm(mA3m,V3m)
#print(f"Resistências da lâmpada 3 em Ohms:\n {R3}")
IR3 = IncResPont(V3m,mA3m,incertezaL3mA,incertezaL3V,3)
#print(f"Incertezas das Resistências da lâmpada 3 em Ohms:\n {IR3}")
RT03 = RT0[1]
IRT03 = IRT0[1]
T03 = T0[1]
T3 = T(R3,T03,RT03)
print(f"Temperaturas da lâmpada 3 em Kelvin:\n {T3}")
IT3 = IncTempPont(R3, IR3, T03, RT03, IT0, IRT03, 3)
#print(IT3)





#Lâmpada IV (2 ohms)
mA4 = [[43.3], [81.15], [130.3], [166.2], [194.9], [231.65], [275.6], [315], [341.1],
[ 403.7], [431.2], [458.6], [515], [540], [560], [615], [630], [660], 
[690], [725], [760],[830]]

V4 = [[0.076], [0.154], [0.350], [0.715], [1.029], [1.457], [2.027], [ 2.591], 
[2.928], [4.041], [4.522], [5.053], [6.05], [6.54], [7.04], [8.06], [8.08], 
[9.24], [10.03], [11.02], [12], [13.88]]

mA4m = lista_media(mA4)
#print(f"Corrente da lâmpada 4 em miliampere:\n {mA4m}")
incertezaL4mA = cal_mA(mA4m,4)
#print(f"Incerteza da corrente da lâmpada 4 em mA:\n {incertezaL4mA}")
V4m = lista_media(V4)
#print(f"Voltagem da lâmpada 4 em Volts:\n {V4m}")
incertezaL4V = cal_V(V4m,4)
#print(f"Incerteza da voltagem da lâmpada 4 em V:\n {incertezaL4V}")
R4 = Rohm(mA4m,V4m)
#print(f"Resistências da lâmpada 4 em Ohms:\n {R4}")
IR4 = IncResPont(V4m,mA4m,incertezaL4mA,incertezaL4V,4)
#print(f"Incertezas das Resistências da lâmpada 4 em Ohms:\n {IR4}")
RT04 = RT0[2]
IRT04 = IRT0[2]
T04 = T0[2]
T4 = T(R4,T04,RT04)
print(f"Temperaturas da lâmpada 4 em Kelvin:\n {T4}")
IT4 = IncTempPont(R4, IR4, T04, RT04, IT0, IRT04, 4)
#print(IT4)






#Lâmpada VI (1,9 ohms)
mA6 = [[42.67, 42,4], [82.3, 82.1, 81.9], [154.6, 154.6], [217.9, 217.6], 
[251.1, 249.5], [282.2, 281.5], [307], [362.1], [336.5, 336.3], [410.8, 409.5], 
[429.3, 429.8], [454.7, 453.7], [496, 495.5, 496.8], [517.7, 517.8], [535.5], 
[571.6, 571.5], [592.4, 590.7], [620], [650], [670, 680], [710], [760]]

V6 = [[0.077, 0.076], [0.156, 0.155, 0.154], [0.358], [0.720, 0.721],[1.09, 1.094], 
[1.569],[2.025],[3.032], [2.536, 2.535], [4.072, 4.074], [4.498], [5.055, 5.057], 
[6.03], [6.54], [7.01], [8.01], [8.71], [9.26, 9.25], [10.16], [11.06], [12.05], [14.04]]

mA6m = lista_media(mA6)
#print(f"Corrente da lâmpada 6 em miliampere:\n {mA6m}")
incertezaL6mA = cal_mA(mA6m,6)
#print(f"Incerteza da corrente da lâmpada 6 em mA:\n {incertezaL6mA}")
V6m = lista_media(V6)
#print(f"Voltagem da lâmpada 6 em Volts:\n {V6m}")
incertezaL6V = cal_V(V6m,6)
#print(f"Incerteza da voltagem da lâmpada 6 em V:\n {incertezaL6V}")
R6 = Rohm(mA6m,V6m)
#print(f"Resistências da lâmpada 6 em Ohms:\n {R6}")
IR6 = IncResPont(V6m,mA6m,incertezaL6mA,incertezaL6V,6)
#print(f"Incertezas das Resistências da lâmpada 6 em Ohms:\n {IR6}")
RT06 = RT0[3]
IRT06 = IRT0[3]
T06 = T0[3]
T6 = T(R6,T06,RT06)
print(f"Temperaturas da lâmpada 6 em Kelvin:\n {T6}")
IT6 = IncTempPont(R6, IR6, T06, RT06, IT0, IRT06, 6)
#print(IT6)