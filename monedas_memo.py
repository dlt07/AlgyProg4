def cambio_memo(cantidad, monedas, memo={}):
    if cantidad in memo:
        return memo[cantidad]
    

    #CASOS BASE
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf') #Retorna infinito
    
    minimo = float ('inf') 
    for moneda in monedas:
        resultado = cambio_memo(cantidad - moneda,monedas, memo)
        minimo = min(minimo, resultado + 1)

    memo[cantidad] = minimo
    return minimo