from classes import mesh, node,sizeE,parameterD,element,condition
from math_tools import determinant, inverseMatrix, productMatrixVector, productRealMatrix, zeroesM, zeroesNM, zeroesV

def showMatrix(matrix):
    for i in range(0,len(matrix)):
        print("[\t")
        for j in range(0,len(matrix[0])):
            print(matrix[i][j])
        print("]\t")

def showKs(Ks):
    for i in range(0,len(Ks)):
        print("K del elemento "+str(i+1)+":\n")
        showMatrix(Ks[i])
        print("*************************************\n")

def showVector(b):
    print("[\t")
    for i in range(0,len(b)):
        print(b[i])
    print("]\n")

def showBs(Bs):
    for i in range(0,len(Bs)):
        print("b del elemento "+str(i+1)+":\n")
        showVector(Bs[i])
        print("*************************************\n")

def calculateLocalA(c1,c2):
    return -((1.0/(192*(c2**2)))*((4*c1-c2)**4))-((1.0/(24*c2))*((4*c1-c2)**3))-((1.0/(3840*(c2**3)))*((4*c1-c2)**5))+((1.0/(3840*(c2**3)))*((4*c1+3*c2)**5))

def calculateLocalB(c1,c2):
    return -((1.0/(192*(c2**2)))*((4*c1+c2)**4))+((1.0/(24*c2))*((4*c1+c2)**3))-((1.0/(3840*(c2**3)))*((4*c1+c2)**5))+((1.0/(3840*(c2**3)))*((4*c1-3*c2)**5))

def calculateLocalC(c1,c2):
    return (4.0/15)*(c2**2)

def calculateLocalD(c1,c2):
    return ((1.0/(192*(c2**2)))*((4*c2-c1)**4)) - ((1.0/(3840*(c2**3)))*((4*c2-c1)**5)) + ((1.0/(7680*(c2**3)))*((4*c2+8*c1)**5)) - ((7.0/(7680*(c2**3)))*((4*c2-8*c1)**5)) + ((1.0/(768*(c2**3)))*((-8*c1)**5)) - (((c1*1.0)/(96*(c2**3)))*((4*c2-8*c1)**4)) + ((((2*c1-1)*1.0)/(192*(c2**3)))*((-8*c1)**4))

def calculateLocalE(c1,c2):
    return ((8.0/3)*(c1**2))+((1.0/30)*(c2**2))

def calculateLocalF(c1,c2):
    return ((2.0/3)*c1*c2) - ((1.0/30)*(c2**2))

def calculateLocalG(c1,c2):
    return -((16.0/3)*(c1**2))-((4.0/3)*c1*c2)-((2.0/15)*(c2**2))

def calculateLocalH(c1,c2):
    return ((2.0/3)*c1*c2) + ((1.0/30)*(c2**2))

def calculateLocalI(c1,c2):
    return -((16.0/3)*(c1**2))-((2.0/3)*(c2**2))

def calculateLocalJ(c1,c2):
    return (2.0/15)*(c2**2)

def calculateLocalK(c1,c2):
    return -((4.0/3)*c1*c2)

def calculateLocalC1(x1,x2):
    x = x2-x1
    if(x==0.0):
        x=0.00000000000000001
    return 1.0/((x)**2)

def calculateLocalC2(x1,x2,x8):
    x = x2 = x1
    m = 4*x1+4*x2-8*x8
    if(x==0.0 or m==0.0):
        if(x==0.0):
            x=0.00000000000000001
        if(m==0.0):
            m = 0.00000000000000001
    return (1.0/(x))*(m)

def calculateLocalU(x1:float,x2:float,x8:float):
    

    c1 = calculateLocalC1(x1,x2)
    c2 = calculateLocalC2(x1,x2,x8)

    A:float = calculateLocalA(c1,c2)
    B:float = calculateLocalB(c1,c2)
    C:float = calculateLocalC(c1,c2)
    D:float = calculateLocalD(c1,c2)
    E:float = calculateLocalE(c1,c2)
    F:float = calculateLocalF(c1,c2)
    G:float = calculateLocalG(c1,c2)
    H:float = calculateLocalH(c1,c2)
    I:float = calculateLocalI(c1,c2)
    J:float = calculateLocalJ(c1,c2)
    K:float = calculateLocalK(c1,c2)

    U = []

    zeroesM(U,10)

    U[0][0] = A
    U[0][1] = E
    U[0][4] = -1*F
    U[0][6] = -1*F
    U[0][7] = G
    U[0][8] = F
    U[0][9] = F

    U[1][0] = E
    U[1][1] = B
    U[1][4] = -1*H
    U[1][6] = -1*H
    U[1][7] = I
    U[1][8] = H
    U[1][9] = H

    U[4][0] = -1*F
    U[4][1] = -1*H
    U[4][4] = C
    U[4][6] = J
    U[4][7] = -1*K
    U[4][8] = -1*C
    U[4][9] = -1*J

    U[6][0] = -1*F
    U[6][1] = -1*H
    U[6][4] = J
    U[6][6] = C
    U[6][7] = -1*K
    U[6][8] = -1*J
    U[6][9] = -1*C

    U[7][0] = G
    U[7][1] = I
    U[7][4] = -1*K
    U[7][6] = -1*K
    U[7][7] = D
    U[7][8] = K
    U[7][9] = K

    U[8][0] = F
    U[8][1] = H
    U[8][4] = -1*C
    U[8][6] = -1*J
    U[8][7] = K
    U[8][8] = C
    U[8][9] = J

    U[9][0] = F
    U[9][1] = H
    U[9][4] = -1*J
    U[9][6] = -1*C
    U[9][7] = K
    U[9][8] = J
    U[9][9] = C

    return U

def calculateDeterminanteJ(n1:node,n2:node,n3:node,n4:node):
    MatrixJ = []

    x1:float = n1.getX()
    x2:float = n2.getX()
    x3:float = n3.getX()
    x4:float = n4.getX()

    y1:float = n1.getY()
    y2:float = n2.getY()
    y3:float = n3.getY()
    y4:float = n4.getY()

    z1:float = n1.getZ()
    z2:float = n2.getZ()
    z3:float = n3.getZ()
    z4:float = n4.getZ()

    zeroesM(MatrixJ,3)

    a = x2-x1
    b = x3-x1
    c = x4-x1

    d = y2-y1
    e = y3-y1
    f = y4-y1

    g = z2-z1
    h = z3-z1
    i = z4-z1

    J = a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i
    return J



def createLocalK(ind:int, m:mesh):
    K = []

    EI:float = m.getParameter(0)

    el:element = m.getElement(ind)
    n1:node = m.getNode(el.getNode1()-1)
    n2:node = m.getNode(el.getNode2()-1)
    n3:node = m.getNode(el.getNode3()-1)
    n4:node = m.getNode(el.getNode4()-1)
    n8:node = m.getNode(el.getNode8()-1)

    x1:float = n1.getX()
    x2:float = n2.getX()
    x8:float = n8.getX()

    J:float = calculateDeterminanteJ(n1,n2,n3,n4)
    MatrixTemp = []

    U = calculateLocalU(x1,x2,x8)

    zeroesM(MatrixTemp,30)

    l = 0
    for i in range(10):
        for j in range(10):
            MatrixTemp[i+l][j+l] = U[i][j]
    l = 10
    for i in range(10):
        for j in range(10):
            MatrixTemp[i+l][j+l] = U[i][j]
    l = 20
    for i in range(10):
        for j in range(10):
            MatrixTemp[i+l][j+l] = U[i][j]

    productRealMatrix(EI*J,MatrixTemp,K)

    return K

def createLocalB(ind:int, m:mesh):
    B = []

    el:element = m.getElement(ind)
    n1:node = m.getNode(el.getNode1()-1)
    n2:node = m.getNode(el.getNode2()-1)
    n3:node = m.getNode(el.getNode3()-1)
    n4:node = m.getNode(el.getNode4()-1)
    F = []
    F.append(m.getParameter(1)) #F_x
    F.append(m.getParameter(2)) #F_y
    F.append(m.getParameter(3)) #F_z
    T = []
    zeroesV(T, 10)
    T[0] = 59
    T[1] = -1
    T[2] = -1
    T[3] = -1
    T[4] = 4
    T[5] = 4
    T[6] = 4
    T[7] = 4
    T[8] = 4
    T[9] = 4

    J:float = calculateDeterminanteJ(n1,n2,n3,n4)

    Matrixtemp = []
    zeroesNM(Matrixtemp,30,3)

    l = 0
    for i in range(0,10):
        Matrixtemp[i][l] = T[i]
    
    l = 1
    for i in range(0,10):
        Matrixtemp[i][l] = T[i]
    
    l = 2
    for i in range(0,10):
        Matrixtemp[i][l] = T[i]
    
    VB = []
    productRealMatrix(J/120,Matrixtemp,VB)
    productMatrixVector(VB,F,B)
    return B



def crearSistemasLocales(m:mesh, localKs:list, localBs:list):
    for i in range(0,m.getSize(sizeE["ELEMENTS"])):
        localKs.append(createLocalK(i,m))
        localBs.append(createLocalB(i,m))

def assemblyK(e:element,localK:list,K:list):
    index1:int = e.getNode1() - 1
    index2:int = e.getNode2() - 1
    index3:int = e.getNode3() - 1
    index4:int = e.getNode4() - 1
    index5:int = e.getNode5() - 1
    index6:int = e.getNode6() - 1
    index7:int = e.getNode7() - 1
    index8:int = e.getNode8() - 1
    index9:int = e.getNode9() - 1
    index10:int = e.getNode10() - 1

    K[index1][index1]+=localK[0][0]
    K[index1][index2]+=localK[0][1] 
    K[index1][index3]+=localK[0][2] 
    K[index1][index4]+=localK[0][3]
    K[index1][index5]+=localK[0][4] 
    K[index1][index6]+=localK[0][5] 
    K[index1][index7]+=localK[0][6] 
    K[index1][index8]+=localK[0][7] 
    K[index1][index9]+=localK[0][8] 
    K[index1][index10]+=localK[0][9]

    K[index2][index1]+=localK[1][0]
    K[index2][index2]+=localK[1][1] 
    K[index2][index3]+=localK[1][2] 
    K[index2][index4]+=localK[1][3]
    K[index2][index5]+=localK[1][4] 
    K[index2][index6]+=localK[1][5] 
    K[index2][index7]+=localK[1][6] 
    K[index2][index8]+=localK[1][7] 
    K[index2][index9]+=localK[1][8] 
    K[index2][index10]+=localK[1][9]

    K[index3][index1]+=localK[2][0]
    K[index3][index2]+=localK[2][1] 
    K[index3][index3]+=localK[2][2] 
    K[index3][index4]+=localK[2][3]
    K[index3][index5]+=localK[2][4] 
    K[index3][index6]+=localK[2][5] 
    K[index3][index7]+=localK[2][6] 
    K[index3][index8]+=localK[2][7] 
    K[index3][index9]+=localK[2][8] 
    K[index3][index10]+=localK[2][9]

    K[index4][index1]+=localK[3][0]
    K[index4][index2]+=localK[3][1] 
    K[index4][index3]+=localK[3][2] 
    K[index4][index4]+=localK[3][3]
    K[index4][index5]+=localK[3][4] 
    K[index4][index6]+=localK[3][5] 
    K[index4][index7]+=localK[3][6] 
    K[index4][index8]+=localK[3][7] 
    K[index4][index9]+=localK[3][8] 
    K[index4][index10]+=localK[3][9]

    K[index5][index1]+=localK[4][0]
    K[index5][index2]+=localK[4][1] 
    K[index5][index3]+=localK[4][2] 
    K[index5][index4]+=localK[4][3]
    K[index5][index5]+=localK[4][4] 
    K[index5][index6]+=localK[4][5] 
    K[index5][index7]+=localK[4][6] 
    K[index5][index8]+=localK[4][7] 
    K[index5][index9]+=localK[4][8] 
    K[index5][index10]+=localK[4][9]

    K[index6][index1]+=localK[5][0]
    K[index6][index2]+=localK[5][1] 
    K[index6][index3]+=localK[5][2] 
    K[index6][index4]+=localK[5][3]
    K[index6][index5]+=localK[5][4] 
    K[index6][index6]+=localK[5][5] 
    K[index6][index7]+=localK[5][6] 
    K[index6][index8]+=localK[5][7] 
    K[index6][index9]+=localK[5][8] 
    K[index6][index10]+=localK[5][9]

    K[index7][index1]+=localK[6][0]
    K[index7][index2]+=localK[6][1] 
    K[index7][index3]+=localK[6][2] 
    K[index7][index4]+=localK[6][3]
    K[index7][index5]+=localK[6][4] 
    K[index7][index6]+=localK[6][5] 
    K[index7][index7]+=localK[6][6] 
    K[index7][index8]+=localK[6][7] 
    K[index7][index9]+=localK[6][8] 
    K[index7][index10]+=localK[6][9]

    K[index8][index1]+=localK[7][0]
    K[index8][index2]+=localK[7][1] 
    K[index8][index3]+=localK[7][2] 
    K[index8][index4]+=localK[7][3]
    K[index8][index5]+=localK[7][4] 
    K[index8][index6]+=localK[7][5] 
    K[index8][index7]+=localK[7][6] 
    K[index8][index8]+=localK[7][7] 
    K[index8][index9]+=localK[7][8] 
    K[index8][index10]+=localK[7][9]

    K[index9][index1]+=localK[8][0]
    K[index9][index2]+=localK[8][1] 
    K[index9][index3]+=localK[8][2] 
    K[index9][index4]+=localK[8][3]
    K[index9][index5]+=localK[8][4] 
    K[index9][index6]+=localK[8][5] 
    K[index9][index7]+=localK[8][6] 
    K[index9][index8]+=localK[8][7] 
    K[index9][index9]+=localK[8][8] 
    K[index9][index10]+=localK[8][9]

    K[index10][index1]+=localK[9][0]
    K[index10][index2]+=localK[9][1] 
    K[index10][index3]+=localK[9][2] 
    K[index10][index4]+=localK[9][3]
    K[index10][index5]+=localK[9][4] 
    K[index10][index6]+=localK[9][5] 
    K[index10][index7]+=localK[9][6] 
    K[index10][index8]+=localK[9][7] 
    K[index10][index9]+=localK[9][8] 
    K[index10][index10]+=localK[9][9]
    

def assemblyB(e:element,localb:list,B:list):
    index1:int = e.getNode1() - 1
    index2:int = e.getNode2() - 1
    index3:int = e.getNode3() - 1
    index4:int = e.getNode4() - 1
    index5:int = e.getNode5() - 1
    index6:int = e.getNode6() - 1
    index7:int = e.getNode7() - 1
    index8:int = e.getNode8() - 1
    index9:int = e.getNode9() - 1
    index10:int = e.getNode10() - 1

    B[index1] += localb[0]
    B[index2] += localb[1]
    B[index3] += localb[2]
    B[index4] += localb[3]
    B[index5] += localb[4]
    B[index6] += localb[5]
    B[index7] += localb[6]
    B[index8] += localb[7]
    B[index9] += localb[8]
    B[index10] += localb[9]


def assembly(m:mesh,localKs:list,localbs:list,K:list,B:list):
    for i in range (0,m.getSize(sizeE.ELEMENTS)):
        e:element = m.getElement(i)
        assemblyK(e,localKs[i],K)
        assemblyB(e,localbs[i],B)

def applyNeumann(m:mesh, B:list):
    for i in range(0,m.getSize(sizeE.NEUMANN)):
        c:condition = m.getCondition(i,sizeE.NEUMANN)
        B[c.getNode1()-1] += c.getvalue()


def applyDirichlet(m:mesh,K:list,B:list):
    ndirich = int(m.getSize(sizeE.DIRICHLET))
    for i in range (0,ndirich):

        c:condition = m.getCondition(i, sizeE.DIRICHLET)

        index:int = c.getNode1()-1


        K.pop(i)
        B.pop(i)

        for row in range(0,len(K)):
            
            cell:float = K[row][index]

            K[row].pop(i)
            B[row] += (-1*c.getvalue()*cell)

def calculate(K:list,B:list,T:list):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    productMatrixVector(Kinv,B,T)


