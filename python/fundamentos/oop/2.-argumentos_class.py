#Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al 
# método __init__ y que de esta manera 
# podamos asignarle a los atributos los valores correspondientes.
class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
#creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
david = Usuario("david", "tobar", "david@gmail.com", 2000, 300000)

#imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


#tarea
'''
crear una clase estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
'''
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

kitty = Estudiante("20.135.692-8", "jester", "kitty", "contabilidad", "09/06/2008")
pocki = Estudiante("19.073.107-0", "shadow", "pocki", "programacion", "15/11/2006")
flor = Estudiante("17.390.069-1", "florecilla", "flor", "logistica", "08/06/2009")
print(f"Me llamo {kitty.nombre}, me apellido {kitty.apellido}, y soy de {kitty.especialidad}")
print(f"me llamo {pocki.nombre}, me apellido {pocki.apellido}, y soy de {pocki.especialidad}")
print(f"me llamo {flor.nombre}, me apellido {flor.apellido}, y soy de {flor.especialidad}")