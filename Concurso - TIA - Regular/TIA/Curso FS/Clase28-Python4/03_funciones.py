# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función con parámetros opcionales
# ------------------------------------------------------------

# Definimos una funcion que suma los números enteros entre dos dados.
# Muestra solo el resultado o un mensaje mas completo si se le indica:
def sumar(num1, num2, mensaje=False):
    suma = 0   # Inicializamos la variable suma
    for i in range(num1, num2+1):
        suma += i

    if mensaje:    
        print(f"La suma de los enteros entre {num1} y {num2} es {suma}.")
    else:
        print(suma)

# Invocamos a la función suma():
sumar(1, 100)
sumar(1, 100, True)




