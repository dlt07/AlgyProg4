# ============================
# LISTA SIMPLE (RECURSIVA)
# ============================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    # Agregar al final de forma recursiva
    def agregar_final(self, dato, nodo=None):
        nuevo = Nodo(dato)

        # Caso 1: lista vacía
        if self.cabeza is None:
            self.cabeza = nuevo
            print("Agregado (era el primero).")
            return

        # Primera llamada: arrancamos desde la cabeza
        if nodo is None:
            nodo = self.cabeza

        # Caso base: si el siguiente es None, este es el último
        if nodo.next is None:
            nodo.next = nuevo
            print("Agregado al final.")
            return

        # Paso recursivo: avanzar
        return self.agregar_final(dato, nodo.next)

    # Mostrar lista recursivamente
    def mostrar(self, nodo=None):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cabeza
            print("LISTA:", end=" ")

        print(nodo.dato, end=" -> ")

        if nodo.next is None:
            print("None")
            return

        return self.mostrar(nodo.next)

    # Contar nodos recursivamente
    def contar(self, nodo=None):
        if self.cabeza is None:
            return 0

        if nodo is None:
            nodo = self.cabeza

        if nodo is None:
            return 0

        if nodo.next is None:
            return 1

        return 1 + self.contar(nodo.next)

    # Buscar dato recursivamente (True/False)
    def buscar(self, dato, nodo=None):
        if self.cabeza is None:
            return False

        if nodo is None:
            nodo = self.cabeza

        if nodo is None:
            return False

        if nodo.dato == dato:
            return True

        if nodo.next is None:
            return False

        return self.buscar(dato, nodo.next)

    # Eliminar la primera ocurrencia (recursivo)
    def eliminar(self, dato, nodo=None, anterior=None):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cabeza
            anterior = None

        # Si encontramos el dato
        if nodo.dato == dato:
            # Si es la cabeza
            if anterior is None:
                self.cabeza = nodo.next
            else:
                anterior.next = nodo.next
            print("Dato eliminado.")
            return

        # Si llegamos al final y no está
        if nodo.next is None:
            print("Dato no encontrado.")
            return

        # Paso recursivo
        return self.eliminar(dato, nodo.next, nodo)


def menu():
    print("\n=== LISTA SIMPLE (RECURSIVA) ===")
    print("1) Agregar al final")
    print("2) Mostrar")
    print("3) Contar")
    print("4) Buscar")
    print("5) Eliminar")
    print("0) Salir")


if __name__ == "__main__":
    lista = ListaSimple()

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            d = input("Dato: ")
            lista.agregar_final(d)
        elif op == "2":
            lista.mostrar()
        elif op == "3":
            print("Total:", lista.contar())
        elif op == "4":
            d = input("Dato a buscar: ")
            print("Encontrado." if lista.buscar(d) else "No está.")
        elif op == "5":
            d = input("Dato a eliminar: ")
            lista.eliminar(d)
        elif op == "0":
            break
        else:
            print("Opción inválida.")