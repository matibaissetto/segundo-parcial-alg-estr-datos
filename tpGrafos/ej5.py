#5. eliminar_arista(vértice, destino). Elimina y devuelve del vértice si encuentra una arista que
#coincida con el destino dado –el primero que encuentre–, si devuelve None significa que no se
#encontró la arista destino en el vértice, y por ende no se elimina ningún elemento;

from graph import Graph

# ============================================
# CREAR GRAFO Y CARGAR DATOS DE PRUEBA
# ============================================
print("=" * 60)
print("EJERCICIO: Eliminar arista de un grafo")
print("=" * 60)

grafo = Graph(is_directed=False)  # creo un grafo no dirigido

# Inserto vértices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']  # lista de vértices
for vertice in vertices:  # recorro cada vértice
    grafo.insert_vertex(vertice)  # inserto el vértice en el grafo

print("\nVértices insertados: A, B, C, D, E, F\n")

# Inserto aristas (conexiones entre vértices)
grafo.insert_edge('A', 'B', 5)  # A conectado con B, peso 5
grafo.insert_edge('A', 'C', 3)  # A conectado con C, peso 3
grafo.insert_edge('B', 'D', 7)  # B conectado con D, peso 7
grafo.insert_edge('C', 'D', 2)  # C conectado con D, peso 2
grafo.insert_edge('C', 'E', 4)  # C conectado con E, peso 4
grafo.insert_edge('D', 'F', 6)  # D conectado con F, peso 6
grafo.insert_edge('E', 'F', 8)  # E conectado con F, peso 8

print("Aristas insertadas:")
print("  A-B (peso: 5)")
print("  A-C (peso: 3)")
print("  B-D (peso: 7)")
print("  C-D (peso: 2)")
print("  C-E (peso: 4)")
print("  D-F (peso: 6)")
print("  E-F (peso: 8)\n")


# ============================================
# MOSTRAR GRAFO INICIAL
# ============================================
print("=" * 60)
print("GRAFO INICIAL:")
print("=" * 60)
grafo.show()  # muestro todo el grafo con sus aristas
print()


# ============================================
# ELIMINAR ARISTAS - PRUEBA 1
# ============================================
print("=" * 60)
print("PRUEBA 1: Eliminar arista A -> B")
print("=" * 60)

arista_eliminada = grafo.delete_edge('A', 'B', 'value')  # elimino la arista de A a B

if arista_eliminada:  # si se eliminó algo
    print(f"Arista eliminada: A -> {arista_eliminada.value} (peso: {arista_eliminada.weight})")
else:  # si no se encontró
    print("No se encontró la arista A -> B")

print("\nGrafo después de eliminar A -> B:")
grafo.show()  # muestro el grafo actualizado
print()


# ============================================
# ELIMINAR ARISTAS - PRUEBA 2
# ============================================
print("=" * 60)
print("PRUEBA 2: Eliminar arista C -> D")
print("=" * 60)

arista_eliminada = grafo.delete_edge('C', 'D', 'value')  # elimino la arista de C a D

if arista_eliminada:  # si se eliminó algo
    print(f"Arista eliminada: C -> {arista_eliminada.value} (peso: {arista_eliminada.weight})")
else:  # si no se encontró
    print("No se encontró la arista C -> D")

print("\nGrafo después de eliminar C -> D:")
grafo.show()  # muestro el grafo actualizado
print()


# ============================================
# ELIMINAR ARISTAS - PRUEBA 3 (Arista inexistente)
# ============================================
print("=" * 60)
print("PRUEBA 3: Intentar eliminar arista A -> F (no existe)")
print("=" * 60)

arista_eliminada = grafo.delete_edge('A', 'F', 'value')  # intento eliminar arista que no existe

if arista_eliminada:  # si se eliminó algo
    print(f"Arista eliminada: A -> {arista_eliminada.value} (peso: {arista_eliminada.weight})")
else:  # si no se encontró
    print("No se encontró la arista A -> F (no existía)")

print()


# ============================================
# GRAFO FINAL
# ============================================
print("=" * 60)
print("GRAFO FINAL:")
print("=" * 60)
grafo.show()  # muestro el estado final del grafo
print()






"""
# ============================================
# EXPLICACIÓN DEL MÉTODO delete_edge
# ============================================
print("=" * 60)
print("EXPLICACIÓN:")
print("=" * 60)
print(
El método delete_edge(origin, destination, key_value):
1. Busca el vértice de origen en el grafo
2. Si lo encuentra, busca la arista hacia el destino
3. Elimina la arista del vértice origen
4. Si el grafo NO es dirigido, también elimina la arista inversa
5. Retorna la arista eliminada o None si no la encuentra

**EXPLICACIÓN:**

El método `delete_edge` que ya existe en tu clase Graph hace exactamente lo que pide el ejercicio:
- Elimina la arista del vértice de origen al destino
- Devuelve la arista eliminada si la encuentra
- Devuelve None si no existe la arista
"""