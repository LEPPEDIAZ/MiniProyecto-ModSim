import numpy as np
from scipy.integrate import quad
import math
import matplotlib.pyplot as plt
import pandas as pd


def integrand(x):
    return np.exp(-x ** 2)

#10,000 iteraciones
def integrate(x1,x2,func=integrand,n=10000):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)
#100 iteraciones
def integrate2(x1,x2,func=integrand,n=100):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)
#1,000,000 de iteraciones
def integrate3(x1,x2,func=integrand,n=1000000):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)
def menu():
    print("************Ejercicio 4**************")
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
        iteraciones = input("""
                      1: 100
                      2: 10000
                      3: 1000000
                      Seleccione una opcion: """)
        if iteraciones == "1":
            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.show()
            print("resultado : ", integrate2(0,1)[0])
            TrueIntegral = quad(integrand, 0, 1)
            print("resultado fijo :", TrueIntegral)
            #define cuantos puntos va a tener
            _,x,y,c=integrate2(0,1,n=100)
            df=pd.DataFrame()
            df['x']=x
            df['y']=y
            df['c']=c

            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.scatter(df[df['c']==0]['x'],df[df['c']==0]['y'],color='red')
            plt.scatter(df[df['c']==1]['x'],df[df['c']==1]['y'],color='blue')
            plt.show()
            
        elif choice == "B":
            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.show()
            print("resultado : ", integrate(0,1)[0])
            TrueIntegral = quad(integrand, 0, 1)
            print("resultado fijo :", TrueIntegral)
            #define cuantos puntos va a tener
            _,x,y,c=integrate(0,1,n=100)
            df=pd.DataFrame()
            df['x']=x
            df['y']=y
            df['c']=c

            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.scatter(df[df['c']==0]['x'],df[df['c']==0]['y'],color='red')
            plt.scatter(df[df['c']==1]['x'],df[df['c']==1]['y'],color='blue')
            plt.show()
            
        elif choice == "C" or choice =="c":
            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.show()
            print("resultado : ", integrate3(0,1)[0])
            TrueIntegral = quad(integrand, 0, 1)
            print("resultado fijo :", TrueIntegral)
            #define cuantos puntos va a tener
            _,x,y,c=integrate3(0,1,n=100)
            df=pd.DataFrame()
            df['x']=x
            df['y']=y
            df['c']=c

            X=np.linspace(0,1,100)
            plt.plot(X,integrand(X))
            plt.scatter(df[df['c']==0]['x'],df[df['c']==0]['y'],color='red')
            plt.scatter(df[df['c']==1]['x'],df[df['c']==1]['y'],color='blue')
            plt.show()
        else:
            print("Debes seleccionar A, B o C")
            print("Vuelvelo a intentar")
        
    else:
        print("Debes seleccionar A, B o C")
        print("Vuelvelo a intentar")
        menu()

menu()
