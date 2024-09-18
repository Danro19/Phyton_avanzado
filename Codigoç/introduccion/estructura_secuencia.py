#Sobre un estudiante conocemos las calificaciones parciales
#obtenidas en los retos, nota reto1, nota reto2, 
# nota reto 3 y nota de ingles y el nombre del estudiante. 
# Si los porcentajes para cada reto e ingles son 20%, 25%, 35% y 20%
# respectivamente, calcular su calificaicon definitiva e imprimirla, 
# ademas del nombre
nombre=str(input("Ingrese el nombre del estudiante "))
nota1=float(input("ingrese la calificacion del reto1 "))
nota2=float(input("ingrese la calificacion del reto2 "))
nota3=float(input("ingrese la calificacion del reto3 "))
ingles=float(input("ingrese la calificacion del reto1 "))

notap1=nota1/100*20
notap2=nota2/100*25
notap3=nota3/100*35
inglesp=ingles/100*20
notaP=notap1+notap2+notap3+inglesp
print("La calificacion definitiva de", nombre, f"es:  {notaP:.1}")