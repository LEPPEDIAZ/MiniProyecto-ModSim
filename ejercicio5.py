"""
---------------------------------------------- Primer mini proyecto -------------------------------------------------
Ana Lucía Leppe - 16
Pablo Viana - 16091 

Utilización de método de montecarlo para aproximación de integrales dobles o simples con limites en 0 y 1 
"""

import numpy as np
import math
import time
import random
import sys

it = 1000000

def funcion_xy(x, y):
	#Aqui definimos la función que vamos a integrar doble
	return (math.exp(-(1-x+x*y-x**2*y)/x**3))/x**2

def hacer_integral(funcion):
	montecarlo_prip = (1/it)**2
	def integrando():
		suma_de_respuestas = 0
		for i in range(it):
			x = random.random()
			y = random.random()
			suma_de_respuestas += funcion_xy(x,y)
		return suma_de_respuestas/it
	return integrando

respuesta = hacer_integral(funcion_xy)
print(respuesta())



