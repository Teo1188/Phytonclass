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

print("\n Anidar Condiciones")

edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")


# Más fácil
# if edad < 18:
#     print("No puedes entrar a la disco")
# elif tiene_dinero:
#     print("Puedes ir a la discoteca")
# else:
#     print("Quédate en casa")

numero = 5
if numero:  #True
    print("El número no es cero")

numero = 0
if numero:  #False
    print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
    print("El nombre no es vacio")

numero = 3 #asignacion
es_el_tres = numero = 3 #Comparación

if es_el_tres:
    print("El numero es 3")


print("\n Condición ternaria")

# es una forma concisa de un if-else en una linea de código
#[código si cumple la condición] if [condición] else [código si no cumple]

edad = 18
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# numero1 = input("digita el primer número")

# numero2 = input("digita el segundo número")

# if numero1 > numero2:
#     print(f"{numero1} es mayor que {numero2}")
# elif numero2 > numero1:
#     print(f"{numero2} es mayor que {numero1}")
# else:
#     print("Los números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numero1 = int(input("digita el primer número: "))
numero2 = int(input("digita el segundo número: "))
operacion = input("digita una operacion (+ - * /): ")

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
            resultado = numero1 / numero2
else:
        print("Operación no válida.")

if 'resultado' in locals(): #comprueba si la variable resultado existe.
    print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# anio = int(input("introduce un año: "))

# if (anio %4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto...")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# edad = int(input("Introduce una edad: "))

# if 0 <= edad <= 2:
#     print("Bebé")
# elif 3 <= edad <= 12:
#     print("Niñez")
# elif 13 <= edad <= 17:
#     print("Adolecente")
# elif 18 <= edad <= 64:
#     print("Adulto")
# elif edad >= 65:
#     print("Adulto Mayor")
# else:
#     print("Edad no válida.")


