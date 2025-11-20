from typing import Any, Optional

from datos_superheroes import superheroes

class BinaryTree:

    class __nodeTree:

        def __init__(self,value:Any,is_villain: bool, other_values: Optional[Any] = None):
            self.value = value
            self.is_villain = is_villain
            self.other_values = other_values
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any,is_villain: bool, other_values: Optional[Any] = None):
        def __insert(root, value,is_villain, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, is_villain, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value,is_villain, other_values)
            else:
                root.right = __insert(root.right, value,is_villain, other_values)

            return root
        self.root = __insert(self.root, value,is_villain, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                tipo = "villano"
                if not root.is_villain:
                     print(f"{root.value} - {tipo}")
                else:
                     print(f"{root.value} - Heroe")
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                tipo = "villano"
                if not root.is_villain:
                     print(f"{root.value} - {tipo}")
                else:
                     print(f"{root.value} - Heroe")
                __in_order(root.right)

        if self.root is not None:
                __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                __post_order(root.left)
                tipo = "villano"
                if not root.is_villain:
                     print(f"{root.value} - {tipo}")
                else:
                     print(f"{root.value} - Heroe")

        if self.root is not None:
                __post_order(self.root)

    def by_level(self):
                pass
    
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


        



arbol = BinaryTree()

for superheroe in superheroes:
     arbol.insert(superheroe["name"],
                  superheroe["is_villain"],
                    superheroe)
     







'''Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
'''

print("\n")
arbol.in_order()




#b. listar los villanos ordenados alfabéticamente;

villanos = []

def listar_villano(node):
     
     if node is not None:
          listar_villano(node.left)
          if node.is_villain == True:
               villanos.append(node.value)
          listar_villano(node.right)
    

listar_villano(arbol.root)

villanos.sort()

print("\n")
print("Lista de villanos ordenados alfabéticamente")
for villano in villanos:
    print(villano)





#c. mostrar todos los superhéroes que empiezan con C;
heroesConC = []

def listar_superheroes_con_c(node):
     if node is not None:
          listar_superheroes_con_c(node.left)
          if node.is_villain == False and node.value.upper().startswith("C"):
               heroesConC.append(node.value)
          listar_superheroes_con_c(node.right)

listar_superheroes_con_c(arbol.root)

print("\n")
print("super heroes que empiezan con c")
for heroes in heroesConC:
     print(heroes)
          

#d. determinar cuántos superhéroes hay el árbol;
def cont_heroes(node):
     if node is None:
          return 0
     
     contador = 0
     if not node.is_villain == False:
          contador = 1
        
     return contador + cont_heroes(node.left) + cont_heroes(node.right)

total_heroes = cont_heroes(arbol.root)

print("\n")
print(f"la cantidad de heroes es de: {total_heroes}")


#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;

print("\n")
print("nombre anterior")
arbol.proximity_search("Dr Strange")


def update_dr_strange(arbol, nombreActual, nombreNuevo):
     nodo = arbol.search(nombreActual)
     if nodo:
          nodo.value = nombreNuevo
          return True
     return False

update_dr_strange(arbol, "Dr Strange", "Doctor Strange")


print("nombre actualizado")
arbol.proximity_search("Doctor")

#f. listar los superhéroes ordenados de manera descendente;
def heroes_descendentes(node):
     if node is not None:
          heroes_descendentes(node.right)
          if node.is_villain == False:
               print(node.value)
          heroes_descendentes(node.left)
print("\n")
print("super heroes en orden descendente:")
heroes_descendentes(arbol.root)


#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#4I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol.'''


arbol_villanos = BinaryTree()
arbol_heroes = BinaryTree()

for superheroe in superheroes:
     if superheroe["is_villain"] == True:
          arbol_villanos.insert(superheroe["name"],
                                False,
                                superheroe)
     else:
          arbol_heroes.insert(superheroe["name"],
                              True,
                              superheroe)
#print("arbol villanos")
#arbol_villanos.in_order()


#print("arbol heroes")
#arbol_heroes.in_order()


#nodos del arbol superheroe - (Hecho en el inciso d)
print("\n")
print(f"la cantidad de nodos del arbol de heroes es de:{total_heroes}")


def cont_villanos(node):
     if node is None:
          return 0
     
     contador = 0
     if not node.is_villain == True:
          contador = 1
        
     return contador + cont_villanos(node.left) + cont_villanos(node.right)

total_villanos = cont_villanos(arbol.root)
print("\n")
print(f"La cantidad de nodos del arbol de villanos es de: {total_villanos}")


#barrido arbol de heroes
print("\n")
print("barrido arbol de heroes:")
arbol_heroes.in_order()

#barrido arbol de villanos
print("\n")
print("Barrido arbol de villanos:")
arbol_villanos.in_order()