import numpy as np

x = 77617
y = 33096

R = 33375./100.*y**6 + x**2*(11.*x**2*y**2 - y**6 - 121.*y**4 -2.) + 55./10.*y**8 + x/(2.*y)

from sympy.mpmath import *

mp.dps = 30
x = mpf('77617')
y = mpf('33096')
R_30 = 33375./100.*y**6 + x**2*(11.*x**2*y**2 - y**6 - 121*y**4 -2.) + 55./10.*y**8 + x/(2.*y)

mp.dps = 60
x = mpf('77617')
y = mpf('33096')
R_60 = 33375./100.*y**6 + x**2*(11.*x**2*y**2 - y**6 - 121*y**4 -2.) + 55./10.*y**8 + x/(2.*y)

mp.dps = 80
x = mpf('77617')
y = mpf('33096')
R_80 = 33375./100.*y**6 + x**2*(11.*x**2*y**2 - y**6 - 121*y**4 -2.) + 55./10.*y**8 + x/(2.*y)

from sympy import Rational, pprint
x = Rational(77617)
y = Rational(33096)

R_Rat = (Rational(33375,100)*y**6 + x**2*(11*x**2*y**2 - y**6 - 121*y**4 -2) + Rational(55,10)*y**8 + x/(Rational(2)*y))

print "Valor de R(x,y) normal de numpy: ", R
print "Valor de R(x,y) con 30 digitos de precision", R_30
print "Valor de R(x,y) con 60 digitos de precision", R_60
print "Valor de R(x,y) con 80 digitos de precision", R_80
print "Valor de R(x,y) con la libreria Rational", R_Rat
