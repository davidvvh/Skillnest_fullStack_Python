#codigo base
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f"titulo '{titulo}' agregado correctamente")


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f"el usuario {self.nombre} esta viendo '{titulo}'")
        else:
            print(f"titulo no encontrado {titulo}")


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        susAntigua = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"suscripcion cambio de {susAntigua} a {nueva_suscripcion}")


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"nombre: {self.nombre}")
        print(f"email: {self.email}")
        print(f"suscripcion: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print("la lista de reproduccion esta vacia")
        else:
            print(f"lista de reproduccion: \n- {"\n- ".join(self.lista_reproduccion)}")

shadow = UsuarioStreaming("shadow", "shadow@gmail.com")
shadow.agregar_a_lista("la mascara")
shadow.cambiar_suscripcion("premium")
shadow.ver_contenido("the mask")
shadow.mostrar_info_usuario()

kitty = UsuarioStreaming("kitty", "kitty@gmail.com")
kitty.agregar_a_lista("doki doki")
kitty.cambiar_suscripcion("estandar")
kitty.ver_contenido("Gliter Force")
kitty.mostrar_info_usuario()




continuar = True
while continuar:
    print("\n---ejercicios python---")
    print("---1.- ejercicio 1---")
    print("---2.- ejercicio 2---")
    print("---3.- ejercicio 3---")
    print("---4.- ejercicio 4---")
    print("---5.- ejercicio 5---")
    opcion = input("\n---- elige una opcion: (1-5) (0 para salir) =")
    if opcion == "1":
        print("\nejecutando ejercicio 1: ")
        ()
    elif opcion == "2":
        print("\nejecutando ejercicio 2: ")
        ()
    elif opcion == "3":
        print("\nejecutando ejercicio 3: ")
        ()
    elif opcion == "4":
        print("\nejecutando ejercicio 4: ")
        ()
    elif opcion == "5":
        print("\nejecutando ejercicio 5: ")
    elif opcion == "0":
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")
#todos los valores que deban registrar debe ser con input
#añadir un menu while para llamar a los metodos
#(menu de seleccion)