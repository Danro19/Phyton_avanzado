#ingrese el numero de palabras
#ingrese el prefijo
#ingrese las palabras

np=int(input("Ingrese el numero de palabras: "))

pref=(input("Ingrese el prefijo: "))


cpre=0
for i in range(np):
    pal = input("palabra: ")

    if pal.startswith(pref) == True:
        cpre+=1
print(cpre)        