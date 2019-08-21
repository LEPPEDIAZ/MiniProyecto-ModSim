"""
---------------------------------------------- Primer mini proyecto -------------------------------------------------
Ana Lucía Leppe - 16
Pablo Viana - 16091 

Ejercicio 2 juego de caos para el helecho de barnsley: sigue con las mismas funciones del juego de caos anterior. Pero modifica 
las probabilidades y las funciones. 
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
def graficar(puntos):
    xx = [x for (x, y) in puntos]
    yy = [y for (x, y) in puntos]
    plt.plot(xx, yy, 'g.')
    plt.show()

def mostrar_resultado(puntos):
    xx = [x for (x, y) in puntos]
    yy = [y for (x, y) in puntos]
    fig = plt.figure()
    def pasos(i):
        scale = 0.1 - i * 0.0000001
        ax = plt.axes(xlim=(0, scale), ylim=(0, scale))
        return ax.plot(xx, yy, 'g.')
    plt.show()

def probabilidad(F, P):
    puntos = []
    for dato, prob in zip(F,P):
         puntos += [dato] * int(prob * 1000)
    return random.choice(puntos)

def paso_deterministico( x, y):
    return [(x*0.86 + y*0.04+ 0.0, x*-0.04 + y* 0.85 + 1.6), (-0.15*x + 0.28*y + 0.0, x*0.26+ y*0.24+ 0.44), (x*0.2 + y*-0.26 + 0.0, x*0.23 + y*0.22 + 1.6), (x*0.0 + y*0.0, x*0.0 + y*0.16)]

def Barnsley(P= [0.85, 0.07, 0.07, 0.01] , n = 100000):
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

Barnsley = Barnsley()
plt.plot(Barnsley[0], Barnsley[1], "g.")
print(Barnsley[0], Barnsley[1]  )
plt.show()
