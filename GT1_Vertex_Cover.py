import Problema
class GT1_Vertex_Cover():
    nombre = ""
    genSize = 0
    fitness = 0.0
    cantidadVertices = 0
    
    def __init__(self):
        Problema.Problema.__init__(self)

    def readProblema(self,file):
        contadorLineas = 0;
        archivo = open(file, "r")
        for linea in archivo.readlines():
            if contadorLineas == 0:
                self.nombre = linea[:-1]
            elif contadorLineas == 1:
                cantidadVertices = int(linea[:-1])
                
            contadorLineas += 1
            

    def getGeneSize(self):
        return self.genSize

    def getFitness(self,gen):
        return fitness
    
    def getName(self):
        return self.nombre
