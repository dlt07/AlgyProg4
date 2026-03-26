# ═════════════════════════════════════════════════════════════════════
# 1. SPOTIFY - OPERACIONES DE CONJUNTOS
# ═════════════════════════════════════════════════════════════════════

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

playlist_comun = conjunto_juan & conjunto_maria
recomendaciones_juan = conjunto_maria - conjunto_juan
recomendaciones_maria = conjunto_juan - conjunto_maria
catalogo = conjunto_juan | conjunto_maria
subconjunto_juan = conjunto_juan <= conjunto_maria
subconjunto_maria = conjunto_maria <= conjunto_juan
exclusivas = conjunto_juan ^ conjunto_maria

print("=" * 60)
print("SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print("\nCanciones de Juan:")
for cancion in sorted(conjunto_juan):
    print("♪", cancion)

print("\nCanciones de María:")
for cancion in sorted(conjunto_maria):
    print("♪", cancion)

print("\n1. Playlist en común:")
for cancion in sorted(playlist_comun):
    print("♪", cancion)

print("\n2. Recomendaciones para Juan:")
for cancion in sorted(recomendaciones_juan):
    print("→", cancion)

print("\n   Recomendaciones para María:")
for cancion in sorted(recomendaciones_maria):
    print("→", cancion)

print("\n3. Catálogo combinado:")
for cancion in sorted(catalogo):
    print("♪", cancion)

print("\n4. ¿Juan es subconjunto de María?", subconjunto_juan)
print("   ¿María es subconjunto de Juan?", subconjunto_maria)

print("\n5. Canciones exclusivas:")
for cancion in sorted(exclusivas):
    print("♪", cancion)


# ═════════════════════════════════════════════════════════════════════
# 2. UNIVERSIDAD - ESTUDIANTES Y MATERIAS
# ═════════════════════════════════════════════════════════════════════

algoritmos = {'Ana', 'Luis', 'Carlos', 'Sofia', 'Maria'}
bases_datos = {'Carlos', 'Diana', 'Sofia', 'Maria', 'Juan'}
redes = {'Natalia', 'Eduardo', 'Ivan', 'Sofia', 'Maria'}

estudian_todas = algoritmos & bases_datos & redes
solo_algoritmos = algoritmos - (bases_datos | redes)
solo_bases_datos = bases_datos - (algoritmos | redes)
solo_redes = redes - (algoritmos | bases_datos)
solo_en_una = solo_algoritmos | solo_bases_datos | solo_redes

print("\n" + "=" * 60)
print("UNIVERSIDAD - MATERIAS")
print("=" * 60)

print("\nEstudian las 3 materias:")
for alumno in sorted(estudian_todas):
    print("•", alumno)

print("\nSolo estudian Algoritmos:")
for alumno in sorted(solo_algoritmos):
    print("•", alumno)

print("\nSolo estudian Bases de Datos:")
for alumno in sorted(solo_bases_datos):
    print("•", alumno)

print("\nSolo estudian Redes:")
for alumno in sorted(solo_redes):
    print("•", alumno)

print("\nEstudian solo una materia:")
for alumno in sorted(solo_en_una):
    print("•", alumno)


# Diccionario para saber qué materias estudia cada alumno
materias = {}

for alumno in algoritmos:
    materias[alumno] = "Algoritmos"

for alumno in bases_datos:
    if alumno in materias:
        materias[alumno] += " y Bases de Datos"
    else:
        materias[alumno] = "Bases de Datos"

for alumno in redes:
    if alumno in materias:
        materias[alumno] += " y Redes"
    else:
        materias[alumno] = "Redes"

print("\nAlumnos y sus materias:")
for alumno, materia in sorted(materias.items()):
    print(f"{alumno}: {materia}")


# ═════════════════════════════════════════════════════════════════════
# 3. PELÍCULAS Y GÉNEROS
# ═════════════════════════════════════════════════════════════════════

catalogo_peliculas = {
    'Inception': {'ciencia ficción', 'acción', 'thriller', 'drama'},
    'Matrix': {'ciencia ficción', 'acción', 'thriller'},
    'The Notebook': {'romance', 'drama', 'histórica'},
    'Avengers': {'acción', 'ciencia ficción', 'aventura'},
    'John Wick': {'acción', 'thriller', 'aventura'},
    'Interstellar': {'ciencia ficción', 'drama', 'thriller'},
}

peliculas = list(catalogo_peliculas.keys())
peliculas_comunes = []

for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1 = peliculas[i]
        p2 = peliculas[j]
        comunes = catalogo_peliculas[p1] & catalogo_peliculas[p2]

        if len(comunes) >= 2:
            peliculas_comunes.append((p1, p2, comunes))

print("\n" + "=" * 60)
print("PELÍCULAS CON GÉNEROS EN COMÚN")
print("=" * 60)

for p1, p2, comunes in peliculas_comunes:
    print(f"{p1} - {p2}: {sorted(comunes)}")


# ═════════════════════════════════════════════════════════════════════
# 4. RECOMENDACIÓN DE PELÍCULAS SEGÚN GÉNEROS FAVORITOS
# ═════════════════════════════════════════════════════════════════════

favoritos_mios = {'acción', 'thriller', 'aventura'}
recomendaciones = []

for pelicula, generos in catalogo_peliculas.items():
    coincidencia = generos & favoritos_mios

    if coincidencia:
        porcentaje = round((len(coincidencia) / len(favoritos_mios)) * 100)
        recomendaciones.append((pelicula, porcentaje, coincidencia))

print("\n" + "=" * 60)
print("RECOMENDACIONES DE PELÍCULAS")
print("=" * 60)

for pelicula, porcentaje, coincidencia in recomendaciones:
    print(f"{pelicula}: {porcentaje}% de coincidencia -> {sorted(coincidencia)}")