# ------------------------------------------------------------
# PYTHON 3 - Strings
# Ejemplo 4
# ------------------------------------------------------------

# isupper()devuelve True si todos los caracteres son mayúsculas
cadena = input("Ingrese una cadena:")
if cadena.isupper():
    print("Todos los caracteres son mayúsculas")
else:
    print("No todos los caracteres son mayúsculas")


#islower()devuelve True si todos los caracteres son minúsculas
cadena = input("Ingrese una cadena:")
if cadena.islower():
    print("Todos los caracteres son minúsculas")
else:
    print("No todos los caracteres son minúsculas") 

# upper() y lower() convierten a mayúsculas / minúsculas
cadena = input("Ingrese una cadena:")
print("upper: " + cadena.upper())
print("lower: " + cadena.lower())
print()

# center() centra una cadena
# cadena.center( ancho, [relleno])
cadena = "Hola"
print(cadena.center(20, "*"))
print(cadena.center(20))

# ljust() alinea la cadena a la izquierda
# rjust() alinea la cadena a la derecha
# zfill() rellena con ceros a la izquierda
cadena = "Hola"
print(cadena.ljust(20, "*"))
print(cadena.rjust(20, "*"))
print(cadena.zfill(20))
print()

# strip() elimina los espacios en blanco al inicio y al final
# lstrip() elimina los espacios en blanco al inicio
# rstrip() elimina los espacios en blanco al final
cadena = "***Hola***"
print(cadena.strip("*"))
print(cadena.lstrip("*"))
print(cadena.rstrip("*"))
print()

# find() devuelve la posición de la primera ocurrencia de un caracter
cadena = "Es una cadena nada de nada"
print(cadena)
print(cadena.find("nada"))         # devuelve la posición de la primera ocurrencia de "nada"
print(cadena.find("nada", 15))     # busca desde la posición 15
print(cadena.find("nada", 0, 10))  # -1 es que no encontró
print()


# rfind() devuelve la posición de la última ocurrencia de un caracter
cadena = "Es una cadena nada de nada"
print(cadena)
print(cadena.rfind("nada"))         # devuelve la posición de la última ocurrencia de "nada"
print(cadena.rfind("nada", 15))     # busca desde el final hasta la posición 15
print(cadena.rfind("nada", 10, 20)) # busca desde la posición 10 hasta la posición 20
print()


