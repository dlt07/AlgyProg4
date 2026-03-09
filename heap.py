import heapq as h

def demo_operaciones_basicas():

    print("=" * 60)
    print("OPERACIONES BASICAS")
    print("=" * 60)


    print("\n1. Crear Heap (heapify)")
    datos = [5, 3, 8, 1, 2, 9, 4]
    print(f"Lista Original: {datos}")

    h.heapify(datos)
    print(f" Despues de hipify: {datos}")

demo_operaciones_basicas()