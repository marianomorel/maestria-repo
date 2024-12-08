# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Funciones lambda o anónimas con map
# ------------------------------------------------------------

# Función lambda para calcular el cuadrado de una lista de números:
lista_de_valores = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, lista_de_valores))

print(cuadrados)
