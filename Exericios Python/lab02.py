###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
###################################################

d1= float(input())
v1= float(input()) 
t= float(input())
d2= float(input())
v2= float(input())

ts= d1/v1
tb= t*24+d2/v2

if ts<tb:
    print(True)
else:
    print(False)
