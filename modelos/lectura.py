import copy

def lectura_instancia_del_problema():
    #Se abre archivo#
    fo = open("problema.txt", "r")
    lines = fo.readlines()
    
    #Se dimensiona matriz#
    aux = lines[0].split()
    filas = aux[0]
    columnas = aux[1]
    filas = int(filas)
    columnas = int(columnas)

    aux = 1
    contador = 0     
    #Se leen los costos por columnas#
    costos_columnas = []
    for i in lines:
        if(i == lines[0]):
            continue
        cadena = i.split()
        costos_columnas.extend(cadena)
        contador = len(costos_columnas)
        aux += 1
        if(contador == columnas):
            break;
   
    #Al final de bucle anterior. Aux tiene el número de línea#
    #en que quedó la lectura del archivo .txt#
    j = 0
    casosInstanciados = 0
    vecinos = [ ] #Vecinos tiene los vecinos por area geográfica#
    buffer = [ ] 
     
    for i in lines:
        buffer.append(lines[aux])
        total_vecinos = int(lines[aux])
        j = 0
        while (j < total_vecinos):
            aux +=1
            buffer.extend(lines[aux].split() )
            j = len(buffer) - 1
        aux += 1
        vecinos.append(copy.deepcopy(buffer) )
        buffer.clear()
        if(aux >= len(lines) ):
            break
      
    print("Lecutra de problema exitosa")
#    return "Se pueden devolver datos por la función correctamente"

         #FORMATO TXT#
#El formato del .txt es el siguiente: #
#1)Numero de filas y columnas.
#2)El costo de cada columna.
#3)Por cada fila "i", el número de columnas que cubre la fila "i" seguido por la lista de columnas que cubren "i"


# Línea para depurar programa#
    #print(filas)
    #print(columnas)
    print(costos_columnas)
    print(vecinos)
