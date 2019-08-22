import math
from random import random , uniform
import numpy as np
from scipy.integrate import quad

def g(y):
	return 2 * (math.exp(-((1/y)-1)**2)/ y**2)
def MonteCarlo(F, iteraciones):
    for i in range(iteraciones):
        decision = np.random.uniform(0,1) + 1
        calcular = 0
        calcular += F(decision) 
        calcular = calcular / iteraciones
    return  calcular + decision

print("MonteCarlo:")
print("100: " + str(MonteCarlo(g, 100)))       
print("10,000: " + str(MonteCarlo(g, 10000)))    
print("1,000,000: " + str(MonteCarlo(g, 1000000)))   