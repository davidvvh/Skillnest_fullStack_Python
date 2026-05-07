#atributos; metodos de clase; metodos estaticos

#definicion de la clase
class estudiante:
    #atributo de la clase
    colegio = "liceo vate vicente huidobro"
    #lista en donde esten todos los estudiantes
    estudiantes = []

    #metodo constructor
    def __init__(self, nombre, nota):
        #atributos de instancia
        self.nombre = nombre
        self.nota = nota

        #agregar elementos a la lista estudiante (objeto)
        estudiante.estudiantes.append(self)

    #metodo de instancia
    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"nota: {self.nota}")

    #metodo de clase
    #usa "cls" porque trabaja con la informacion de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod #contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #metodo estatico
    #este no usa cls ni self, solo parametros
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
        
#creacion de objetos (instancia)
e1 = estudiante("donovan", 4.0)
e2 = estudiante("randy", 6.7)
e3 = estudiante("shado", 3.5)

#uso de metodos de instancia
print("== METODO DE INSTANCIA==")
#mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()
e3.mostrar_info()
print()


#usar atributo de clase
print("===ATRIBUTO DE CLASE===")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#uso de metodo de clase
print("===METODO DE CLASE===")
estudiante.cambiar_colegio("purkuyen")
e1.colegio = "VVH"
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)
print()

#contar estudiantes
print("===CONTAR ESTUDIANTES===")
print(f"total de estudiantes entre {estudiante.cantidad_estudiantes()}")

#metodo estatico
print("===METODO ESTATICO===")

print(f"¿{e1.nombre} aprueba?")
print(estudiante.aprobar(e1.nota))
print()

print(f"¿{e2.nombre} aprueba?")
print(estudiante.aprobar(e2.nota))
print()

print(f"¿{e3.nombre} aprueba?")
print(estudiante.aprobar(e3.nota))
print()


##funcion repaso
##crear una funcion que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print(f"acceso denegado")
        return False

def enviarDatos():
    username = input("ingrese su nombre usuario: ")
    password = input("ingrese su contraseña: ")
    validador(username, password)

enviarDatos()

