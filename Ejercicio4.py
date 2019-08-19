import numpy as np
from scipy.integrate import quad
import math


def integrand(x):
    return np.exp(-x ** 2)

def menu():
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      A: Resultado de Integral de infinito a menos infinito
                      B: Resultado de integral de 0 a 1 
                      C: Resultado de integral con grafica de MonteCarlo
                      Seleccione una opcion: """)

    if choice == "A" or choice =="a":
        I = quad(integrand, float(- math.inf), float(math.inf))
        print(I)
    elif choice == "B" or choice =="b":
        Integral = quad(integrand, 0, 1)
        print(Integral)
    elif choice == "C" or choice =="c":
        print("Resultado de MonteCarlo")
    else:
        print("Debes seleccionar A, B o C")
        print("Vuelvelo a intentar")
        menu()

menu()
