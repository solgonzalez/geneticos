import abc
from abc import ABCMeta # importaciones para simular clases abstractas
from SP5_RecubrimientoMinimo import * 
from GT1_Vertex_Cover import *

class Problema(object):
    __metaclass__ = ABCMeta

    problema ="";
    
    @abc.abstractmethod
    def readProblema(self,file):
        """
           Carga el archivo y seleciona si es GT1 o SP5
        """
        try:
            archivo = open(file, "r")
            linea = archivo.readline()
        except IOError:
            print("No se pudo abrir el archivo")
            return
        
        if(linea[:-1] == "GT1"):
            self.problema = GT1_Vertex_Cover()
            self.problema.readProblema(file)
        elif(linea[:-1] == "SP5"):
            self.problema = SP5_RecubrimientoMinimo()
            self.problema.readProblema(file)   
            
    @abc.abstractmethod
    def geneSize(self):
        """
           retorna el size del gen
        """
        return self.problema.getGeneSize()
        
    @abc.abstractmethod
    def fitness(self,gen):
        """
           Retorna el fitness del gen que se pasa como parámetro
        """
        return self.problema.getFitness(gen)
    
    @abc.abstractmethod
    def name(self):
        """
           retorna el nombre del problema
        """
        return self.problema.getName()






               
               
                
                
                    
                
                
            
        
        
    
            
        
    

    
    
