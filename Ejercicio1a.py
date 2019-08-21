"""
---------------------------------------------- Primer mini proyecto -------------------------------------------------
Ana Lucía Leppe - 16
Pablo Viana - 16091 

Ejercicio 1a: Eleccion de el punto que se tomara dependiendo de su probabilidad , crea una lista y escoge que puntos se agregan a la lista
juego de caos es un algoritmo no deterministico usado para generar fractales, que parte un punto dado y da saltos deterministicos hacia otros
puntos del plano
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation

def graficar(puntos):
    xx = [x for (x, y) in puntos]
    yy = [y for (x, y) in puntos]
    plt.plot(xx, yy, 'y.')
    plt.show()

def mostrar_resultado(puntos):
    xx = [x for (x, y) in puntos]
    yy = [y for (x, y) in puntos]
    fig = plt.figure()
    def pasos(i):
        scale = 0.1 - i * 0.0000001
        ax = plt.axes(xlim=(0, scale), ylim=(0, scale))
        return ax.plot(xx, yy, 'y.')
    plt.show()

def probabilidad(F, P):
    puntos = []
    for dato, prob in zip(F,P):
         puntos += [dato] * int(prob * 1000)
    return random.choice(puntos)

def paso_deterministico( x, y):
    return [(x/2, y/2), (x/2 + 0.5, y/2 ), (x/2 + 0.25, y/2 + 0.5)]

def Shierpinski(P= [0.33, 0.33, 0.33] , n = 100000):
    x = []
    y = []
    x.append(0)
    y.append(0)
    for i in range(1,n):
        F = paso_deterministico(x[i-1], y[i-1])
        puntos= probabilidad(F, P)
        x.append(puntos[0])
        y.append(puntos[1]) 
    return x, y

Shierpinski = Shierpinski()
plt.plot(Shierpinski[0], Shierpinski[1], "y.")
print(Shierpinski[0], Shierpinski[1]  )
plt.show()



