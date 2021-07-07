from sel import showVector
from classes import mesh, node,sizeE,parameterD,element,condition,lines,modes,indicators

def datoslist(lista:list,datos:list):
    cadena = ""
    for k in range(0,len(lista)):
        if(lista[k]!=" " and lista[k] != "\t"):
            cadena += lista[k]
        else:
            if(len(cadena)!=0):
                datos.append(cadena)
                cadena = ""
                
    if(len(cadena)!=0):
        datos.append(cadena)
    

def obtenerDatos(lineas:list, i:list, nlines:int,ind:int,n:int, mode:int, item_list:list):
    if(nlines == lines["DOUBLELINE"]):
        i[0]+=1
    i[0]+=2
    for j in range(ind,n):
        data = []
        datoslist(lineas[i[0]],data)
        i[0]+=1
        if(mode == modes["INT_FLOAT"]):
            e0:int = int(data[0])
            r0:float = float(data[1])
            item_list[j].setValues(indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,e0,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,r0)
        elif(mode == modes["INT_FLOAT_FLOAT_FLOAT"]):
            e = int(data[0])
            r= float(data[1])
            rr = float(data[2])
            rrr = float(data[3])
            item_list[j].setValues(e,r,rr,rrr,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,indicators.NOTHING)
        elif(mode == modes["INT_x10"]):
            item_list[j].setValues(int(data[0]),indicators.NOTHING,indicators.NOTHING,indicators.NOTHING,int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6]),int(data[7]),int(data[8]),int(data[9]),int(data[10]),indicators.NOTHING)



def correctConditions(n:int,clist:list,indices:list):
    for i in range(0,n):
        indices[i] = clist[i].getNode1()
    
    for i in range(0,n-1):
        pivot:int = clist[i].getNode1()
        for j in range(i,n):
            if(clist[j].getNode1()>pivot):
                clist[j].setNode1(clist[j].getNode1()-1)

def addExtension(newfilename:list,filename:list, extension:list):
    ori_length:int = len(filename)
    ext_length:int = len(extension)
    j:int = 0
    for i in range(0,ori_length):
        newfilename[i] = filename[i];
    
    for i in range(0,ext_length):
        j = ori_length+i
        newfilename[j] = extension[i]
    
    newfilename[j+1] = '\0'
    

def leerMallayCondiciones(m:mesh, filename:list):
    inputfilename = filename+".dat"
    

    #addExtension(inputfilename,filename,".dat")

    file = open(inputfilename,"r")
    lineas:list = file.readlines() #Lineas en forma de lista
    i = [0] #indice lineas

    data = []
    datoslist(lineas[i[0]],data)

    EI:float = float(data[0])
    F_X:float = float(data[1])
    F_Y:float = float(data[2])
    F_Z:float = float(data[3])
    i[0]+=1

    data = []
    datoslist(lineas[i[0]],data)
    nnodes:int = int(data[0])
    neltos:int = int(data[1])
    ndirichX:int = int(data[2])
    ndirichY:int = int(data[3])
    ndirichZ:int = int(data[4])
    ndirich:int = ndirichX+ndirichY+ndirichZ
    nneu:int = int(data[5])
    i[0]+=1

    m.setParameters(EI, F_X, F_Y, F_Z)
    m.setSizes(nnodes,neltos,ndirich,nneu)
    m.createData()
    obtenerDatos(lineas,i,lines["SINGLELINE"],0,nnodes,modes.INT_FLOAT_FLOAT_FLOAT,m.getNodes())
    obtenerDatos(lineas,i,lines["DOUBLELINE"],0,neltos,modes.INT_x10,m.getElements())
    obtenerDatos(lineas,i,lines["DOUBLELINE"],0,ndirichX,modes.INT_FLOAT,m.getDirichlet())
    obtenerDatos(lineas,i,lines["DOUBLELINE"],ndirichX,ndirichX+ndirichY,modes.INT_FLOAT,m.getDirichlet())
    obtenerDatos(lineas,i,lines["DOUBLELINE"],ndirichX+ndirichY,ndirich,modes.INT_FLOAT,m.getDirichlet())
    obtenerDatos(lineas,i,lines["DOUBLELINE"],0,nneu,modes.INT_FLOAT,m.getNeumann())

def findIndex(v:int,s:int,arr:list):
    for i in range(0,s):
        if(arr[i]==v): return True
    return False 

def writeResult(m, T, filename:list):
    outputFilename = filename+".post.res"
    dirichIndices = m.getDirichletIndices()
    dirich = m.getDirichlet()


    file = open(outputFilename, "w")

    file.write("GiD Post Results File 1.0\n")
    file.write("Result \"Fuerza\" \"Load Case 1\" 1 Scalar OnNodes\nComponentNames \"w\"\nValues\n")

    Tpos = 0
    Dpos = 0
    n = m.getSize(sizeE["NODES"])
    nd = m.getSize(sizeE["DIRICHLET"])
    for i in range(n):
        if(findIndex(i+1, nd, dirichIndices)):
            string = str(i+1) + " " + str(dirich[Dpos].getValue()) + "\n"
            file.write(string)
            Dpos+= 1
        else:
            string2 = str(i+1) + " " + str(T[Tpos]) + "\n"
            file.write(string2)
            Tpos+= 1
    
    file.write("End values\n")
    file.close()

