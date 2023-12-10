# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Thu Mar 23 18:31:26 2023)---
test_list_tour = [1, 2, 3, 4, 5]
test_dict_tour = {'a': 1, 'b': 2}
runfile('C:/Users/gabri/.spyder-py3/temp.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Sat Mar 25 13:54:16 2023)---
chop(3.1415678, 4)
runfile('C:/Users/gabri/.spyder-py3/funchop.py', wdir='C:/Users/gabri/.spyder-py3')
x=12.82*0.4114
d=chop(x, 4)
print((d-x)/x)
runfile('C:/Users/gabri/.spyder-py3/funchop.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/matplolibteste.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Sun Mar 26 10:56:39 2023)---
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Apr 13 21:05:16 2023)---
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri Apr 14 10:00:52 2023)---
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
x
b
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
b
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
x
b
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
x
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
x
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
import sys
sys.getsizeof(A)
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
format long
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Tue Apr 18 08:21:11 2023)---
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed Apr 19 20:24:01 2023)---
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
def metodo1(n, a, b):
    #quantidade de operações -- n**2
    inicio = time.time()
    x = [0] * n

    for i in range(n):

        x[i]=b[i]

        for j in range(i):


            x[i]=x[i]-a[i][j]*x[j]

        x[i]=x[i]/a[i][i]
    fim = time.time()
    tempo = fim - inicio 
    print('Tempo de operação 1 %.10f' %tempo)

    return x
    def metodo2(n, a, b):
    #quantidade de operações -- n**2
    inicio = time.time()
    x = [0] * n

    for j in range(n):


        x[j]=b[j]/a[j][j]

        for i in range(j+1, n):
            #

            b[i]=b[i]-a[i][j]*x[j]

    fim = time.time()
    tempo1 = fim - inicio 
    print('Tempo de operação 2 %.10f' %tempo1)
    return x

def matriz(n):
    m=[]
    t=[]
    for i in range(n):
        linha = []
        t.append(0)
        for j in range(n):
            if j>i:
                linha.append(0)

            else:
                linha.append(i+j+1)

        m.append(linha)   
    p=m.copy()  

    for i in range(n):
        for j in range(n):
           t[i]=p[i][j]+t[i]
    return m

def matriz2(n, m):
    p=m.copy()  
    t=[]
    for i in range(n):
        t.append(0)
        for j in range(n):
           t[i]=p[i][j]+t[i]
    return t
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed Apr 19 21:20:23 2023)---
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Apr 20 08:17:16 2023)---
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/teste666.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Apr 20 20:52:56 2023)---
runfile('C:/Users/gabri/.spyder-py3/atividade3p2.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/Downloads/atividade 3.2 (1).py', wdir='C:/Users/gabri/Downloads')

## ---(Fri Apr 21 15:28:40 2023)---
runfile('C:/Users/gabri/Downloads/incertezas F359.py', wdir='C:/Users/gabri/Downloads')
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/resistencia.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri Apr 21 18:55:00 2023)---
runfile('C:/Users/gabri/.spyder-py3/resistencia.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/Downloads/atividade 3.2 (1).py', wdir='C:/Users/gabri/Downloads')
runfile('C:/Users/gabri/.spyder-py3/temperatura.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu May  4 20:21:11 2023)---
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu May  4 21:07:51 2023)---
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/temperatura.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/resistencia.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/temperatura.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/grafff.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri May  5 08:17:25 2023)---
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri May  5 08:50:02 2023)---
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri May  5 17:24:37 2023)---
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri May 12 10:13:37 2023)---
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu May 18 17:59:21 2023)---
mola
mola = pd.read_csv('Experimento_Mola.txt')
import pandas as pd
mola = pd.read_csv('Experimento_Mola.txt')
runfile('C:/Users/gabri/.spyder-py3/monbreno.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('D:/monitoria/gambling_program.py', wdir='D:/monitoria')

## ---(Sun May 28 16:14:44 2023)---
runfile('C:/Users/gabri/.spyder-py3/monbreno.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/monbreno.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/plottest.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
a=[1, 2, 4, 5]
a
a/3
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Mon May 29 12:42:39 2023)---
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed May 31 13:38:15 2023)---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Jun  1 11:44:42 2023)---
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Sun Jun 25 17:39:39 2023)---
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Sun Jun 25 18:16:57 2023)---
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Mon Jun 26 21:31:31 2023)---
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/incertezas F359 (1).py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/fitf359ideal.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Tue Jul  4 12:55:41 2023)---
runcell(0, 'C:/Users/gabri/Downloads/witeximport.py')
runcell(1, 'C:/Users/gabri/Downloads/witeximport.py')
runcell(0, 'C:/Users/gabri/Downloads/witeximport.py')
runcell(1, 'C:/Users/gabri/Downloads/witeximport.py')
runfile('C:/Users/gabri/Downloads/witeximport.py', wdir='C:/Users/gabri/Downloads')
runfile('C:/Users/gabri/OneDrive/Área de Trabalho/Amostras - Raman e PL/Medusa 2/tratamento.py', wdir='C:/Users/gabri/OneDrive/Área de Trabalho/Amostras - Raman e PL/Medusa 2')
runfile('C:/Users/gabri/.spyder-py3/tratamento.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/tratamento.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/tratamento.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/tratamento.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/tratamento.py', wdir='C:/Users/gabri/.spyder-py3')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runfile('C:/Users/gabri/.spyder-py3/untitled1.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/untitled1.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runfile('C:/Users/gabri/.spyder-py3/separador_tabelas.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/separador_tabelas.py')
i=2
print('oi'+i+'oi')
print('oi',i,'oi')
runcell(0, 'C:/Users/gabri/.spyder-py3/separador_tabelas.py')
i=5
print('dados_separados', i, '.csv')
runcell(0, 'C:/Users/gabri/.spyder-py3/separador_tabelas.py')

## ---(Thu Jul  6 09:57:51 2023)---
runfile('C:/Users/gabri/.spyder-py3/separador_tabelas.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Fri Jul  7 00:09:17 2023)---
runfile('C:/Users/gabri/.spyder-py3/separador_tabelas.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamento.py')
runfile('C:/Users/gabri/.spyder-py3/formatacaodados.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runfile('C:/Users/gabri/.spyder-py3/bsep.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runfile('C:/Users/gabri/.spyder-py3/bsep.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runfile('C:/Users/gabri/.spyder-py3/bsep.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runfile('C:/Users/gabri/.spyder-py3/bsep.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runfile('C:/Users/gabri/.spyder-py3/formatacaodados.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Sun Jul  9 10:17:08 2023)---
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Mon Jul 10 11:11:26 2023)---
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Wed Jul 12 08:18:48 2023)---
runcell(0, 'C:/Users/gabri/.spyder-py3/HORIBA.py')
runfile('C:/Users/gabri/.spyder-py3/HORIBA.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Jul 13 08:53:46 2023)---
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Mon Jul 17 11:21:06 2023)---
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/formatacaodados.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Wed Jul 19 14:42:08 2023)---
runcell(2, 'C:/Users/gabri/.spyder-py3/bsep.py')

## ---(Tue Aug  1 13:50:23 2023)---
runfile('C:/Users/gabri/.spyder-py3/diagnostica.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/diagnostica.py')
runfile('C:/Users/gabri/.spyder-py3/diagnostica.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/diagnostica.py')
runfile('C:/Users/gabri/.spyder-py3/diagnostica.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Thu Aug  3 15:58:33 2023)---
runfile('C:/Users/gabri/.spyder-py3/diagnostica.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed Sep 27 15:11:10 2023)---
runfile('C:/Users/gabri/.spyder-py3/tratamentoHBT.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(2, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(3, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(0, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')
runcell(1, 'C:/Users/gabri/.spyder-py3/tratamentoHBT.py')

## ---(Sun Oct  8 23:14:36 2023)---
runfile('C:/Users/gabri/.spyder-py3/animacaoic.py', wdir='C:/Users/gabri/.spyder-py3')
runcell(0, 'C:/Users/gabri/.spyder-py3/animacaoic.py')

## ---(Mon Oct  9 10:17:45 2023)---
runfile('C:/Users/gabri/.spyder-py3/animacaoic.py', wdir='C:/Users/gabri/.spyder-py3')

## ---(Wed Oct 11 15:20:18 2023)---
runfile('C:/Users/gabri/.spyder-py3/animacaoic.py', wdir='C:/Users/gabri/.spyder-py3')