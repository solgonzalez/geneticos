import Problema

class SP5_RecubrimientoMinimo():
    nombre = ""
    genSize = 0
    fitness = 0.0
    tamañoConjunto_S = 0 #Conjunto principal del problema
    numeroSubconjuntos_S = 0
    conjuntosDe_C = []

    def __init__(self):
        """ Constructor """
        Problema.Problema.__init__(self)
        
    def readProblema(self,file):
        """
           Lee el problema
           Carga la informacion del problema
        """
        contadorLineas = 0;
        archivo = open(file, "r") # modo lectura del archivo
        
        for linea in archivo.readlines():
            if contadorLineas == 0: #Primera Linea del archivo
                self.nombre = linea[:-1]
                
            elif contadorLineas == 1: # Segunda Linea del archivo
                self.tamañoConjunto_S = int(linea[:-1])
                self.genSize = self.tamañoConjunto_S
                
            elif contadorLineas == 2: #Tecera linea del archivo
                self.numeroSubconjuntos_S = int(linea[:-1])

            elif contadorLineas >=3: # Siguientes lineas
                self.conjuntosDe_C += [eval(linea[:-1])]
                
            contadorLineas += 1           
 

    def getGeneSize(self):
        """ Retorna el tamaño del gen
        """
        return self.genSize

    def getFitness(self,gen):
        """ Calcula el fitness de un gen
        """
        if(len(gen)!= self.tamañoConjunto_S):
            print("El tamaño del gen debe corresponder al tamaño del conjunto S")
            return
        
        self.fitness += self.calcularFitness(gen)
        return self.fitness
    
    def getName(self):
        """
           Obtiene el nombre del problema
        """
        return self.nombre
    
    def calcularFitness(self,gen):
        tempFitness = []
        
        for subconjunto in self.conjuntosDe_C:
            elementoGen = 0
            sumatoriaNoEsta = 0
            if(len(subconjunto) <= self.numeroSubconjuntos_S):
                for c_prima in subconjunto:
                    
                    if gen[elementoGen] == 0:
                       
                        sumatoriaNoEsta += 1
                    elementoGen += 1
                print("here")
                    
            print(self.tamañoConjunto_S, sumatoriaNoEsta,
                  (self.tamañoConjunto_S - elementoGen))
            tempFitness += [self.tamañoConjunto_S - sumatoriaNoEsta - 100
                            *(self.tamañoConjunto_S - elementoGen)]
        print(tempFitness)
        return max(tempFitness)
