#13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
#verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
#usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
#las siguientes actividades:
#a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,además mostrar el nombre de dichas películas;
#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben cargarse por separado;
#e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.



from stack import Stack
from trajes import pila_trajes


# ============================================
# CARGAR TRAJES EN LA PILA
# ============================================
pila = Stack()  # creo la pila vacía
for traje in pila_trajes:  # recorro cada traje de la lista
    pila.push(traje)  # meto el traje en la pila con push()


# ============================================
#PUNTO A - BUSCAR MARK XLIV
# ============================================
print("=" * 50)
print("PUNTO A: Buscar Mark XLIV (Hulkbuster)")
print("=" * 50)

pila_aux = Stack()  # creo una pila auxiliar vacía
peliculas_encontradas = []  # lista vacía para guardar películas

# Recorro la pila sacando elementos
while pila.size() > 0:
    traje = pila.pop()  # saco el traje de arriba
    if traje["modelo"] == "Mark XLIV":  # si es el Mark XLIV
        peliculas_encontradas.append(traje["pelicula"])  # guardo la película
    pila_aux.push(traje)  # meto el traje en la pila auxiliar


# Restauro la pila original
while pila_aux.size() > 0:  # mientras la auxiliar tenga elementos
    pila.push(pila_aux.pop())  # saco de auxiliar y meto en pila original


# Muestro resultados
if peliculas_encontradas:  # si la lista tiene algo
    print("✓ El Mark XLIV fue utilizado en:")
    for pelicula in peliculas_encontradas:  # recorro cada película
        print(f"  - {pelicula}")  # la imprimo
else:  # si la lista está vacía
    print("✗ El Mark XLIV no fue encontrado")


# ============================================
#PUNTO B - TRAJES DAÑADOS
# ============================================
print("\n" + "=" * 50)
print("PUNTO B: Trajes que quedaron DAÑADOS")
print("=" * 50)

pila_aux = Stack()  # nueva pila auxiliar vacía
trajes_danados = []  # lista vacía para dañados

# Recorro la pila buscando dañados
while pila.size() > 0:  # mientras haya trajes
    traje = pila.pop()  # saco el de arriba
    if traje["estado"] == "Dañado":  # si está dañado
        trajes_danados.append(traje)  # lo guardo en la lista
    pila_aux.push(traje)  # lo meto en auxiliar de todas formas

# Restauro la pila
while pila_aux.size() > 0:  # mientras auxiliar tenga elementos
    pila.push(pila_aux.pop())  # devuelvo a la pila original


# Muestro dañados
if trajes_danados:  # si hay trajes dañados
    print("Modelos dañados:")
    for traje in trajes_danados:  # recorro cada dañado
        print(f"  - {traje['modelo']} en {traje['pelicula']}")  # muestro info
else:
    print("No hay trajes dañados")


# ============================================
#PUNTO C - ELIMINAR DESTRUIDOS
# ============================================
print("\n" + "=" * 50)
print("PUNTO C: Eliminar trajes DESTRUIDOS")
print("=" * 50)

pila_aux = Stack()  # nueva pila auxiliar
trajes_eliminados = []  # lista para nombres eliminados

# Recorro la pila y filtro destruidos
while pila.size() > 0:  # mientras haya trajes
    traje = pila.pop()  # saco el de arriba
    if traje["estado"] == "Destruido":  # si está destruido
        trajes_eliminados.append(traje["modelo"])  # guardo su nombre
        # NO lo meto en pila_aux, así lo elimino
    else:  # si NO está destruido
        pila_aux.push(traje)  # lo meto en auxiliar

# Restauro solo los NO destruidos
while pila_aux.size() > 0:  # mientras auxiliar tenga elementos
    pila.push(pila_aux.pop())  # devuelvo solo los que no estaban destruidos


# Muestro qué eliminé
if trajes_eliminados:  # si eliminé algo
    print("Trajes eliminados:")
    for modelo in trajes_eliminados:  # recorro los nombres
        print(f"  - {modelo}")  # los muestro
else:
    print("No había trajes destruidos para eliminar")



# ============================================
#PUNTO E - AGREGAR MARK LXXXV
# ============================================
print("\n" + "=" * 50)
print("PUNTO E: Agregar Mark LXXXV")
print("=" * 50)

# Defino el nuevo traje
nuevo_traje = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"}


pila_aux = Stack()  # pila auxiliar
existe_en_pelicula = False  # bandera en falso

# Verifico si ya existe
while pila.size() > 0:  # mientras haya trajes
    traje = pila.pop()  # saco uno
    # Comparo modelo Y película
    if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
        existe_en_pelicula = True  # cambio la bandera a verdadero
    pila_aux.push(traje)  # lo guardo en auxiliar

# Restauro la pila
while pila_aux.size() > 0:  # mientras auxiliar tenga elementos
    pila.push(pila_aux.pop())  # devuelvo todo

# Agrego si no existe
if not existe_en_pelicula:  # si NO existe
    pila.push(nuevo_traje)  # lo agrego con push()
    print(f"✓ Agregado: {nuevo_traje['modelo']} en {nuevo_traje['pelicula']}")
else:  # si ya existe
    print(f"✗ Ya existe el {nuevo_traje['modelo']} en {nuevo_traje['pelicula']}")
# 📝 Si no estaba repetido lo agrego, si no aviso que ya existe


# ============================================
#PUNTO F - TRAJES EN PELÍCULAS
# ============================================
print("\n" + "=" * 50)
print("PUNTO F: Trajes en Spider-Man y Civil War")
print("=" * 50)

# Lista de películas que busco
peliculas_buscar = ["Spider-Man: Homecoming", "Capitan America: Civil War"]


pila_aux = Stack()  # pila auxiliar
# Creo un diccionario con listas vacías para cada película
trajes_encontrados = {pelicula: [] for pelicula in peliculas_buscar}


# Busco trajes de esas películas
while pila.size() > 0:  # mientras haya trajes
    traje = pila.pop()  # saco uno
    if traje["pelicula"] in peliculas_buscar:  # si la película está en mi lista
        trajes_encontrados[traje["pelicula"]].append(traje["modelo"])  # guardo el modelo
    pila_aux.push(traje)  # lo paso a auxiliar


# Restauro la pila
while pila_aux.size() > 0:  # mientras auxiliar tenga elementos
    pila.push(pila_aux.pop())  # devuelvo todo


# Muestro resultados
for pelicula in peliculas_buscar:  # recorro cada película
    print(f"\n{pelicula}:")  # imprimo el nombre
    if trajes_encontrados[pelicula]:  # si tiene trajes
        for modelo in trajes_encontrados[pelicula]:  # recorro los modelos
            print(f"  - {modelo}")  # los muestro
    else:  # si no tiene
        print("  - No se usaron trajes en esta película")
