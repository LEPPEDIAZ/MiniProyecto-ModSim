import math
from random import random
import numpy as np
x = 0
function = np.exp(-x ** 2)
#funcion de transformacion
transformacion = lambda x: (1/x - 1) * function * (1 + (1/x - 1))
def MonteCarlo(F, iteraciones):
    for i in range(1,iteraciones):
        calcular = 0
        calcular += F(random())/iteraciones
    return calcular

print("MonteCarlo:")
print("100: " + str(MonteCarlo(transformacion, 100)))       
print("10,000: " + str(MonteCarlo(transformacion, 10000)))    
print("1,000,000: " + str(MonteCarlo(transformacion, 1000000)))   