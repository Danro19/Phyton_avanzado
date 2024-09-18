#pedir al usuario numeros hasta que la suma sea 1000 
#multiplo de 6
#suma de los numeros que se encuentren entre 1 y 10
#input n 
#suman=0
#multiplo6= 0
#while n <1000
    #suman+=n
    #if n%6=0
        #multplo6+=1

sn=0
m6=0
n1=0
while sn <1000:
    n=int(input("Ingrese un número:\n"))
    sn+=n
    if n%6==0:
        m6+=1
    print("La suma va en: ",sn)
    print("La cantidad de multiplos de 6 son: ", m6 )    
    for i in range(0,11):
        n1+=i

    if n1<56:
        print("la suma de los numeros de 1 a 10 son: ", n1)
