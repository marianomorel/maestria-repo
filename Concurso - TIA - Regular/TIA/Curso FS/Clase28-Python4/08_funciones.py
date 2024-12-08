# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función que devuelve mas de un valor
# ------------------------------------------------------------

# Esta función recibe un arreglo de números, y devuelve una tupla con
# el mayor y el menor valor:
def funcion_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return (mayor, menor)



# Invoco a la función con un arreglo de números:
numeros = [1, 2, 3, 4, 5]
print(funcion_mayor_menor(numeros))

# Tambien puedo hacer esto:
num_mayor, num_menor = funcion_mayor_menor(numeros)
print(f"El mayor es {num_mayor} y el menor es {num_menor}")

