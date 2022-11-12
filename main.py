import logging
from modelos.lectura import lectura_instancia_del_problema
from modelos.tabuSearch import tabu_search
from modelos.fitness import fitness

def resolver_scp():
    problema = lectura_instancia_del_problema() 
    solucion = tabu_search(problema)
    print("solucion encontrada: ")
    print(solucion)
    print("Con fitnes igual a : ")
    fitness_solucion = fitness(problema[0], solucion)
    print(fitness_solucion)
    return solucion


#MAIN#
solucion_final = resolver_scp()
