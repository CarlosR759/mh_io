import numpy as np

def fitness(costos, solucion):
    #Función ayuda a calcular el costo de implementación#
    precio_implementacion = float(0)
   
    for i in range(0,len(costos)):
        if(solucion[i] == 1):
            precio_implementacion += float(costos[i])
            

    return precio_implementacion 
