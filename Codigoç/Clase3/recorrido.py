#Recorrido de cadenas

#1. por sus elementos
s = "Voy volando..."
for c in s:
    print(c)

#Ejemplo: cuantas vocales hay en la cadena
vocales = 0
for c in s:
    if c=="a" or c == "A" or\
        c == "e" or c == "E" or \
        c=="i" or c=="I" or\
        c=="o" or c=="O" or \
        c=="u" or c=="U":
        vocales+=1
print ("Cantidad de vocales: ", vocales)







vocales=0
print("="*120)




# 2. por su INDICE
for i in range(len(s)):
    print(s[i])
for i in range(len(s)):
    if s[i]=="a" or s[i] == "A" or\
        s[i] == "e" or s[i] == "E" or \
        s[i]=="i" or s[i]=="I" or\
        s[i]=="o" or s[i]=="O" or \
        s[i]=="u" or s[i]=="U":
        vocales+=1
print ("Cantidad de vocales: ", vocales) 


#ejemplo: en que posición esta el primer espacio
for i in range(len(s)):
    if s[i]==" ":
        break
print("El primer espacio se encuentra en la posicion ", i) 