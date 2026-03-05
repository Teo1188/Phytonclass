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



