"""def suma_lista_tail(lista):
    list = [1,2,3,4,5]
    if len(lista) == 0:
        return -1
    actual = lista[0]
    next = lista[i+1]
    return suma_lista_tail(actual + next)

import time
inicio = time.time()

print(suma_lista_tail(100))

fin = time.time()-inicio"""""


def suma_lista_tail(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista_tail(lista[1:], acumulador + lista[0])
