lista = [1,2,3,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

conjunto = set(lista)
conjunto_lista = list(set(lista)) #Imprime con [] como si fuera una lista

print(conjunto)
print (conjunto_lista)

#Remove si el elemento no existe, sale error
#Discard No saca error
#Add añade elementos
#Pop() Saca cualquier elemento
#For num in numeros
#Para ordenar, se convierte a una lista. sorted(conjunto)

"""j
A|B --> Unión
A.intersection(B) --> Intersección
A-B o B-A (No es conmutativa) --> Diferencia
A^B | (A-B)|(B-A) --> Diferencia Siemtrica
issubset --> Saber si un subconjunto es conjunto de otro --> A.issubset(B) a ES SUBCONJUNTO DE B
A < B --> A es subcojunto propio de B
A = B --> Igualdad --> No importa el orden entonces A = {1, 2} B = {2, 1} son iguales
"""