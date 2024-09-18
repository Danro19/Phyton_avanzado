
usuarios=print("Ingrese la cantidad de usuarios")
suma=0

for i in range(1,usuarios):

    codigo=print("Ingrese el codigo de la factura: \n")
    nombre=print("Ingrese el nombre del usuario: \n")
    estado=print("Ingrese el estado de su servicio: Vigente(V o v) o Suspendido(S o s): \n")
    estrato=int(print("Ingrese el estrato de la vivienda:\n"))
    consumo=int(print("Ingrese el Consumo del mes: \n"))
    if estado=="V" or estado=="v":
        tarifa1=10000
        tarifa2=20000
        tarifa3=30000
        tarifa4=40000
        tarifa5=50000
        tarifa6=60000
        tarifa7=70000
        consumo1=200
        valorc=0
        estado="Vigente"
        if estrato==1: 
            valorc=(consumo1*consumo)+tarifa1
           
        elif estrato==2:
            valorc=(consumo1*consumo)+tarifa2
          
        elif estrato==3:
            valorc=(consumo1*consumo)+tarifa3
           

        elif estrato==4:
            valorc=(consumo1*consumo)+tarifa4
        

        elif estrato==5:
            valorc=(consumo1*consumo)+tarifa5
           

        elif estrato==6:
            valorc=(consumo1*consumo)+tarifa6
          

        elif estrato==7:
            valorc=(consumo1*consumo)+tarifa7
           
    else:
            print("El servicio esta Suspendido")
    suma+=valorc

    print("Codigo: ", codigo)
    print("Nombre: ", nombre)
    print("Estado del Servicio: ", estado)
    print("Valor a pagar: ", valorc)
print("El valor total de todas las facturas es: ", suma)