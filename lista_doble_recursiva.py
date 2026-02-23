# ============================
# LISTA DOBLE (RECURSIVA)
# ============================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.prev = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None  # útil para mostrar hacia atrás

    # Agregar al final (recursivo recorriendo desde cabeza)
    def agregar_final(self, dato, nodo=None):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            print("Agregado (era el primero).")
            return

        if nodo is None:
            nodo = self.cabeza

        if nodo.next is None:
            nodo.next = nuevo
            nuevo.prev = nodo
            self.cola = nuevo
            print("Agregado al final.")
            return

        return self.agregar_final(dato, nodo.next)

    # Mostrar hacia adelante (recursivo)
    def mostrar_adelante(self, nodo=None):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cabeza
            print("ADELANTE:", end=" ")

        print(nodo.dato, end=" <-> ")

        if nodo.next is None:
            print("None")
            return

        return self.mostrar_adelante(nodo.next)

    # Mostrar hacia atrás (recursivo desde cola)
    def mostrar_atras(self, nodo=None):
        if self.cola is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cola
            print("ATRÁS:", end=" ")

        print(nodo.dato, end=" <-> ")

        if nodo.prev is None:
            print("None")
            return

        return self.mostrar_atras(nodo.prev)

    # Contar (recursivo)
    def contar(self, nodo=None):
        if self.cabeza is None:
            return 0

        if nodo is None:
            nodo = self.cabeza

        if nodo.next is None:
            return 1

        return 1 + self.contar(nodo.next)

    # Buscar (recursivo)
    def buscar(self, dato, nodo=None):
        if self.cabeza is None:
            return False

        if nodo is None:
            nodo = self.cabeza

        if nodo.dato == dato:
            return True

        if nodo.next is None:
            return False

        return self.buscar(dato, nodo.next)

    # Eliminar primera ocurrencia (recursivo)
    def eliminar(self, dato, nodo=None):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cabeza

        if nodo.dato == dato:
            # Caso: es cabeza
            if nodo.prev is None:
                self.cabeza = nodo.next
                if self.cabeza is not None:
                    self.cabeza.prev = None
                else:
                    self.cola = None  # quedó vacía
            # Caso: es cola
            elif nodo.next is None:
                self.cola = nodo.prev
                self.cola.next = None
            # Caso: está en medio
            else:
                nodo.prev.next = nodo.next
                nodo.next.prev = nodo.prev

            print("Dato eliminado.")
            return

        if nodo.next is None:
            print("Dato no encontrado.")
            return

        return self.eliminar(dato, nodo.next)


def menu():
    print("\n=== LISTA DOBLE (RECURSIVA) ===")
    print("1) Agregar al final")
    print("2) Mostrar adelante")
    print("3) Mostrar atrás")
    print("4) Contar")
    print("5) Buscar")
    print("6) Eliminar")
    print("0) Salir")


if __name__ == "__main__":
    lista = ListaDoble()

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            d = input("Dato: ")
            lista.agregar_final(d)
        elif op == "2":
            lista.mostrar_adelante()
        elif op == "3":
            lista.mostrar_atras()
        elif op == "4":
            print("Total:", lista.contar())
        elif op == "5":
            d = input("Dato a buscar: ")
            print("Encontrado." if lista.buscar(d) else "No está.")
        elif op == "6":
            d = input("Dato a eliminar: ")
            lista.eliminar(d)
        elif op == "0":
            break
        else:
            print("Opción inválida.")