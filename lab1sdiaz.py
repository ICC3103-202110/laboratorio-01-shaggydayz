# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:08:34 2021

@author: santi
"""
from random import sample

def generar_mazo(n):
    l = []
    for i in range(n):
        l.append(i+1)
        l.append(i+1)
    return l

def armar_tablero_aleatorio(lista,numero):
    l = lista
    n = numero
    k = []
    k1 = sample(l,n)
    for i in range(len(k1)):
        l.remove(k1[i])
    k2 = sample(l,n)
    k.append(k1)
    k.append(k2)
    return k

def imprimir_tablero(mazo,vez,coordx,coordy,coordx1,coordy1):
    carta1 = mazo[coordx][coordy]
    carta2 = mazo[coordx1][coordy1]
    n = len(mazo[0])
    if vez == 0:
        for i in range(n):
            for j in range(2):
                if j == 0:
                    if mazo[j][i] != " ":
                        print("("+str(j)+","+str(i)+") "+"*", end="  ")
                    else:
                        print("("+str(j)+","+str(i)+") "+" ", end="  ")
                else:
                    if mazo[j][i] != " ":
                        print("*"+" ("+str(j)+","+str(i)+") ", end="  ")
                    else:
                        print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
            print(" ")
    elif vez == 1:
        for i in range(n):
            for j in range(2):
                if coordx == j and coordy == i:
                    if j == 0:
                        if mazo[j][i] != " ":
                            print("("+str(j)+","+str(i)+") "+str(carta1), end="  ")
                        else:
                            print("("+str(j)+","+str(i)+") "+" ", end="  ")
                    else:
                        if mazo[j][i] != " ":
                            print(str(carta1)+" ("+str(j)+","+str(i)+") ", end="  ")
                        else:
                            print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
                else:
                    if j == 0:
                        if mazo[j][i] != " ":
                            print("("+str(j)+","+str(i)+") "+"*", end="  ")
                        else:
                            print("("+str(j)+","+str(i)+") "+" ", end="  ")
                    else:
                        if mazo[j][i] != " ":
                            print("*"+" ("+str(j)+","+str(i)+") ", end="  ")
                        else:
                            print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
            print(" ")
    else:
        for i in range(n):
            for j in range(2):
                if coordx == j and coordy == i:
                    if j == 0:
                        if mazo[j][i] != " ":
                            print("("+str(j)+","+str(i)+") "+str(carta1), end="  ")
                        else:
                            print("("+str(j)+","+str(i)+") "+" ", end="  ")
                    else:
                        if mazo[j][i] != " ":
                            print(str(carta1)+" ("+str(j)+","+str(i)+") ", end="  ")
                        else:
                            print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
                elif coordx1 == j and coordy1 == i:
                    if j == 0:
                        if mazo[j][i] != " ":
                            print("("+str(j)+","+str(i)+") "+str(carta2), end="  ")
                        else:
                            print("("+str(j)+","+str(i)+") "+" ", end="  ")
                    else:
                        if mazo[j][i] != " ":
                            print(str(carta2)+" ("+str(j)+","+str(i)+") ", end="  ")
                        else:
                            print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
                else:
                    if j == 0:
                        if mazo[j][i] != " ":
                            print("("+str(j)+","+str(i)+") "+"*", end="  ")
                        else:
                            print("("+str(j)+","+str(i)+") "+" ", end="  ")
                    else:
                        if mazo[j][i] != " ":
                            print("*"+" ("+str(j)+","+str(i)+") ", end="  ")
                        else:
                            print(" "+" ("+str(j)+","+str(i)+") ", end="  ")
            print(" ")
    return carta1,carta2

def eliminar_carta(l,carta):
    p = []
    q = []
    for i in l:
        for j in i:
            if j == carta:
                p.append(" ")
            else:
                p.append(j)
        q.append(p)
        p = []
    return q
#print(q)

ncartas = int(input("¿Cuantas cartas quiere poner en juego?: "))
mazo = generar_mazo(ncartas)
k = armar_tablero_aleatorio(mazo, ncartas)
ptje_J1 = 0
ptje_J2 = 0
turno = 2
print(k)

while(ncartas != 0):
    if turno%2 == 0:
        carta1 = 0
        carta2 = 1
        print("----------------------------------")
        print("Puntaje J1: "+str(ptje_J1))
        print("Puntaje J2: "+str(ptje_J2))
        print("----------------------------------")
        imprimir_tablero(k,0,1,1,1,1)
        print("")
        print("Juega J1")
        cx = int(input("Ingrese coord x primera carta: "))
        cy = int(input("Ingrese coord y primera carta: "))
        carta1,c = imprimir_tablero(k,1,cx,cy,1,1) 
        cx1 = int(input("Ingrese coord x segunda carta: "))
        cy1 = int(input("Ingrese coord y segunda carta: "))
        c,carta2 = imprimir_tablero(k,2,cx,cy,cx1,cy1)
        if carta1 == carta2:
            ptje_J1 = ptje_J1 + 1
            ncartas = ncartas - 1
            k = eliminar_carta(k, carta1)
            turno = 2
        else:
            turno = turno + 1
    elif turno%2 != 0:
        print("----------------------------------")
        print("Puntaje J1: "+str(ptje_J1))
        print("Puntaje J2: "+str(ptje_J2))
        print("----------------------------------")
        carta1 = 0
        carta2 = 1
        print("Juega J2")
        imprimir_tablero(k,0,1,1,1,1)
        cx = int(input("Ingrese coord x primera carta: "))
        cy = int(input("Ingrese coord y primera carta: "))
        carta1,c = imprimir_tablero(k,1,cx,cy,1,1) 
        cx1 = int(input("Ingrese coord x segunda carta: "))
        cy1 = int(input("Ingrese coord y segunda carta: "))
        c,carta2 = imprimir_tablero(k,2,cx,cy,cx1,cy1)
        if carta1 == carta2:
            ptje_J2 = ptje_J2 + 1
            ncartas = ncartas - 1
            k = eliminar_carta(k, carta1)
            turno = 3
        else:
            turno = turno + 1
    if ncartas == 0:
        break

if ptje_J1 < ptje_J2:
    print("Fin del juego: J2 gana")
elif ptje_J1 > ptje_J2:
    print("Fin del juego: J1 gana")
else:
    print("Fin del juego: Empate")