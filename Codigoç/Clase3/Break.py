#Instruccion BREAK
#Break: Rommper o terminar forzosamente el ciclo mas cercano
#sumar los numeros del 1 al 50
suma=0
for i in range(1, 51):
    suma += i #   es equivalente a suma = suma + i
    if i == 20:
        break
print(suma)