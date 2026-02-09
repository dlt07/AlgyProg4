class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.prev = None

class Cancion:
    def __init__(self, nombre, duracion, artista):
        self.nombre = nombre
        self.duracion = duracion
        self.artista = artista