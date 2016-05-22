import random

class Algoritmo():
    tipoSeleccion = ["Azar","RuedaFortuna", "Torneo"]
    typoGen = [1,0]

    def __init__(self, pPolitica, pNumCruces, pMutacion, pTamPoblacion,pProblema):
        self.politica = pPolitica
        self.numCruces = pNumCruces
        self.mutacion = p.Mutacion
        self.tamPoblacion = pTamPoblacion
        self.problema = pProblema

    def resetPoblacion(pTamaPoblacion):
        """
           Crea una nueva poblacion
        """
        return [individual(0,1) for i in range(pTamPoblacion)]
    

    def readPoblacion(file):
        pass

    def writePoblacion(file):
        pass

    def generacion():
        pass
    def getBest():
        pass

    # Metodo auxiliar
    def individual(min,max):
        """
           Crea un individuo
        """
        tamGen = self.Problema.geneSize()
        return [random.randint(min,max) for i in range(tamGen)]

    
