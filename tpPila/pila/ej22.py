#22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, costo de la recompensa. Resolver las siguientes actividades:
#a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
#b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
#c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

from stack import Stack

# Datos de las bitácoras
pila_boba_fett = [
    {"planeta": "Tatooine", "capturado": "Han Solo", "recompensa": 50000},
    {"planeta": "Bespin", "capturado": "Lando Calrissian", "recompensa": 30000},
    {"planeta": "Kamino", "capturado": "Clone Rebel", "recompensa": 15000},
    {"planeta": "Tatooine", "capturado": "Jabba the Hutt", "recompensa": 75000},
    {"planeta": "Coruscant", "capturado": "Jedi Fugitive", "recompensa": 45000}
]

pila_din_djarin = [
    {"planeta": "Nevarro", "capturado": "The Child", "recompensa": 100000},
    {"planeta": "Sorgan", "capturado": "Fugitive Droids", "recompensa": 20000},
    {"planeta": "Tatooine", "capturado": "Fennec Shand", "recompensa": 35000},
    {"planeta": "Mandalore", "capturado": "Imperial Officer", "recompensa": 60000},
    {"planeta": "Nevarro", "capturado": "Guild Target", "recompensa": 25000}
]

# ============================================
# CARGAR BITÁCORAS EN LAS PILAS
# ============================================
pila_boba = Stack()  # creo pila para Boba Fett
for mision in pila_boba_fett:  # recorro cada misión de la lista
    pila_boba.push(mision)  # meto la misión en la pila

pila_din = Stack()  # creo pila para Din Djarin
for mision in pila_din_djarin:  # recorro cada misión de la lista
    pila_din.push(mision)  # meto la misión en la pila


# ============================================
# PUNTO A - PLANETAS VISITADOS
# ============================================
print("=" * 60)
print("PUNTO A: Planetas visitados en orden de misiones")
print("=" * 60)

# Boba Fett
print("\n BOBA FETT:")
pila_aux = Stack()  # primera pila auxiliar
pila_aux2 = Stack()  # segunda pila auxiliar

while pila_boba.size() > 0:  # mientras haya misiones
    mision = pila_boba.pop()  # saco la misión de arriba
    pila_aux.push(mision)  # meto en primera auxiliar

while pila_aux.size() > 0:  # mientras primera auxiliar tenga misiones
    mision = pila_aux.pop()  # saco de primera auxiliar
    pila_aux2.push(mision)  # meto en segunda auxiliar

contador = 1  # contador para número de misión
while pila_aux2.size() > 0:  # mientras segunda auxiliar tenga misiones
    mision = pila_aux2.pop()  # saco de segunda auxiliar
    print(f"  Misión {contador}: {mision['planeta']}")  # muestro número y planeta
    contador += 1  # aumento el contador
    pila_boba.push(mision)  # devuelvo a la pila original


# Din Djarin
print("\n DIN DJARIN:")
pila_aux = Stack()  # primera pila auxiliar
pila_aux2 = Stack()  # segunda pila auxiliar

while pila_din.size() > 0:  # mientras haya misiones
    mision = pila_din.pop()  # saco la misión de arriba
    pila_aux.push(mision)  # meto en primera auxiliar

while pila_aux.size() > 0:  # mientras primera auxiliar tenga misiones
    mision = pila_aux.pop()  # saco de primera auxiliar
    pila_aux2.push(mision)  # meto en segunda auxiliar

contador = 1  # contador para número de misión
while pila_aux2.size() > 0:  # mientras segunda auxiliar tenga misiones
    mision = pila_aux2.pop()  # saco de segunda auxiliar
    print(f"  Misión {contador}: {mision['planeta']}")  # muestro número y planeta
    contador += 1  # aumento el contador
    pila_din.push(mision)  # devuelvo a la pila original


# ============================================
# PUNTO B - CRÉDITOS GALÁCTICOS
# ============================================
print("\n" + "=" * 60)
print("PUNTO B: Créditos galácticos recaudados")
print("=" * 60)

# Boba Fett
pila_aux = Stack()  # pila auxiliar
total_boba = 0  # contador en cero

while pila_boba.size() > 0:  # mientras haya misiones
    mision = pila_boba.pop()  # saco una misión
    total_boba += mision["recompensa"]  # sumo la recompensa al total
    pila_aux.push(mision)  # meto en auxiliar

while pila_aux.size() > 0:  # mientras auxiliar tenga misiones
    pila_boba.push(pila_aux.pop())  # devuelvo a la pila original

print(f"\n Boba Fett: {total_boba:,} créditos galácticos")  # muestro el total


# Din Djarin
pila_aux = Stack()  # nueva pila auxiliar
total_din = 0  # contador en cero

while pila_din.size() > 0:  # mientras haya misiones
    mision = pila_din.pop()  # saco una misión
    total_din += mision["recompensa"]  # sumo la recompensa al total
    pila_aux.push(mision)  # meto en auxiliar

while pila_aux.size() > 0:  # mientras auxiliar tenga misiones
    pila_din.push(pila_aux.pop())  # devuelvo a la pila original

print(f" Din Djarin: {total_din:,} créditos galácticos")  # muestro el total


# Determinar quién ganó más
if total_boba > total_din:  # si Boba ganó más
    print(f"\n Mayor fortuna: Boba Fett con {total_boba:,} créditos")
elif total_din > total_boba:  # si Din ganó más
    print(f"\n Mayor fortuna: Din Djarin con {total_din:,} créditos")
else:  # si están empatados
    print(f"\n Empate: ambos con {total_boba:,} créditos")


# ============================================
# PUNTO C - MISIÓN DE HAN SOLO
# ============================================
print("\n" + "=" * 60)
print("PUNTO C: Misión donde Boba Fett capturó a Han Solo")
print("=" * 60)

pila_aux = Stack()  # primera pila auxiliar
pila_aux2 = Stack()  # segunda pila auxiliar

while pila_boba.size() > 0:  # mientras haya misiones
    mision = pila_boba.pop()  # saco una misión
    pila_aux.push(mision)  # meto en auxiliar

while pila_aux.size() > 0:  # mientras primera auxiliar tenga misiones
    mision = pila_aux.pop()  # saco de primera auxiliar
    pila_aux2.push(mision)  # meto en segunda auxiliar

numero_mision = 0  # número de misión donde capturó a Han Solo
contador = 0  # contador de posición

while pila_aux2.size() > 0:  # mientras segunda auxiliar tenga misiones
    mision = pila_aux2.pop()  # saco una misión
    contador += 1  # aumento el contador
    if mision["capturado"] == "Han Solo":  # si capturó a Han Solo
        numero_mision = contador  # guardo el número de misión
    pila_boba.push(mision)  # devuelvo a la pila original

if numero_mision > 0:  # si encontré a Han Solo
    print(f"\n Han Solo fue capturado en la misión número: {numero_mision}")
    print(f"   (contando desde el fondo de la pila)")
else:  # si no lo encontré
    print("\n❌ Han Solo no fue capturado en ninguna misión")


# ============================================
# PUNTO D - CANTIDAD DE CAPTURAS
# ============================================
print("\n" + "=" * 60)
print("PUNTO D: Cantidad de capturas realizadas")
print("=" * 60)

# Boba Fett
pila_aux = Stack()  # pila auxiliar
capturas_boba = 0  # contador en cero

while pila_boba.size() > 0:  # mientras haya misiones
    mision = pila_boba.pop()  # saco una misión
    capturas_boba += 1  # sumo 1 al contador (cada misión es una captura)
    pila_aux.push(mision)  # meto en auxiliar

while pila_aux.size() > 0:  # mientras auxiliar tenga misiones
    pila_boba.push(pila_aux.pop())  # devuelvo a la pila original

print(f"\n Boba Fett: {capturas_boba} capturas")  # muestro cuántas capturas


# Din Djarin
pila_aux = Stack()  # nueva pila auxiliar
capturas_din = 0  # contador en cero

while pila_din.size() > 0:  # mientras haya misiones
    mision = pila_din.pop()  # saco una misión
    capturas_din += 1  # sumo 1 al contador
    pila_aux.push(mision)  # meto en auxiliar

while pila_aux.size() > 0:  # mientras auxiliar tenga misiones
    pila_din.push(pila_aux.pop())  # devuelvo a la pila original

print(f" Din Djarin: {capturas_din} capturas")  # muestro cuántas capturas

print("\n" + "=" * 60)