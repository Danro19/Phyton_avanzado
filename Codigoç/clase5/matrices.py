
def ingresarDatosMat(mat):
    for f in range(len(mat)):
        print(f"Ingrese datos de la fila {f}")
        for c in range(len(mat[f])):
            mat[f][c]=int(input(f"mat[{f+1}][{c+1}]? "))
    

def creaMatriz(fil, col):
    m=[]
    for f in range (fil):
        m.append([None]* col)
    return m

def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end="\t")
        print("")    


m = [[1, 2, 3] , #Fila 0
[4, 5, 6]] #Fila 1
        #2x3
print(m[0])

print(m[1][1])


mat=[]
mat = creaMatriz(3, 5)


# mat[2][2]=15
# imprimirMat(mat)

ingresarDatosMat(mat)
imprimirMat(mat)



#m = [None, None, None, None, None],
#[None, None, None, None, None],
#[None, None, None, None, None] 