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

    aux = 0
    contador = 0     
    #Se leen los costos por columnas#
    costos_columnas = []
    for i in lines:
        if(i == lines[0]):
            continue
        cadena = i.split()
        costos_columnas.append(cadena)
        contador += len(costos_columnas[aux])
        aux += 1
        if(contador == columnas):
            break;
    
    #Al final de bucle anterior. Aux tiene el número de línea#
    #en que quedó la lectura del archivo .txt#
    aux += 1
    j = 0
    casosInstanciados = 0
    vecinos = [ ]
    
    
    for i in lines:
        vecinos.append(lines[aux])
        total_vecinos = lines[aux]
        aux +=1
        vecinos.append(lines[aux].split() )    
        aux +=1
        if(aux >= len(lines) ):
            break
    
    
    print("Lecutra de problema exitosa")
    return "Se pueden devolver datos por la función correctamente"

         #FORMATO TXT#
#El formato del .txt es el siguiente: #
#1)Numero de filas y columnas.
#2)El costo de cada columna.
#3)Por cada fila "i", el número de columnas que cubre la fila "i" seguido por la lista de columnas que cubren "i"


# Línea para depurar programa#
    #print(filas)
    #print(columnas)
    #print(costos_columnas)
    #print(vecinos)
