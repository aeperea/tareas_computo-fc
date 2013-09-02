import numpy as np
from sympy.mpmath import *

mp.dps = 30
Res = quad(lambda x: 1./sqrt(pi)*exp(-x**2), [0,1])

print Res