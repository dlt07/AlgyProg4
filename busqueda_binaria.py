def buscar_binario(lista, objetivo, inicio=0, fin=None): 
    if fin is None:
        fin = len(lista)-1
    
    #Inicializar fin en la primera llamada
    if inicio > fin:
        return -1
    
    #Calcular punto medio
    medio = (inicio + fin)//2

    if lista[medio] == objetivo:
        return medio #Encontrado
    
    elif objetivo < lista[medio]:
        #Buscar en la mitad izquierda
        return buscar_binario(lista, objetivo, inicio, medio -1)
    else:
        #Buscar en la mitad derecha
        return buscar_binario(lista, objetivo, medio+1, fin)