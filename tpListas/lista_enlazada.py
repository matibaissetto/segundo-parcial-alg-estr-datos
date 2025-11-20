from typing import Any, Optional

# ============================================
# CLASE NODO
# ============================================
# Qué hace: Representa un nodo individual de la lista enlazada. Cada nodo tiene un dato y una referencia al siguiente nodo
class Nodo:
    def __init__(self, dato: Any):
        self.dato = dato  # el dato que guarda el nodo
        self.siguiente = None  # referencia al siguiente nodo (inicialmente None)


# ============================================
# CLASE LISTA ENLAZADA
# ============================================
class ListaEnlazada:
    
    # Qué hace: Inicializa la lista enlazada vacía con cabeza=None, tamaño=0 y un diccionario de criterios vacío
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
        self.criterios = {}
    
    
    # Qué hace: Guarda una función de búsqueda con un nombre clave para usar después en búsquedas/eliminaciones
    # Ejemplo: add_criterion("nombre", get_nombre) → guarda la función para buscar por nombre
    def add_criterion(self, key_criterion: str, function):
        self.criterios[key_criterion] = function
    
    
    # Qué hace: Inserta un nodo AL FINAL de la lista. Crea un nuevo nodo, si la lista está vacía lo hace cabeza, si no recorre hasta el final y lo agrega ahí
    def insert_value(self, value: Any, position=None):
        nuevo_nodo = Nodo(value)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamaño += 1
    
    
    # Qué hace: Elimina el PRIMER nodo que coincida con el valor buscado. Recorre la lista, cuando lo encuentra lo "desenlaza" conectando el anterior con el siguiente
    # Visualización: Antes: [A] → [B] → [C]  (eliminar B) → Después: [A] → [C]
    def delete_value(self, value, key_value: str = None):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if key_value and key_value in self.criterios:
                valor_comparar = self.criterios[key_value](actual.dato)
            else:
                valor_comparar = actual.dato
            
            if valor_comparar == value:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                self.tamaño -= 1
                return actual.dato
            
            anterior = actual
            actual = actual.siguiente
        
        return None
    
    
    # Qué hace: Busca un elemento por nombre. Funciona tanto con "name" como con "nombre". Recorre secuencialmente todos los nodos y devuelve el diccionario completo si lo encuentra
    def buscar_por_nombre(self, nombre: str):
        actual = self.cabeza
        while actual:
            # Busca tanto por "name" como por "nombre"
            if actual.dato.get("name") == nombre or actual.dato.get("nombre") == nombre:
                return actual.dato
            actual = actual.siguiente
        return None
    
    
    # Qué hace: Muestra nodos que cumplen una condición. Recibe una función que retorna True/False, recorre todos los nodos y muestra solo los que cumplen. Puedes personalizar cómo mostrar con mostrar_func
    def mostrar_por_condicion(self, condicion, mostrar_func=None):
        actual = self.cabeza
        while actual:
            if condicion(actual.dato):
                if mostrar_func:
                    mostrar_func(actual.dato)
                else:
                    # Intenta mostrar "name" o "nombre" según lo que tenga el dato
                    nombre = actual.dato.get('name') or actual.dato.get('nombre')
                    print(f"- {nombre}")
            actual = actual.siguiente
    
    
    # Qué hace: Cuenta cuántos superhéroes hay de cada casa. Recorre todos los nodos, por cada casa incrementa un contador y devuelve un diccionario con el conteo {"Marvel": 95, "DC": 10}
    def contar_por_casa(self):
        casas = {}
        actual = self.cabeza
        while actual:
            casa = actual.dato.get("comic_house", "Desconocida")
            casas[casa] = casas.get(casa, 0) + 1
            actual = actual.siguiente
        return casas
    
    
    # Qué hace: Muestra TODOS los datos de la lista. Recorre secuencialmente desde la cabeza e imprime cada dato completo
    def show(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    
    # Qué hace: Permite usar la lista en un for (ejemplo: for elemento in lista:). Es un generador que va devolviendo cada dato
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
    
    
    # Qué hace: Devuelve la cantidad de nodos. Permite usar len(lista)
    def __len__(self):
        return self.tamaño
    
    
    # Qué hace: Muestra la estructura de la lista enlazada de forma visual. Recorre los primeros 5 nodos y muestra cómo están enlazados
    def demostrar_estructura(self):
        print("\n" + "=" * 50)
        print("ESTRUCTURA DE LISTA ENLAZADA:")
        print("=" * 50)
        
        actual = self.cabeza
        contador = 0
        print("Recorriendo nodos:")
        while actual and contador < 5:
            # Intenta obtener "name" o "nombre"
            nombre = actual.dato.get('name') or actual.dato.get('nombre')
            siguiente_nombre = None
            if actual.siguiente:
                siguiente_nombre = actual.siguiente.dato.get('name') or actual.siguiente.dato.get('nombre')
            siguiente_nombre = siguiente_nombre if siguiente_nombre else "NULL"
            print(f"Nodo {contador + 1}: {nombre} -> Siguiente: {siguiente_nombre}")
            actual = actual.siguiente
            contador += 1
        
        if self.tamaño > 5:
            print(f"... hasta {self.tamaño} nodos")
        print(f"Total: {self.tamaño} nodos")
        print("=" * 50)