#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#se (MCU), desarrollar un algoritmo que contemple lo siguiente:

#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol.

from tree import BinaryTree
from datos_superhereos import superheroes

# ============================================
# CARGAR SUPERHÉROES EN EL ÁRBOL
# ============================================
print("=" * 60)
print("EJERCICIO 5 - ÁRBOL DE SUPERHÉROES MCU")
print("=" * 60)

arbol = BinaryTree()  # creo el árbol binario vacío

for superhero in superheroes:  # recorro cada superhéroe de la lista
    arbol.insert(superhero['name'], superhero)  # inserto en el árbol por nombre

print(f"\n✓ Árbol creado con {len(superheroes)} personajes\n")


# ============================================
# PUNTO B - LISTAR VILLANOS ORDENADOS ALFABÉTICAMENTE
# ============================================
print("=" * 60)
print("PUNTO B: Villanos ordenados alfabéticamente")
print("=" * 60)

def listar_villanos():  # función para listar villanos in-order
    def __listar_villanos(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_villanos(root.left)  # recorro el subárbol izquierdo
            if root.other_values["is_villain"] is True:  # si es villano
                print(f"  - {root.value}")  # muestro el nombre
            __listar_villanos(root.right)  # recorro el subárbol derecho

    if arbol.root is not None:  # si el árbol no está vacío
        __listar_villanos(arbol.root)  # inicio el recorrido

print()
listar_villanos()  # ejecuto la función
print()


# ============================================
# PUNTO C - SUPERHÉROES QUE EMPIEZAN CON C
# ============================================
print("=" * 60)
print("PUNTO C: Superhéroes que empiezan con C")
print("=" * 60)

def superheroes_con_c():  # función para buscar superhéroes con C
    def __superheroes_con_c(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __superheroes_con_c(root.left)  # recorro el subárbol izquierdo
            if root.value.startswith('C') and root.other_values["is_villain"] is False:  # si empieza con C y es héroe
                print(f"  - {root.value}")  # muestro el nombre
            __superheroes_con_c(root.right)  # recorro el subárbol derecho

    if arbol.root is not None:  # si el árbol no está vacío
        __superheroes_con_c(arbol.root)  # inicio el recorrido

print()
superheroes_con_c()  # ejecuto la función
print()


# ============================================
# PUNTO D - CONTAR SUPERHÉROES
# ============================================
print("=" * 60)
print("PUNTO D: Cantidad de superhéroes en el árbol")
print("=" * 60)

def contar_superheroes():  # función para contar superhéroes
    def __contar_superheroes(root):  # función recursiva interna
        count = 0  # contador inicializado en 0
        if root is not None:  # si el nodo existe
            if root.other_values["is_villain"] is False:  # si es superhéroe
                count += 1  # incremento el contador
            count += __contar_superheroes(root.left)  # sumo los del subárbol izquierdo
            count += __contar_superheroes(root.right)  # sumo los del subárbol derecho
        return count  # retorno el total

    total = 0  # inicializo total
    if arbol.root is not None:  # si el árbol no está vacío
        total = __contar_superheroes(arbol.root)  # cuento desde la raíz
    return total  # retorno el resultado

cantidad = contar_superheroes()  # obtengo la cantidad
print(f"\n✓ Hay {cantidad} superhéroes en el árbol\n")


# ============================================
# PUNTO E - BUSCAR Y MODIFICAR DOCTOR STRANGE
# ============================================
print("=" * 60)
print("PUNTO E: Buscar y modificar Doctor Strange")
print("=" * 60)

def buscar_por_proximidad(valor):  # función de búsqueda por proximidad
    def __buscar_proximidad(root, valor):  # función recursiva interna
        resultado = []  # lista para almacenar resultados
        if root is not None:  # si el nodo existe
            if root.value.startswith(valor):  # si el nombre empieza con el valor
                resultado.append(root)  # agrego el nodo al resultado
            resultado.extend(__buscar_proximidad(root.left, valor))  # busco en izquierda
            resultado.extend(__buscar_proximidad(root.right, valor))  # busco en derecha
        return resultado  # retorno los nodos encontrados

    if arbol.root is not None:  # si el árbol no está vacío
        return __buscar_proximidad(arbol.root, valor)  # busco desde la raíz
    return []  # retorno lista vacía si no hay árbol

print("\nBuscando con 'Dr':")
resultados = buscar_por_proximidad("Dr")  # busco por proximidad

if resultados:  # si encontré resultados
    for nodo in resultados:  # recorro cada nodo encontrado
        print(f"  - Encontrado: {nodo.value}")
        
    # Modifico el nombre
    nombre_viejo = resultados[0].value  # guardo el nombre viejo
    datos = resultados[0].other_values  # guardo los datos
    arbol.delete(nombre_viejo)  # elimino el nodo viejo
    
    nombre_nuevo = "Doctor Strange"  # nuevo nombre correcto
    datos['name'] = nombre_nuevo  # actualizo el nombre en los datos
    arbol.insert(nombre_nuevo, datos)  # inserto con el nuevo nombre
    
    print(f"\n✓ Modificado: '{nombre_viejo}' → '{nombre_nuevo}'")
else:  # si no encontré nada
    print("  ✗ No se encontró ningún personaje")

print()


# ============================================
# PUNTO F - LISTAR SUPERHÉROES DESCENDENTE
# ============================================
print("=" * 60)
print("PUNTO F: Superhéroes ordenados descendentemente")
print("=" * 60)

def listar_superheroes_descendente():  # función para listar en orden descendente
    def __listar_descendente(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            __listar_descendente(root.right)  # primero recorro derecha (mayor)
            if root.other_values["is_villain"] is False:  # si es superhéroe
                print(f"  - {root.value}")  # muestro el nombre
            __listar_descendente(root.left)  # luego recorro izquierda (menor)

    if arbol.root is not None:  # si el árbol no está vacío
        __listar_descendente(arbol.root)  # inicio el recorrido

print()
listar_superheroes_descendente()  # ejecuto la función
print()


# ============================================
# PUNTO G - GENERAR BOSQUE (HÉROES Y VILLANOS)
# ============================================
print("=" * 60)
print("PUNTO G: Generar bosque separando héroes y villanos")
print("=" * 60)

arbol_heroes = BinaryTree()  # creo árbol para héroes
arbol_villanos = BinaryTree()  # creo árbol para villanos

def dividir_arbol():  # función para dividir el árbol original
    def __dividir_arbol(root):  # función recursiva interna
        if root is not None:  # si el nodo existe
            if root.other_values["is_villain"] is False:  # si es héroe
                arbol_heroes.insert(root.value, root.other_values)  # inserto en árbol héroes
            else:  # si es villano
                arbol_villanos.insert(root.value, root.other_values)  # inserto en árbol villanos
            __dividir_arbol(root.left)  # proceso subárbol izquierdo
            __dividir_arbol(root.right)  # proceso subárbol derecho

    __dividir_arbol(arbol.root)  # inicio la división desde la raíz

dividir_arbol()  # ejecuto la división
print("\n✓ Bosque generado correctamente\n")


# ============================================
# PUNTO G-I - CONTAR NODOS DE CADA ÁRBOL
# ============================================
print("=" * 60)
print("PUNTO G-I: Cantidad de nodos en cada árbol")
print("=" * 60)

def contar_nodos(root):  # función para contar todos los nodos
    if root is None:  # si no hay nodo
        return 0  # retorno 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)  # cuento este + hijos

nodos_heroes = contar_nodos(arbol_heroes.root)  # cuento nodos del árbol héroes
nodos_villanos = contar_nodos(arbol_villanos.root)  # cuento nodos del árbol villanos

print(f"\n  - Árbol de Héroes: {nodos_heroes} nodos")
print(f"  - Árbol de Villanos: {nodos_villanos} nodos\n")


# ============================================
# PUNTO G-II - BARRIDO ORDENADO DE CADA ÁRBOL
# ============================================
print("=" * 60)
print("PUNTO G-II: Barrido ordenado alfabéticamente")
print("=" * 60)

def listar_inorden(root):  # función para listar in-order
    if root is not None:  # si el nodo existe
        listar_inorden(root.left)  # recorro subárbol izquierdo
        print(f"  - {root.value}")  # muestro el nombre
        listar_inorden(root.right)  # recorro subárbol derecho

print("\nÁRBOL DE HÉROES:")
listar_inorden(arbol_heroes.root)  # listo héroes

print("\nÁRBOL DE VILLANOS:")
listar_inorden(arbol_villanos.root)  # listo villanos

print("\n" + "=" * 60)