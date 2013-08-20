import numpy as np

ini = 4
fin = 250

def calcula_pi(n):
	R = 1
	alfa = 2*np.pi/n
	lado_in = np.sqrt(2.0-2.0*np.cos(alfa))
	per_in = lado_in*n
	pi_in = per_in/2
	
	betta = (np.pi-alfa)/2.0
	betta_comp = np.pi/2 - betta
	lado_out = lado_in * 1/np.cos(betta_comp)
	per_out = lado_out*n
	pi_out = per_out/2
	
	print "n = ", n, "lim inf: ", pi_in, " lim_sup: ", pi_out
	return pi_in, pi_out

X = np.array([calcula_pi(n) for n in range(ini,fin)])
pi_int = X[:,0]
pi_ext = X[:,1]

x = range(ini,fin)

from matplotlib import pyplot as plt
plt.figure()
plt.ion()
plt.plot(x,pi_int,'o-')
plt.plot(x,pi_ext,'o-')
plt.xlabel("$n$ - lados del poligono")
plt.title("calculo de $\pi$ por metodo de Arquimides")
plt.grid(True)
plt.show()

error_int = pi_int - np.pi
error_ext = pi_ext - np.pi

plt.figure()
plt.grid(True)
plt.xlabel("$n$ - lados del poligono")
plt.ylabel("$\epsilon_n$",fontsize=18)
plt.title("Error de la cota inferior")
plt.plot(x,error_int)

plt.figure()
plt.grid(True)
plt.xlabel("$n$ - lados del poligono")
plt.ylabel("$\epsilon_n$",fontsize=18)
plt.title("Error de la cota superior")
plt.plot(x,error_ext)

x = np.array(x)

plt.figure()
plt.loglog(x,np.abs(error_int),'o')
plt.xlabel("$n$ - lados del poligono")
plt.ylabel("$\epsilon_n$",fontsize=18)
plt.title("Error de la cota inferior (escala logaritmica)")
plt.loglog(x, (1/np.pi)**(-3./2.)*x**(-2.),'-')
plt.grid(True)

plt.figure()
plt.loglog(x,np.abs(error_ext),'o')
plt.xlabel("$n$ - lados del poligono")
plt.ylabel("$\epsilon_n$",fontsize=18)
plt.title("Error de la cota superior (escala logaritmica)")
plt.loglog(x, (1/np.pi*x)**(-2.),'-')
plt.grid(True)
