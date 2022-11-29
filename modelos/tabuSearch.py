import numpy as np
import copy
from .solucionAleatoria import solucion_aleatoria
from .fitness import fitness

def bitFlip(solucion,problema,bit):
    solucionNueva=copy.deepcopy(solucion)
   
    done=0
    if(solucionNueva[bit]==0):
        solucionNueva[bit]=1
        done=1
    if(solucionNueva[bit]==1 and done==0):
        solucionNueva[bit]=0

    
    #print("La solucion cambiada es: ",solucionNueva)
   
    return solucionNueva 

    

def tabu_search(problema):
    #la lista va a tener las ultimas 15 iteraciones de las soluciones generadas aleatoriamente
    tabu_list = []
    mejor_solucion = []
    iteraciones = 5000 #Parametro de iteraciones del tabuSearch#
    intentos = 0
     
    while(intentos < iteraciones):
        #Se genera solución inicial de manera aleatoría#
        solucion_inicial = solucion_aleatoria(problema, tabu_list)   
        tabu_list.append(solucion_inicial) 
        if(len(tabu_list)>15):
            tabu_list.pop(0)

        #print("la solucion inicial es ")
        #print(solucion_inicial)
        #print("costo solucionInicial: ") 
        factibilidad(problema,solucion_inicial)
        fitness(problema[0],solucion_inicial) 
      
        if(intentos == 0):
            mejor_solucion = copy.deepcopy(solucion_inicial)
        if(factibilidad(problema,mejor_solucion)==False and intentos==(iteraciones-1)):
            intentos-=1
        #Se crean vecinos a la solución aleatoria por bitFlip#
        j = 0
        while(j < 36):
            #print("empezo el loop")
            buffer = bitFlip(solucion_inicial,tabu_list,j)    
            #print("La lista original es: ", solucion_inicial)
            #print("La lista cambiada es: ", buffer) 
            #Se comprueba si solución generada es mejor#
            fitness_buffer = fitness(problema[0], buffer)
            fitness_mejor_solucion = fitness(problema[0], mejor_solucion) 
            if(fitness_mejor_solucion > fitness_buffer and factibilidad(problema,buffer)==True):
                mejor_solucion = copy.deepcopy(buffer)
            #print("pasa x j")
            j += 1  
        
        intentos += 1 
   
    return mejor_solucion

def factibilidad(problema,solucion):
 factibilidad=[]
 j=0 
 while(j<len(solucion)):
  if(solucion[j]==1):
    cantidad=copy.deepcopy(problema[j+36][:1])
    #print(problema[j+36][:1], " la cantidad de la antena ---z-z-z-z-zz-z-z-z-z-z-")
    k=int(cantidad[0])
    while(k>0):
      factibilidad.append(problema[j+36][k])
      k-=1

  j+=1
 else:
  j+=1
 #print("termino la facti")
 #print(factibilidad)
 #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
 fact=sorted(set(factibilidad))
 #print(fact)
 if(len(fact)==36):
    print("si es factible")
    print("fitness: ",fitness(problema[0],solucion))
    return True
 else:
    #print("no es factible")
    return False
#print("ordenada y eliminada duplicados")
#factibilidad=sorted(set(factibilidad))
