
fd = open ("datos txt/data.txt","r")

cad=fd.readlines()#trae una lista de cadenas, con su respectivo "\n" cada elemento es una linea del archivo
print(cad)

fd.close()

