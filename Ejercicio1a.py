"""
 Ejercicio 1a: comienza desde un vertice del triangulo y luego elige aleatoriamente el siguiente vertice
  y dibuja un pixel en medio, luego selecciona aleatoriamente un nuevo vertice y dibuja el punto medio.
"""
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
        scale = 1 - i * 0.02
        ax = plt.axes(xlim=(0, scale), ylim=(0, scale))
        return ax.plot(xx, yy, 'y.')
    plt.show()


def Shierpinski(n, pasos=False):
    vertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
    puntos = []
    #inicializa el vertice
    x, y = random.choice(vertices)
    for i in range(n):
        #selecciona el nuevo vertice
        vx, vy = random.choice(vertices)
        #encuentra el punto medio
        x = (vx + x) / 2.0
        y = (vy + y) / 2.0
        puntos.append((x, y))
        print(x,y)
    if pasos:
        mostrar_resultado(puntos)
    else:
        graficar(puntos)
#iteraciones
Shierpinski(n=100000, pasos=False)