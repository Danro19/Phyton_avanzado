
with open("datos txt/mbox.txt", "r") as fd:

    lstEmail= []
    for linea in fd:
        if linea.startswith("From:"):
            correo= linea.split()[1]+ " enviado [ok]\n"
            if correo not in lstEmail:
                lstEmail.append(correo)

lstEmail2 = lstEmail[::-1]


with open("datos txt/correos_enviados.txt", "w") as fd:
    fd.writelines(lstEmail2)