# ==========================================
# LISTA CIRCULAR DOBLE (RECURSIVA + MENÚ)
# Tipo playlist: actual, siguiente, anterior
# ==========================================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.prev = None


class CircularDoble:
    def __init__(self):
        self.cabeza = None
        self.actual = None  # puntero a "lo que está sonando"

    # Agregar al final (recursivo)
    def agregar_final(self, dato, nodo=None):
        nuevo = Nodo(dato)

        # Caso: lista vacía -> nodo se apunta a sí mismo
        if self.cabeza is None:
            nuevo.next = nuevo
            nuevo.prev = nuevo
            self.cabeza = nuevo
            self.actual = nuevo
            print("Agregado (primero).")
            return

        # Primera llamada
        if nodo is None:
            nodo = self.cabeza

        # En circular, el último es el que apunta a cabeza
        if nodo.next == self.cabeza:
            ultimo = nodo

            nuevo.next = self.cabeza
            nuevo.prev = ultimo

            ultimo.next = nuevo
            self.cabeza.prev = nuevo

            print("Agregado al final.")
            return

        return self.agregar_final(dato, nodo.next)

    # Mostrar playlist completa (recursivo, parando al volver al inicio)
    def mostrar(self, nodo=None, inicio=None, i=1):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza
            print("PLAYLIST:")

        marca = " <== ACTUAL" if nodo == self.actual else ""
        print(f"{i}. {nodo.dato}{marca}")

        # Parar cuando el siguiente vuelve al inicio
        if nodo.next == inicio:
            return

        return self.mostrar(nodo.next, inicio, i + 1)

    # Contar nodos (recursivo, circular)
    def contar(self, nodo=None, inicio=None):
        if self.cabeza is None:
            return 0

        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza

        if nodo.next == inicio:
            return 1

        return 1 + self.contar(nodo.next, inicio)

    # Buscar (recursivo, circular)
    def buscar(self, dato, nodo=None, inicio=None):
        if self.cabeza is None:
            return False

        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza

        if nodo.dato == dato:
            return True

        if nodo.next == inicio:
            return False

        return self.buscar(dato, nodo.next, inicio)

    # Canción actual (O(1))
    def ver_actual(self):
        if self.actual is None:
            print("Lista vacía.")
        else:
            print("ACTUAL:", self.actual.dato)

    # Siguiente (O(1))
    def siguiente(self):
        if self.actual is None:
            print("Lista vacía.")
            return
        self.actual = self.actual.next
        self.ver_actual()

    # Anterior (O(1))
    def anterior(self):
        if self.actual is None:
            print("Lista vacía.")
            return
        self.actual = self.actual.prev
        self.ver_actual()


def menu():
    print("\n=== CIRCULAR DOBLE (PLAYLIST) ===")
    print("1) Ver actual")
    print("2) Siguiente")
    print("3) Anterior")
    print("4) Agregar al final")
    print("5) Mostrar lista")
    print("6) Contar")
    print("7) Buscar")
    print("0) Salir")


if __name__ == "__main__":
    lista = CircularDoble()

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            lista.ver_actual()
        elif op == "2":
            lista.siguiente()
        elif op == "3":
            lista.anterior()
        elif op == "4":
            d = input("Dato (ej canción): ")
            lista.agregar_final(d)
        elif op == "5":
            lista.mostrar()
        elif op == "6":
            print("Total:", lista.contar())
        elif op == "7":
            d = input("Dato a buscar: ")
            print("Encontrado." if lista.buscar(d) else "No está.")
        elif op == "0":
            break
        else:
            print("Opción inválida.")