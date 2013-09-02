import numpy as np

from matplotlib import pyplot as plt

x = np.linspace(0.01,1,1001)
f = 1./x*np.cos(np.log(x)/x)

plt.plot(x, f)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(True)
plt.show()

from sympy.mpmath import *

mp.dps = 50
f = lambda x: (1./x)*cos(log(x)/x)

I = quad(f, [0, 1], maxdegree=16, method='tanh-sinh')
print I
