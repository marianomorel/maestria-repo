# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función con parámetros
# ------------------------------------------------------------

# Definimos una funcion que suma los números enteros entre dos dados:
def sumar(num1, num2):
    suma = 0   # Inicializamos la variable suma
    for i in range(num1, num2+1):
        suma += i
    print(f"La suma de los enteros entre {num1} y {num2} es {suma}.")


# Invocamos a la función suma():
sumar(1, 100)

#-------------------------------------------------------
# Tip: ¿Conoces la historia del pequeño Gauss
# y la suma de los enteros entre 1 y 100?
#-------------------------------------------------------



