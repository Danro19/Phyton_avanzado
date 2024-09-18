cantidadSegundos=(float(input("Ingrese la cantidad de segundos: ")))

minutos=cantidadSegundos//60
horas=minutos//60
minutosFinal = minutos % 60
segundosFinal= cantidadSegundos%60

restaMinutos=minutos 
print("las horas son: ", horas, "los minutos son: ", minutosFinal, "los segundos son: ", segundosFinal)