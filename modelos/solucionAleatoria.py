import numpy as np

def solucion_aleatoria(problema):

    solucionFactible = False
    aux = 0 
    while(solucionFactible == False): 
        solucion = np.random.choice([0,1], size=(36))
        aux = np.sum(solucion) 
        #Se descartan peor solucion y no construir nada#
        while( (aux == 0) or (aux == 36) ):
            solucion = np.random.choice([0,1], size=(36))
            aux = solucion 
        solucionFactible = comprobar_factibilidad(problema, solucion) 
         
    return solucion 


def comprobar_factibilidad(problema, solucion):
    cobertura_del_area = [0] * 36
    es_factible = False


    #print(problema)
    return True 
