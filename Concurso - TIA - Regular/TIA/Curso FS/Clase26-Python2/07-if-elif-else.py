#--------------------------------------------------------
# Ejemplo de condicional if en Python - 7
#--------------------------------------------------------
# Escribir un programa que pida al usuario un número entero. 
# Si su valor es 2, 4 o 6 mostrar su valor en letras.

numero = int(input("Ingrese un número entero: "))
if numero == 2:
    print("El número es DOS")
elif numero == 4:
    print("El número es CUATRO")
elif numero == 6:
    print("El número es SEIS")
else:
    print("El número no es 2, 4 o 6")
# Fin del programa  