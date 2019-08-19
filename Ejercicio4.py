import numpy as np
from scipy.integrate import quad
import math


def integrand(x):
    return np.exp(-x ** 2)

#-INFINITO a INFINITO
I = quad(integrand, float(- math.inf), float(math.inf))
print(I)

# 0 a 1
Integral = quad(integrand, 0, 1)
print(Integral)