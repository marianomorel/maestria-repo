# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Funciones lambda o anónimas
# ------------------------------------------------------------

# Resumen de la sintaxis:
# variable = lambda parametros: return


# Función lambda para calcular el cuadrado de un número:
cuadrado = lambda x: x**2

# Funcion lambda para determinar si un número es par o impar:
par_impar = lambda x: "Par" if x % 2 == 0 else "Impar"


print(cuadrado(10))
print(par_impar(14))