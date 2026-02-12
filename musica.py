class Nodo:
    def __init__(self, dato): #Guardar canción
        self.dato = dato      
        self.next = None
        self.prev = None


class Cancion:
    def __init__(self, nombreCancion, duracion, artista):
        self.nombreCancion = nombreCancion
        self.duracion = duracion
        self.artista = artista

    def __str__(self):
        return f"'{self.nombre}' - {self.artista} ({self.duracion})"


class PlaylistCircularDoble:
    def __init__(self):
        self.cabeza = None
        self.actual = None   

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_final(self, cancion: Cancion):
        nuevo = Nodo(cancion)

        if self.esta_vacia():
            nuevo.next = nuevo
            nuevo.prev = nuevo
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            ultimo = self.cabeza.prev

            # Conectar nuevo entre ultimo y cabeza
            nuevo.next = self.cabeza
            nuevo.prev = ultimo
            ultimo.next = nuevo
            self.cabeza.prev = nuevo

        print("Canción agregada exitosamente.")

    def mostrar_actual(self):
        if self.esta_vacia():
            print("Playlist vacía. No hay canción sonando.")
        else:
            print("SONANDO AHORA:", self.actual.dato)

    def siguiente(self):
        if self.esta_vacia():
            print("Playlist vacía.")
        else:
            self.actual = self.actual.next
            self.mostrar_actual()

    def anterior(self):
        if self.esta_vacia():
            print("Playlist vacía.")
        else:
            self.actual = self.actual.prev
            self.mostrar_actual()

    def mostrar_playlist(self):
        if self.esta_vacia():
            print("Playlist vacía.")
            return

        print("PLAYLIST:")
        temp = self.cabeza
        i = 1
        while True:
            marcador = " <== ACTUAL" if temp == self.actual else ""
            print(f"{i}. {temp.dato}{marcador}")
            temp = temp.next
            i += 1
            if temp == self.cabeza:
                break


def menu():
    print("\n=== APP DE MÚSICA ===")
    print("1) Ver canción actual")
    print("2) Siguiente canción")
    print("3) Canción anterior")
    print("4) Agregar canción al final")
    print("5) Mostrar playlist completa")
    print("0) Salir")


# --- Prueba / Programa principal ---
playlist = PlaylistCircularDoble()

# Puedes precargar unas canciones para probar
playlist.agregar_al_final(Cancion("Blinding Lights", "3:20", "The Weeknd"))
playlist.agregar_al_final(Cancion("Nights", "5:07", "Frank Ocean"))
playlist.agregar_al_final(Cancion("Pasarela", "3:30", "Reykon"))

while True:
    menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        playlist.mostrar_actual()
    elif opcion == "2":
        playlist.siguiente()
    elif opcion == "3":
        playlist.anterior()
    elif opcion == "4":
        nombre = input("Nombre de la canción: ").strip()
        artista = input("Artista: ").strip()
        duracion = input("Duración (ej: 3:45): ").strip()
        playlist.agregar_al_final(Cancion(nombre, duracion, artista))
    elif opcion == "5":
        playlist.mostrar_playlist()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
