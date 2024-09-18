n1=int(input("Ingrese el primer numero entero \n"))
n2=int(input("Ingrese el primer segundo entero \n"))
n3=int(input("Ingrese el primer tercer entero \n"))

if n1>n2 and n2>n3:
    print(n1,"",n2,"",n3)
elif n1<n2 and n2<n3:
    print(n3,"",n2,"",n1)
elif n1>n2 and n1>n3 and n2<n3:
    print(n1, "", n3, "", n2)
elif n1<n2 and n2>n3 and n1>n3:
    print (n2,"",n1,"",n3)
elif n1<n2 and n2>n3 and n1<n3:
    print (n2,"",n3,"",n1)
else:
    print(n3, "", n1,"", n2)