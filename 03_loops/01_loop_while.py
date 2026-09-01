print("\n Bucle While")

#Bucle con una simple condición.

contador = 0
while contador <=5:
    print(contador)
    contador += 1 #Esto es importante para evitar un bucle infinito

#Utilizando la palabra brake, para romper el bucle.

print("\n Bucle While con break")

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break #sale del bucle

# continue,  que lo que hace es saltar esa iteracion en concreto
# y continuar con el bucle
print("\n Bucle while con continue")

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


# else, esta condicion cuando se ejecuta?
print("\n Bucle while con else")

contador = 0

while contador < 5:
    print(contador)
    contador += 1
else: # y si no...
    print("El bucle ha terminado")



# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
# uso de try y except para manejo de errores

# numero = -1
# while numero < 0:
#     try:
#         numero = int(input("Escribe un número positivo: "))
#         if numero < 0:
#             print("El número debe ser positivo. Intenta otra vez!")
#     except:
#         print("Lo que introduces debe ser un número, que si no se cae el programa")

# print(f"El número que has introducido es {numero}")



###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
numero = 10
while numero >= 1:
  print(numero)
  numero -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 1
suma_pares = 0
while numero <= 20:
  if numero % 2 == 0:
    suma_pares += numero
  numero += 1

print(f"La suma de los números pares hasta 20 es: {suma_pares}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1

while contador <= numero:
  factorial *= contador
  contador += 1

print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contrasena = ""
while len(contrasena) < 8:
  contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
  if len(contrasena) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Introduce un número: "))
multiplicador = 1

while multiplicador <= 10:
  resultado = numero * multiplicador
  print(f"{numero} x {multiplicador} = {resultado}")
  multiplicador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1