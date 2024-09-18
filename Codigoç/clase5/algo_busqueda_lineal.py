def busquedaLineal(lst, elem):
    for i in range(len(lst)):
        if lst[i]==elem:
            return [True, i]
    return [False, None]

lista = ["Carlos", "Daniel", "Maria", "Laia", "Angel", "Oscar"]

existe, pos = busquedaLineal(lista, "Oscar")

if existe :
    print("Pasa al ciclo 3")
    print("Posicion: ", pos)
else:
    print("Muchas Gracias por estar en Campus")