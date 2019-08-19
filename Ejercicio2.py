"""
---------------------------------------------- Primer mini proyecto -------------------------------------------------
Ana Lucía Leppe - 16
Pablo Viana - 16091 

Ejercicio 2 juego de caos para el helecho de barnsley
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

def Barnsley(n, pasos=False):
    puntos = []
    f1 = lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
    f2 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
    f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
    f4 = lambda x,y: (0., 0.16*y)
    fs = [f4, f1, f3, f2]
    width, height = 300, 300
    aimg = np.zeros((width, height))
    x, y = 0, 0
    for i in range(n):
        f = np.random.choice(fs, p=[0.01, 0.85, 0.07, 0.07])
        x, y = f(x,y)
        ix, iy = int(width / 2 + x * width / 10), int(y * height / 12)
        print(x,y)
        aimg[iy, ix] = 1
    plt.imshow(aimg[::-1,:], cmap=cm.Greens)
    plt.show()
Barnsley(n=100000, pasos=False)