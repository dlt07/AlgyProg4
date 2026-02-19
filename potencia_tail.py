def potencia_lista_tail(base, exp, acumulador=1):
    if base == 0:
        return acumulador
    return potencia_lista_tail(base, exp - 1, acumulador * base)

