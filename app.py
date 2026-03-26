class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self, elementos = 0):
        self.cabeza = None
        self.tamaño = 0
        
    def esta_vacio(self):
            return self.tamaño == 0

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
            self.tamaño += 1
            return True
        
    def eliminar(self, x):
            if self.esta_vacio():
                return False
            
            if self.cabeza.dato == x:
                self.cabeza = self.cabeza.siguiente
                tamaño -= 1
                return True
            
            actual = self.cabeza
            while actual.siguiente:
                if actual.siguiente.dato == x:
                    actual.siguiente = actual.siguiente.siguiente
                    self.tamaño -= 1
                    return True
                actual = actual.siguiente
            return False
        
    def union(self, otro):
            resultado = Conjunto()

            actual = self.cabeza
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
        
    def diferencia(self,otro):
            resultado = Conjunto()
            actual = self.cabeza

            while actual:
                if not otro.pertenece(actual.dato):
                    resultado.agregar(actual.dato)

                actual = actual.siguiente
            return resultado
        
    def diferencia_simetrica(self, otro):
            return self.diferencia(otro).union(otro.diferencia(self))

        
    def a_lista(self):

            resultado = []

            actual = self.cabeza
            while actual:
                resultado.append(actual.dato)
                actual = actual.siguiente
            return resultado
        
    def __str__(self): #Reemplazar el comportamiento cuando hago un print
            return '{' + ','.join(str(x)for x in self.a_lista())+'}'


    '''Una empresa necesita un sistema de control de acceso basado en roles.
        Cada rol tiene un conjunto de permisos. El sistema debe:
        
        1. Verificar si un usuario puede realizar una acción
        2. Encontrar permisos comunes entre roles
        3. Encontrar permisos exclusivos de cada rol
        4. Verificar si un rol es "superior" a otro (tiene todos sus permisos)
        5. Crear un nuevo rol combianando permisos de otros
        
        Implementar usando operaciones de conjuntos'''

roles = {'admin':{'leer','escribir','editar','eliminar','crear_usuarios','ver_logs',
        'configurar','backup','restaurar'},
        'editor':{'leer','escribir','subir_archivo'},
        'viewer':{'leer'},
        'moderador':{'leer','escribir','editar','eliminar'},
        'auditor':{'leer','ver_logs','ver_logs'}}

usuarios = {
    'juan' : 'admin',
    'maria' : 'editor',
    'pedro' : 'viewer',
    'ana' : 'moderador',
    'luis' : 'auditor'
}

#Hacer los puntos usando los metodos de operaciones entre conjuntos

# Verificar si un usuario puede realizar una acción
def puede_realizar(usuario, accion):
    usuario_rol = Conjunto(usuarios.values())
    if not usuario_rol.pertenece(usuario):
        return False
    rol_usuario = usuario_rol.diferencia(Conjunto([usuario]))
    permisos_usuario = roles[rol_usuario.a_lista()[0]]
    return accion in permisos_usuario

# Encontrar permisos comunes entre roles usando los metodos de operaciones entre conjuntos
def permisos_comunes(rol1, rol2):
    conjunto_rol1 = Conjunto(roles[rol1])
    conjunto_rol2 = Conjunto(roles[rol2])
    return conjunto_rol1.interseccion(conjunto_rol2)
# Encontrar permisos exclusivos de cada rol comparando con todos los demás roles usando los metodos de operaciones entre conjuntos
def permisos_exclusivos(rol1, roles):
    conjunto_rol1 = Conjunto(roles[rol1])
    permisos_exclusivos_rol1 = conjunto_rol1
    for rol in roles:
        if rol != rol1:
            conjunto_rol = Conjunto(roles[rol])
            permisos_exclusivos_rol1 = permisos_exclusivos_rol1.diferencia(conjunto_rol)
    return permisos_exclusivos_rol1
         
# Verificar si un rol es "superior" a otro (tiene todos sus permisos) usando los metodos de operaciones entre conjuntos
def es_superior(rol1, rol2):
    conjunto_rol1 = Conjunto(roles[rol1])
    conjunto_rol2 = Conjunto(roles[rol2])
    return conjunto_rol2.diferencia(conjunto_rol1).esta_vacio()
# Crear un nuevo rol combinando permisos de otros usando los metodos de operaciones entre conjuntos
def crear_rol_combinado(nuevo_rol, rol1, rol2):
    conjunto_rol1 = Conjunto(roles[rol1])
    conjunto_rol2 = Conjunto(roles[rol2])
    nuevo_conjunto = conjunto_rol1.union(conjunto_rol2)
    roles[nuevo_rol] = set(nuevo_conjunto.a_lista())


# Ejemplo de uso
print(puede_realizar('juan', 'editar'))  # True
print(permisos_comunes('admin', 'moderador'))  # {'leer', 'escribir', 'editar', 'eliminar'}
print(permisos_exclusivos('admin', roles))  # ({'crear_usuarios', 'ver_logs', 'configurar', 'backup', 'restaurar'}, set())
print(es_superior('admin', 'editor'))  # True
crear_rol_combinado('super_editor', 'editor', 'moderador') # Crea un nuevo rol 'super_editor' que combina los permisos de 'editor' y 'moderador'
print(roles['super_editor'])  # {'leer', 'escribir', 'subir_archivo', 'editar', 'eliminar'} 

#TAREA, IMPLEMENTAR TODO ESTO CON LISTAS

