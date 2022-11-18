import numpy as np
import copy
from .solucionAleatoria import solucion_aleatoria
from .fitness import fitness

def bitFlip(solucion,problema,bit):
    solucionMala=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    solucionNueva=copy.deepcopy(solucion)
    #print("-------------Comenzando el bitFlip")
    #print("la soluncion es: " , solucion)
    #print("Se cambia el bit: ", bit)
    #print("el valor del bit a cambiar: ",solucion[bit])
    done=0
    if(solucionNueva[bit]==0):
     #   print("pasa por if 1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        solucionNueva[bit]=1
        done=1
    if(solucionNueva[bit]==1 and done==0):
      #  print("pasa por if  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        solucionNueva[bit]=0

    #print("")
    #print("La solucion cambiada es: ",solucionNueva)
    #print("")
    return solucionNueva 

    

def tabu_search(problema):
    #la lista va a tener las ultimas 15 iteraciones
    tabu_list = []
    mejor_solucion = []
    iteraciones = 5 #Parametro de iteraciones del tabuSearch#
    intentos = 0
     
    while(intentos < 10):
        #Se genera solución inicial de manera aleatoría#
        solucion_inicial = solucion_aleatoria(problema, tabu_list)    
        costo_solucion_inicial = costoTorres(problema,solucion_inicial) 
        print("la solucion inicial es ")
        print(solucion_inicial)
        print("costo solucionInicial: ") 
        
        if(intentos == 0):
            mejor_solucion = copy.deepcopy(solucion_inicial)
        #Se crean vecinos a la solución aleatoria por bitFlip#
        j = 0
        mejor_vecino = copy.deepcopy(solucion_inicial)
        #fitness_mejor_vecino = copy.deepcopy(fitness_solucion_inicial)


        while(j < 36):
            buffer = bitFlip(solucion_inicial,tabu_list,j)    
            tabu_list.append(buffer)
            print("La lista original es: ", solucion_inicial)
            print("La lista cambiada es: ", buffer)

            
            j += 1 


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

def costoTorres(problema,solucion):
 print("Comienza a calcular el costo")
 i=36
 while(i<72):
    if((i-34)<32):
       print("Antena " , (i-34) , ": ", problema[i])
       i+=1
       print("el costo es: ", problema[0][i-37])
    else:
        print("Antena " , (i-33) , ": ", problema[i])
        i+=1


# TO DO LIST#
#1)Arreglar swap.
#3)Corregir problemas de lectura.
#4)Luego de corregir punto 3, forzar función de busqueda aleatoria, que cumpla restricciones.
#PUNTO 4 LISTO. HAY QUE VERIFICAR QUE SE REALIZA BIEN.




# TO DO LIST#
#1)Arreglar swap.
#3)Corregir problemas de lectura.
#4)Luego de corregir punto 3, forzar función de busqueda aleatoria, que cumpla restricciones.
#PUNTO 4 LISTO. HAY QUE VERIFICAR QUE SE REALIZA BIEN
