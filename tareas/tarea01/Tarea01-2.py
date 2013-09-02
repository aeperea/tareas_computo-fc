import numpy as np
from sympy.mpmath import *

mp.dps = 25

def funcion(x0):
	return x0**2

def recursion(x0,n):
	for i in xrange(n):
		x1 = funcion(x0)
		x0 = x1;
		print "el valor ", i+1," es", x1
	return
	
n  = 75
a = mpf('1')
b = mpf('10e-20')
x0 = a-b

recursion(x0,n)