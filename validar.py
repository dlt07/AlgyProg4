'''Validar si una expresión cierra bien una expresión, True está bien, false está mal. Se debe usar pilas, push, pop. Comparar expresiones'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class Pila:
    def __init__(self):
        self.top = None

    def esta_vacia(self):
        return self.top is None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.next = self.top
        self.top = nuevo

    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.top.dato
        self.top = self.top.next
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self.top.dato


def validar_expresion(expresion):
    pila = Pila()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caracter in expresion:
        # Si es apertura, se mete a la pila
        if caracter in "([{":
            pila.push(caracter)

        # Si es cierre, se compara con el tope
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False

            tope = pila.pop()

            if tope != pares[caracter]:
                return False

    # Si al final la pila quedó vacía, está bien
    return pila.esta_vacia()


# Pruebas
print(validar_expresion("([4+5]*2)"))     # True
print(validar_expresion("([4+5+7)]"))     # False
print(validar_expresion("{[2+(3*4)]}"))   # True
print(validar_expresion("( [ ] { )"))     # False
print(validar_expresion("[(3+2)]"))        # False