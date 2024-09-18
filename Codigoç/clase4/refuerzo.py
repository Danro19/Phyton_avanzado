#10 personas consultar la edad 
#sumaedades=0
#mayores=0
# for i in range(0,11)
#  if edad < 18
#  mayores+=1
#sumaedades+=edad
#promedio= sumaedades/cantidad de personas (10)


sumaEdad=0
mayores=0
cp=10
for i in range(0,10):
    edad=int(input("Ingrese la edad: "))
    if edad >= 18: 
        mayores+=1
    sumaEdad+=edad
promedio=sumaEdad/cp           
print("El promedio de edad es: ", promedio)
print("La cantidad de personas que son mayores de edad es: ",mayores)

