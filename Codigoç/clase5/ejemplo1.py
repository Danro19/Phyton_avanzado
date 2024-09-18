from re import I


def sumalista(lst):
    suma = 0
    for e in lst:
        suma += e
    return suma

def imprimeLista(lst):
    for e in lst:
        print(e, end=" | ")
print("")

def mayorLista(lst):
    mayor = lst[0]
    for e in lst:
        if e in lst:
            if e>mayor:
                mayor = e
    return mayor

def menorLista(lst):
    menor=lst[0]
    for e in lst:
        if e in lst:
            if e < menor:
                menor = e
    return menor

def posMayList(lst):
    mayor = lst[0]
    pos=0
    for i in range(len(lst)):
        if lst[i] in lst:
            if e>mayor:
                mayor = lst[i]
                pos= i
    return pos

def posElemMayList(lst):
    mayor = lst[0]
    pos=0
    for i in range(len(lst)):
        if lst[i] in lst:
            if e>mayor:
                mayor = lst[i]
                pos= i
    return [pos, mayor]

lista_numeros = [10, 15, 20, 30, 40]
print(type(lista_numeros))
print(lista_numeros)
print(lista_numeros[3])
print(lista_numeros[-1])
print(lista_numeros[-5])


#Recorre una lista
#1. por sus posiciones
for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=", ")
print("")


for i in range(-1, -len(lista_numeros)-1, -1):
    print(lista_numeros[i], end="* ")
print("")
for i in range(len(lista_numeros)-1,-1, -1):
    print(lista_numeros[i], end="; ")
print("\n" + "-" * 30)

#2. por sus elementos
for e in lista_numeros:
    print(e, end="| ")
print("")

# Llamado a una funció. Se le pasa la lista
imprimeLista(lista_numeros)

#Funcion que devuelve la suma de los elementos de lista
print("La suma de los elementos de la lista es: ", sumalista(lista_numeros))

# Imprimir el mayor elemento de lista
print("El mayor elemento es: ", mayorLista(lista_numeros))
#imprimir el menor de la lista
print("El menor elemento es: ", menorLista(lista_numeros))

#Imprimir la posicion del elemento mayor de la lista
print("El elemento mayor se encuentra en la posicion: ", posMayList(lista_numeros) + 1)

result=posElemMayList(lista_numeros)
print("El lemento mayor y su posicion es: ", result[1], result[0]+1)

#Modificar una lista
#lista_numeros = [10, 15, 20, 30, 40]
lista_numeros[-1]=35 #lista_numero[4] = 35

#operadores de las listas 
lista_numeros2=[1, 2]

#operador de concatenacion
lstrlst=lista_numeros+lista_numeros2
print(lstrlst)

#operador (*)
lstrlst=lista_numeros2 * 3
print(lstrlst)