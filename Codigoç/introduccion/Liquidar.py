#numero de placa nombre, valor de los pasajes 25% valor de las encomiendas 15%
nombre = str(input("Ingrese el Nombre del conductor "))
placa = str(input("Ingrese el numero de placa del vehículo "))
valorPasajes = int(input("Ingrese la totalidad del dinero de los pasajes en pesos "))
valorEncomiendas = int(input("Ingrese la totalidad del dinero de las encomiendas en pesos "))

valor1C=valorPasajes*0.25
valor2C=valorEncomiendas*0.15
valorTotal=valor1C+valor2C
print("El conductor ", nombre)
print("Numero de placa ", placa)
print(f"El valor total de los pasajes es: $ {valorPasajes:,.0f}", f"El concepto a pagar a favor del conductor es: $ {valor1C:,.0f}")
print(f"El valor total de las encomiendas es: $ {valorEncomiendas:,.0f}", f"El concepto a pagar a favor del conductor es: $ {valor2C:,.0f}")
print(f"El total a pagar al conductor es: ${valorTotal:,.0f}" )