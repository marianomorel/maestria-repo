# ------------------------------------------------------------
# PYTHON 3 - Listas
# Ejemplo 1
# -----------------------------------------------------------

# Declaracion de listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colores = ["rojo", "azul", "verde", "amarillo"]
lista_vacia = []
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accedemos por subindices:
print(numeros[0])    # 1
print(colores[1])    # azul
print(matriz[1][1])  # 5 (¿Crees que es correcto?)

# Impresión
print(numeros)

i = 0
while i < len(numeros):
    print(numeros[i], end=" ")
    i += 1

print() # Imprimo un salto de linea
for numero in numeros:
    print(numero, end=" ")


print() # Imprimo un salto de linea
for color in colores:
    print(color, end=" ")


print() # Imprimo un salto de linea
print (matriz)

print() # Imprimo un salto de linea
for elemento in matriz:
    print(elemento, end="")


print() # Imprimo un salto de linea
for elemento in matriz:
    for subelemento in elemento:
        print(subelemento, end=" ")

