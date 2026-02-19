def permutaciones(lista):
    if len(lista) <=1:
        return [lista[:]] #Retorna copia de la lista
    
    resultado = []

    #Para cada elemento de la lista
    for i in range(len(lista)):
        #Elemento actual
        elemento = lista[i]
        #Lista sin el elemento actual
        resto = lista[:i] + lista[i+1:]
        #Obtener permutaciones del resto
        for perm in permutaciones(resto):
            #Agregar elemento al inicio de cada permutación
            resultado.append([elemento]+perm)

        
    return resultado