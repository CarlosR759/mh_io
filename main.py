import logging
from modelos.lectura import lectura_instancia_del_problema


def resolver_scp():
    func = lectura_instancia_del_problema() 
    print(func)

#MAIN#
resolver_scp()


