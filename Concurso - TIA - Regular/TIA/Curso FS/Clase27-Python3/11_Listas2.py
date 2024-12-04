# ------------------------------------------------------------
# PYTHON 3 - Listas
# Ejemplo 2 - Desempaquetado y operaciones
# -----------------------------------------------------------

# Declaracion de  la lista
colores = ["rojo", "azul", "verde", "amarillo"]

# Desempaquetado en variables
color1, color2, color3, color4 = colores
print(color1)
print(color2)
print(color3)
print(color4)

# Sumar listas:
numeros1 = [ 1, 2, 3, 4, 5 ]
numeros2 = [ 6, 7, 8, 9, 10]
suma = numeros1 + numeros2
print(suma)

suma = suma + [11]
print(suma)

# Podemos ver la longitud de una lista
print (len(suma))

# Podemos modificar sus elementos:
suma[0] = 100
print(suma)

# max() devuelve el mayor elemento de una lista.
# min() devuelve el menor elemento de una lista.
# sum() devuelve la suma de los elementos de una lista:
print(max(suma)) # 100
print(min(suma)) # 2
print(sum(suma)) # 165

# list() convierte una cadena a una lista:
cadena = "Hola mundo"
print(cadena)
lista = list(cadena) # ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
print(lista)

# Tambien funciona con range():
lista = list(range(10, 101, 10))
print(lista)