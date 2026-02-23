# =========================
#   APP DE MÚSICA (RECURSIVA)
#   Playlist circular doble
# =========================

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.next = None
        self.prev = None


class Cancion:
    def __init__(self, nombre, duracion, artista):
        self.nombre = nombre
        self.duracion = duracion
        self.artista = artista

    def __str__(self):
        # Cómo se verá cuando imprimimos una canción
        return f"'{self.nombre}' - {self.artista} ({self.duracion})"


class PlaylistCircularDoble:
    def __init__(self):
        self.cabeza = None   # primer nodo
        self.actual = None   # nodo "sonando ahora"

    # -----------------------------------
    # Agregar canción al final (RECURSIVO)
    # -----------------------------------
    def agregar_al_final(self, cancion, nodo_actual=None):
        """
        Este método es recursivo y se llama así:
        playlist.agregar_al_final(Cancion(...))

        Internamente, usa nodo_actual para recorrer hasta el último.
        """

        nuevo = Nodo(cancion)

        # Caso 1: lista vacía -> el nuevo se apunta a sí mismo (circular)
        if self.cabeza is None:
            nuevo.next = nuevo
            nuevo.prev = nuevo
            self.cabeza = nuevo
            self.actual = nuevo
            print("Canción agregada (primera en la playlist).")
            return

        # Si no me pasaron nodo_actual, arrancamos desde la cabeza
        if nodo_actual is None:
            nodo_actual = self.cabeza

        # En una lista circular doble, "el último" es el que apunta a cabeza
        # o más fácil: el último es cabeza.prev
        # Pero como queremos hacerlo recursivo "recorriendo", detectamos el último
        if nodo_actual.next == self.cabeza:
            # nodo_actual es el último, insertamos nuevo entre último y cabeza
            ultimo = nodo_actual

            nuevo.next = self.cabeza
            nuevo.prev = ultimo

            ultimo.next = nuevo
            self.cabeza.prev = nuevo

            print("Canción agregada al final.")
            return

        # Paso recursivo: avanzar al siguiente nodo
        return self.agregar_al_final(cancion, nodo_actual.next)

    # -----------------------------
    # Mostrar canción actual (O(1))
    # -----------------------------
    def mostrar_actual(self):
        if self.actual is None:
            print("Playlist vacía. No hay canción sonando.")
        else:
            print("SONANDO AHORA:", self.actual.cancion)

    # ------------------------------------
    # Ir a la siguiente canción (O(1))
    # ------------------------------------
    def siguiente(self):
        if self.actual is None:
            print("Playlist vacía.")
            return
        self.actual = self.actual.next
        self.mostrar_actual()

    # ------------------------------------
    # Ir a la canción anterior (O(1))
    # ------------------------------------
    def anterior(self):
        if self.actual is None:
            print("Playlist vacía.")
            return
        self.actual = self.actual.prev
        self.mostrar_actual()

    # ----------------------------------------
    # Mostrar playlist completa (RECURSIVO)
    # ----------------------------------------
    def mostrar_playlist(self, nodo=None, inicio=None, i=1):
        """
        Recorrido recursivo de una lista circular:
        - inicio: el nodo donde empezamos (para saber cuándo parar)
        - nodo: nodo actual que estamos imprimiendo
        - i: contador para numeración
        """

        if self.cabeza is None:
            print("Playlist vacía.")
            return

        # Primera llamada: definimos nodo e inicio
        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza
            print("PLAYLIST:")

        # Imprimimos el nodo actual
        marca = " <== ACTUAL" if nodo == self.actual else ""
        print(f"{i}. {nodo.cancion}{marca}")

        # Si el siguiente vuelve al inicio, terminamos (para no hacer infinito)
        if nodo.next == inicio:
            return

        # Paso recursivo
        return self.mostrar_playlist(nodo.next, inicio, i + 1)

    # ----------------------------------------
    # Contar canciones (RECURSIVO)
    # ----------------------------------------
    def contar_canciones(self, nodo=None, inicio=None):
        """
        Retorna cuántos nodos hay en la playlist.
        """

        if self.cabeza is None:
            return 0

        # Primera llamada
        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza

        # Si el siguiente vuelve al inicio, esta es la última canción a contar
        if nodo.next == inicio:
            return 1

        # 1 por este nodo + lo que falta
        return 1 + self.contar_canciones(nodo.next, inicio)

    # ----------------------------------------
    # Buscar canción por nombre (RECURSIVO)
    # Devuelve True/False
    # ----------------------------------------
    def buscar_por_nombre(self, nombre, nodo=None, inicio=None):
        """
        Busca si existe una canción con ese nombre (ignorando mayúsculas/minúsculas).
        """

        if self.cabeza is None:
            return False

        if nodo is None:
            nodo = self.cabeza
            inicio = self.cabeza

        if nodo.cancion.nombre.lower() == nombre.lower():
            return True

        if nodo.next == inicio:
            return False

        return self.buscar_por_nombre(nombre, nodo.next, inicio)


# =========================
#         MENÚ
# =========================

def menu():
    print("\n=== APP DE MÚSICA (PLAYLIST CIRCULAR DOBLE) ===")
    print("1) Ver canción actual")
    print("2) Siguiente canción")
    print("3) Canción anterior")
    print("4) Agregar canción")
    print("5) Mostrar playlist")
    print("6) Contar canciones")
    print("7) Buscar canción por nombre")
    print("0) Salir")


# Programa principal
playlist = PlaylistCircularDoble()

# Precarga (opcional) para que puedas probar rápido
playlist.agregar_al_final(Cancion("Nights", "5:07", "Frank Ocean"))
playlist.agregar_al_final(Cancion("Blinding Lights", "3:20", "The Weeknd"))
playlist.agregar_al_final(Cancion("Pasarela", "3:30", "Reykon"))

while True:
    menu()
    op = input("Elige una opción: ").strip()

    if op == "1":
        playlist.mostrar_actual()

    elif op == "2":
        playlist.siguiente()

    elif op == "3":
        playlist.anterior()

    elif op == "4":
        nombre = input("Nombre: ").strip()
        artista = input("Artista: ").strip()
        duracion = input("Duración (ej 3:45): ").strip()
        playlist.agregar_al_final(Cancion(nombre, duracion, artista))

    elif op == "5":
        playlist.mostrar_playlist()

    elif op == "6":
        print("Total de canciones:", playlist.contar_canciones())

    elif op == "7":
        nombre = input("Nombre a buscar: ").strip()
        existe = playlist.buscar_por_nombre(nombre)
        print("Sí está en la playlist." if existe else "No está en la playlist.")

    elif op == "0":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")