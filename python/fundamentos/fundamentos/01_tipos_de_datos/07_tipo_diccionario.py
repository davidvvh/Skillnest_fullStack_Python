#diccionario de python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal

#imprimir el nombre del estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente


#diccionario de paises
paises = {} #Diccionario vacío
paises["MEX"] = "Mexico" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Peru"
paises["ARG"] = "Argentina"

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"

#eliminar valores de diccionario
print(paises)
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print(f"valor removido: {valor_removido}")
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

#diccionario pintor
pintor = { 
    "nombre": "Frida Kahlo", 
    "pais": "México", 
    "fecha_nacimiento": "6 de julio de 1907"
    }

#diccionarios aninados
escuela = {
    "nombre": "Coding Dojo LATAM",
    "profesores": [
        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}