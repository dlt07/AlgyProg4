def cambio(cantidad, monedas):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float ('inf')
    
    minimo = float ('inf')

    for moneda in monedas:
        resultado = cambio(cantidad - moneda, monedas)
        minimo = min(resultado + 1, minimo)

    return minimo

monedas = [1, 5, 10, 25]
print(cambio(30, monedas))

