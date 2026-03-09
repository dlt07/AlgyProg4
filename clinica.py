'''prioridad = 1, 2, 3....
    nombre
    orden de llegada = 1, 2, 3, 4....
    (1, 2, nombre)
    '''
#Tupla de Paciente donde su primera posicion sea la prioridad
#Su segunda posicion el orden


import heapq as h

    
def paciente():
       
        print("=" * 60)
        print("CLINICA")
        print("=" * 60)

        print("1) Agregar un paciente")
        print("2) Salir")

     
        for paciente in pacientes:

            op = input("Elige una opción")
        
            if op == "1":
                prioridad = input("\nIngrese la prioridad del paciente 1 siendo muy prioritario y 3 la menor")
                orden = input("\nIngrese el orden del paciente 1 siendo que llegó primero y 3 de ultimo")
                nombre = input("\nIngrese el nombre del paciente")
            elif op == "0":
                print("Saliendo...")
                return 0
        pacientes = [(prioridad, orden, nombre)]

        h.heappush(paciente)
        print(f" Arbol: {paciente}")


paciente()




      



    

    

