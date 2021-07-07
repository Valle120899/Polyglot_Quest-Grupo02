import sys
from types import new_class
import math_tools
from classes import mesh,sizeE
import tools
import sel


def main():
    filename = str()
    filename = sys.argv[1]
    #filename = "Alexa"
    m = mesh()
    tools.leerMallayCondiciones(m,filename)
    print("Datos obtenidos correctamente\n********************\n")

    localKs = []
    localBs = []
    sel.crearSistemasLocales(m,localKs,localBs)
    print( "Sistemas Locales creados****************************\n")

    K = []
    B = []
    math_tools.zeroesM(K,m.getSize(sizeE["NODES"])*3)
    math_tools.zeroesV(B,m.getSize(sizeE["NODES"])*3)
    sel.assembly(m,localKs,localBs,K,B)
    print( "Ensamblaje*****************************************\n")

    sel.applyNeumann(m,B)
    print( "Neuman********************************************\n")

    sel.applyDirichlet(m,K,B)
    print( "Dirichlet********************************************\n")

    T = []
    math_tools.zeroesV(T,len(B))
    sel.calculate(K,B,T)
    tools.writeResult(m,T,filename)


main()







