from graph import Graph

# Ejercicio 14: Ambientes de una casa

casa = Graph(is_directed=False)

# a. Cargar vertices (ambientes)
casa.insert_vertex('Cocina')
casa.insert_vertex('Comedor')
casa.insert_vertex('Cochera')
casa.insert_vertex('Quincho')
casa.insert_vertex('Baño 1')
casa.insert_vertex('Baño 2')
casa.insert_vertex('Habitación 1')
casa.insert_vertex('Habitación 2')
casa.insert_vertex('Sala de estar')
casa.insert_vertex('Terraza')
casa.insert_vertex('Patio')

# b. Cargar aristas (al menos 3 por vertice, dos vertices con 5 aristas)
# Sala de estar - 5 aristas
casa.insert_edge('Sala de estar', 'Comedor', 3)
casa.insert_edge('Sala de estar', 'Habitación 1', 5)
casa.insert_edge('Sala de estar', 'Habitación 2', 6)
casa.insert_edge('Sala de estar', 'Baño 1', 4)
casa.insert_edge('Sala de estar', 'Terraza', 7)

# Cocina - 5 aristas
casa.insert_edge('Cocina', 'Comedor', 2)
casa.insert_edge('Cocina', 'Patio', 4)
casa.insert_edge('Cocina', 'Quincho', 8)
casa.insert_edge('Cocina', 'Baño 2', 6)
casa.insert_edge('Cocina', 'Terraza', 9)

# Comedor - 4 aristas (ya tiene 2)
casa.insert_edge('Comedor', 'Quincho', 5)
casa.insert_edge('Comedor', 'Patio', 6)

# Habitacion 1 - 3 aristas (ya tiene 1)
casa.insert_edge('Habitación 1', 'Baño 1', 2)
casa.insert_edge('Habitación 1', 'Baño 2', 8)

# Habitacion 2 - 3 aristas (ya tiene 1)
casa.insert_edge('Habitación 2', 'Baño 2', 2)
casa.insert_edge('Habitación 2', 'Terraza', 4)

# Cochera - 3 aristas
casa.insert_edge('Cochera', 'Patio', 5)
casa.insert_edge('Cochera', 'Quincho', 7)
casa.insert_edge('Cochera', 'Comedor', 8)

# Quincho - 4 aristas (ya tiene 3)
casa.insert_edge('Quincho', 'Patio', 3)

# Baño 1 - 3 aristas (ya tiene 2)
casa.insert_edge('Baño 1', 'Habitación 2', 7)

# Baño 2 - 4 aristas (ya tiene 3)
casa.insert_edge('Baño 2', 'Patio', 5)

# Terraza - 4 aristas (ya tiene 3)
casa.insert_edge('Terraza', 'Patio', 6)

casa.show()

# c. Arbol de expansion minima
print()
print('arbol de expansion minima')
expansion_tree = casa.kruskal('Habitación 1')
print(expansion_tree)
peso_total = 0
for edge in expansion_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total} metros de cable')

# d. Camino mas corto desde Habitacion 1 hasta Sala de estar
print()
print('camino mas corto desde Habitación 1 a Sala de estar')
path = casa.dijkstra('Habitación 1')
destination = 'Sala de estar'
peso_total = None
camino_completo = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]

camino_completo.reverse()
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total} metros')