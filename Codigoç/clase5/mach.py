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
        letra.lower() == "a"
        match letra:
            case "a" :
                lstvocales[0] +=1
            case "e" :
                lstvocales[1] +=1
            case "i" :
                lstvocales[2] +=1
            case "o" :
                lstvocales[3] +=1
            case "u" :
                lstvocales[4] +=1
            case _:
                pass

imprimeLista(lstvocales)   