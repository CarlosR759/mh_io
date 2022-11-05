import logging
from modelos.lectura import lectura_instancia_del_problema
from modelos.tabuSearch import tabu_search

def resolver_scp():
    problema = lectura_instancia_del_problema() 
    solucion = tabu_search(problema)
    #return solucion


#MAIN#
resolver_scp()
#print(solucion)

