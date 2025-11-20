from tree import BinaryTree
from queue_ import Queue
from lista_pokemones import pokemones

# Ejercicio 1: Se tiene los datos de Pokemons de las 9 generaciones cargados de manera aleatoria (1025 en total)
# de los cuales se conoce su nombre, numero, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool)
# y si tiene forma gigamax (bool) para el cual debemos construir tres arboles para acceder de manera eficiente
# a los datos contemplando lo siguiente:

# ============================================
# a. los indices de cada uno de los arboles deben ser nombre, numero y tipo
# ============================================
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemones:
    arbol_nombre.insert(pokemon['nombre'], pokemon)
    arbol_numero.insert(pokemon['numero'], pokemon)
    for tipo in pokemon['tipo']:
        arbol_tipo.insert(tipo, pokemon)

print("arboles creados y cargados correctamente\n")


# ============================================
# b. mostrar todos los datos de un Pokemon a partir de su numero y nombre
# para este ultimo, la busqueda debe ser por proximidad, es decir si busco "bul"
# se deben mostrar todos los Pokemons cuyos nombres comiencen o contengan dichos caracteres
# ============================================

# busqueda por numero
def mostrar_pokemon_por_numero(arbol_numero, numero_buscado):
    nodo = arbol_numero.search(numero_buscado)
    
    if nodo is not None:
        print(f"\npokemon #{numero_buscado}")
        print(f"nombre: {nodo.other_values['nombre']}")
        print(f"numero: {nodo.other_values['numero']}")
        print(f"tipos: {', '.join(nodo.other_values['tipo'])}")
        print(f"debilidades: {', '.join(nodo.other_values['debilidad'])}")
        print(f"mega evolucion: {'si' if nodo.other_values['mega_evolucion'] else 'no'}")
        print(f"forma gigamax: {'si' if nodo.other_values['gigamax'] else 'no'}")
    else:
        print(f"no se encontro el pokemon con numero {numero_buscado}")

mostrar_pokemon_por_numero(arbol_numero, 6)
mostrar_pokemon_por_numero(arbol_numero, 94)


# busqueda por proximidad de nombre
def buscar_por_proximidad_nombre(arbol_nombre, substring):
    print(f"\nbusqueda por proximidad: '{substring}'")
    encontrados = []
    
    def __buscar_proximidad(root, substring):
        if root is not None:
            __buscar_proximidad(root.left, substring)
            
            if substring.lower() in root.value.lower():
                encontrados.append(root)
                print(f"\npokemon encontrado")
                print(f"nombre: {root.other_values['nombre']}")
                print(f"numero: {root.other_values['numero']}")
                print(f"tipos: {', '.join(root.other_values['tipo'])}")
                print(f"debilidades: {', '.join(root.other_values['debilidad'])}")
                print(f"mega evolucion: {'si' if root.other_values['mega_evolucion'] else 'no'}")
                print(f"forma gigamax: {'si' if root.other_values['gigamax'] else 'no'}")
            
            __buscar_proximidad(root.right, substring)
    
    if arbol_nombre.root is not None:
        __buscar_proximidad(arbol_nombre.root, substring)
    
    if len(encontrados) == 0:
        print("no se encontraron pokemons con ese criterio")
    else:
        print(f"\ntotal encontrados: {len(encontrados)}")

buscar_por_proximidad_nombre(arbol_nombre, "bul")
buscar_por_proximidad_nombre(arbol_nombre, "saur")


# ============================================
# c. mostrar todos los nombres de los Pokemons de un determinado tipo:
# fantasma, fuego, acero y electrico
# ============================================
def mostrar_pokemones_por_tipo(arbol_tipo, tipo_buscado):
    print(f"\npokemons tipo {tipo_buscado}")
    contador = 0
    
    def __buscar_tipo(root, tipo_buscado):
        nonlocal contador
        if root is not None:
            __buscar_tipo(root.left, tipo_buscado)
            
            if root.value == tipo_buscado:
                print(f"  - {root.other_values['nombre']}")
                contador += 1
            
            __buscar_tipo(root.right, tipo_buscado)
    
    if arbol_tipo.root is not None:
        __buscar_tipo(arbol_tipo.root, tipo_buscado)
    
    print(f"total: {contador} pokemons")

mostrar_pokemones_por_tipo(arbol_tipo, "Fantasma")
mostrar_pokemones_por_tipo(arbol_tipo, "Fuego")
mostrar_pokemones_por_tipo(arbol_tipo, "Acero")
mostrar_pokemones_por_tipo(arbol_tipo, "Electrico")


# ============================================
# d. realizar un listado en orden ascendente por numero y nombre de Pokemon,
# y ademas un listado por nivel por nombre
# ============================================

# listado ascendente por numero
def listado_por_numero(arbol_numero):
    print("\nlistado por numero (ascendente)")
    
    def __in_order_numero(root):
        if root is not None:
            __in_order_numero(root.left)
            print(f"#{root.value:03d} - {root.other_values['nombre']}")
            __in_order_numero(root.right)
    
    if arbol_numero.root is not None:
        __in_order_numero(arbol_numero.root)

listado_por_numero(arbol_numero)


# listado ascendente por nombre
def listado_por_nombre(arbol_nombre):
    print("\nlistado por nombre (alfabetico ascendente)")
    
    def __in_order_nombre(root):
        if root is not None:
            __in_order_nombre(root.left)
            print(f"{root.value} - #{root.other_values['numero']}")
            __in_order_nombre(root.right)
    
    if arbol_nombre.root is not None:
        __in_order_nombre(arbol_nombre.root)

listado_por_nombre(arbol_nombre)


# listado por nivel por nombre
def listado_por_nivel(arbol_nombre):
    print("\nlistado por nivel (nombre)")
    tree_queue = Queue()
    
    if arbol_nombre.root is not None:
        tree_queue.arrive(arbol_nombre.root)
        
        while tree_queue.size() > 0:
            node = tree_queue.attention()
            print(f"{node.value} - #{node.other_values['numero']}")
            
            if node.left is not None:
                tree_queue.arrive(node.left)
            if node.right is not None:
                tree_queue.arrive(node.right)

listado_por_nivel(arbol_nombre)


# ============================================
# e. mostrar todos los Pokemons que son debiles frente a Jolteon, Lycanroc y Tyrantrum
# ============================================
def pokemones_debiles_a(arbol_nombre, nombre_atacante):
    nodo_atacante = arbol_nombre.search(nombre_atacante)
    
    if nodo_atacante is None:
        print(f"\nno se encontro el pokemon {nombre_atacante}")
        return
    
    tipos_atacante = nodo_atacante.other_values['tipo']
    
    print(f"\npokemons debiles frente a {nombre_atacante}")
    print(f"tipos de {nombre_atacante}: {', '.join(tipos_atacante)}")
    print("\npokemons debiles:")
    contador = 0
    
    def __buscar_debiles(root, tipos_atacante):
        nonlocal contador
        if root is not None:
            __buscar_debiles(root.left, tipos_atacante)
            
            debilidades = root.other_values['debilidad']
            for tipo in tipos_atacante:
                if tipo in debilidades:
                    print(f"  - {root.value} (debil a: {', '.join(debilidades)})")
                    contador += 1
                    break
            
            __buscar_debiles(root.right, tipos_atacante)
    
    if arbol_nombre.root is not None:
        __buscar_debiles(arbol_nombre.root, tipos_atacante)
    
    print(f"total: {contador} pokemons debiles")

pokemones_debiles_a(arbol_nombre, "Jolteon")
pokemones_debiles_a(arbol_nombre, "Lycanroc")
pokemones_debiles_a(arbol_nombre, "Tyrantrum")


# ============================================
# f. mostrar todos los tipos de Pokemons y cuantos hay de cada tipo
# ============================================
def contar_pokemones_por_tipo(arbol_tipo):
    conteo_tipos = {}
    
    def __contar_tipos(root):
        if root is not None:
            __contar_tipos(root.left)
            
            tipo = root.value
            if tipo not in conteo_tipos:
                conteo_tipos[tipo] = 0
            conteo_tipos[tipo] += 1
            
            __contar_tipos(root.right)
    
    if arbol_tipo.root is not None:
        __contar_tipos(arbol_tipo.root)
    
    print("\ncantidad de pokemons por tipo")
    for tipo in sorted(conteo_tipos.keys()):
        print(f"{tipo}: {conteo_tipos[tipo]} pokemons")
    
    print(f"\ntotal de tipos diferentes: {len(conteo_tipos)}")

contar_pokemones_por_tipo(arbol_tipo)


# ============================================
# g. determinar cuantos Pokemons tienen megaevolucion
# ============================================
def contar_mega_evoluciones(arbol_nombre):
    def __contar_mega(root):
        contador = 0
        if root is not None:
            contador += __contar_mega(root.left)
            
            if root.other_values['mega_evolucion'] == True:
                contador += 1
            
            contador += __contar_mega(root.right)
        
        return contador
    
    total = 0
    if arbol_nombre.root is not None:
        total = __contar_mega(arbol_nombre.root)
    
    print(f"\ntotal de pokemons con megaevolucion: {total}")
    return total

contar_mega_evoluciones(arbol_nombre)


# ============================================
# h. determinar cuantos Pokemons tiene forma gigamax
# ============================================
def contar_forma_gigamax(arbol_nombre):
    def __contar_gigamax(root):
        contador = 0
        if root is not None:
            contador += __contar_gigamax(root.left)
            
            if root.other_values['gigamax'] == True:
                contador += 1
            
            contador += __contar_gigamax(root.right)
        
        return contador
    
    total = 0
    if arbol_nombre.root is not None:
        total = __contar_gigamax(arbol_nombre.root)
    
    print(f"\ntotal de pokemons con forma gigamax: {total}")
    return total

contar_forma_gigamax(arbol_nombre)
