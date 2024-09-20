import random



"""
mat(2,3)

# Column 0    1     2
mat=[ [None, None, None], # fila 0
      [None, None, None]  # fila 1 
      ] 

"""

def crearMat(fil,col):  #funcion de crear matriz
    matriz = []
    for f in range(fil): #recorrer la cantidad de filas
        matriz.append([None]*col)
    return matriz


def printMat(mat): #imprime la matriz
    for f in range(len(mat)): #devuelve el tamaño de la lista de filas
        for c in range(len(mat[f])):
            print(mat[f][c], end="\t")
        print("")    

def inputMatriz(mat): #Pedir que llene la matriz
    for f in range (len(mat)):
        print("Fila", f+1)
        for c in range (len(mat[f])):
            mat[f][c] = int(input(f"mat[{f+1}][{c+1}]? "))

        print ("_"* 10, "\n")

def randomMatriz(mat, ini, fin):
    for f in range (len(mat)):
    
        for c in range (len(mat[f])):
            mat[f][c] = random.randrange(ini,fin)
        print ("_"* 10, "\n")

def matrizIdentidad(mat,):
    tamf = len(mat)
    tamc = len(mat[0])
    if tamf== tamc:
        for f in range (tamf):
            for c in range (tamc):
                if f != c:
                    mat[f][c] = 0
                else:
                    mat[f][c]=1  
        print ("_"* 10, "\n")             
        return mat      
    else:
        return None                       
    
