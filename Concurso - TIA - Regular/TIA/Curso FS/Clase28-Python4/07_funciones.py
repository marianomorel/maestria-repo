# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función que recibe listas (y devuelve una lista!)
# ------------------------------------------------------------

# Esta funcion recibe dos listas y devuelve una lista con los 
# elementos que se encuentran en ambas listas:
def funcion_interseccion(lista1, lista2):
    lista_interseccion = []
    for elemento in lista1:
        if elemento in lista2:
            lista_interseccion.append(elemento)
    return lista_interseccion



# Invoco a la función con un par de listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(funcion_interseccion(lista1, lista2))


# ------------------------------------------------------------
# TIP: Claramente, esta función tambien puede trabajar con 
# listas cuyos elementos no sean numéricos:
#
# lista1 = ['a', 'b', 'c', 'd', 'e']
# lista2 = ['c', 'd', 'e', 'f', 'g']
# print(funcion_interseccion(lista1, lista2))
#
# ------------------------------------------------------------