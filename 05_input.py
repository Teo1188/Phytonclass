###
# 05 - Entrada de usuario (input()) - Version simplificada
# La funcion input() permite obtener datos del usuario a través de la consola.
###


nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Dentro de 20 años tendrás {age + 20}")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")