import os 
def limpiarConsola():
    os.system()
#Crear una función que reciba una lista de números enteros y genere una nueva lista solo con los números
#pares mayores a 10.
#Luego debe mostrar la nueva lista y la cantidad de elementos encontrados.
#!!!Alexiel Retamales!!!
def listaNumeros(lista):
    nueva_lista = []
    for numero in lista:
        if numero % 2 == 0 and numero >= 10:
            nueva_lista.append(numero)
    print(f"La nueva lista es: {nueva_lista}")
    print(f"La cantidad de elementos encontrados es: {len(nueva_lista)}")

#Crear una función que reciba una lista de nombres y una letra.
#Debe mostrar todos los nombres que comiencen con esa letra y contar cuántos cumplen la condición.


#Crear una función que reciba una lista de notas (decimales) y genere dos listas: una con aprobados (≥ 4.0) y otra con reprobados (< 4.0).
#Debe mostrar ambas listas y la cantidad de estudiantes en cada grupo.
#Mauricio Rivera


#Crear una función que reciba una lista de números y determine cuál es el número que más se repite.
#Debe mostrar el número y la cantidad de veces que aparece.

# Ignacio diaz
def lista(listado):
    conteo = {}
    for num in listado:
        conteo[num] = conteo.get(num, 0) + 1  
    mas_repetido = max(conteo, key=conteo.get)
    repeticiones = conteo[mas_repetido]
    print(f"El número que más se repite es {mas_repetido} y aparece {repeticiones} veces.")
    return mas_repetido, repeticiones




#Crear una función que reciba una lista de palabras y genere una nueva lista solo con aquellas que tengan más de 4 letras y contengan la letra “a”.
#Debe mostrar la lista resultante.



#Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
#Debe mostrar la cantidad de personas en cada grupo.



#Crear una función que reciba una lista de números y determine si todos los números son positivos.
#Si encuentra al menos un número negativo, debe indicarlo y detener el recorrido.
#Mauricio Rivera


#Crear una función que reciba una lista de productos (diccionarios con nombre y precio).
#Debe mostrar los productos cuyo precio esté entre 1000 y 5000, y calcular el promedio de esos precios.



#Crear una función que reciba una lista de palabras y un número entero.
#Debe mostrar solo las palabras cuya longitud sea mayor al número ingresado.
#david tobar
def filtrar(lista, cantidad):
    result = [palabra for palabra in lista if len(palabra) > cantidad]
    return result

def mostrar():
    palabras = []
    cantidad = int(input("ingrese el numero de longitud: "))
    for i in range(cantidad):
        palabra = input("ingresa una palabra: ")
        print(f"{palabra} agregada exitosamente a la lista")
        palabras.append(palabra)
    listaPalabras = filtrar(palabras, cantidad)
    if listaPalabras:
        print(f"las palabras con una longitud mayor a {cantidad} son: \n- {("\n").join(listaPalabras)}")
    else:
        print(f"no se ingresaron palabras con longitud por encima de {cantidad}")

#Crear una función que reciba una lista de números y genere una nueva lista sin elementos repetidos.
#Luego debe mostrar la lista original y la lista resultante.




#Menu while

def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. reciba una lista de números enteros y genere una nueva lista solo con los números pares mayores a 10.")
        print("2.función que reciba una lista de números y determine cuál es el número que más se repite")
        print("3. función que reciba una lista de palabras con una longitud impuesta por un numero entero")
        print("0.Salír")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            print("\nEjecutando el primer ejercici")
            listaNumeros([4, 12, 15, 22, 9])
            print()
        elif opcion == "2":
            lista([1,2,3,4,5,5])
        elif opcion == "3":
            print("\nEjecutando ejercicio 3")
            print()
            mostrar()
        elif opcion == "0":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()