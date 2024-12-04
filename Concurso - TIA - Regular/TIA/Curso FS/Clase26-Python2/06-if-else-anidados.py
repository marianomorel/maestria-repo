#--------------------------------------------------------
# Ejemplo de condicional if en Python - 6
#--------------------------------------------------------
# Escribir un programa que pida al usuario un número entero. 
# Si es mayor de 10, mostrar si es par o impar.

numero = int(input("Ingrese un número entero: "))
if numero > 10:
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("El número es menor o igual a 10")

# Fin del programa