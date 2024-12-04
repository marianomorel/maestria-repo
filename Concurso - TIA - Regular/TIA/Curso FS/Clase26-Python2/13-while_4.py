#--------------------------------------------------------
# Ejemplo de bucle While en Python - 4
#--------------------------------------------------------
# Leer números enteros  y mostrarlos hasta que se ingrese 
# un número negativo.


while True: # Este bucle no finaliza nunca...
    numero = int(input("Escribe un número (negativo para terminar): "))
    print(f"Ingresado: {numero}")
    print()
    if numero < 0: # Si el número es negativo...
        break      #...termina el bucle

# Fin del programa



# Fin del programa  