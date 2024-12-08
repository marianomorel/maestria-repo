# ------------------------------------------------------------
# PYTHON 3 - Strings
# Ejemplo 5
# -----------------------------------------------------------

# Formato de cadenas de caracteres
nombre = "Juan"
apellido = "Perez"
edad = 30

print ("Hola, %s %s, tienes %d años" % (nombre, apellido, edad))
print ("Hola, {} {}, tienes {} años".format(nombre, apellido, edad))
print ("Hola, {1} {0}, tienes {2} años".format(nombre, apellido, edad))
print (f"Hola, {nombre} {apellido}, tienes {edad} años")


