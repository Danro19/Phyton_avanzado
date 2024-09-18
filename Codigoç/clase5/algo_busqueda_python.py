lista = ["Carlos", "Daniel", "Maria", "Laia", "Angel", "Oscar"]

nombre="Oscar"
if nombre in lista:
    pos = lista.index(nombre)  
    print("Pasa al ciclo3")
    print("Posicion en la lista: ", pos)
else:
    print("Gracias por participar en python")