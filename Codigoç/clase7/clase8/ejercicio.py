#se debe estipular N productos input
#se debe hacer 2 diccionarios, precio y articulo
#se debe imprimir la cantidad del articulo, el nombre, el valor total, valor unitario

articulos={1:"Lapiz", 2:"Cuadernos", 3:"borrador", 4:"Calculadora", 5:"Escuadra"}
valores={1:25000, 2:3800, 3:1200, 4:35000, 5:3700}

compratotad={}
suma=0
compra=0
iNarticulo=int(input("Ingrese el articulo que desea (1:Lapiz, 2:Cuaderno, 3:Borrador, 4:Calculadora, 5:Escuadra, 6:Terminar): "))
while iNarticulo != 6:
    articuloc={}
    articuloc["cantidad"]=int(input("Ingrese la cantidad del articulo: "))    
    if iNarticulo == 1:
        compra=articuloc["cantidad"]*valores[1]
        compratotad["lapiz"]=articuloc

        
    elif iNarticulo == 2:
        compra=articuloc["cantidad"]*valores[2]
        compratotad["cuaderno"]=articuloc 

    elif iNarticulo == 3:  
        compra=articuloc["cantidad"]*valores[3]
        compratotad["borrador"]=articuloc

    elif iNarticulo == 4:
        compra=articuloc["cantidad"]*valores[4]
        compratotad["calculadora"]=articuloc

    elif iNarticulo == 5:
        compra=articuloc["cantidad"]*valores[5] 
        compratotad["escuadra"]=articuloc
    
    suma+=compra

    

    iNarticulo=int(input("Ingrese el articulo que desea (1:Lapiz, 2:Cuaderno, 3:Borrador, 4:Calculadora, 5:Escuadra, 6:Terminar  )"))     
