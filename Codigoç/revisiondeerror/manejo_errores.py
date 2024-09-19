from datetime import datetime

def leerfecha(msg):
    while True:
        try:
            fecha= datetime.strptime(input(msg), "%d/%m/%Y")
            ano, mes, dia=str(fecha).split()[0].split("-")
            return f"{dia}/{mes}/{ano}"
        except ValueError:
            print("Error. Formato de fecha inválido")



def leerFloat(msg):
    while True:
        try: 
            num=float(input(msg))
            return num
        except ValueError:
            print("Error. ingrese un numero decimal valido.\n")

def leerEnteroPositivo(msg):
    while True:
        try:
            num = int(input(msg))
            if num < 0:
                print("Error, ingrese un número postivo.\n")
                continue
            return num  
        except ValueError:
            print("Error. ingrese un numero entero valido.\n")
           

def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print("Error. ingrese un numero entero valido.\n")
    return num     

#___________________________________________________________________
edad = leerEnteroPositivo("Ingrese la edad: ")
print(edad,"",type(edad))



temperatura = leerFloat("Ingrese la temperatura: ")
print(temperatura,"",type(temperatura))


fecnac=leerfecha("Ingrese la fecha de nacimiento: ")
print(fecnac)