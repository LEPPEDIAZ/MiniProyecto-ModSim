"""
---------------------------------------------- Primer mini proyecto -------------------------------------------------
Ana Lucía Leppe - 16
Pablo Viana - 16091 

python ejercicio3.py [numero de generador a utilizar] [iteraciones]

numero de generador 1 2 o 3 

Programa para comaprar 3 generador de números pseudoaleatorios

"""
import random
import sys
import matplotlib.pyplot as plt
from matplotlib import animation

#Declaramos variables
seed = 0.05
it = int(sys.argv[2])
primero_generados = [seed]
segundo_generados = [seed]
tercero_generados = [seed]

#Funcion para imprimir resultados
def stats(argumento):
	if int(argumento) == 1:
		for x in range(it):
			segundo_generador(segundo_generados[x])
		sorteo(segundo_generados,0.0,0.1)
		sorteo(segundo_generados,0.1,0.2)
		sorteo(segundo_generados,0.2,0.3)
		sorteo(segundo_generados,0.3,0.4)
		sorteo(segundo_generados,0.4,0.5)
		sorteo(segundo_generados,0.5,0.6)
		sorteo(segundo_generados,0.6,0.7)
		sorteo(segundo_generados,0.7,0.8)
		sorteo(segundo_generados,0.8,0.9)
		sorteo(segundo_generados,0.9,1.0)
	elif int(argumento) == 2:
		for x in range(it):
			primer_generador(primero_generados[x])
		sorteo(primero_generados,0.0,0.1)
		sorteo(primero_generados,0.1,0.2)
		sorteo(primero_generados,0.2,0.3)
		sorteo(primero_generados,0.3,0.4)
		sorteo(primero_generados,0.4,0.5)
		sorteo(primero_generados,0.5,0.6)
		sorteo(primero_generados,0.6,0.7)
		sorteo(primero_generados,0.7,0.8)
		sorteo(primero_generados,0.8,0.9)
		sorteo(primero_generados,0.9,1.0)
	else:
		for x in range(it):
			tercero_generados.append(random.randrange(1))
		sorteo(tercero_generados,0.0,0.1)
		sorteo(tercero_generados,0.1,0.2)
		sorteo(tercero_generados,0.2,0.3)
		sorteo(tercero_generados,0.3,0.4)
		sorteo(tercero_generados,0.4,0.5)
		sorteo(tercero_generados,0.5,0.6)
		sorteo(tercero_generados,0.6,0.7)
		sorteo(tercero_generados,0.7,0.8)
		sorteo(tercero_generados,0.8,0.9)
		sorteo(tercero_generados,0.9,1.0)

#recuento de numeros entres inferior y superior
def sorteo(lista, inferior, superior):
    cont = 0
    histo  = []
    for x in lista: 
        if x>= inferior and x<= superior: 
            cont += 1
            if(cont%15 == 0):
            	histo.append("*")
    cont = cont - 1
    if cont < 0:
    	cont = 0
    print(str(inferior)+'-'+str(superior)+': '+' '.join(map(str, histo))+" total:" + str(cont))
    
    
#Generador numero 1
def primer_generador(numero):
	xn = (5**5*numero)%(2**35-1)
	primero_generados.append(xn%1)

#Generados numero 2
def segundo_generador(numero):
	yn = (7**5*numero)%(2**31-1)
	segundo_generados.append(yn%1)

#main
stats(sys.argv[1])

