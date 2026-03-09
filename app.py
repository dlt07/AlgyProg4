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
        new = Nodo(dato)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        dato = self.top.dato
        self.top = self.top.next
        return dato
    
    def peek(self):
        return None if self.esta_vacia() else self.top.dato

    @staticmethod
    def infija_a_postfija(expresion):
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida = []
        pila = Pila()

        # IMPORTANTE: aquí NO quitamos espacios, porque vamos a usar split()
        tokens = expresion.split()

        for token in tokens:
            if token.lstrip('-').replace('.', '', 1).isdigit():  # <- isdigit()
                salida.append(token)

            elif token == '(':
                pila.push(token)

            elif token == ')':
                while not pila.esta_vacia() and pila.peek() != '(':
                    salida.append(pila.pop())
                pila.pop()  # sacar '('

            elif token in precedencia:
                while (not pila.esta_vacia()
                       and pila.peek() != '('
                       and pila.peek() in precedencia
                       and precedencia[pila.peek()] >= precedencia[token]):
                    salida.append(pila.pop())
                pila.push(token)

        # Vaciar pila al final (FUERA del for)
        while not pila.esta_vacia():
            salida.append(pila.pop())

        return " ".join(salida)


# Llamada FUERA de la clase
print(Pila.infija_a_postfija("3 + ( 5 * 2 )"))  