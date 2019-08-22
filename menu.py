
import os
import sys
ejercicio1 = "python Ejercicio1a.py"
ejercicio2 = "python Ejercicio2.py"
ejercicio3 = "python Ejercicio4.py"
ejercicio4 = "python ejercicio5.py"
ejercicio5 = "python Ejercicio5-1.py"

def main():
    menu()

def menu():
    print()
    print("************MINI PROYECTO MODSIM**************")
    print()

    opcion = input("""
                    Ingrese la letra de la Opcion requerida:
                      A: Ejercicio1
                      B: Ejercicio2
                      C: Ejercicio4
                      D: Ejercicio5 (Pablo)
                      H: Ejercicio5 (Ana)
                      *El ejercicio 3 no se encuentra dentro del menu pero si esta incluido
                      Q: Salir
                    """)
    if opcion == "A" or opcion == "a":
        os.system(ejercicio1)
    elif opcion == "B" or opcion == "b":
        os.system(ejercicio2)
    elif opcion == "C" or opcion == "c":
        os.system(ejercicio3)
    elif opcion == "D" or opcion == "d":
        os.system(ejercicio4)
    elif opcion == "H" or opcion == "h":
        os.system(ejercicio5)
    elif opcion == "Q" or opcion == "q":
        sys.exit
    else:
        print("Seleccione una opcion existente")
        print("Vuelva a intentarlo!")
        menu()





main()