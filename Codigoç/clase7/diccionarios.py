#Metodos

dCampers = {1:"Ada", 2:"Juan", 3:"Diego", 4:"Oscar", 5:"Anderson"}
print(dCampers)

#crear un diccionario vacio
#dCampers={}#esto es un diccionario vacio
#dCampers= dict()


print(dCampers.setdefault(4)) #Existe la llave

print(dCampers.setdefault(6, "Maria")) #en caso de que no existe, devuelve none, pero se le puede añadir un nuevo valor,en el orden llave y elemento 
print(dCampers)