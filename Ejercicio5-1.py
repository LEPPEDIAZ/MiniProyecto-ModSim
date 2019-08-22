import math
from random import random , uniform
import numpy as np
from scipy.integrate import quad

def g(x,y):
	return (math.exp(-1*((1/x)-1) * (1+y))/ (x**2)) * ((1/x)-1)
def MonteCarlo(F, iteraciones):
    for i in range(iteraciones):
        decision = np.random.uniform(0,1) 
        calcular = 0
        decision1 = np.random.random() + 1
        calcular += calcular + F(decision1, decision1) 
        calcular = calcular / iteraciones
    return  calcular + decision

print("MonteCarlo:")
print("100: " + str(MonteCarlo(g, 100)))       
print("10,000: " + str(MonteCarlo(g, 10000)))    
print("1,000,000: " + str(MonteCarlo(g, 1000000)))   