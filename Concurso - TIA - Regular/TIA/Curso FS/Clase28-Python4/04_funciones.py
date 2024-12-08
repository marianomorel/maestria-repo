# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función con parámetros posicionales / con nombres
# ------------------------------------------------------------

# Definimos una funcion que saluda a una persona
def saludar(apellido, nombre, saludo):
    print(saludo, nombre, apellido)


# Invocamos a la función saludar()
# de la forma "tradicional":
saludar("Perez", "Juan", "Hola")

# Ahora, pasamos los parámetros con su nombre
saludar(saludo = "Hola, cómo estas,", nombre = "Ariadna", apellido = "Farías")

# Y ahora, un "mix":
saludar("Borges", saludo = "Muy buenos días", nombre = "Jorge Luis")


# Importante: en el ejemplo anterior, vemos  que podemos mezclar
# el orden de los parámetros si indicamos su nombre. Eso sí,
# los que van con su nombre siempre deben estar a la derecha de
# los parámetros posicionales, # es decir, aquellos que se indican
# sin nombre.


