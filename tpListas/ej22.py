from lista_enlazada import ListaEnlazada
from Jedis import jedis

# ============================================
# CARGAR JEDIS EN LA LISTA ENLAZADA
# ============================================
print("=" * 60)
print("EJERCICIO 22 - LISTA ENLAZADA DE JEDIS")
print("=" * 60)

lista_jedis = ListaEnlazada()  # creo la lista enlazada vacía

for jedi in jedis:  # recorro cada jedi de la lista
    lista_jedis.insert_value(jedi)  # inserto el jedi en la lista enlazada

print(f"\n✓ Lista enlazada creada con {len(lista_jedis)} jedis\n")


# ============================================
# CONFIGURAR CRITERIOS DE BÚSQUEDA
# ============================================
def get_nombre(jedi):  # función que devuelve el nombre
    return jedi.get("nombre", "")

def get_especie(jedi):  # función que devuelve la especie
    return jedi.get("especie", "")

lista_jedis.add_criterion("nombre", get_nombre)  # agrego criterio por nombre
lista_jedis.add_criterion("especie", get_especie)  # agrego criterio por especie


# ============================================
# PUNTO A - LISTADO ORDENADO POR NOMBRE Y ESPECIE
# ============================================
print("=" * 60)
print("PUNTO A: Listado ordenado por nombre y por especie")
print("=" * 60)

# Ordenado por nombre
print("\nORDENADO POR NOMBRE:")
jedis_ordenados_nombre = sorted(lista_jedis, key=lambda j: j["nombre"])  # ordeno por nombre

for jedi in jedis_ordenados_nombre:  # recorro los jedis ordenados
    print(f"  - {jedi['nombre']}")  # muestro cada nombre

# Ordenado por especie
print("\nORDENADO POR ESPECIE:")
jedis_ordenados_especie = sorted(lista_jedis, key=lambda j: j["especie"])  # ordeno por especie

for jedi in jedis_ordenados_especie:  # recorro los jedis ordenados
    print(f"  - {jedi['nombre']} ({jedi['especie']})")  # muestro nombre y especie

print()


# ============================================
# PUNTO B - INFORMACIÓN DE AHSOKA TANO Y KIT FISTO
# ============================================
print("=" * 60)
print("PUNTO B: Información completa de Ahsoka Tano y Kit Fisto")
print("=" * 60)

ahsoka = lista_jedis.buscar_por_nombre("Ahsoka Tano")  # busco a Ahsoka Tano
kit_fisto = lista_jedis.buscar_por_nombre("Kit Fisto")  # busco a Kit Fisto

if ahsoka:  # si encontré a Ahsoka
    print("\nAHSOKA TANO:")
    for key, value in ahsoka.items():  # recorro cada clave-valor
        print(f"  {key}: {value}")  # muestro la información
else:  # si no la encontré
    print("\n✗ Ahsoka Tano: No encontrada")

if kit_fisto:  # si encontré a Kit Fisto
    print("\nKIT FISTO:")
    for key, value in kit_fisto.items():  # recorro cada clave-valor
        print(f"  {key}: {value}")  # muestro la información
else:  # si no lo encontré
    print("\n✗ Kit Fisto: No encontrado")

print()


# ============================================
# PUNTO C - PADAWANS DE YODA Y LUKE SKYWALKER
# ============================================
print("=" * 60)
print("PUNTO C: Padawans de Yoda y Luke Skywalker")
print("=" * 60)

yoda = lista_jedis.buscar_por_nombre("Yoda")  # busco a Yoda
luke = lista_jedis.buscar_por_nombre("Luke Skywalker")  # busco a Luke

if yoda:  # si encontré a Yoda
    print("\nPADAWANS DE YODA:")
    padawans_yoda = yoda.get("padawans", [])  # obtengo sus padawans
    if padawans_yoda:  # si tiene padawans
        for padawan in padawans_yoda:  # recorro cada padawan
            print(f"  - {padawan}")  # muestro el nombre
    else:  # si no tiene padawans
        print("  - No tiene padawans")

if luke:  # si encontré a Luke
    print("\nPADAWANS DE LUKE SKYWALKER:")
    padawans_luke = luke.get("padawans", [])  # obtengo sus padawans
    if padawans_luke:  # si tiene padawans
        for padawan in padawans_luke:  # recorro cada padawan
            print(f"  - {padawan}")  # muestro el nombre
    else:  # si no tiene padawans
        print("  - No tiene padawans")

print()


# ============================================
# PUNTO D - JEDIS HUMANOS Y TWI'LEK
# ============================================
print("=" * 60)
print("PUNTO D: Jedis de especie humana y twi'lek")
print("=" * 60)

def es_humano_o_twilek(jedi):  # función que verifica si es humano o twi'lek
    return jedi.get("especie") in ["humana", "twi'lek"]  # comparo la especie

def mostrar_jedi_con_especie(jedi):  # función para mostrar nombre y especie
    print(f"  - {jedi['nombre']} ({jedi['especie']})")

lista_jedis.mostrar_por_condicion(es_humano_o_twilek, mostrar_jedi_con_especie)  # muestro
print()


# ============================================
# PUNTO E - JEDIS QUE COMIENZAN CON A
# ============================================
print("=" * 60)
print("PUNTO E: Jedis que comienzan con la letra A")
print("=" * 60)

def comienza_con_a(jedi):  # función que verifica si comienza con A
    return jedi.get("nombre", "").startswith("A")  # verifico el inicio del nombre

lista_jedis.mostrar_por_condicion(comienza_con_a)  # muestro los que cumplen
print()


# ============================================
# PUNTO F - JEDIS CON MÁS DE UN COLOR DE SABLE
# ============================================
print("=" * 60)
print("PUNTO F: Jedis que usaron sable de luz de más de un color")
print("=" * 60)

def mas_de_un_color(jedi):  # función que verifica si tiene más de un color
    return len(jedi.get("colores_sable", [])) > 1  # cuento los colores

def mostrar_jedi_con_colores(jedi):  # función para mostrar nombre y colores
    colores = ", ".join(jedi["colores_sable"])  # uno los colores con comas
    print(f"  - {jedi['nombre']}: {colores}")

lista_jedis.mostrar_por_condicion(mas_de_un_color, mostrar_jedi_con_colores)  # muestro
print()


# ============================================
# PUNTO G - JEDIS CON SABLE AMARILLO O VIOLETA
# ============================================
print("=" * 60)
print("PUNTO G: Jedis que utilizaron sable amarillo o violeta")
print("=" * 60)

def usa_amarillo_o_violeta(jedi):  # función que verifica si usa amarillo o violeta
    colores = jedi.get("colores_sable", [])  # obtengo la lista de colores
    return "amarillo" in colores or "violeta" in colores  # verifico si alguno está

def mostrar_jedi_con_colores_especificos(jedi):  # función para mostrar nombre y colores
    colores = ", ".join(jedi["colores_sable"])  # uno los colores
    print(f"  - {jedi['nombre']}: {colores}")

lista_jedis.mostrar_por_condicion(usa_amarillo_o_violeta, mostrar_jedi_con_colores_especificos)
print()


# ============================================
# PUNTO H - PADAWANS DE QUI-GON JINN Y MACE WINDU
# ============================================
print("=" * 60)
print("PUNTO H: Padawans de Qui-Gon Jinn y Mace Windu")
print("=" * 60)

qui_gon = lista_jedis.buscar_por_nombre("Qui-Gon Jinn")  # busco a Qui-Gon
mace = lista_jedis.buscar_por_nombre("Mace Windu")  # busco a Mace Windu

if qui_gon:  # si encontré a Qui-Gon
    print("\nPADAWANS DE QUI-GON JINN:")
    padawans_quigon = qui_gon.get("padawans", [])  # obtengo sus padawans
    if padawans_quigon:  # si tiene padawans
        for padawan in padawans_quigon:  # recorro cada padawan
            print(f"  - {padawan}")  # muestro el nombre
    else:  # si no tiene padawans
        print("  - No tuvo padawans")

if mace:  # si encontré a Mace Windu
    print("\nPADAWANS DE MACE WINDU:")
    padawans_mace = mace.get("padawans", [])  # obtengo sus padawans
    if padawans_mace:  # si tiene padawans
        for padawan in padawans_mace:  # recorro cada padawan
            print(f"  - {padawan}")  # muestro el nombre
    else:  # si no tiene padawans
        print("  - No tuvo padawans")

print("\n" + "=" * 60)