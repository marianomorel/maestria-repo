#--------------------------------------------------------
# Ejemplo de bucle For en Python - 3
#--------------------------------------------------------
# Escribir en pantalla los mpultiplos de 3 entre 1 y 100
# Sumarlos, y mostrar la suma al final

suma = 0   # Inicializar la variable suma
for i in range(1, 101):
    if i % 3 == 0:
        print(i)    # Mostrar el múltiplo de 3
        suma += i   # Sumar el multiplo de 3
print("La suma de los multiplos de 3 es:", suma)


# Fin del programa  