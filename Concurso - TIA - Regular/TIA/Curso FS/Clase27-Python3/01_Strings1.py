# ------------------------------------------------------------
# PYTHON 3 - Strings
# Ejemplo 1
# ------------------------------------------------------------

# Guardamos strings en variables:
mensaje = "Hola"
nombre = "Juan"
apellido = 'Perez'

# Podemos contaternarlas con +
saludo = mensaje + " " + nombre + " " + apellido

# E imprimirlas con print
print(saludo)

# len(cadena) retorna la longitud de cadena
print( len(saludo))

# Podemos acceder en forma individual a cada 
# caracter del string mediante un subíndice:
nombre = "Viviana Garcia"
print(nombre[0])   # V
print(nombre[1])   # i
print(nombre[2])   # v
print(nombre[-1])  # a
print(nombre[4:7]) # ana

# Podemos "multiplicar" cadenas con *
risa = "Ja "
carcajada = risa * 6
print(carcajada)
