# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Funciones lambda o anónimas con map y lista de
#           funciones
# ------------------------------------------------------------

# Defino una funcion que devuelve si un número es par o impar
par_impar = lambda x: "Par" if x % 2 == 0 else "Impar"

# Defino una funcion que devuelve el cuadrado de un número
cuadrado = lambda x: x**2

# Defino una lista de funciones:
lista_de_funciones = [par_impar, cuadrado]

# Defino la lista de valores a utilizar
lista_de_valores = [1, 2, 3, 4, 5]

# Recorro la lista de valores y aplico las funciones de la lista:
for elemento in lista_de_valores:
    valores = list(map(lambda x: x(elemento), lista_de_funciones))
    print(elemento, "--->", valores)


# Puedes mostrar la información de una manera mas clara.
# Prueba cambiando el print() dentro del bucle for por el
# siguiente:
#
# print(f"{elemento} es {valores[0]}, y elevado al cuadrado es {valores[1]}")