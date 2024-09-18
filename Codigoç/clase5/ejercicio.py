#CONTADOR DE VOCALES
def imprimeLista(lst):
    for e in lst:
        print(e, end=" | ")
print("")


n=int(input("cuantas letras va a ingresar: "))

lstvocales = [0, 0, 0, 0, 0] # [0] * 5

for i in range(n):
    letra=input(f"Ingrese la letra {i+1}: ")

    if len(letra.strip()) >0:
        if letra.lower() == "a":
            lstvocales[0]+= 1
        elif letra.lower() == "e":
            lstvocales [1]+= 1
        elif letra.lower() == "i":
            lstvocales [2]+= 1
        elif letra.lower() == "o":
            lstvocales [3]+= 1
        elif letra.lower() == "u":
            lstvocales [4]+= 1

imprimeLista(lstvocales)        
    
    
    

