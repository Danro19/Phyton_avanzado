#dado la base y la altura de un triangulo, calcular y mostrar su area, a través
#de la fórmula área = (base*altura)/2
base = float(input("Introduzca la base del triangulo "))
altura = float(input("Introduzca la altura del triangulo "))

resultado = base * altura / 2
#formateando la salida con format()
print ("El Área del triangulo es: {:.1f}".format(resultado))


#formateando la salida con cadenas f-string
print(f"el área del tríangulo es: {resultado:.1f}")
#ENTADA
#b:base 
#h:altura
#PROCESO 
#a = b * h / 2
#SALIDA
#a:area