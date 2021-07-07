from abc import abstractmethod
from enum import IntEnum,auto
from dataclasses import dataclass

class indicators(IntEnum):
    NOTHING = 0

class lines(IntEnum):
    NOLINE = 0
    SINGLELINE = 1
    DOUBLELINE = 2

class modes(IntEnum):
    NOMODE = 0
    INT_FLOAT = 1
    INT_FLOAT_FLOAT_FLOAT = 2
    INT_x10 = 3

class parameterD(IntEnum):
    EI = 0
    F_X = 1
    F_Y = 2
    F_Z = 3

class sizeE(IntEnum):
    NODES = 0
    ELEMENTS = 1
    DIRICHLET = 2
    NEUMANN = 3

@dataclass
class item:
    idItem:int
    x:float
    y:float
    z:float
    node1:int
    node2:int
    node3:int
    node4:int
    node5:int
    node6:int
    node7:int
    node8:int
    node9:int
    node10:int
    value:float

    def __init__(self):
        pass

    def setId(self, idItem:int):
        self.idItem = idItem
    
    def setX(self, x_coord:float):
        self.x=x_coord

    def setY(self, y_coord:float):
        self.y=y_coord

    def setZ(self, z_coord:float):
        self.z=z_coord

    def setNode1(self, node1:int):
        self.node1 = node1
    
    def setNode2(self, node2:int):
        self.node2 = node2

    def setNode3(self, node3:int):
        self.node3 = node3

    def setNode4(self, node4:int):
        self.node4 = node4

    def setNode5(self, node5:int):
        self.node5 = node5

    def setNode6(self, node6:int):
        self.node6 = node6

    def setNode7(self, node7:int):
        self.node7 = node7

    def setNode8(self, node8:int):
        self.node8 = node8

    def setNode9(self, node9:int):
        self.node9 = node9

    def setNode10(self, node10:int):
        self.node10 = node10

    def getId(self):
        return self.Id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getNode3(self):
        return self.node3

    def getNode4(self):
        return self.node4

    def getNode5(self):
        return self.node5

    def getNode6(self):
        return self.node6

    def getNode7(self):
        return self.node7

    def getNode8(self):
        return self.node8
    
    def getNode9(self):
        return self.node9

    def getNode10(self):
        return self.node10

    def getvalue(self):
        return self.value

    @abstractmethod
    def setValues(self,a:int,b:float,c:float,d:float,e:int,f:int,g:int,h:int,j:int,k:int,l:int,m:int,n:int,o:int,i:float):
        pass

@dataclass
class node(item):
    def __init__(self):
        pass

    def setValues(self,a:int,b:float,c:float,d:float,e:int,f:int,g:int,h:int,j:int,k:int,l:int,m:int,n:int,o:int,i:float):
        self.idItem = a
        self.x = b
        self.y = c
        self.z = d

@dataclass
class element(item):
    def __init__(self):
        pass
    def setValues(self,a:int,b:float,c:float,d:float,e:int,f:int,g:int,h:int,j:int,k:int,l:int,m:int,n:int,o:int,i:float):
        self.idItem = a
        self.node1 = e
        self.node2 = f
        self.node3 = g
        self.node4 = h
        self.node5 = j
        self.node6 = k
        self.node7 = l
        self.node8 = m
        self.node9 = n
        self.node10 = o

@dataclass
class condition(item):
    def __init__(self):
        pass
    def setValues(self, a: int, b: float, c: float, d: float, e: int, f: int, g: int, h: int, j: int, k: int, l: int, m: int, n: int, o: int, i: float):
        self.node1 = e
        self.value = i


@dataclass
class mesh:
    
    parameters = [None]*4
    sizes = [None]*4
    node_list = []
    element_list = []
    indices_dirich = []
    dirichlet_list = []
    neuman_list = []

    def __init__(self):
        pass

    def setParameters(self,EI:float,F_X:float,F_Y:float,F_Z:float):
        self.parameters[parameterD.EI] = EI
        self.parameters[parameterD.F_X] = F_X
        self.parameters[parameterD.F_Y] = F_Y
        self.parameters[parameterD.F_Z] = F_Z
    
    def setSizes(self,nnodes:int,neltos:int,ndirich:int,nneu:int):
        self.sizes[sizeE.NODES] = nnodes
        self.sizes[sizeE.ELEMENTS] = neltos
        self.sizes[sizeE.DIRICHLET] = ndirich
        self.sizes[sizeE.NEUMANN] = nneu

    def getSize(self,s:int):
        return self.sizes[s]

    def getParameter(self, p:int):
        return self.parameters[p]


    def createData(self):
        #Inicializar lista de nodos
        for i in range(self.sizes[sizeE.NODES]):
            n = node()
            self.node_list.append(n)
        
        #Inicializar lista de elementos
        for i in range(self.sizes[sizeE.ELEMENTS]):
            n = element()
            self.element_list.append(n)

        for i in range(self.sizes[sizeE.DIRICHLET]):
            n:int
            self.indices_dirich.append(n)

        for i in range(self.sizes[sizeE.DIRICHLET]):
            n = condition()
            self.dirichlet_list.append(n)

        for i in range(self.sizes[sizeE.NEUMANN]):
            n = condition()
            self.neuman_list.append(n)

    def getNodes(self):
        return self.node_list

    def getElements(self):
        return self.element_list

    def getDirichletIndices(self):
        return self.indices_dirich

    def getDirichlet(self):
        return self.dirichlet_list

    def getNeumann(self):
        return self.neuman_list

    def getNode(self, i:int):
        return self.node_list[i]

    def getElement(self, i:int):
        return self.element_list[i]

    def getCondition(self, i:int, type:int):
        if(type == sizeE.DIRICHLET): 
            return self.dirichlet_list[i]
        else:
            return self.neuman_list[i]



