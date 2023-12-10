from uncertainties import ufloat
from uncertainties.umath import *  # sin(), etc.
x = ufloat(1, 0.1)  # x = 1+/-0.1
print (2*x)

sin(2*x)  # In a Python shell, "print" is optional
