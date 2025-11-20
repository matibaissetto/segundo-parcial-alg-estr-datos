#Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
#a. listado inorden de las criaturas y quienes la derrotaron;
#b. se debe permitir cargar una breve descripción sobre cada criatura;
#c. mostrar toda la información de la criatura Talos;
#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#e. listar las criaturas derrotadas por Heracles;
#f. listar las criaturas que no han sido derrotadas;
#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
#i. se debe permitir búsquedas por coincidencia;
#j. eliminar al Basilisco y a las Sirenas;
#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#m. realizar un listado por nivel del árbol;
#n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree
from datos_criaturas import criaturas

# ============================================
# CARGAR CRIATURAS EN EL ÁRBOL
# ============================================
print("=" * 60)
print("EJERCICIO 23 - ÁRBOL DE CRIATURAS MITOLÓGICAS")
print("=" * 60)

arbol_criaturas = BinaryTree()  # creo el árbol binario vacío

for criatura in criaturas:  # recorro cada criatura de la lista
    # Agrego campos adicionales
    criatura['descripcion'] = ""  # campo para descripción
    criatura['capturada'] = None  # campo para indicar quién la capturó
    arbol_criaturas.insert(criatura['nombre'], criatura)  # inserto en el árbol

print(f"\n✓ Árbol creado con {len(criaturas)} criaturas\n")


# ============================================
# PUNTO A - LISTADO INORDEN DE CRIATURAS Y DERROTADORES
# ============================================
print("=" * 60)
print("PUNTO A: Listado inorden de criaturas y quienes las derrotaron")
print("=" * 60)

def listar_criaturas_inorden():  # función para listar in-order
    def __listar_inorden(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_inorden(root.left)  # recorro subárbol izquierdo
            derrotador = root.other_values['derrotado_por']  # obtengo quién la derrotó
            if derrotador:  # si fue derrotada
                print(f"  - {root.value} → Derrotada por: {derrotador}")
            else:  # si no fue derrotada
                print(f"  - {root.value} → No derrotada")
            __listar_inorden(root.right)  # recorro subárbol derecho

    if arbol_criaturas.root is not None:  # si el árbol no está vacío
        __listar_inorden(arbol_criaturas.root)  # inicio el recorrido

print()
listar_criaturas_inorden()  # ejecuto la función
print()


# ============================================
# PUNTO B - CARGAR DESCRIPCIÓN DE TALOS
# ============================================
print("=" * 60)
print("PUNTO B: Cargar descripción de Talos")
print("=" * 60)

nodo_talos = arbol_criaturas.search("Talos")  # busco a Talos en el árbol
if nodo_talos:  # si lo encontré
    nodo_talos.other_values['descripcion'] = "Autómata gigante de bronce que protegía Creta"
    print(f"\n✓ Descripción de Talos actualizada correctamente\n")
else:  # si no lo encontré
    print("\n✗ Talos no encontrado en el árbol\n")


# ============================================
# PUNTO C - MOSTRAR INFORMACIÓN DE TALOS
# ============================================
print("=" * 60)
print("PUNTO C: Información completa de Talos")
print("=" * 60)

if nodo_talos:  # si encontré a Talos
    print(f"\nNOMBRE: {nodo_talos.value}")
    print(f"DERROTADO POR: {nodo_talos.other_values['derrotado_por']}")
    print(f"DESCRIPCIÓN: {nodo_talos.other_values['descripcion']}")
    print(f"CAPTURADA: {nodo_talos.other_values['capturada']}")
else:  # si no lo encontré
    print("\n✗ Talos no encontrado")

print()


# ============================================
# PUNTO D - TOP 3 HÉROES CON MÁS DERROTAS
# ============================================
print("=" * 60)
print("PUNTO D: Top 3 héroes que derrotaron más criaturas")
print("=" * 60)

def obtener_ranking():  # función para obtener ranking de derrotas
    ranking = {}  # diccionario para contar derrotas
    
    def __contar_derrotas(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __contar_derrotas(root.left)  # proceso subárbol izquierdo
            heroe = root.other_values['derrotado_por']  # obtengo el derrotador
            if heroe is not None:  # si hay derrotador
                if heroe not in ranking:  # si no está en el ranking
                    ranking[heroe] = 1  # inicializo en 1
                else:  # si ya está
                    ranking[heroe] += 1  # incremento el contador
            __contar_derrotas(root.right)  # proceso subárbol derecho
    
    __contar_derrotas(arbol_criaturas.root)  # inicio el conteo
    return ranking  # retorno el diccionario

ranking = obtener_ranking()  # obtengo el ranking
top_3 = sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:3]  # ordeno y tomo top 3

print()
for i, (heroe, cantidad) in enumerate(top_3, 1):  # recorro el top 3
    print(f"  {i}. {heroe}: {cantidad} criatura(s) derrotada(s)")
print()


# ============================================
# PUNTO E - CRIATURAS DERROTADAS POR HERACLES
# ============================================
print("=" * 60)
print("PUNTO E: Criaturas derrotadas por Heracles")
print("=" * 60)

def listar_derrotadas_por(heroe):  # función para listar criaturas derrotadas por un héroe
    def __listar_derrotadas(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_derrotadas(root.left)  # recorro subárbol izquierdo
            if root.other_values['derrotado_por'] == heroe:  # si fue derrotada por el héroe
                print(f"  - {root.value}")  # muestro el nombre
            __listar_derrotadas(root.right)  # recorro subárbol derecho
    
    if arbol_criaturas.root is not None:  # si el árbol no está vacío
        __listar_derrotadas(arbol_criaturas.root)  # inicio el recorrido

print()
listar_derrotadas_por("Heracles")  # listo las derrotadas por Heracles
print()


# ============================================
# PUNTO F - CRIATURAS NO DERROTADAS
# ============================================
print("=" * 60)
print("PUNTO F: Criaturas que no han sido derrotadas")
print("=" * 60)

def listar_no_derrotadas():  # función para listar criaturas no derrotadas
    def __listar_no_derrotadas(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_no_derrotadas(root.left)  # recorro subárbol izquierdo
            if root.other_values['derrotado_por'] is None:  # si no fue derrotada
                print(f"  - {root.value}")  # muestro el nombre
            __listar_no_derrotadas(root.right)  # recorro subárbol derecho
    
    if arbol_criaturas.root is not None:  # si el árbol no está vacío
        __listar_no_derrotadas(arbol_criaturas.root)  # inicio el recorrido

print()
listar_no_derrotadas()  # ejecuto la función
print()


# ============================================
# PUNTO H - MARCAR CRIATURAS CAPTURADAS POR HERACLES
# ============================================
print("=" * 60)
print("PUNTO H: Marcar criaturas capturadas por Heracles")
print("=" * 60)

criaturas_capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]

print()
for nombre_criatura in criaturas_capturadas:  # recorro las criaturas a capturar
    nodo = arbol_criaturas.search(nombre_criatura)  # busco la criatura
    if nodo:  # si la encontré
        nodo.other_values['capturada'] = "Heracles"  # marco como capturada por Heracles
        print(f"  ✓ {nombre_criatura} marcada como capturada por Heracles")
    else:  # si no la encontré
        print(f"  ✗ {nombre_criatura} no encontrada")
print()


# ============================================
# PUNTO I - BÚSQUEDA POR COINCIDENCIA
# ============================================
print("=" * 60)
print("PUNTO I: Búsqueda por coincidencia")
print("=" * 60)

def busqueda_por_coincidencia(valor):  # función de búsqueda por coincidencia
    def __buscar_coincidencia(root, valor):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __buscar_coincidencia(root.left, valor)  # busco en subárbol izquierdo
            if valor.lower() in root.value.lower():  # si el valor está contenido (case insensitive)
                print(f"  - {root.value}")  # muestro el resultado
            __buscar_coincidencia(root.right, valor)  # busco en subárbol derecho
    
    if arbol_criaturas.root is not None:  # si el árbol no está vacío
        __buscar_coincidencia(arbol_criaturas.root, valor)  # inicio la búsqueda

print("\nBuscando criaturas que contengan 'Cerbero':")
busqueda_por_coincidencia("Cerbero")  # busco coincidencias
print()


# ============================================
# PUNTO J - ELIMINAR BASILISCO Y SIRENAS
# ============================================
print("=" * 60)
print("PUNTO J: Eliminar Basilisco y Sirenas")
print("=" * 60)

print()
# Elimino Basilisco
valor_eliminado, _ = arbol_criaturas.delete("Basilisco")  # elimino del árbol
if valor_eliminado:  # si se eliminó correctamente
    print(f"  ✓ {valor_eliminado} eliminado del árbol")
else:  # si no se encontró
    print(f"  ✗ Basilisco no encontrado")

# Elimino Sirenas
valor_eliminado, _ = arbol_criaturas.delete("Sirenas")  # elimino del árbol
if valor_eliminado:  # si se eliminó correctamente
    print(f"  ✓ {valor_eliminado} eliminado del árbol")
else:  # si no se encontró
    print(f"  ✗ Sirenas no encontrado")
print()


# ============================================
# PUNTO K - MODIFICAR AVES DEL ESTÍNFALO
# ============================================
print("=" * 60)
print("PUNTO K: Modificar información de Aves del Estínfalo")
print("=" * 60)

nodo_aves = arbol_criaturas.search("Aves del Estinfalo")  # busco las aves
if nodo_aves:  # si las encontré
    nodo_aves.other_values['derrotado_por'] = "Heracles"  # marco que las derrotó Heracles
    nodo_aves.other_values['descripcion'] = "Heracles derrotó a varias de estas aves"
    print(f"\n✓ Información de Aves del Estínfalo actualizada\n")
else:  # si no las encontré
    print(f"\n✗ Aves del Estínfalo no encontradas\n")


# ============================================
# PUNTO L - MODIFICAR LADÓN POR DRAGÓN LADÓN
# ============================================
print("=" * 60)
print("PUNTO L: Modificar nombre de Ladón")
print("=" * 60)

nodo_ladon = arbol_criaturas.search("Ladon")  # busco a Ladón
if nodo_ladon:  # si lo encontré
    datos = nodo_ladon.other_values  # guardo los datos
    arbol_criaturas.delete("Ladon")  # elimino el nodo con nombre viejo
    datos['nombre'] = "Dragón Ladón"  # actualizo el nombre
    arbol_criaturas.insert("Dragón Ladón", datos)  # inserto con nuevo nombre
    print(f"\n✓ Nombre modificado: 'Ladon' → 'Dragón Ladón'\n")
else:  # si no lo encontré
    print(f"\n✗ Ladon no encontrado\n")


# ============================================
# PUNTO M - LISTADO POR NIVEL
# ============================================
print("=" * 60)
print("PUNTO M: Listado por nivel del árbol")
print("=" * 60)

print()
arbol_criaturas.by_level()  # uso el método by_level del árbol
print()


# ============================================
# PUNTO N - CRIATURAS CAPTURADAS POR HERACLES
# ============================================
print("=" * 60)
print("PUNTO N: Criaturas capturadas por Heracles")
print("=" * 60)

def listar_capturadas_por(heroe):  # función para listar capturadas por un héroe
    def __listar_capturadas(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_capturadas(root.left)  # recorro subárbol izquierdo
            if root.other_values['capturada'] == heroe:  # si fue capturada por el héroe
                print(f"  - {root.value}")  # muestro el nombre
            __listar_capturadas(root.right)  # recorro subárbol derecho
    
    if arbol_criaturas.root is not None:  # si el árbol no está vacío
        __listar_capturadas(arbol_criaturas.root)  # inicio el recorrido

print()
listar_capturadas_por("Heracles")  # listo las capturadas por Heracles

print("\n" + "=" * 60)