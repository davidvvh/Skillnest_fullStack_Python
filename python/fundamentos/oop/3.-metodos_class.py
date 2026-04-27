class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def aumentarCredito(self, aumento):
        self.limite_credito += aumento

    def cambiarCorreo(self, email):
        self.email = email

#instancia de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

print("-------------compras de miyagi-------------")
miyagi.hacer_compra(2000)
print(f"primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"segunda compra de {miyagi.nombre}: {segundacompra}")
#imprimir cuanto credito le queda a miyagi
print(f"credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")

#compras de daniel 2 y muestra saldo a pagar
print("-------------compras de daniel-------------")
daniel.hacer_compra(45)
print(daniel.saldo_pagar) #Imprime: 45

#tarea
print("-------------task-------------")
'''
1.-crear un nuevo metodo que permita aumentar el limite de credito
imprimir el nuevo limite de credito

2.- crear un nuevo metodo que permita cambiar el correo de la instancia
mostrar el nuevo correo
'''
miyagi.aumentarCredito(2000)
print(f"el nuevo limite de credito es: {miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagi@gmail.com")
print(f"el nuevo email es: {miyagi.email}")