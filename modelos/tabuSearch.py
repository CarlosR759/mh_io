import numpy as np
from .solucionAleatoria import solucion_aleatoria


def tabu_search(problema):
    tabu_list = []
    mejor_solucion = []
    iteraciones = 5 #Parametro de iteraciones de tabuSearch#
    intentos = 0
     
    while(intentos < 5):
        #Se genera solución inicial de manera  aleatoría#
        solucion_inicial = solucion_aleatoria(problema)    
        if(intentos == 0):
            mejor_solucion = solucion_inicial

        print(solucion_inicial)
         
        #Se crean vecinos a la solución aleatoria por swap#
        #Se devuelve el mejor vecino al final del bucle#
        j = 0
        while(j <= 100):
            j += 1 


        #Mejor vecino de la solución inicial se deja en #
        #conjunto con la solución inicial en la tabu_list#

        #tabu_list.append(solucion_inicial)
        #tabu_list.append(mejor_vecino)



        #Se comprueba si solución generada es mejor#



        intentos += 1 
         
    #return mejor_solucion
