import os
#funciones basicas practica 2

#ejercicio1
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
    return result
def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


#ejercicio2
# Analiza publicaciones
def suma_y_resta(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma : {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"retorno / resta: {resta}")

# Imprime: 235 y retorna: 5


#ejercicio3
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"total = {total}, longitud = {longitud}")
    return resultado
def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"el resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21


#ejercicio4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * segEle)
        long = len(nuevaLista)
        print(long)
        return nuevaLista

# Imprime: 4 y retorna: [300, 9, 150, 60]
def ejercicio4():
    result1 = valores_multiplicados_segundo([100, 3, 50, 20])
    print(result1)
    print()
    result2 = valores_multiplicados_segundo([100])
    print(result2)
# Imprime: 1 y retorna: []


#ejercicio5
# Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range(0, b):
        multList.append(a*b)
    return multList

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"resultado 1: {result1}")
    #debe retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"resultado 2: {result2}")
    # Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
    os.system('cls')

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
        limpiar_consola()
        print("\nejecutando ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        limpiar_consola()
        print("\nejecutando ejercicio 2: ")
        ejercicio2()
    elif opcion == "3":
        limpiar_consola()
        print("\nejecutando ejercicio 3: ")
        ejercicio3()
    elif opcion == "4":
        limpiar_consola()
        print("\nejecutando ejercicio 4: ")
        ejercicio4()
    elif opcion == "5":
        limpiar_consola()
        print("\nejecutando ejercicio 5: ")
        ejercicio5()
    elif opcion == "0":
        limpiar_consola()
        print("saliendo...")
        continuar = False
    else:
        limpiar_consola()
        print("opcion no valida, intenta otra vez")