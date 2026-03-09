import heapq as h

def ejemplo_urgencias():

    urgencias = []
    hora = 0

    def llega_paciente(nombre, gravedad):
        nonlocal hora
        hora += 1
        h.heappush(urgencias, (gravedad, hora, nombre))
        nivel = {1: "Critico", 2: "Moderado", 3:"Leve"}

    def atender_siguiente():
        if urgencias:
            gravedad, _, nombre = h.heappop(urgencias)
            print(f"Atendiendo a {nombre}")
            return nombre
        return None



    