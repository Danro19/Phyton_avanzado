# Escriba un programa que envie un mensaje "Vota por mi mascota" a todos los correos que aparecen en el From:
#Su programa debe mostrar un mensaje como el siguiente por cada correo:
#cwen@uipi.edu --> "Vota por mi mascota" :::> [CORREO ENVIADO]


fd=open("datos txt/mbox.txt","r")


email= set()
for linea in fd:
    if linea.startswith("From: "):
        correo= linea.split()[1]
        if correo not in email:
            print(correo," -->Vota por mi mascota :::> [CORREO ENVIADO]") 
            email.add(correo)       


fd.close