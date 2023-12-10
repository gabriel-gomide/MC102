# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:35:12 2023

@author: gabri
"""
import sys
import atividade3 as at3



n=5000
ma = at3.matriz(n)
mb = at3.matrizind(n)


print('Tamanho da matriz', sys.getsizeof(ma))

solução1 = at3.metodo1(n, ma, mb)
solução2 = at3.metodo2(n, ma, mb)
#print(solução2)

