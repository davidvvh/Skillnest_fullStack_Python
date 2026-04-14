#Guía de Ejercicios: Lógica Fundamental
#I. Interacción y Condicionales (Básico)

#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
#El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuántos números pares deseas ver?: "))
    pares = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares.append
    print(f"mostrando pares: {pares}")

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
# Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificador_edad():
    campo = input("ingrese su año de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif int(campo) >= 18:
        print(f"tienes acceso ya que tu edad es: {edad}")
    elif edad > 0 and edad < 18:
        print("no tienes acceso: te faltan {18 - edad} años.")
    else:
        print("ingrese valores validos")
verificador_edad()

#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, 
# aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuento():
    precio = float(input("ingresa el precio del producto: "))
    cantidad = int(input("ingresar cantidad: "))
    producto = precio * cantidad
    if producto > 100:
        descuento = producto * 0.15
    else:
        descuento = 0
    total = producto - descuento
    print(f"el subtotal es: {producto} el descuento aplicado es: {descuento} y el Total es: {total}")

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, 
#Negativo-Par, Negativo-Impar o Cero.
def  clasificadorNum():
    num = int(input("Ingresa un número: "))
    if num > 0:
        if num % 2 ==0:
            print("positivo-par")
        elif num % 2 ==1:
            print("positivo-impar")
    elif num <0:
        if num % 2 == 0:
            print("negativo-par")
        elif num % 2 == 1:
            print("negativo-impar")
    else:
        print("es 0")


#II. Iteraciones y Bucles (Intermedio)

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
#pero solo muestra los resultados que sean múltiplos de 3.
def tablaMultiplicar():
    num = int(input("Ingresar número a trabajar: "))
    for i in range(1, 13):
        resultado = num * i
        if resultado % 3 == 0:
            print(f"del {num} numeros son divisibles por 3: {resultado} ")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar 
# cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
def sumatoriaCentinela():
    suma_total = 0
    while True:
        n = int(input("Ingresa un número (negativo para salir): "))
        if n < 0:
            break
        suma_total += n
    print(f"La suma total es: {suma_total}")

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la 
# cadena y contar cuántas vocales tiene en total.
def contadorVocales():
    texto = input("Ingrese una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
    print(f"La cadena '{texto}' tiene {vocales} vocales en total") 

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
# Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
def validacion():
    con = 12345678
    intentos = 1
    while True:
        ingresa = int(input("ingresa la contraseña:"))
        if ingresa == con:
            print("acceso concedido")
            break
        else:
            intentos += 1
            if intentos > 3:
                print("acceso denegado")
                break
            else:
                print(f"numeros de intentos: {intentos}")


#III. Manejo de Arreglos / Listas (Avanzado)

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, 
# al final, imprímelos en orden inverso al que fueron ingresados.
def nombre():
    nombres = []
    maxi = 0

    while maxi < 5:
        inp = input("Por favor ingresar nombre")
        if inp != "":
            nombres.append(inp)
        else:
            print("Tienes que ingresar un nombre")
        maxi += 1
    for i in range(4, -1, -1):
        print(nombres[i])

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
# Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
def promedioNotas():
    cantidad =int(input("¿Cuantas notas desea ingresar?"))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    print(f"Nota mas alta: {max(notas)}")
    print(f"Nota mas baja: {min(notas)}")

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
# solo los números que sean mayores a 50. Muestra ambos arreglos.
# Suponiendo que el usuario ingresa números separados por espacio
def filtroArreglos():
    cantidad = int(input("¿Cuantos numeros desea ingresar?: "))
    mayor50 = []
    nUser = []
    for i in range(1, cantidad + 1):
        arrayUsuario = int(input("Ingrese un numero: "))
        if arrayUsuario > 50:
            mayor50.append(arrayUsuario)
        else:
            nUser.append(arrayUsuario)
        print(f"Valor ingresado por el usuario: {nUser} \nValor mayor a 50: {mayor50}")

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y 
# el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
def buscadorElementos():
    ciudades = ["Tokio", "Seul", "NewYork", "Moscu", "Madril", "Paris", "Ottawa", "Lisboa"]
    ciudad = input("Ingresar ciudad (con mayuscula al inicio): ")
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
        print(f"Tu ciudad está en el arreglo, en la posicion {esta}")
    else:
        print("Tu ciudad no está en el arreglo")


#IV. Retos de Lógica Combinada

#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 
# 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
def inventario():
    nombre_productos = []
    precios = []

    for i in range(3):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        nombre_productos.append(nombre)
        precios.append(precio)
    print("\nInventario: ")
    for i in range(3):
        print(f"Producto: {nombre_productos[i]} - precio {precio[i]}")


#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso 
# termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
def listaCompras():
    lista = []
    while True:
        item = input("Artículo (o 'terminar')")
        if item.lower() == "terminar":
            break
        lista.append(item)
    print(f"Ordenado: {sorted(lista)}")

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
# El promedio semanal.
# Cuántos días la temperatura fue superior a 25 grados.
# El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
def analisisTemperatura():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    diasSuperior = []
    total = 0
    baja = 100
    diaBaja = ""
    cant = 0

    while cant < 7:
        temps = float(input(f"ingrese temperatura del dia {dias(cant)}"))
        total += temps

        if temps < baja and temps < 25:
            baja = temps
            diaBaja = dias[cant]
        elif temps > 25:
            diasSuperior.append(dias[cant])

        cant += 1

    print(f"el promedio de las temperaturas fue de {total / 7}")
    print(f"el dia con la temperatura mas baja fue el dia {diaBaja} con {baja}")
    print(f"los dias mas calurosos fueron {diasSuperior}")



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
    print("---11.- ejercicio 11---")
    print("---12.- ejercicio 12---")
    print("---13.- ejercicio 13---")
    print("---14.- ejercicio 14---")
    print("---15.- ejercicio 15---")
    opcion = input("\n---- elige una opcion: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nejecutando ejercicio 1: ")
        numerosDinamicos()
    elif opcion == "2":
        print("\nejecutando ejercicio 2: ")
        verificador_edad()
    elif opcion == "3":
        print("\nejecutando ejercicio 3: ")
        aplicarDescuento()
    elif opcion == "4":
        print("\nejecutando ejercicio 4: ")
        clasificadorNum()
    elif opcion == "5":
        print("\nejecutando ejercicio 5: ")
        tablaMultiplicar()
    elif opcion == "6":
        print("\nejecutando ejercicio 6: ")
        sumatoriaCentinela()
    elif opcion == "7":
        print("\nejecutando ejercicio 7: ")
        contadorVocales()
    elif opcion == "8":
        print("\nejecutando ejercicio 8: ")
        validacion()
    elif opcion == "9":
        print("\nejecutando ejercicio 9: ")
        nombre()
    elif opcion == "10":
        print("\nejecutando ejercicio 10: ")
        promedioNotas()
    elif opcion == "11":
        print("\nejecutando ejercicio 11: ")
        filtroArreglos()
    elif opcion == "12":
        print("\nejecutando ejercicio 12: ")
        buscadorElementos()
    elif opcion == "13":
        print("\nejecutando ejercicio 13: ")
        inventario()
    elif opcion == "14":
        print("\nejecutando ejercicio 14: ")
        listaCompras()
    elif opcion == "15":
        print("\nejecutando ejercicio 15: ")
        analisisTemperatura()
    elif opcion == "0":
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")