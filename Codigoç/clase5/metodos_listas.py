#append añade al final

lista= [10, 20, "Juan", 30, "Sergio"]
lista.append(40)
print(lista)

lista2 = ["Maria", 20]
lista.append(lista2)#Se añade como lista, cuando se agrega una lista
print(lista)
#extend:
lista.extend(lista2) #Se añade como elemento lo de la otra lista
print(lista)

#Insert: inserta un elemento en N posicion decidida por el programado
lista.insert(2, 50)
print(lista)

#pop: borra el item de la poscision que el programador decida y si se deja en vacio borra el ultimo valor

lista.pop(2)
print(lista)

#remove borra el elemento(item) sin tener en cuenta la poscision, solo el nombre del item
lista.remove("Sergio")
print(lista)




lista = [40, 30, 5, 90, 20]

#min imprime el menor numero
print(min(lista))

#max imprime el numero mayor de la lista
print(max(lista))

#len imprime la longitud de la lista 
print("Tamaño lista: ", len(lista))

#sorted ordena e imprime de menor a mayor
print(sorted(lista))

#sorted(lista, reverse=True) ordena e imprime de mayor a menor
print(sorted(lista, reverse=True))

lista = [40, 30, 5, 90, 20, 1, 20, 50, 60, 20]

#Count imprime el numero de veces que n caracter aparece en la lista
print(lista.count(20))

#del borrar de la lista un elemento teniendo en cuenta la poscision
del(lista[3])
print(lista)

#limpiar listas 
#Clear, borra todos los elementos y deja la lista vacia
lista.clear()
print(lista)
print(type(lista))