from graph import Graph
from heap import HeapMin
from stack import Stack
from lista_star_wars import grafo_star_wars, personajes_detalle

# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars,
# implementar los algoritmos necesarios para resolver las siguientes tareas:

# ============================================
# a. cada vertice debe almacenar el nombre de un personaje, las aristas representan
# la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan
# ============================================

# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,
# C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8
# (lo resolvemos junto con el punto a)

grafo = Graph(is_directed=False)

# insertar todos los vertices (personajes)
personajes_unicos = set()
for personaje1, personaje2, _ in grafo_star_wars:
    personajes_unicos.add(personaje1)
    personajes_unicos.add(personaje2)

for personaje in personajes_unicos:
    grafo.insert_vertex(personaje)

# insertar todas las aristas (episodios juntos)
for personaje1, personaje2, episodios in grafo_star_wars:
    grafo.insert_edge(personaje1, personaje2, episodios)

print("grafo creado correctamente")
print(f"total de personajes (vertices): {len(grafo)}")
print(f"total de relaciones (aristas): {len(grafo_star_wars)}\n")


# ============================================
# b. hallar el arbol de expansion minimo desde el vertice que contiene a:
# C-3PO, Yoda y Leia
# ============================================
def arbol_expansion_minimo(grafo, personaje_origen):
    print(f"\narbol de expansion minimo desde {personaje_origen}")
    expansion_tree = grafo.kruskal(personaje_origen)
    
    # kruskal retorna un string o una lista con string
    arbol_str = expansion_tree if isinstance(expansion_tree, str) else (expansion_tree[0] if expansion_tree else None)
    
    if arbol_str:
        print(f"\narbol generado:")
        
        # calcular peso total
        peso_total = 0
        aristas = arbol_str.split(';')
        print("\naristas del arbol de expansion minimo:")
        for arista in aristas:
            partes = arista.split('-')
            if len(partes) == 3:
                origen = partes[0]
                destino = partes[1]
                peso = partes[2]
                print(f"  {origen} -- {destino} (episodios: {peso})")
                peso_total += int(peso)
        
        print(f"\npeso total del arbol: {peso_total} episodios")
    else:
        print("no se pudo generar el arbol de expansion minimo")
    
    return expansion_tree

arbol_expansion_minimo(grafo, "C-3PO")
arbol_expansion_minimo(grafo, "Yoda")
arbol_expansion_minimo(grafo, "Leia")


# ============================================
# c. determinar cual es el numero maximo de episodio que comparten dos personajes,
# e indicar todos los pares de personajes que coinciden con dicho numero
# ============================================
def maximo_episodios_compartidos(grafo_star_wars):
    print("\ndeterminando numero maximo de episodios compartidos")
    
    # encontrar el maximo
    maximo = 0
    for personaje1, personaje2, episodios in grafo_star_wars:
        if episodios > maximo:
            maximo = episodios
    
    print(f"\nnumero maximo de episodios compartidos: {maximo}")
    print("\npares de personajes con ese numero:")
    
    # buscar todos los pares con el maximo
    pares_maximos = []
    for personaje1, personaje2, episodios in grafo_star_wars:
        if episodios == maximo:
            pares_maximos.append((personaje1, personaje2, episodios))
            print(f"  - {personaje1} y {personaje2}: {episodios} episodios")
    
    print(f"\ntotal de pares con {maximo} episodios: {len(pares_maximos)}")
    return maximo, pares_maximos

maximo_episodios_compartidos(grafo_star_wars)


# ============================================
# e. calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader
# ============================================
def camino_mas_corto(grafo, origen, destino):
    print(f"\ncalculando camino mas corto desde {origen} hasta {destino}")
    
    # usar dijkstra
    path = grafo.dijkstra(origen)
    
    # reconstruir el camino
    peso_total = None
    camino_completo = []
    destino_actual = destino
    
    # pasar todos los elementos del stack a una lista para buscar
    elementos = []
    while path.size() > 0:
        elementos.append(path.pop())
    
    # buscar el nodo destino
    nodo_destino = None
    for elemento in elementos:
        if elemento[0] == destino:
            nodo_destino = elemento
            peso_total = elemento[1]
            break
    
    if nodo_destino is None:
        print(f"no existe camino entre {origen} y {destino}")
        return None, None
    
    # reconstruir el camino hacia atras
    camino_completo.append(destino)
    predecesor = nodo_destino[2]
    
    while predecesor is not None:
        camino_completo.append(predecesor)
        # buscar el predecesor
        for elemento in elementos:
            if elemento[0] == predecesor:
                predecesor = elemento[2]
                break
        else:
            break
    
    camino_completo.reverse()
    
    if len(camino_completo) > 0 and camino_completo[0] == origen:
        print(f"camino: {' -> '.join(camino_completo)}")
        print(f"costo total: {peso_total} episodios")
    else:
        print(f"no existe camino entre {origen} y {destino}")
        return None, None
    
    return camino_completo, peso_total

camino_mas_corto(grafo, "C-3PO", "R2-D2")
camino_mas_corto(grafo, "Yoda", "Darth Vader")


# ============================================
# f. indicar que personajes aparecieron en los nueve episodios de la saga
# ============================================
def personajes_en_nueve_episodios(personajes_detalle):
    print("\npersonajes que aparecieron en los 9 episodios de la saga")
    
    personajes_9_episodios = []
    for personaje in personajes_detalle:
        if personaje['total_episodios'] == 9:
            personajes_9_episodios.append(personaje['nombre'])
            print(f"  - {personaje['nombre']}: episodios {personaje['episodios']}")
    
    print(f"\ntotal de personajes en los 9 episodios: {len(personajes_9_episodios)}")
    return personajes_9_episodios

personajes_en_nueve_episodios(personajes_detalle)