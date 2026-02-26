class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = next

class Pila:
    def __init__(self):
        self.top = None
        self.size = 0

    def esta_vacia(self):
        return self.top is None
    
    def push(self, dato):
        new = Nodo(dato)
        new.next = self.top
        self.top = new
        self.size += 1

    def pop(self):
        if self.esta_vacia():
            raise Exception('Error: L pila está vacia')
        dato = self.top.dato
        self.top = self.top.next
        self.size -= 1
        return dato


    """def evaluar_postfija(self, dato):
        if dato == '+':
            return dato + dato
        elif dato == '-':
            return dato - dato
        elif dato == '*':
            return dato * dato
        elif dato == '/':
            if dato == 0:
                raise ZeroDivisionError("División por cero.")
            return dato / dato
        else:
            raise ValueError(f"Operador no válido: {dato}") """
    
    def evaluar_postfija(expresion):
        pila = Pila()
        tokens = expresion.split()

        operadores = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: a/b,
            '%': lambda a, b: a%b,
            '**': lambda a, b: a**b,
        }

        for token in tokens:
            if token.lstrip('-').replace('.','').isdigit():
                #Es un numero (soporta negativos y decimales)
                valor = float (token) if '.'in token else int(token)
                pila.push(valor)
                print (f" Token '{token}'")
        
     
        

