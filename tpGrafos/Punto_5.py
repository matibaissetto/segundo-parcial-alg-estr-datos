from graph import Graph

# Ejercicio 5: Red de computadoras

g = Graph(is_directed=False)

# a. Cargar vertices (equipos)
g.insert_vertex('Red Hat')
g.insert_vertex('Debian')
g.insert_vertex('Arch')
g.insert_vertex('Ubuntu')
g.insert_vertex('Mint')
g.insert_vertex('Router 1')
g.insert_vertex('Router 2')
g.insert_vertex('Switch 1')
g.insert_vertex('Switch 2')
g.insert_vertex('Manjaro')
g.insert_vertex('Fedora')
g.insert_vertex('Guarani')
g.insert_vertex('MongoDB')
g.insert_vertex('Impresora')
g.insert_vertex('Parrot')

# Cargar aristas segun el diagrama
g.insert_edge('Red Hat', 'Router 2', 25)
g.insert_edge('Debian', 'Router 2', 17)
g.insert_edge('Debian', 'Switch 1', 20)
g.insert_edge('Debian', 'Ubuntu', 18)
g.insert_edge('Ubuntu', 'Switch 1', 24)
g.insert_edge('Ubuntu', 'Mint', 22)
g.insert_edge('Switch 1', 'Router 1', 15)
g.insert_edge('Switch 1', 'Impresora', 29)
g.insert_edge('Router 1', 'Switch 2', 12)
g.insert_edge('Router 1', 'Fedora', 18)
g.insert_edge('Router 2', 'Switch 2', 14)
g.insert_edge('Router 2', 'Guarani', 9)
g.insert_edge('Switch 2', 'Manjaro', 40)
g.insert_edge('Switch 2', 'Parrot', 12)
g.insert_edge('Switch 2', 'MongoDB', 55)
g.insert_edge('Switch 2', 'Arch', 68)

g.show()

# b. Barrido en profundidad y amplitud desde Red Hat, Debian, Arch
print()
print('barrido profundidad desde Red Hat')
g.deep_sweep('Red Hat')

print()
print('barrido amplitud desde Red Hat')
g.amplitude_sweep('Red Hat')

print()
print('barrido profundidad desde Debian')
g.deep_sweep('Debian')

print()
print('barrido amplitud desde Debian')
g.amplitude_sweep('Debian')

print()
print('barrido profundidad desde Arch')
g.deep_sweep('Arch')

print()
print('barrido amplitud desde Arch')
g.amplitude_sweep('Arch')

# c. Camino mas corto para imprimir desde Manjaro a Red Hat, Fedora y a Impresora
print()
print('camino mas corto desde Manjaro a Red Hat')
path = g.dijkstra('Manjaro')
destination = 'Red Hat'
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
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

print()
print('camino mas corto desde Manjaro a Fedora')
path = g.dijkstra('Manjaro')
destination = 'Fedora'
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
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

print()
print('camino mas corto desde Fedora a Impresora')
path = g.dijkstra('Fedora')
destination = 'Impresora'
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
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# d. Arbol de expansion minima
print()
print('arbol de expansion minima')
expansion_tree = g.kruskal('Red Hat')
print(expansion_tree)
peso_total = 0
for edge in expansion_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total}')

# e. Camino mas corto desde pc (no notebook) hasta Guarani
print()
print('camino mas corto desde Router 1 a Guarani')
path = g.dijkstra('Router 1')
destination = 'Guarani'
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
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# f. Camino mas corto desde switch a MongoDB
print()
print('camino mas corto desde Switch 1 a MongoDB')
path = g.dijkstra('Switch 1')
destination = 'MongoDB'
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
print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# g. Cambiar conexion de impresora a router 2
print()
print('cambiando conexion de impresora')
g.delete_edge('Impresora', 'Switch 1', 'value')
g.insert_edge('Impresora', 'Router 2', 35)

print()
print('nuevo barrido profundidad desde Red Hat')
g.deep_sweep('Red Hat')

print()
print('nuevo barrido amplitud desde Red Hat')
g.amplitude_sweep('Red Hat')