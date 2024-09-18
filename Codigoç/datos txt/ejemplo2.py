import io

fd = open ("datos txt/data.txt","r")

cad=fd.readline().strip()#strip quita el ultimo caractere \n  
print(cad)


cad=fd.readline()#lee por lineas hasta el cambio de linea \n
print(cad)




