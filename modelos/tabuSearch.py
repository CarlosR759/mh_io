import numpy as np
from .solucionAleatoria import solucion_aleatoria
from .solucionAleatoria import comprobar_factibilidad
from .fitness import fitness

def swap(solucion, tabu_list):
    #Aseguramos que swap entrega solución no tabu#
    tabu = True
    hay_repeticion = False;
    while(tabu == True):
        numero_aleatorio = np.random.uniform(low=0, high=1) 
        hay_repeticion = False;
        for i in range(0,len(tabu_list)):
            if(tabu_list[i] == str(numero_aleatorio) ):
                hay_repeticion = True;

        if(hay_repeticion == False):
            tabu = False 
       
 
    diferencia_de_porcentaje = float(2.777777778)
    posicion_encontrada = False
    porcentaje = 2.777777778
    k = 1#Índice de la lista a recorrer# 

    #Swap para números que cubren solo primera casilla#
    if(numero_aleatorio <=  2.777777778):
        if(solucion[0] == 1):
            solucion[0] == 0
        else:
            solucion[0] == 1
        return solucion


    #Swap para encontrar casilla a modificar#
    while(posicion_encontada == False):
        porcentaje += 2.777777778 
        if((numero_aleatorio * 100) > porcentaje):
            k += 1 
        else:
            if(solucion[k-1] == 0):
                solucion[k-1] = 1 
            else:
                solucion[k-1] = 0
            posicion_encontrada = True

    #Se entrega solución con solo un bit cambiado# 
    return solucion 

def tabu_search(problema):
    tabu_list = []
    mejor_solucion = []
    iteraciones = 5 #Parametro de iteraciones del tabuSearch#
    intentos = 0
     
    while(intentos < 5):
        #Se genera solución inicial de manera aleatoría#
        solucion_inicial = solucion_aleatoria(problema, tabu_list)    
        fitness_solucion_inicial = fitness(problema[0],solucion_inicial) 
        print("fitness solucionInicial: ") 
        print( fitness_solucion_inicial)
        if(intentos == 0):
            mejor_solucion = solucion_inicial
        
        print(solucion_inicial)


        #Se crean vecinos a la solución aleatoria por swap#
        #Se devuelve el mejor vecino al final del bucle#
        j = 0
        es_factible = False
        mejor_vecino = solucion_inicial
        fitness_mejor_vecino = fitness_solucion_inicial
        print("buffers: ")
        while(j < 36):
            buffer = swap(solucion_inicial,tabu_list)    
            tabu_list.append(buffer)
            print(buffer)
            fitness_buffer = fitness(problema[0],buffer)
            #Se comprueba si es factible#
            es_factible = comprobar_factibilidad(problema,buffer,tabu_list)
            if(es_factible == True):
                if(fitness_buffer <= fitness_solucion_inicial):
                    if(fitness_buffer <= fitness_mejor_vecino):
                        mejor_vecino = buffer 
            j += 1 
            es_factible = False


        #Mejor vecino de la solución inicial se deja en #
        #conjunto con la solución inicial en la tabu_list#
        tabu_list.append(solucion_inicial)
        tabu_list.append(mejor_vecino)



        #Se comprueba si solución generada es mejor#
        fitness_mejor_solucion = fitness(problema[0], mejor_solucion)
        fitness_mejor_vecino = fitness(problema[0], mejor_vecino) 
        if(fitness_mejor_solucion > fitness_mejor_vecino):
            mejor_solucion = mejor_vecino 

        intentos += 1 

    return mejor_solucion


# TO DO LIST#
#1)Arreglar swap.
#3)Corregir problemas de lectura.
#4)Luego de corregir punto 3, forzar función de busqueda aleatoria, que cumpla restricciones.
#PUNTO 4 LISTO. HAY QUE VERIFICAR QUE SE REALIZA BIEN.
