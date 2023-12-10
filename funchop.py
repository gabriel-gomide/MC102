# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:54:37 2023

@author: gabri
"""

def chop(x, n):
    y=str(x)
    z=list()
    for d in y:
        z.append(d)

    z=float(''.join(z))
    z=round(z, n-1)
    return z

x=0.975
p=x**3-3*(x**2)+3*x-1
q=((x-3)*x+3)*x-1
r=(x-1)**3

            
print(p)
print(q)
print(r)