# ------------------------------------------------------------
# PYTHON 3 - Listas
# Ejemplo 3 - Métodos
# -----------------------------------------------------------

# Declaracion de  la lista
numeros = [ 1, 2, 3, 4, 5 ]

# append() agrega un elemento al final de la lista
numeros.append(6) # [1, 2, 3, 4, 5, 6]

# insert() agrega un elemento en una posicion especifica
numeros.insert(2, 7) # [1, 2, 7, 3, 4, 5, 6]

# pop() elimina el ultimo elemento de la lista
numeros.pop() # [1, 2, 7, 3, 4, 5]

# remove() elimina la primer aparición de un elemento
# (Si no existe, da error)
numeros.remove(7) # [1, 2, 3, 4, 5]

# index() devuelve la posicion la primer aparición
# de un elemento (Si no existe, da error)
print(numeros.index(3)) # 2

# count() devuelve la cantidad de veces que aparece
# un elemento en la lista. (0 si no existe)
print(numeros.count(3)) # 1

# reverse() invierte el orden de los elementos
colores = [ 'rojo', 'azul', 'verde', 'amarillo' ]
print(colores)
colores.reverse()
print(colores)

# sort() ordena los elementos de la lista
colores.sort()  
print(colores)

# sort( reverse = True) ordena los elementos de la lista
# en orden inverso
colores.sort(reverse = True)  
print(colores)

# clear() elimina todos los elementos de la lista
colores.clear()
print("Colores: " , colores)


