from collections import deque
from pprint import pprint

def personajes(nombre_real,superheroe,genero):
    return{
        "nombre_real": nombre_real,
        "superheroe": superheroe,
        "genero": genero
    }

cola_personajes = deque([
    {"nombre_real": "tony stark", "superheroe": "iron man", "genero": "M" },
    {"nombre_real": "steve rogers", "superheroe": "capitan america", "genero": "M" },
    {"nombre_real": "natasha romanoff", "superheroe": "black widow", "genero": "F"},
    {"nombre_real": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre_real": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre_real": "Paul Rudd", "superheroe": "Scott Lang","genero": "M"},
    {"nombre_real": "Bruce Banner", "superheroe": "Hulk", "genero": "M"},
    {"nombre_real": "Clint Barton", "superheroe": "Hawkeye", "genero": "M"},
    {"nombre_real": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"}
])


print("lista de todos los personajes")
pprint(cola_personajes)

print("\n")
print("ITEM A")

for personaje in cola_personajes:
    if personaje["superheroe"].lower() == "capitana marvel":
        print(f"el nombre real de capitana marvel es: {personaje["nombre_real"]}" )
        




print("\n")
print("ITEM B")
print("Los superheroes de genero femenino de la cola son:  ")
cola_item_2 = deque(cola_personajes.copy())
cola_pers_fem = deque()
while cola_item_2:
    personaje = cola_item_2.popleft()
    if personaje["genero"] == "F":
        cola_pers_fem.append(personaje["nombre_real"]+ " - " + personaje["superheroe"])

pprint(cola_pers_fem)


print("\n")
print("ITEM C")
print("Los superheroes de genero masculino de la cola son: ")

cola_item_3 = deque(cola_personajes.copy())
cola_pers_masc = deque()

while cola_item_3:
    personaje = cola_item_3.popleft()
    if personaje["genero"] == "M":
        cola_pers_masc.append(personaje["nombre_real"] + " - " + personaje["superheroe"])

pprint(cola_pers_masc)


print("\n")
print("ITEM D")

cola_item_4 = deque(cola_personajes.copy())

while cola_item_4:
    personaje = cola_item_4.popleft()
    if personaje["superheroe"].lower() == "scott lang":
        print("El nombre real de scott lang es : " + personaje["nombre_real"])

        
 
print("\n")
print("ITEM E")
print("Los personajes que comienzan con la letra S son: ")

cola_item_5 = deque(cola_personajes.copy())
letra_S = deque()
letra = "S"

while cola_item_5:
    personaje = cola_item_5.popleft()
    if personaje["superheroe"].lower().startswith(letra.lower()):
        letra_S.append(personaje)

pprint(letra_S)


print("\n")
print("ITEM F")

for personaje in cola_personajes:
    if personaje["nombre_real"].lower() == "carol danvers":
        print(f"Carol Danvers es un elemento de la cola y su nombre de superheroe es: {personaje["superheroe"]}" )