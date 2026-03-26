conjunto_juan = {
    "Blinding Lights",
    "Levitating",
    "Bad Habits",
    "Stay",
    "As It Was",
    "Watermelon Sugar",
    "Shivers"
}

conjunto_maria = {
    "Stay",
    "Shivers",
    "Industry Baby",
    "Flowers",
    "Levitating",
    "Heat Waves",
    "As It Was"
}


playlist_comun = conjunto_juan & conjunto_maria #Intersección de canciones que les gustan a los 2
recomendaciones_juan = conjunto_maria - conjunto_juan #Canciones que tenga Maria pero que no tenga Juan
catalogo =  conjunto_juan | conjunto_maria #Unión de los 2 conjuntos
a = {conjunto_juan <= conjunto_maria} 
exclusivas = conjunto_juan ^ conjunto_maria

algoritmos = {'Ana', 'Luis', 'Carlos', 'Sofia', 'Maria'}

bases_datos = {'Carlos', 'Diana', 'Sofia', 'Maria', 'Juan'}

redes = {'Natalia', 'Eduardo', 'Ivan', 'Sofia', 'Maria'}

estudian_todas = algoritmos & bases_datos & redes #Intersección de los 3 conjuntos
solo_algoritmos = algoritmos - (bases_datos | redes) #Alumnos que solo estudian algoritmos
solo_bases_datos = bases_datos - (algoritmos | redes) #Alumnos que solo estudian bases de datos
solo_redes = redes - (algoritmos | bases_datos) #Alumnos que solo estudian redes
solo_en_una = solo_algoritmos | solo_bases_datos | solo_redes #Alumnos que estudian solo una materia


#Algoritmo para saber en que materia estudia cada alumno
materias = {} #Diccionario para almacenar el nombre del alumno como clave y la materia como valor

for alumno in algoritmos:
    materias[alumno] = 'Algoritmos'
for alumno in bases_datos:
    if alumno in materias:
        materias[alumno] += ' y Bases de Datos'
    else:
        materias[alumno] = 'Bases de Datos'

for alumno in redes:
    if alumno in materias:
        materias[alumno] += ' y Redes'
    else: #Si el alumno no está en el diccionario, se agrega con la materia de redes
        materias[alumno] = 'Redes'

print("Alumnos y sus materias:")
for alumno, materia in materias.items():
    print(f"{alumno}: {materia}")



catalogo_peliculas = {
    'Inception': {'ciencia ficcion', 'accion', 'thriller', 'Drama'},
    'Matrix': {'Ciencia Ficción', 'Acción', 'Thriller'},
    'The Notebook': {'romance', 'drama', 'historica'},
    'Avengers': {'acción', 'ciencia ficción', 'aventura'},
    'John Wick': {'accion', 'ciencia ficción', 'aventura'},
    'Interestellar': {'Ciencia Ficción', 'drama', 'thriller'},
}

peliculas = list(catalogo.keys())

for i in range (len(peliculas)):
    peliculas_comunes = []
    for j in range(i+1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[i+1]
        comunes = catalogo[p1] & catalogo[p2]
        if len(comunes) >= 2:
            peliculas_comunes.append((p1, p2, comunes))

print (peliculas_comunes)

favoritos_mios = {'acción', 'thriller', 'aventura'}
recomendaciones = []

for pelicula, generos in catalogo.items():
    coincidencia = generos & favoritos_mios

    if coincidencia:
        porcentaje = round(len(coincidencia/len(favoritos_mios))) * 100
        recomendaciones.append((pelicula, porcentaje))

print (recomendaciones)
