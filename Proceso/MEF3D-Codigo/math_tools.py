import math


def row(tam,value):
    v=[]
    for i in range(0,tam):
        v.append(value)
    return v

#Matriz de ceros
def zeroesM(matrix,n):
    for i in range(0,n):
        matrix.append(row(n, 0.0))

#Matriz de ceros N*M
def zeroesNM(matrix,n,m):
    for i in range(0,n):
        matrix.append(row(m, 0.0))


#Vector de ceros
def zeroesV(vector,n):
    for i in range(0,n):
        vector.append(0.0)

#Copiar Matriz
def copyMatrix(MatrixA,MatrixC):

    zeroesM(MatrixC, len(MatrixA))

    for i in range(0,len(MatrixA)):
        for j in range(0,len(MatrixA[0])):
            MatrixC[i][j]=MatrixA[i][j]

#Matriz Identidad
def identityMatrix(n,MatrixI):
    zeroesM(MatrixI,n)
    for i in range(n):
        MatrixI[i][i] = 1.0


def calculateMember(i,j,r,MatrixA,MatrixB):
    member = 0
    for k in range(0,r):
        member += MatrixA[i][k]*MatrixB[k][j]
    return member


def productMatrixMatrix(MatrixA,MatrixB, n, r, m):
    R = []
    zeroesM(R,n,m)
    for i in range(0,n):
        for j in range(0,m):
            R[i][j] = calculateMember(i,j,r,MatrixA,MatrixB)
    return R


def productMatrixVector(MatrixA,VectorV,VectorR):
    zeroesV(VectorR,len(MatrixA))
    for f in range(0,len(MatrixA)):
        cell = 0.0
        for c in range(0,len(VectorV)):
            cell+= MatrixA[f][c]*VectorV[c]    
        VectorR[f] += cell
    

def productRealMatrix(real,MatrixM,MatrixR):
    zeroesNM(MatrixR, len(MatrixM),len(MatrixM[0]))
    for i in  range(0,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            MatrixR[i][j]=real*MatrixM[i][j]


def getMinor(MatrixM,i,j):
    #eliminar fila
    #MatrixM[i].clear()
    MatrixM.pop(i)
    #eliminar columna
    for c in range(0,len(MatrixM)):
        MatrixM[c].pop(j)


def determinant(MatrixM):
    if(len(MatrixM)==1):
        return MatrixM[0][0]
    else:
        det=0.0
        for i in range(0,len(MatrixM[0])):
            minor = []
            copyMatrix(MatrixM, minor)
            getMinor(minor, 0, i)

            det += (-1**i)*MatrixM[0][i]*determinant(minor)
        return det


def cofactors(MatrixM,MatrixCof):
    zeroesM(MatrixCof, len(MatrixM))

    for i in range(0,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            minor=[]

            copyMatrix(MatrixM, minor)
            getMinor(minor, i, j)

            MatrixCof[i][j] = (-1**(i+j))*determinant(minor)



def transpose(MatrixM,MatrixT):
    zeroesNM(MatrixT, len(MatrixM[0]),len(MatrixM))
    for i in range(0,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            MatrixT[j][i]=MatrixM[i][j]


#Metood incontrado en internet que lo hace mas rapido
def inverseMatrix(M,IM):
    n = len(M)
    AM = []
    I = []
    copyMatrix(M,AM)
    identityMatrix(n,I)
    copyMatrix(I,IM)
    indices = list(range(n))
    for fd in range(n):
        print(fd)
        if(AM[fd][fd] == 0):
            fdScaler = 1/0.00000000000000001
        else:
            fdScaler = 1.0/AM[fd][fd]

        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        
        for i in indices[0:fd] + indices[fd+1:]:
            crScaler = AM[i][fd]
            for p in range(n):
                AM[i][p] = AM[i][p] - crScaler*AM[fd][p]
                IM[i][p] = IM[i][p] - crScaler*IM[fd][p]


#Tarda Horas mas de 20h ya lleva 1d y 5h para las 10:13 de 6 de julio
#def inverseMatrix(MatrixM,MatrixInv):
#    print("Iniciando calculo de inversa...\n")
#    cof = []
#    adj = []
#    print("Calculo de determinante...\n")
#    det = determinant(MatrixM)
#    if(det==0): exit()
#    print("Iniciando calculo de cofactores...\n")
#    cofactors(MatrixM, cof)
#    print("Calculo de adjunta...\n")
#    transpose(cof, adj)
#    print("Calculo de adjunta...\n")
#    productRealMatrix(1/det, adj, MatrixInv)


