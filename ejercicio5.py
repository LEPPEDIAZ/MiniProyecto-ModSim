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

it = int(sys.argv[2])

def funcion_xy(x, y):
	#Aqui definimos la función que vamos a integrar doble
	return math.exp(-(x+y))

def hacer_integral(funcion, sd):
	suma_de_respuestas = 0
	montecarlo_prip = (1/it)**2
	t = time.clock()
	t1 = time.clock()
	t2 = time.clock()
	def integrando():
		for i in range(it):
			x = random.random()
			if int(sd) == 1:
				suma_de_respuestas += funcion(x)
			elif int(sd) == 2:
				for z in range(it):
					y = random.random()
					suma_de_respuestas += funcion(x,y)



