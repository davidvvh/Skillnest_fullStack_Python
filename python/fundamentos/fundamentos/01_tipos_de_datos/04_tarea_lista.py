'''
actividad: gestor de inventario
'''

'''
1.- creacion: crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "raton", "monitor", "cable hdmi"
'''
inventario = ['laptop', 'raton', 'monitor', 'cable hdmi']

'''
2.- expansion: utiliza el metodo correspondiente para agregar "impresora"
y "teclado" al final de la lista'''
inventario.append("impresora")
inventario.append("teclado")
print(inventario)


'''3.- conteo: utiliza la funcion integrada para mostrar cuantos elementos
totales hay en la lista'''

print(len(inventario))

'''4.- acceso y modificacion: modifica "teclado" por "teclado mecanico" '''

inventario[5] = "teclado mecanico"

'''5.- slicing: crea una nueva lista llamada "promocion", debe contener
solo los 3 primeros elementos de la lista "inventario" '''

promocion = inventario
print(promocion[:4])

'''6.- mostrar la lista de inventario ordenado alfabeticamente'''

inventario.sort()
print(inventario)

'''7.- elimina el ultimo elemento de la lista inventario mostrando el elemento
eliminado y la lista final'''

inventario.pop()
print(inventario)