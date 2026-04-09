import re

# 1. VALOR 20%

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.

    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123
    """
    return re.match(r"^[A-Z]{3}-?\d{3}$", placa) is not None


def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.
    """
    return re.findall(r"#[A-Za-z0-9_]+", texto)


# 2. VALOR 30%

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pedidos")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    def agregar(self, cliente, direccion, valor):
        """
        Agrega un nuevo pedido al FINAL de la lista.
        OBLIGATORIO usar recursividad.
        """
        nuevo = Pedido(cliente, direccion, valor)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        def agregar_recursivo(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                agregar_recursivo(nodo.siguiente)

        agregar_recursivo(self.cabeza)

    def valor_pendiente(self):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.
        """
        def sumar_recursivo(nodo):
            if nodo is None:
                return 0
            valor_actual = 0 if nodo.entregado else nodo.valor
            return valor_actual + sumar_recursivo(nodo.siguiente)

        return sumar_recursivo(self.cabeza)

    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.
        OBLIGATORIO usar recursividad.
        Modifica la lista original.
        """
        def eliminar_recursivo(nodo):
            if nodo is None:
                return None

            nodo.siguiente = eliminar_recursivo(nodo.siguiente)

            if nodo.entregado:
                return nodo.siguiente

            return nodo

        self.cabeza = eliminar_recursivo(self.cabeza)


# 3. VALOR 20%

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    (Intersección de los tres)
    """
    return club_ciencias & club_deportes & club_arte


def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.
    """
    solo_ciencias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_ciencias - club_deportes

    return solo_ciencias | solo_deportes | solo_arte


def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.
    """
    clubes = []

    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")

    return clubes


# 4. VALOR 30%

def escalones_sin_memo(n):
    """
    Calcula de cuántas formas se puede subir una escalera de n escalones.
    En cada paso puedes subir 1 o 2 escalones.

    Implementar con recursividad pura (sin memorización).
    """
    if n == 0 or n == 1:
        return 1
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)


def escalones_con_memo(n, memo=None):
    """
    Misma función pero usando un diccionario para guardar resultados
    ya calculados y evitar recalcular.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 1

    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]