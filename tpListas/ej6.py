from lista_enlazada import ListaEnlazada
from SuperHeroes import superheroes

# ============================================
# CARGAR SUPERHÉROES EN LA LISTA ENLAZADA
# ============================================
print("=" * 60)
print("EJERCICIO 6 - LISTA ENLAZADA DE SUPERHÉROES")
print("=" * 60)

lista_superheroes = ListaEnlazada()  # creo la lista enlazada vacía

for heroe in superheroes:  # recorro cada superhéroe de la lista
    lista_superheroes.insert_value(heroe)  # inserto el héroe en la lista enlazada

print(f"\n✓ Lista enlazada creada con {len(lista_superheroes)} nodos\n")


# ============================================
# CONFIGURAR CRITERIOS DE BÚSQUEDA
# ============================================
def get_name(heroe):  # función que devuelve el nombre
    return heroe.get("name", "")

def get_alias(heroe):  # función que devuelve el alias
    return heroe.get("alias", "")

lista_superheroes.add_criterion("name", get_name)  # agrego criterio de búsqueda por nombre
lista_superheroes.add_criterion("alias", get_alias)  # agrego criterio de búsqueda por alias


# ============================================
# PUNTO A - ELIMINAR LINTERNA VERDE
# ============================================
print("=" * 60)
print("PUNTO A: Eliminar Linterna Verde")
print("=" * 60)

heroe_eliminado = lista_superheroes.delete_value("Green Lantern", "alias")  # elimino por alias

if heroe_eliminado:  # si se eliminó algo
    print(f"✓ Eliminado: {heroe_eliminado['name']}")  # muestro el nombre del eliminado
else:  # si no se encontró
    print("✗ No se encontró Linterna Verde")

print(f"Nodos restantes: {len(lista_superheroes)}\n")


# ============================================
# PUNTO B - AÑO DE APARICIÓN DE WOLVERINE
# ============================================
print("=" * 60)
print("PUNTO B: Año de aparición de Wolverine")
print("=" * 60)

wolverine = lista_superheroes.buscar_por_nombre("Wolverine")  # busco a Wolverine por nombre

if wolverine:  # si lo encontré
    print(f"Wolverine apareció en: {wolverine['first_appearance']}\n")
else:  # si no lo encontré
    print("✗ No se encontró Wolverine\n")


# ============================================
# PUNTO C - CAMBIAR CASA DE DR. STRANGE
# ============================================
print("=" * 60)
print("PUNTO C: Cambiar casa de Doctor Strange a Marvel")
print("=" * 60)

dr_strange = lista_superheroes.buscar_por_nombre("Doctor Strange")  # busco a Doctor Strange

if dr_strange:  # si lo encontré
    casa_anterior = dr_strange["comic_house"]  # guardo la casa anterior
    dr_strange["comic_house"] = "Marvel"  # cambio la casa a Marvel
    print(f"✓ Doctor Strange cambió de {casa_anterior} a {dr_strange['comic_house']}\n")
else:  # si no lo encontré
    print("✗ No se encontró Doctor Strange\n")


# ============================================
# PUNTO D - SUPERHÉROES CON TRAJE O ARMADURA
# ============================================
print("=" * 60)
print("PUNTO D: Superhéroes con 'traje' o 'armadura' en biografía")
print("=" * 60)

def tiene_traje_o_armadura(heroe):  # función que verifica si tiene las palabras clave
    biografia = heroe.get("short_bio", "").lower()  # obtengo la biografía en minúsculas
    palabras_clave = ["traje", "armadura", "suit", "armor", "armour"]  # palabras a buscar
    return any(palabra in biografia for palabra in palabras_clave)  # verifico si alguna está

lista_superheroes.mostrar_por_condicion(tiene_traje_o_armadura)  # muestro los que cumplen
print()


# ============================================
# PUNTO E - SUPERHÉROES ANTERIORES A 1963
# ============================================
print("=" * 60)
print("PUNTO E: Superhéroes con aparición anterior a 1963")
print("=" * 60)

def anterior_a_1963(heroe):  # función que verifica si apareció antes de 1963
    return heroe.get("first_appearance", 9999) < 1963  # comparo el año

def mostrar_nombre_y_casa(heroe):  # función para mostrar nombre y casa
    print(f"- {heroe['name']} ({heroe['comic_house']}) - {heroe['first_appearance']}")

lista_superheroes.mostrar_por_condicion(anterior_a_1963, mostrar_nombre_y_casa)  # muestro
print()


# ============================================
# PUNTO F - CASA DE CAPITANA MARVEL Y MUJER MARAVILLA
# ============================================
print("=" * 60)
print("PUNTO F: Casa de Capitana Marvel y Mujer Maravilla")
print("=" * 60)

capitana_marvel = lista_superheroes.buscar_por_nombre("Captain Marvel")  # busco a Capitana Marvel
mujer_maravilla = lista_superheroes.buscar_por_nombre("Wonder Woman")  # busco a Mujer Maravilla

if capitana_marvel:  # si encontré a Capitana Marvel
    print(f"Captain Marvel: {capitana_marvel['comic_house']}")

if mujer_maravilla:  # si encontré a Mujer Maravilla
    print(f"Wonder Woman: {mujer_maravilla['comic_house']}")

print()


# ============================================
# PUNTO G - INFORMACIÓN COMPLETA DE FLASH Y STAR-LORD
# ============================================
print("=" * 60)
print("PUNTO G: Información completa de Flash y Star-Lord")
print("=" * 60)

flash = lista_superheroes.buscar_por_nombre("The Flash")  # busco a Flash
star_lord = lista_superheroes.buscar_por_nombre("Star-Lord")  # busco a Star-Lord

if flash:  # si encontré a Flash
    print("\nTHE FLASH:")
    for key, value in flash.items():  # recorro cada clave-valor del diccionario
        print(f"  {key}: {value}")  # muestro la información
else:  # si no lo encontré
    print("\n✗ The Flash: No encontrado")

if star_lord:  # si encontré a Star-Lord
    print("\nSTAR-LORD:")
    for key, value in star_lord.items():  # recorro cada clave-valor del diccionario
        print(f"  {key}: {value}")  # muestro la información
else:  # si no lo encontré
    print("\n✗ Star-Lord: No encontrado")

print()


# ============================================
# PUNTO H - SUPERHÉROES QUE COMIENZAN CON B, M Y S
# ============================================
print("=" * 60)
print("PUNTO H: Superhéroes que comienzan con B, M y S")
print("=" * 60)

letras_buscar = ["B", "M", "S"]  # letras a buscar

for letra in letras_buscar:  # recorro cada letra
    print(f"\n Letra {letra}:")
    
    def comienza_con_letra(heroe):  # función que verifica si comienza con la letra
        return heroe.get("name", "").startswith(letra)  # verifico el inicio del nombre
    
    lista_superheroes.mostrar_por_condicion(comienza_con_letra)  # muestro los que cumplen

print()


# ============================================
# PUNTO I - CANTIDAD POR CASA DE COMIC
# ============================================
print("=" * 60)
print("PUNTO I: Cantidad de superhéroes por casa de comic")
print("=" * 60)

conteo_casas = lista_superheroes.contar_por_casa()  # cuento superhéroes por casa

for casa, cantidad in sorted(conteo_casas.items()):  # recorro cada casa ordenada
    print(f"{casa}: {cantidad} superhéroes")  # muestro la casa y cantidad

print(f"\n✓ Total en lista enlazada: {len(lista_superheroes)} nodos")
print("=" * 60)