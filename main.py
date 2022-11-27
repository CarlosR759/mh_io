import logging
from modelos.lectura import lectura_instancia_del_problema
from modelos.tabuSearch import tabu_search
from modelos.tabuSearch import factibilidad
from modelos.fitness import fitness


def solucionConNombre(solucion):
  i=0
  done=0
  while(i<len(solucion)):
    if(solucion[i]==1 ):
      if(i==0):
        print("2.Calle Larga")
      if(i==1):
        print("3.San Esteban")
      if(i==2):
        print("4.Rinconada")
      if(i==3):
        print("5.Los Andes")
      if(i==4):
        print("6.Cabildo")
      if(i==5):
        print("7.La ligua")
      if(i==6):
        print("8.Papudo")
      if(i==7):
        print("9.Petorca")
      if(i==8):
        print("10.Zapallar")
      if(i==9):
        print("11.Hijuelas")
      if(i==10):
        print("12.La Calera")
      if(i==11):
        print("13.La Cruz")
      if(i==12):
        print("14.Limache")
      if(i==13):
        print("15.Nogales")
      if(i==14):
        print("16.Olmue")
      if(i==15):
        print("17.Quillota")
      if(i==16):
        print("18.Algarrobo")
      if(i==17):
        print("19.Cartagena")
      if(i==18):
        print("20.El Quisco")
      if(i==19):
        print("21.El Tabo")
      if(i==20):
        print("22.San Antonio")
      if(i==21):
        print("23.Santo Domingo")
      if(i==22):
        print("24.Catemu")
      if(i==23):
        print("25.Llay Llay")
      if(i==24):
        print("26.Panquehue")
      if(i==25):
        print("27.Putaendo")
      if(i==26):
        print("28.San Felipe")
      if(i==27):
        print("29.Santa Maria")
      if(i==28):
        print("30.Quilpue")
      if(i==29):
        print("31.Concon")
      if(i==30):
        print("33.Puchuncavi")
      if(i==31):
        print("34.Casablanca")
      if(i==32):
        print("35.Quintero")
      if(i==33):
        print("36.Valparaiso")
      if(i==34):
        print("37.Villa Alemana")
      if(i==35):
        print("38.Viña del Mar")
     
    i+=1  

def resolver_scp():
    problema = lectura_instancia_del_problema() 
    print("-----------------------------------------------------------")
    #viajo por la solucion cambiando hasta que encuentre la primera factible
    ##los valores del 1 al 36
    ##print(problema[0])
    ## se intercala la cantidad de vecinos y los vecinos
    ## hay 36 filas con el primer dig la cantidad de vecinos y despues los vecinos
    
    i=0
    while(i<72):
      print("Antena " , i , ": ", problema[i])
      i+=1
    print("-----------------------------------------------------------")

    solucion = tabu_search(problema)
    print("solucion encontrada: ")
    print(solucion)
    print("Con fitnes igual a : ")
    fitness_solucion = fitness(problema[0], solucion)
    print(fitness_solucion)
    factibilidad(problema,solucion)
    #implrime las ciudades con nombre 
    solucionConNombre(solucion)
    return solucion


#MAIN#
solucion_final = resolver_scp()


      
  