#--------------------------------------------------------
# Ejemplo de condicional if en Python - 8
# Operadores lógicos.
#--------------------------------------------------------
# Escribir un programa que pida al usuario su nombre, su
# nacionalidad y su edad. Si es un argentino y mayor a 18
# años, mostrar su nombre.
# Si no, mostrar un mensaje indicando que no puede ingresar.

nombre       = input("Ingrese su nombre: ")
nacionalidad = input("Ingrese su nacionalidad: ")
edad         = int(input("Ingrese su edad: "))

if nacionalidad == "Argentina" and edad >= 18:
    print(f"Bienvenido {nombre}")
else:
    print("No puede ingresar")  
# Fin del programa  