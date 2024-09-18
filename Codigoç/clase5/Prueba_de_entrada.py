#Algoritmo que duplique los "n" datos ingrezados

def duplicar(lst):
    lrta = []
    for e in lst:
        lrta.append(e * 2)

    return lrta    


n = int(input("Ingrese la cantidad de datos: "))
lstNumeros = []
for i in range(n):
    lstNumeros.append(int(input(f"Ingrese el dato #{i+1}: ")))

print(duplicar(lstNumeros))