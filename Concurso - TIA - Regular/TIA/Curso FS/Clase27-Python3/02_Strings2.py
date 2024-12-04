# ------------------------------------------------------------
# PYTHON 3 - Strings
# Ejemplo 2
# ------------------------------------------------------------

# Podemos cortar lineas usando el caracter \ 

cadena = "Hay dos maneras de diseñar software: \
una es hacerlo tan simple que sea obvia su falta \
de deficiencias, y la otra es hacerlo tan complejo \
que no haya deficiencias obvias"

# Con "in" y "not in" podemos verificar si una cadena
# contiene una subcadena:

if "software" in cadena:
    print("La cadena contiene la subcadena 'software'")

if "hardware" not in cadena:
    print("La cadena no contiene la subcadena 'hardware'")

# Se puede iterar sobre una cadena:
for letra in cadena:
    print(letra,end="-")  # end="-" para que no se imprima un salto de linea

# Max() y min() retornan el caracter mas grande y mas pequeño de una cadena:
print("\nMax:",max(cadena)) #ñ tiene el valor ASCII 164, mayor al resto 
print("Min:",min(cadena))   #El espacio tiene el valor ASCII 32, menor al resto

# count() retorna la cantidad de veces que aparece una subcadena en una cadena:
print("\nCantidad de 'a':",cadena.count("a"))
print("Cantidad de 'obvia':",cadena.count("obvia"))

# index() retorna el indice de la primera ocurrencia de una subcadena en una cadena:
print("\nCantidad de 'a':",cadena.index("a"))
print("Cantidad de 'obvia':",cadena.index("obvia"))


