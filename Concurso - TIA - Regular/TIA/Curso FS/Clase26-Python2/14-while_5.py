#--------------------------------------------------------
# Ejemplo de bucle While en Python - 5
#--------------------------------------------------------
# Leer números enteros, y contar la cantidad de pares e 
# impares que se han ingresado hasta que se ingrese 
# un número negativo.

pares = 0
impares = 0

while True: # Este bucle no finaliza nunca...
    numero = int(input("Escribe un número (negativo para terminar): "))
    print(f"Ingresado: {numero}")
    print()
    if numero < 0: # Si el número es negativo...
        break      #...termina el bucle
    else:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

print()
print("---------------------")
print("  Pares:", pares)
print("Impares:", impares)
print("---------------------")


# Fin del programa  