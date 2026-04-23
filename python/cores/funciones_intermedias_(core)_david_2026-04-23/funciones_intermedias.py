# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600
print(puntajes)

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"Nombre": "GameNinjaPro", "Seguidores": 250000},
    {"Nombre": "PixelWarrior", "Seguidores": 180000}
]

streamers[0]["Nombre"] = "EliteGamerX"
print(streamers[0]["Nombre"])


# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
print(eventos["Estados Unidos"][2])
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos["Estados Unidos"][2])


# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
print(ubicacion)

ubicacion[0]["latitud"] = 40.712776 
print(ubicacion)


#lista de streamers
def mostrar_streamers(lista):
    for item in lista:
        print(f"Personas: {item['Nombre']} - Seguidores: {item['Seguidores']}")
mostrar_streamers(streamers)


kick = {
    "nombre": ["EliteGamerX", "PixelWarrior"],
    "seguidores": ["250000", "180000"]
}

for separacion, orden in kick.items():
    print(separacion)
    for item in orden:
        print(item)


#diccionario
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

def mostrar_categorias(diccionario):
    for categoria, items in diccionario.items():
        print(f"{len(items)} {categoria.upper()}")
        for item in items:
            print(item)

mostrar_categorias(categorias)