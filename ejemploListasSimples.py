class Node:
    def __init__(self, nombre, cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.next = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def AddNodeAtTheEnd(self, nombre, cedula, prioridad):
        node = Node(nombre, cedula, prioridad)

        if self.cabeza == None:
            self.cabeza = node
        else:
            actual = self.cabeza
            while actual.next != None:
                actual = actual.next
            
            actual.next = node
        print("Nodo agregado exitosamente")


    def Mostrar(self):
        actual = self.cabeza
        while actual:
            print("************")
            print(actual.nombre, actual.cedula, actual.prioridad, end= "-->")               
            actual = actual.next
        print("Fin")

    def AddWithPriority(self, nombre, cedula, prioridad):
        node = Node(nombre, cedula, prioridad)

        if self.cabeza == None:
            self.cabeza = node
        elif self.cabeza.prioridad > prioridad:
            node.next = self.cabeza
            self.cabeza = node

        else:
            actual = self.cabeza
            while actual.next and actual.next.prioridad <= prioridad:
                actual = actual.next
            node.next = actual.next
            actual.next = node
 

lista = Lista()
lista.AddNodeAtTheEnd("Juan", 1111, 3)
lista.Mostrar()
    

