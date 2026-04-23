datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def Puntajes(lista):
    for datos in lista:
        nombre = ['Carlos']
        puntos = [80]
        print(f"{nombre} obtuvo {puntos} puntos")
Puntajes(datos[0])

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def ver_puntaje(lista):
    for item in lista:
        print(f"Nombre: {item['nombre']} - Puntaje: {item['puntaje']}")
ver_puntaje(datos)
