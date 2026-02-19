def potencia(a, b):
    if b == 0:
        return
    return a * potencia(a, b - 1)

def potencia_optimizado (a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        mitad = potencia_optimizado(a, b // 2)
        return mitad * mitad
    else:
        return a * potencia_optimizado(a, b - 1)
    
def suma_digitos(n):
    #Si n es menor a 10 retorna el numero
    if n < 10:
        return n
    #Toma el ultimo digito
    digito = n % 10 
    #Suma el digito a el div de n
    return digito + suma_digitos(n // 10) 

    
