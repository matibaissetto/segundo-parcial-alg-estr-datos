#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue
from stack import Stack

# Datos de las notificaciones
cola_notificaciones = [
    {"hora": "11:47", "app": "facebook", "mensaje": "Hola, como estas?"},
    {"hora": "12:30", "app": "instagram", "mensaje": "Que haces"},
    {"hora": "12:45", "app": "instagram", "mensaje": "Que comemos?"},
    {"hora": "11:58", "app": "telegram", "mensaje": "A cuanto?"},
    {"hora": "15:12", "app": "facebook", "mensaje": "No voy a ir"},
    {"hora": "16:45", "app": "facebook", "mensaje": "Compra una fresca"},
    {"hora": "18:25", "app": "telegram", "mensaje": "Ahora paso"},
    {"hora": "19:45", "app": "instagram", "mensaje": "Hoy te vi!"},
    {"hora": "20:20", "app": "facebook", "mensaje": "Y.. Axel es terrible"},
    {"hora": "01:15", "app": "instagram", "mensaje": "Estas para House?"},
    {"hora": "17:14", "app": "twitter", "mensaje": "sabes phyton?"},
    {"hora": "11:59", "app": "twitter", "mensaje": "Mañana paso por ahí"},
    {"hora": "12:01", "app": "twitter", "mensaje": "tenes lo de phyton?"}
]

# ============================================
# CARGAR NOTIFICACIONES EN LA COLA
# ============================================
cola = Queue()  # creo la cola vacía
for notificacion in cola_notificaciones:  # recorro cada notificación de la lista
    cola.arrive(notificacion)  # agrego la notificación a la cola


# ============================================
# PUNTO A - ELIMINAR FACEBOOK
# ============================================
print("=" * 60)
print("PUNTO A: Eliminar notificaciones de Facebook")
print("=" * 60)

cola_aux = Queue()  # creo cola auxiliar vacía
contador_eliminadas = 0  # contador en cero

while cola.size() > 0:  # mientras la cola tenga notificaciones
    notificacion = cola.attention()  # saco la primera notificación
    if notificacion["app"] == "facebook":  # si es de Facebook
        contador_eliminadas += 1  # cuento la eliminada
        # NO la agrego a cola_aux, así la elimino
    else:  # si NO es de Facebook
        cola_aux.arrive(notificacion)  # la agrego a la cola auxiliar

while cola_aux.size() > 0:  # mientras la auxiliar tenga notificaciones
    cola.arrive(cola_aux.attention())  # paso de auxiliar a cola original

print(f"\n✓ Se eliminaron {contador_eliminadas} notificaciones de Facebook")


# ============================================
# PUNTO B - MOSTRAR TWITTER CON "PYTHON"
# ============================================
print("\n" + "=" * 60)
print("PUNTO B: Notificaciones de Twitter con la palabra 'Python'")
print("=" * 60)

notificaciones_encontradas = []  # lista vacía para guardar las encontradas
tamanio_original = cola.size()  # guardo el tamaño original de la cola

for i in range(tamanio_original):  # recorro tantas veces como elementos hay
    notificacion = cola.attention()  # saco la primera notificación
    # Verifico si es de Twitter y contiene "python" (sin importar mayúsculas)
    if notificacion["app"] == "twitter" and "python" in notificacion["mensaje"].lower():
        notificaciones_encontradas.append(notificacion)  # guardo la notificación
    cola.arrive(notificacion)  # vuelvo a agregar al final para no perder datos

if notificaciones_encontradas:  # si encontré notificaciones
    print("\n Notificaciones de Twitter con 'Python':")
    for notif in notificaciones_encontradas:  # recorro las encontradas
        print(f"  [{notif['hora']}] {notif['mensaje']}")  # muestro hora y mensaje
else:  # si no encontré ninguna
    print("\n No hay notificaciones de Twitter con 'Python'")


# ============================================
# PUNTO C - PILA DE NOTIFICACIONES 11:43 A 15:57
# ============================================
print("\n" + "=" * 60)
print("PUNTO C: Notificaciones entre 11:43 y 15:57")
print("=" * 60)

pila_temporal = Stack()  # creo pila vacía para almacenar temporalmente
cola_aux = Queue()  # creo cola auxiliar

hora_inicio = "11:43"  # hora de inicio del rango
hora_fin = "15:57"  # hora de fin del rango

while cola.size() > 0:  # mientras la cola tenga notificaciones
    notificacion = cola.attention()  # saco la primera notificación
    # Verifico si la hora está en el rango
    if hora_inicio <= notificacion["hora"] <= hora_fin:  # si está en el rango
        pila_temporal.push(notificacion)  # la meto en la pila
    cola_aux.arrive(notificacion)  # la agrego a auxiliar de todas formas

while cola_aux.size() > 0:  # mientras auxiliar tenga notificaciones
    cola.arrive(cola_aux.attention())  # restauro la cola original

cantidad = pila_temporal.size()  # obtengo la cantidad de notificaciones en la pila
print(f"\n Cantidad de notificaciones entre {hora_inicio} y {hora_fin}: {cantidad}")

if cantidad > 0:  # si hay notificaciones en la pila
    print("\nNotificaciones almacenadas en la pila:")
    pila_aux_stack = Stack()  # pila auxiliar para no perder datos
    while pila_temporal.size() > 0:  # mientras la pila tenga notificaciones
        notif = pila_temporal.pop()  # saco de la pila
        print(f"  [{notif['hora']}] {notif['app']}: {notif['mensaje']}")  # muestro la notificación
        pila_aux_stack.push(notif)  # guardo en auxiliar
    
    while pila_aux_stack.size() > 0:  # mientras auxiliar tenga notificaciones
        pila_temporal.push(pila_aux_stack.pop())  # restauro la pila temporal

print("\n" + "=" * 60)