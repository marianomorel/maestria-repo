# ------------------------------------------------------------
# PYTHON 3 - Diccionarios
# -----------------------------------------------------------

# Creación de un diccionario
alumnos = {'Juan': 8, 'Pedro': 9, 'Maria': 10, 'Luis': 7}
print(alumnos)

# Se pueden crear por compresión:
cuadrados = {x: x**2 for x in range(11)}
print(cuadrados)

#-------------------------------------------------------
#Acceso a los elementos. Hay varias maneras.
#-------------------------------------------------------
print(alumnos.get("Juan")) # Devuelve el valor de la clave Juan
print(alumnos.get("Ana"))  # Devuelve "None", no existe "Ana"


# Acceso por clave, usando keys():
print(alumnos.keys())  # Muestra todas las claves

# Podemos recorrer el diccionario con un for y keys():
for i in alumnos.keys():
    print(i)

# items() devuelve una tupla con las claves y los valores:
for clave, valor in alumnos.items():
    print("Alumno:", clave, "Nota:", valor)


