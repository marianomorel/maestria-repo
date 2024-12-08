# ------------------------------------------------------------
# PYTHON 3 - Conjuntos
# -----------------------------------------------------------

# Creación de un conjunto:
nombres = {"Juan", "Pedro", "Maria", "Luis"}
print (nombres)

# Podemos agregar elementos al conjunto:
nombres.add("Ana")
print (nombres)

# Desempaquetado:
alumno1, alumno2, alumno3, alumno4, alumno5 = nombres
print (alumno1)
print (alumno2)
print (alumno3)
print (alumno4)
print (alumno5)


# NO PODEMOS agregar elementos duplicados al conjunto:
nombres.add("Ana") # No da error, pero no se agrega.
print (nombres) 

