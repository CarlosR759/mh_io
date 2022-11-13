import logging
from modelos.lectura import lectura_instancia_del_problema
from modelos.tabuSearch import tabu_search
from modelos.fitness import fitness

def resolver_scp():
    problema = lectura_instancia_del_problema() 
    print("-----------------------------------------------------------")
    #viajo por la solucion cambiando hasta que encuentre la primera factible





    ##los valores del 1 al 36
    ##print(problema[0])
    ## se intercala la cantidad de vecinos y los vecinos
    ## hay 36 filas con el primer dig la cantidad de vecinos y despues los vecinos
    #i=0
    #while(i<72):
    #    print("Fila " , i , ": ", problema[i])
    #    i+=1
    #print("-----------------------------------------------------------")

    solucion = tabu_search(problema)
    print("solucion encontrada: ")
    print(solucion)
    print("Con fitnes igual a : ")
    fitness_solucion = fitness(problema[0], solucion)
    print(fitness_solucion)
    return solucion


#MAIN#
solucion_final = resolver_scp()
