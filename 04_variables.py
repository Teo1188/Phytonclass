##
#04 - Variables
#Las variables sirven para guardar datos en memoria.
#Python es un lenguaje de tipado dinámico y tipado fuerte.
###

#Asignar una variable
#solo hace falta poner esto
# my_name = "Teo"
# print(my_name)

# age = 32
# print(age)

# age = 37
# print(age)

# Tipado dinámico: el tipo de dato se determine en tiempo de ejecucion
# que no tienes que declararlo explicitamente

# name = "theodev"
# print(type(name))

# name = 32
# print(type(name))

#tipado fuerte: Python no realiza conversiones de tipo automaticas
# print(10 + "2")

##f-string (literal de cadena de formato)
#desde la version 3.6
# print(f"Hola me llamo {my_name}, tengo {age} años")

# #No recomenndada forma de asignar variables
# name, age, city = "theo", 32, "Medellin"

# #convenciones de nombres de variables
# mi_nombre_de_variable = "ok" #snake_case
# nombre = "ok"

# MiNombreDeVariable = "ko" #PascalCase
# minombredevariable = "ko" #todojunto

# mi_nombre_de_variable_123 = "ok"

# MI_CONSTANTE = 3.14 #UPPER_CASE ---> constantes

## nombres no validos de variables
#1231231231_variable = "ko" # mp se permite iniciar variables con numeros
#mi-variable = "ko"
#mi variable = "ko"
# True = False

is_usaer_logged_in: bool = True
print(is_usaer_logged_in)

is_usaer_logged_in = 42
print(is_usaer_logged_in)