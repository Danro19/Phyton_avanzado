import io

fd = open ("datos txt/data.txt","r")

cad=fd.read()
print(cad)



fd.seek(0)#ubica el cursor
cad = fd.read(5) #cantidad de bytes (caracteres)
print(cad)


fd.close()