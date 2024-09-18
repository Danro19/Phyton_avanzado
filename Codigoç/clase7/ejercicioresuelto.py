def Notafinal(n1,n2,n3):
    Notafinal=n1+n2+n3
    return Notafinal

def aprob_reprob(n1):
    if n1 > 3 or 3==n1:
        print("Aprobado")
    else:
        print("Reprobo")


   
dNotasP={1:0.30, 2:0.30, 3:0.40}

n=int(input("Ingrese la cantidad de estudiantes: "))

estudiantes={}

for i in range(n):
    print(f"Estudiante {i+1} ")
    codigo = input("Codigo ")
    if codigo != 999:
        dDatos = {}
        dNotas={}
        dDatos["nombre"]=input("Nombre? ")
        #
        dDatos["Nota_1"] = float(input("Ingrese la nota 1 (La nota va de 1.0 a 5.0)"))
        dNotas["Nota1"] = dDatos["Nota_1"]*dNotasP[1]
        #
        dDatos["Nota_2"] = float(input("Ingrese la nota 2 (La nota va de 1.0 a 5.0)"))
        dNotas["Nota2"]= dDatos["Nota_2"]*dNotasP[2]
        #
        dDatos["Nota_3"] = float(input("Ingrese la nota 3 (La nota va de 1.0 a 5.0)"))
        dNotas["Nota3"]= dDatos["Nota_3"]*dNotasP[3]
        #
        
        
        Notafinal1=Notafinal(dNotas["Nota1"],dNotas["Nota2"],dNotas["Nota3"])

        
        estudiantes[codigo]=dDatos 
        print("")
        print("="*30)
        print(dDatos["nombre"])
        print("La nota final del estudiante es:", Notafinal1)
        aprob_reprob(Notafinal1)
        print("="*30) 
        print("")  
    else:
        break