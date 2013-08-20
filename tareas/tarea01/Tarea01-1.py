import numpy as np

def raiz(y):
	error = 1E-8;	#8 decimales significativos
	x0 = y/2.0		#semilla siendo la mitad del valor a buscar
	x1 = y
	while (np.abs(x1-x0) > error):
		x0 = x1
		x1 = 1/2.0*(x0+y/x0)
	return x1

#generador obtenido de internet, permite iterar dando un incio, 
#fin y un 'paso' (al igual que en MATLAB)
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

#impresion de las raices entre 0 y 10 a intervalos de 0.1
for i in my_range(0,10,0.1):
	print "La raiz de ", i , " es ", raiz(i)		