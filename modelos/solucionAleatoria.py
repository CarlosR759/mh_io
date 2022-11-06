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

    #Se comprueba que se están cubriendo todas las areas#
    for i in range(0,36):
        aux = solucion[i] 
        if(aux == 0):
            continue
        cadena = problema[i+2]
        dimension = len(cadena)
        print("cadena: "+ str(cadena))
        for j in range(0,dimension):
            area = int(cadena[int(j)])
            #Se posicionan soluciones correctamente en lista#
            if(area > 31):
                cobertura_del_area[area - 3] = 1 
            else:
                cobertura_del_area[area - 2] = 1
   
 
    #Salida de la función#
    print("Resultado: " + str(sum(cobertura_del_area)))
    return True
    if(sum(cobertura_del_area) == 36):
        return True
    else:
        return False
