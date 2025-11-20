from graph import Graph

# ============================================
# CREAR GRAFO Y CARGAR DATOS DE PRUEBA
# ============================================
print("=" * 60)
print("EJERCICIO 14: Verificar si existe camino entre vértices")
print("=" * 60)

grafo = Graph(is_directed=True)  # creo un grafo dirigido

# Inserto vértices
vertices = ['A', 'B', 'C', 'D', 'E', 'F'] 
for vertice in vertices: 
    grafo.insert_vertex(vertice)

print("\nVértices insertados: A, B, C, D, E, F\n")

# Inserto aristas dirigidas (las flechas van en un solo sentido)
grafo.insert_edge('A', 'B', 5)  # A → B
grafo.insert_edge('A', 'C', 3)  
grafo.insert_edge('B', 'D', 7)  
grafo.insert_edge('C', 'E', 4)  
grafo.insert_edge('D', 'F', 6)  
grafo.insert_edge('E', 'F', 8)  

print("Aristas insertadas (dirigidas):")
print("  A → B")
print("  A → C")
print("  B → D")
print("  C → E")
print("  D → F")
print("  E → F\n")


# ============================================
# MOSTRAR GRAFO
# ============================================
print("=" * 60)
print("GRAFO:")
print("=" * 60)
grafo.show()  # muestro todo el grafo con sus aristas
print()


# ============================================
# PRUEBA 1: CAMINO QUE EXISTE
# ============================================
print("=" * 60)
print("PRUEBA 1: ¿Existe camino de A a F?")
print("=" * 60)

origen = 'A'  
destino = 'F'  
existe = grafo.exist_path(origen, destino)  # verifico si existe el camino

if existe:  # si existe el camino
    print(f"SÍ existe camino de {origen} a {destino}")
    print(f"Ejemplo de camino: A → B → D → F")
else:
    print(f"NO existe camino de {origen} a {destino}")

print()


# ============================================
# PRUEBA 2: OTRO CAMINO QUE EXISTE
# ============================================
print("=" * 60)
print("PRUEBA 2: ¿Existe camino de A a E?")
print("=" * 60)

origen = 'A' 
destino = 'E' 
existe = grafo.exist_path(origen, destino)  # verifico si existe el camino

if existe:  # si existe el camino
    print(f"SÍ existe camino de {origen} a {destino}")
    print(f"Ejemplo de camino: A → C → E")
else:  # si no existe
    print(f"NO existe camino de {origen} a {destino}")

print()


# ============================================
# PRUEBA 3: CAMINO QUE NO EXISTE
# ============================================
print("=" * 60)
print("PRUEBA 3: ¿Existe camino de F a A?")
print("=" * 60)

origen = 'F' 
destino = 'A'  
existe = grafo.exist_path(origen, destino)  

if existe:  
    print(f"SÍ existe camino de {origen} a {destino}")
else:  
    print(f"NO existe camino de {origen} a {destino}")
    print(f"Razón: El grafo es dirigido y no hay flechas que regresen a A")

print()


# ============================================
# PRUEBA 4: CAMINO QUE NO EXISTE
# ============================================
print("=" * 60)
print("PRUEBA 4: ¿Existe camino de B a C?")
print("=" * 60)

origen = 'B'  
destino = 'C'  
existe = grafo.exist_path(origen, destino) 

if existe:  # si existe el camino
    print(f"SÍ existe camino de {origen} a {destino}")
else:  
    print(f"NO existe camino de {origen} a {destino}")
    print(f"Razón: No hay ninguna ruta que conecte B con C")

print()
