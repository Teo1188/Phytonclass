###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

import os
os.system("clear")

# Creación de listas
print("\n Crear listas")
lista1 = [1, 2, 3, 4, 5] #lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] #lista de cadenas de texto
lista3 = [1, "hola", 3.14, True] #lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ["calcetin", 4]] #lista de listas
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\n Acceso a elementos por índice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas

lista1 = [1, 2, 3, 4, 5]

print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5] crea una copia

# Hay mas magia
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2])#print(lista1[desde:hasta:paso]) indices inpares salta de 2 en 2 [1, 3, 5, 7]
print(lista1[::-1]) # devuelve los indices invertidos

# Modificar una lista
lista1[0] = 20
print(lista1) #[20, 2, 3, 4, 5, 6, 7, 8]

# Añadir elementos a una lista

lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1) #[1, 2, 3, 4, 5, 6]

# forma corta y más eficiente

lista1 += [7, 8, 9]
print(lista1)


###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("\nEjercicio 1:")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print(secreto)



# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
#numeros[0] = 50 yo lo hice asi
#numeros[4] = 10 yo lo hice asi
numeros[0], numeros[-1] = numeros[-1], numeros[0] #puede hacerse asi.
print(numeros)


# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3:")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4:")

lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\nEjercicio 5:")
#mi solucion
#lista = [10, 20, 30, 40, 50]
#centro = lista[2:3]
#print(centro)

#la solucion de midu wtf:
print("\nEjercicio 5:")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\nEjercicio 6:")

lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
resultado = lista[:mitad][::-1] + lista[mitad:]
print(resultado)
