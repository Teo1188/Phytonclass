###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")


print("\n Sentencia simple condicional")

edad = 16
if edad >= 18:
    print("Eres mayor de edad!")#se debe usar una tabulacion especial para separar en phyton
    print("Felicidades!")

print("\n Sentencia condicional con else")
edad = 16
if edad >= 18: 
    print("Eres mayor de edad") #se debe usar una tabulacion especial para separar en phyton
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 2

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("Aprobado")
else:
    print("No esta calificado")


print("\n Condiciones Multiples")

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript: 
# && sería and
# || sería or

edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet: #and revisa que todos los operadores se cumplan, sino entonces no se cumple
    print("Puedes conducir!")
else:
    print("POLICIAAAA")

# Ejemplo especial
if edad >= 18 or tiene_carnet: #or es si una de las dos se cumplen entonces funciona
    print("Puedes conducir")
else:
    print("Paga al policia y te dejara conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Toca buscar empleo")