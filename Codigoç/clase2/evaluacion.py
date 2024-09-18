nombre=input("Ingrese el nombre del estudiante \n")
calificacion=float(input("Ingrese el valor de la calificacion cuantitativa \n"))
cali=""
if calificacion>=0 and calificacion<60:
    cali = "D"
elif calificacion>=60 and calificacion<80:
    cali="C"
elif calificacion>=80 and calificacion<90:
    cali="B"
elif calificacion >= 90 and calificacion <= 100:
    cali="A"
else:
    cali = ""

if  cali !="":
    print("\n-----------------------")
    print("nombre: ", nombre)
    print(f"Calificiación cuantitativa; {calificacion:.1f}")
    print("Calificación cualitativa ", cali)
else:
    print(">>Error. Calificación inválida.")
    