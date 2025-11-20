from typing import Any, Optional
from typing import Dict
from collections import deque

from datos_criaturas import criaturas

class CreatureTree:

    class __nodeTree:
        
        def __init__(self, value: Any, Other_value: Optional[Any] = None):
            self.value = value
            self.other_value = Other_value
            self.descripcion = ""
            self.capturada = None
            self.left = None
            self.right = None 

    def __init__(self):
        self.root = None

    def insert(self: Any,value, other_value: Optional[Any] = None):
        def __insert(root, value, other_value):
            if root is None: 
                return CreatureTree.__nodeTree(value, other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value) 

            return root
        self.root = __insert(self.root, value, other_value)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)


    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                __in_order(root.right)         
        
        if self.root is not None:
            __in_order(self.root)

    
    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                __post_order(root.left)
        
        if self.root is not None:
            __post_order(self.root)

    
    def search(self, value: Any) -> __nodeTree:
                def __search(root, value):
                     if root is not None:
                        if root.value == value:
                              return root
                        elif root.value > value:
                             return __search(root.left, value)
                        else:
                             return __search(root.right, value)
                        
                aux = None
                if self.root is not None:
                     aux = __search(self.root, value)
                return aux
    
    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux


    def busqueda_por_coincidencia(self, value :Any): 
   
        def __search(root, value):
            if root is not None:
         
                if value.lower() in root.value.lower():
                    print(root.value)
          
                __search(root.left, value)
                __search(root.right, value)
    
        if self.root is not None:
            __search(self.root, value)  


    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_value
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_value

                #root = self.auto_balance(root)
                #self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    

arbol = CreatureTree()

for criatura in criaturas:
    arbol.insert(criatura["nombre"],
                 criatura)
    


#a. listado inorden de las criaturas y quienes la derrotaron;
print("Listado de criaturas y quienes la derrotaron")
arbol.in_order()
for c in criaturas:
    print(c)



#b. se debe permitir cargar una breve descripción sobre cada criatura;


def agregar_descripcion(nombre: str, descripcion: str):
    
    for criatura in criaturas:
        if criatura["nombre"] == nombre:
            criatura["descricion"] = descripcion
            print(f"descrición agregada para {nombre}")
            return True
        
agregar_descripcion("Ceto", "Diosa marina primordial, madre de monstruos en la mitologia griega.")
agregar_descripcion("Talos", "Gigante de bronce que protegia Creta circunnavegando la isla.")

print("\n")
print("caso de prueba de agregar descripcion a una criatura")
for criatura in criaturas:
    if criatura["nombre"] == "Ceto":
        print(criatura)


'''
agregar_descripcion("Tifon", "Monstruo gigante con serpientes en lugar de dedos, enemigo de Zeus.")
agregar_descripcion("Equidna", "Madre de todos los monstruos, mitad mujer hermosa y mitad serpiente.")
agregar_descripcion("Dino", "Una de las tres Grayas, hermanas ancianas que compartian un solo ojo.")
agregar_descripcion("Pefredo", "Graya hermana de Dino y Enio, vigilantes de las Gorgonas.")
agregar_descripcion("Enio", "Tercera Graya, diosa de la violencia y destruccion en la guerra.")
agregar_descripcion("Escila", "Monstruo marino de seis cabezas que devoraba marineros en el estrecho.")
agregar_descripcion("Caribdis", "Torbellino marino que tragaba barcos enteros tres veces al dia.")
agregar_descripcion("Euriale", "Gorgona inmortal, hermana de Medusa, convertida en monstruo por Atenea.")
agregar_descripcion("Esteno", "Gorgona más fuerte que sus hermanas, conocida por su ferocidad.")
agregar_descripcion("Medusa", "Gorgona mortal con serpientes por cabello que petrificaba con la mirada.")
agregar_descripcion("Ladon", "Dragon de cien cabezas que custodiaba las manzanas de oro del Jardin.")
agregar_descripcion("Aguila del Caucaso", "Ave gigante que devoraba el higado de Prometeo diariamente.")
agregar_descripcion("Quimera", "Monstruo que escupia fuego con cabeza de leon, cabra y serpiente.")
agregar_descripcion("Hidra de Lerna", "Serpiente de multiples cabezas que regeneraba dos al cortar una.")
agregar_descripcion("Leon de Nemea", "Bestia invulnerable con piel impenetrable que aterrorizaba Nemea.")
agregar_descripcion("Esfinge", "Criatura con cabeza humana y cuerpo de leon que proponía enigmas.")
agregar_descripcion("Dragon de la Colquida", "Serpiente gigante que vigilaba el Vellocino de Oro.")
agregar_descripcion("Cerbero", "Perro de tres cabezas que guardaba la entrada al Inframundo.")
agregar_descripcion("Cerda de Cromion", "Jabali gigante y feroz que devastaba la región de Cromion.")
agregar_descripcion("Ortro", "Perro de dos cabezas, hermano de Cerbero y guardian de ganado.")
agregar_descripcion("Toro de Creta", "Toro salvaje enviado por Poseidón que sembraba el terror en Creta.")
agregar_descripcion("Jabali de Calidon", "Enorme jabali enviado por Artemisa para castigar Calidon.")
agregar_descripcion("Carcinos", "Cangrejo gigante que ayudo a la Hidra contra Heracles.")
agregar_descripcion("Gerion", "Gigante de tres cuerpos que poseia magnificos rebaños de bueyes.")
agregar_descripcion("Cloto", "Una de las tres Moiras, hilaba el hilo de la vida humana.")
agregar_descripcion("Laquesis", "Moira que media la longitud del hilo del destino de cada persona.")
agregar_descripcion("Átropos", "Moira que cortaba el hilo de la vida.")
agregar_descripcion("Minotauro de Creta", "Hombre con cabeza de toro encerrado en el laberinto cretense.")
agregar_descripcion("Harpias", "Criaturas aladas con rostro de mujer que robaban comida.")
agregar_descripcion("Argos Panoptes", "Gigante de cien ojos que vigilaba constantemente sin dormir.")
agregar_descripcion("Aves del Estinfalo", "Aves carnivoras con plumas de bronce que atacaban con ellas.")
agregar_descripcion("Sirenas", "Criaturas marinas que hechizaban a marineros con su canto mortal.")
agregar_descripcion("Piton", "Serpiente gigante que custodiaba el oraculo de Delfos antes de Apolo.")
agregar_descripcion("Cierva de Cerinea", "Cierva sagrada de cuernos dorados y pezuñas de bronce.")
agregar_descripcion("Basilisco", "Rey de las serpientes, capaz de matar con solo una mirada.")
agregar_descripcion("Jabali de Erimanto", "Jabali gigante que devastaba los campos alrededor de Erimanto.")'''


#c. mostrar toda la información de la criatura Talos;
print("\n")
print("informacion complenta sobre talos")

for criatura in criaturas: 
    if criatura["nombre"] == "Talos":
        print(criatura)


#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def masDerrotas(criaturas):

    cont_derrotas = {}
    criaturas_vencidas = {}

    for criatura in criaturas:
        vencedor = criatura["derrotado_por"]
        if vencedor:
            if vencedor in cont_derrotas:
                cont_derrotas[vencedor] +=1
            else:
                cont_derrotas[vencedor] = 1

            if vencedor in criaturas_vencidas:
                criaturas_vencidas[vencedor].append(criatura["nombre"])
            else:
                criaturas_vencidas[vencedor] = [criatura["nombre"]]

    vencedores_ordenados = sorted(cont_derrotas.items(),
                                  key = lambda x: x[1],
                                  reverse = True)
    
    top_tres = vencedores_ordenados[:3]

    print("\n")
    for i, (vencedor, cantidad) in enumerate(top_tres, 1):
        print("top 3 de dioses con mas derrotas a criaturas ")
        print(f"{i}. nombre: {vencedor}: derrotas :{cantidad}")
        
    
    return top_tres

top_tres = masDerrotas(criaturas)




#e. listar las criaturas derrotadas por Heracles;
def derrotas_heracles(criaturas):

    criaturas_heracles = []
    
    for criatura in criaturas:
        if criatura["derrotado_por"] == "Heracles":
            criaturas_heracles.append(criatura["nombre"])
    print("\n")
    print("Las crituras derrotadas por Heracles son:")
    for criatura in criaturas_heracles:
        print(f"{criatura}")
    

    return derrotas_heracles

derrotas_heracles(criaturas)


#f. listar las criaturas que no han sido derrotadas;
def criaturas_sin_derrotas(criaturas):
    criaturas_cero_derrotas = []

    for criatura in criaturas: 
        if criatura["derrotado_por"] is None:
            criaturas_cero_derrotas.append(criatura)
    print("\n")
    print("criaturas que nunca han sido derrotadas:")
    for criatura in criaturas_cero_derrotas:
        print(f"nombre: {criatura['nombre']} - derrotas:{criatura['derrotado_por']}")

    return criaturas_cero_derrotas

criaturas_sin_derrotas(criaturas)


#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#o dios que la capturo;
def asignar_captura_en_arbol(arbol, nombre_criatura: str, captor: str):
    nodo = arbol.search(nombre_criatura)
    if nodo:
        nodo.capturada = captor

# Uso
arbol = CreatureTree()
for criatura in criaturas:
    arbol.insert(criatura["nombre"], criatura)



asignar_captura_en_arbol(arbol,"Medusa", "Perseo"),
asignar_captura_en_arbol(arbol,"Minotauro de Creta", "Teseo"),
asignar_captura_en_arbol(arbol,"Leon de Nemea", "Heracles"),
asignar_captura_en_arbol(arbol,"Hidra de Lerna", "Heracles"),
asignar_captura_en_arbol(arbol,"Cerbero", "Heracles"),
asignar_captura_en_arbol(arbol,"Jabali de Erimanto", "Heracles"),
asignar_captura_en_arbol(arbol,"Cierva de Cerinea", "Heracles"),
asignar_captura_en_arbol(arbol,"Aves del Estinfalo", "Heracles"),
asignar_captura_en_arbol(arbol,"Toro de Creta", "Heracles"),
asignar_captura_en_arbol(arbol,"Cerda de Cromion", "Teseo"),
asignar_captura_en_arbol(arbol,"Ortro", "Heracles"),
asignar_captura_en_arbol(arbol,"Gerion", "Heracles"),
asignar_captura_en_arbol(arbol,"Ladon", "Heracles"),
asignar_captura_en_arbol(arbol,"Quimera", "Belerofonte"),
asignar_captura_en_arbol(arbol,"Esfinge", "Edipo"),
asignar_captura_en_arbol(arbol,"Talos", "Medea"),
asignar_captura_en_arbol(arbol,"Piton", "Apolo"),
asignar_captura_en_arbol(arbol,"Argos Panoptes", "Hermes")

print("\n")
print("prueba de creación de campo capturada")
nodo = arbol.search("Medusa")
print(f"Medusa capturada por : {nodo.capturada}")




#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;

crituras_heracles = [
    "Cerbero",
    "Toro de Creta",
    "Cierva de Cerina",
    "Jabali de Erimanto"
]

for criatura in crituras_heracles:
    asignar_captura_en_arbol(arbol, criatura, "Heracles")

print("\n")
print("modificación de captor a Heracles.")
nodo1 = arbol.search("Cerbero")
print(f"Cerbero fue capturado por: {nodo1.capturada}")
nodo2 = arbol.search("Toro de Creta")
print(f"Toro de Creta fue capturado por: {nodo2.capturada}")
nodo3 = arbol.search("Cierva de Cerinea")
print(f"Cierva de Cerina fue capturado por: {nodo3.capturada}")
nodo4 = arbol.search("Jabali de Erimanto")
print(f"Jabali de erimanto fue capturado por: {nodo4.capturada}")

#i. se debe permitir búsquedas por coincidencia;
print("\n")
print("prueba busqueda por coincidencia")
print("prueba con jabali:")
arbol.busqueda_por_coincidencia("Jabali")

#j. eliminar al Basilisco y a las Sirenas;
criaturas_a_eliminar = ["Basilisco", "Sirenas"]
 
print("\n")
print("Eliminando a Basilisco y Sirenas")

delete_value1, deleter_other_values1 = arbol.delete('Basilisco')
if delete_value1 is not None:
    print(f" Basilisco eliminado: {delete_value1}")
    print(f"   Datos eliminados: {deleter_other_values1}")
else:
    print(" Basilisco no se pudo eliminar (posiblemente no existe)")

# Eliminar a las Sirenas  
delete_value2, deleter_other_values2 = arbol.delete('Sirenas')
if delete_value2 is not None:
    print(f" Sirenas eliminadas: {delete_value2}")
    print(f"   Datos eliminados: {deleter_other_values2}")
else:
    print(" Sirenas no se pudieron eliminar (posiblemente no existen)")


nodo1 = arbol.search('Basilisco')
nodo2 = arbol.search('Sirenas')

#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
nodo_aves = arbol.search("Aves del Estinfalo")

if nodo_aves:
    nodo_aves.descripcion = "Aves carnívoras con plumas de bronce. Heracles derrotó a varias de estas aves como parte de sus doce trabajos."
    

    for criatura in criaturas:
        if criatura["nombre"] == "Aves del Estinfalo":
            criatura["descripcion"] = nodo_aves.descripcion
            break
    
    print(" Información de Aves del Estinfalo actualizada")
    print(f"   Nueva descripcion: {nodo_aves.descripcion}")
else:
    print("Aves del Estinfalo no encontradas en el arbol")


print("\n")
print("modificacion del nodo aves")
nodo_verificacion = arbol.search("Aves del Estinfalo")
if nodo_verificacion and nodo_verificacion.descripcion:
    print(f" Aves del Estinfalo - Descripcion: {nodo_verificacion.descripcion}")
else:
    print(" No se pudo verificar la modificacion")


#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
nodo_ladon = arbol.search("Ladon")

if nodo_ladon:
    nombre_original = nodo_ladon.value
    datos_originales = nodo_ladon.other_value

    delete_value, other_value = arbol.delete("Ladon")

    if delete_value:
        arbol.insert("Dragon Ladon", datos_originales)

        nuevo_nodo = arbol.search("Dragon Ladon")
        if nuevo_nodo:
            nuevo_nodo.descripcion = nodo_ladon.descripcion
            nuevo_nodo.capturada = nodo_ladon.capturada

        print(f"nombre cambiado {nombre_original} - Dragon Ladon")
        print(f"datos mantenidos: {datos_originales}")


#m. realizar un listado por nivel del árbol;
def listado_por_nivel_externo(arbol):

    
    if arbol.root is None:
        print("El arbol está vacio")
        return
    
    from collections import deque
    cola = deque()
    cola.append(arbol.root)
    nivel_actual = 0
    
    print("LISTADO POR NIVEL DEL ARBOL")
    
    while cola:
        nodos_en_nivel = len(cola)
        print(f"\nNivel {nivel_actual}: ", end="")
        
        for i in range(nodos_en_nivel):
            nodo_actual = cola.popleft()
            print(nodo_actual.value, end="")
            
            if i < nodos_en_nivel - 1:
                print(" | ", end="")
            
            if nodo_actual.left:
                cola.append(nodo_actual.left)
            if nodo_actual.right:
                cola.append(nodo_actual.right)
        
        nivel_actual += 1
    print()


print("\n")
listado_por_nivel_externo(arbol)


#n. muestre las criaturas capturadas por Heracles.
print("\n")
print("Criaturas capturadas por Heracles. ")
for criatura in crituras_heracles:
    print(criatura)