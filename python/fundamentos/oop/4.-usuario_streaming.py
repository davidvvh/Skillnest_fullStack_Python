#codigo base
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        pass


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        pass


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        pass


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass

miyagi = UsuarioStreaming("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = UsuarioStreaming("Daniel", "Larusso", "daniel@codingdojo.la")




continuar = True
while continuar:
    print("\n---ejercicios python---")
    print("---1.- ejercicio 1---")
    print("---2.- ejercicio 2---")
    print("---3.- ejercicio 3---")
    print("---4.- ejercicio 4---")
    print("---5.- ejercicio 5---")
    print("---6.- ejercicio 6---")
    print("---7.- ejercicio 7---")
    print("---8.- ejercicio 8---")
    print("---9.- ejercicio 9---")
    print("---10.- ejercicio 10---")
    opcion = input("\n---- elige una opcion: (1-15) (0 para salir) =")
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
        ()
    elif opcion == "6":
        print("\nejecutando ejercicio 6: ")
        ()
    elif opcion == "7":
        print("\nejecutando ejercicio 7: ")
        ()
    elif opcion == "8":
        print("\nejecutando ejercicio 8: ")
        ()
    elif opcion == "9":
        print("\nejecutando ejercicio 9: ")
        ()
    elif opcion == "10":
        print("\nejecutando ejercicio 10: ")
        ()
    elif opcion == "0":
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")
#todos los valores que deban registrar debe ser con input
#añadir un menu while para llamar a los metodos
#(menu de seleccion)