class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamano = 0

        if elementos is not None:
            for elemento in elementos:
                self.agregar(elemento)

    def esta_vacio(self):
        return self.tamano == 0

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return False

        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        return True

    def eliminar(self, x):
        if self.esta_vacio():
            return False

        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamano -= 1
                return True
            actual = actual.siguiente

        return False

    def union(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado

    def interseccion(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado

    def diferencia(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado

    def diferencia_simetrica(self, otro):
        return self.diferencia(otro).union(otro.diferencia(self))

    def es_subconjunto_de(self, otro):
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __str__(self):
        return "{" + ", ".join(self.a_lista()) + "}"


# ==============================
# ROLES Y USUARIOS
# ==============================

roles = {
    'admin': Conjunto([
        'leer', 'escribir', 'editar', 'eliminar',
        'crear_usuarios', 'ver_logs', 'configurar',
        'backup', 'restaurar'
    ]),
    'editor': Conjunto([
        'leer', 'escribir', 'subir_archivo'
    ]),
    'viewer': Conjunto([
        'leer'
    ]),
    'moderador': Conjunto([
        'leer', 'escribir', 'editar', 'eliminar'
    ]),
    'auditor': Conjunto([
        'leer', 'ver_logs'
    ])
}

usuarios = {
    'juan': 'admin',
    'maria': 'editor',
    'pedro': 'viewer',
    'ana': 'moderador',
    'luis': 'auditor'
}


# 1. Verificar si un usuario puede realizar una acción
def puede_realizar(usuario, accion):
    if usuario not in usuarios:
        return False

    rol_usuario = usuarios[usuario]
    permisos = roles[rol_usuario]
    return permisos.pertenece(accion)


# 2. Encontrar permisos comunes entre roles
def permisos_comunes(rol1, rol2):
    return roles[rol1].interseccion(roles[rol2])


# 3. Encontrar permisos exclusivos de cada rol
def permisos_exclusivos(rol1, rol2):
    exclusivos_rol1 = roles[rol1].diferencia(roles[rol2])
    exclusivos_rol2 = roles[rol2].diferencia(roles[rol1])
    return exclusivos_rol1, exclusivos_rol2


# 4. Verificar si un rol es superior a otro
def es_superior(rol1, rol2):
    return roles[rol2].es_subconjunto_de(roles[rol1])


# 5. Crear un nuevo rol combinando permisos de otros
def crear_rol_combinado(nuevo_rol, rol1, rol2):
    roles[nuevo_rol] = roles[rol1].union(roles[rol2])


# ==============================
# PRUEBAS
# ==============================

print("1. ¿Juan puede editar?")
print(puede_realizar('juan', 'editar'))   # True

print("\n2. Permisos comunes entre admin y moderador:")
print(permisos_comunes('admin', 'moderador'))

print("\n3. Permisos exclusivos entre admin y editor:")
ex_admin, ex_editor = permisos_exclusivos('admin', 'editor')
print("Solo admin:", ex_admin)
print("Solo editor:", ex_editor)

print("\n4. ¿Admin es superior a editor?")
print(es_superior('admin', 'editor'))   # True

print("\n5. Crear rol combinado super_editor = editor + moderador")
crear_rol_combinado('super_editor', 'editor', 'moderador')
print(roles['super_editor'])