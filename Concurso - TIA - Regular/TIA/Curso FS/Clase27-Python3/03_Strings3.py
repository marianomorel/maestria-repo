# ------------------------------------------------------------
# PYTHON 3 - Strings
# Ejemplo 3
# ------------------------------------------------------------

# join() retorna una cadena con una separación entre cada elemento:
cadena = "Hola Mundo!"
print("\n"+cadena)
cadena_separada = ",".join(cadena)
print(cadena_separada)

# split() retorna una lista con las subcadenas separadas por una separación:
cadena = "Si la depuración es el proceso de eliminar \
errores, entonces la programación debe ser el proceso \
de introducirlos"  # Cadena original

cadena_separada = cadena.split(" ") # Separamos por espacios en blanco
print(cadena_separada)

# replace() reemplaza una subcadena por otra:
cadena = "El buen código es su mejor documentación"
print("\n"+cadena)
cadena_reemplazada = cadena.replace("buen","mal")
print(cadena_reemplazada)

# isalpha() retorna True si la cadena contiene solo letras:
cadena = "Hola Mundo!"
print("\n",cadena.isalpha())
cadena = "Hola Mundo"
print(cadena.isalpha())

# isdigit() retorna True si la cadena contiene solo dígitos:
cadena = "25304020"
print("\n", cadena.isdigit())
cadena = "DNI:25304020"
print(cadena.isdigit())

# isalnum() retorna True si la cadena contiene solo letras y dígitos:
cadena = "25304020"
print("\n", cadena.isalnum())
cadena = "DNI25304020"
print(cadena.isalnum())
cadena = "DNI:25304020"
print(cadena.isalnum())


