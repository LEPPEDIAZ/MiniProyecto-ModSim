import math
from random import random
import numpy as np
from scipy.integrate import quad
x = 0
function = np.exp(-x ** 2)
def g(x):
	#Aqui definimos la función que vamos a integrar doble
	return np.exp(-x ** 2)
#funcion de transformacion
#siguiendo (b-a)g(a+(b-a)y)
#transformacion = lambda x: (1/x - 1) * g (1 + (1/x - 1))
#transformacion = lambda x: (math.inf + math.inf) * g (-math.inf + (math.inf + math.inf))
transformacion = lambda x: ((1 - 0) * g (1 + (1 - 0)))
integral= quad(transformacion,0, 1)
integral2= quad(transformacion,math.inf, -math.inf)
print("prueba", integral)
print("prueba", integral[0])
print("prueba", integral2)
print("prueba", integral2[0])
def MonteCarlo(F, iteraciones):
    for i in range(1,iteraciones):
        calcular = 0
        calcular += F(random())/iteraciones
    return calcular

print("MonteCarlo:")
print("100: " + str(MonteCarlo(transformacion, 100)))       
print("10,000: " + str(MonteCarlo(transformacion, 10000)))    
print("1,000,000: " + str(MonteCarlo(transformacion, 1000000)))   