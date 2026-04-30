#Requisitos obligatorios

#Su trabajo debe cumplir con lo siguiente:
#Uso de funciones con parámetros
#Uso de menú con ciclo while
#Uso de input() para solicitar datos
#Uso de listas (arreglos)
#Uso de diccionarios
#Uso de ciclos for
#Uso de estructuras condicionales (if, elif, else)
#Código ordenado, comentado y correctamente indentado
#Opción de salida del programa (0. Salir)



'''
Ejercicios a desarrollar
Su programa deberá considerar las siguientes funciones:
1.-Crear una función que reciba una lista de números 
enteros y muestre cuál es el número mayor y cuál es el menor.

2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.

3.-Crear una función que reciba una lista de nombres y muestre 
únicamente aquellos que tengan más de 5 letras.

4.-Crear una función que reciba una lista de notas (números decimales), 
calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).

5.-Crear una función que reciba una lista de precios de productos y 
aplique un descuento del 10%, mostrando el valor original y el nuevo valor.

6.-Crear una función que reciba un número entero y determine si es par o impar.

7.-Crear una función que reciba una lista de edades y muestre 
cuántas personas son mayores de edad (18 años o más).

8.-Crear una función que reciba una lista de palabras y permita 
buscar cuántas veces aparece una palabra específica ingresada por el usuario.

9.-Crear una función que reciba una lista de números y genere una 
nueva lista que contenga únicamente los números positivos.

10.-Crear una función que reciba una lista de productos 
(utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
'''

#ejercicio 1
def listaRecibida(listado):
    listaNum = listado
    menor = min(listaNum)
    mayor = max(listaNum)
    print(f"el numero mayor es {mayor}\nEl numero menor es {menor}")

def numerosLista():
    limit = int(input("ingresa el limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input(f"ingresa un numero entero {i} de {limit} :"))
        listadoNum.append(num)
        i+=1
    listaRecibida(listadoNum)


#ejercicio 2
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"la cadena contiene {contador} vocales.")

def textoVocales():
    texto = input("ingrese una cadena de texto: ")
    contar_vocales(texto)


#ejercicio 3
def nombreListado(listado):
    listalet = listado
    menos = min(listalet)
    mas = max(listalet)
    print(f"el numero mayor es {mas}\nEl numero menor es {menos}")

def C():
    nombres = []
    maxi = 0
    while maxi < 5:
        inp = input("porfavor ingresa un nombre: ")
        if inp !="":
            nombres.append(inp)
        else:
            print("tienes que ingresar un nombre")
            


#ejercicio 4
def C():
    return

def C():
    return


#ejercicio 5
def C():
    return

def C():
    return


#ejercicio 6
def C():
    return

def C():
    return


#ejercicio 7
def C():
    return

def C():
    return


#ejercicio 8
def C():
    return

def C():
    return


#ejercicio 9
def C():
    return

def C():
    return


#ejercicio 10
def C():
    return

def C():
    return



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
        print("\n-------------mayor y menor-------------")
        numerosLista()
    elif opcion == "2":
        print("\n-------------vocales-------------")
        textoVocales()
    elif opcion == "3":
        print("\n-------------mas de 5 letras-------------")
        ()
    elif opcion == "4":
        print("\n-------------notas-------------")
        ()
    elif opcion == "5":
        print("\n-------------descuento 10%-------------")
        ()
    elif opcion == "6":
        print("\n-------------par o impar-------------")
        ()
    elif opcion == "7":
        print("\n-------------calcular edad-------------")
        ()
    elif opcion == "8":
        print("\n-------------buscar palabras-------------")
        ()
    elif opcion == "9":
        print("\n-------------lista de números y nueva lista-------------")
        ()
    elif opcion == "10":
        print("\n-------------lista de productos-------------")
        ()
    elif opcion == "0":
        print("saliendo...")
        continuar = False
    else:
        print("opcion no valida, intenta otra vez")