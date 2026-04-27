#creacion de la clase usuario - entidad
class Usuario:
    def __init__(self): #constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#instancias de una clase
miyagi = Usuario()
daniel = Usuario()
david = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Miyagi
print(miyagi.email) #Imprime miyagi@codingdojo.la
print(miyagi.limite_credito) #Imprime 30000
print(miyagi.saldo_pagar) #Imprime 0


#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido) #Imprime: Miyagi
print(daniel.email) #Imprime miyagi@codingdojo.la
print(daniel.limite_credito) #Imprime 30000
print(daniel.saldo_pagar) #Imprime 0

#valores a nueva instancia
david.nombre = "david"
david.apellido = "tobar"
david.email = "david@gmail"
david.limite_credito = 2000
david.saldo_pagar = 300000

print(david.nombre) #Imprime: Daniel
print(david.apellido) #Imprime: Miyagi
print(david.email) #Imprime miyagi@codingdojo.la
print(david.limite_credito) #Imprime 30000
print(david.saldo_pagar) #Imprime 0

#imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(david.nombre)
