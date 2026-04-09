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
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad comprada: "))
subtotal = precio * cantidad

if subtotal > 100:
    descuento = subtotal * 0.15
else:
    descuento = 0

total = subtotal - descuento
print(f"Subtotal: ${subtotal:.2f} | Descuento: ${descuento:.2f} | Total: ${total:.2f}")

#4. Clasificador de Números
#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, 
#Negativo-Par, Negativo-Impar o Cero.
num = int(input("Ingresa un número: "))

if num == 0:
    print("Cero")
else:
    # Determinamos signo
    signo = "Positivo" if num > 0 else "Negativo"
    # Determinamos paridad
    paridad = "Par" if num % 2 == 0 else "Impar"
    print(f"{signo}-{paridad}")


#II. Iteraciones y Bucles (Intermedio)

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
#pero solo muestra los resultados que sean múltiplos de 3.
num = int(input("Ingresa un número para su tabla: "))
for i in range(1, 13):
    resultado = num * i
    if resultado % 3 == 0:
        print(f"{num} x {i} = {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar 
# cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
suma = 0
while True:
    n = int(input("Ingresa un número (negativo para salir): "))
    if n < 0:
        break
    suma += n
print(f"La suma total es: {suma}")

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la 
# cadena y contar cuántas vocales tiene en total.
frase = input("Ingresa una frase: ").lower()
vocales = "aeiouáéíóú"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1
print(f"Total de vocales: {contador}")

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
# Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
password_real = "python123"
intentos = 3

while intentos > 0:
    intento = input(f"Ingresa la contraseña ({intentos} intentos restantes): ")
    if intento == password_real:
        print("¡Acceso concedido!")
        break
    intentos -= 1
    if intentos == 0:
        print("Acceso bloqueado.")


#III. Manejo de Arreglos / Listas (Avanzado)

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, 
# al final, imprímelos en orden inverso al que fueron ingresados.
nombres = []
for i in range(5):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    nombres.append(nombre)

print("Nombres en orden inverso:")
for n in reversed(nombres):
    print(n)

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
# Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
cantidad = int(input("¿Cuántas notas vas a ingresar?: "))
notas = []

for i in range(cantidad):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
# solo los números que sean mayores a 50. Muestra ambos arreglos.
# Suponiendo que el usuario ingresa números separados por espacio
entrada = input("Ingresa números separados por espacio: ")
original = [int(x) for x in entrada.split()]
filtrados = [n for n in original if n > 50]

print(f"Original: {original}")
print(f"Mayores a 50: {filtrados}")

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y 
# el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
ciudades = ["Madrid", "Bogotá", "Santiago", "CDMX", "Lima", "Buenos Aires", "Quito", "Montevideo", "Asunción", "La Paz"]
busqueda = input("Ingresa la ciudad a buscar: ").title()

if busqueda in ciudades:
    indice = ciudades.index(busqueda)
    print(f"{busqueda} se encuentra en el índice {indice}.")
else:
    print("La ciudad no está en la lista.")


#IV. Retos de Lógica Combinada

#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 
# 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
nombres_productos = []
precios = []

for i in range(3):
    nombres_productos.append(input(f"Nombre del producto {i+1}: "))
    precios.append(float(input(f"Precio del producto {i+1}: ")))

print("\n--- Inventario ---")
for i in range(3):
    print(f"Producto: {nombres_productos[i]} - Precio: ${precios[i]:.2f}")

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso 
# termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
lista = []
while True:
    item = input("Agrega un artículo (o escribe 'terminar'): ").lower()
    if item == "terminar":
        break
    lista.append(item)

lista.sort()
print(f"Tu lista de compras: {lista}")

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
# El promedio semanal.
# Cuántos días la temperatura fue superior a 25 grados.
# El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temps = []

for dia in dias:
    t = float(input(f"Temperatura del {dia}: "))
    temps.append(t)

promedio = sum(temps) / 7
sobre_25 = len([t for t in temps if t > 25])
min_temp = min(temps)
dia_frio = dias[temps.index(min_temp)]

print(f"\nResultados:")
print(f"- Promedio semanal: {promedio:.1f}°C")
print(f"- Días con más de 25°C: {sobre_25}")
print(f"- El día más frío fue el {dia_frio} con {min_temp}°C")
