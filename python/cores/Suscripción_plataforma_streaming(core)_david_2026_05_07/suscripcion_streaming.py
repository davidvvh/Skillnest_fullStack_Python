class suscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estandar": 5.99, "Premium": 10.99}

#primera funcion: usuario y tipo_suscripcion
    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual
        print()

#segunda funcion: monto
    def realizar_pago(self, monto):
        self.saldo_pendiente = self.saldo_pendiente - monto
        print("Usuario:", self.usuario)
        print("Monto pagado:", monto)
        print("Saldo actual:", self.saldo_pendiente)

#tercera funcion: cambio de suscripcion
    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.saldo_pendiente + self.costo_mensual
        print("Cambio su tipo de plan a:", nuevo_tipo)
        print()

#cuarta funcion: ver contenido exclusivo
    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print("Acceso denegado")
        else:
            print("Acceso permitido para", self.usuario)
            print()

#ultima funcion: ver la info de la suscripcion
    def mostrar_info_suscripcion(self):
        print("Nombre:", self.usuario)
        print("Suscripcion:", self.tipo_suscripcion)
        print("Costo:", self.costo_mensual)
        print("Saldo:", self.saldo_pendiente)

print("------------------Usuario Juan------------------")
user1 = suscripcionStreaming("Juan", "Gratis")
user1.ver_contenido_exclusivo()
user1.cambiar_suscripcion("Estandar")
user1.realizar_pago(5.99)
user1.mostrar_info_suscripcion()

print("------------------Usuario Carlos------------------")
user2 = suscripcionStreaming("Carlos", "Estandar")
user2.ver_contenido_exclusivo()
user2.cambiar_suscripcion("Premium")
user2.realizar_pago(7.00)
user2.realizar_pago(10.00)
user2.mostrar_info_suscripcion()

print("------------------Usuario Patricio------------------")
user3 = suscripcionStreaming("Patricio", "Premium")
user3.realizar_pago(0)
user3.ver_contenido_exclusivo()
user3.mostrar_info_suscripcion()