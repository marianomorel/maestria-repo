#--------------------------------------------------------
# Ejemplo de bucle While en Python - 3
#--------------------------------------------------------
# Leer números enteros  y mostrarlos hasta que se ingrese 
# un número negativo.

numero = 0 # Asigno un valor inicial a la variable

while numero >= 0:
    numero = int(input("Escribe un número (negativo para terminar): "))
    print(f"Ingresado: {numero}")
    print()

# Fin del programa
