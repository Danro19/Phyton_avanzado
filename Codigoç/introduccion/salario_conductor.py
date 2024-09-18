Nombre=input("Ingrese el nombre del trabajador: \n ")
salario = int(input("ingrese el salario del trabajador: \n"))


aux = 0

if salario > 1_200_000:
    aux = 120_000

print("el Salario de ", Nombre, "es", salario)
print(f"El auxiolo de transporte es de {aux:,}")    