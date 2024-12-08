numero = 1

while numero != "0":
    numero = input("Numero (0 para salir): ")
    cadena1 = ""

    if numero.isdigit():
        if numero != "0":
            final = 0
            puntero = len(numero)-1
            while puntero > final - 1:
                cadena1 = cadena1 + numero[puntero]
                puntero = puntero - 1

            if cadena1 == numero:
                print(numero, "es capicúa!")
            else:
                print(numero, "no es capicúa!")
    else:
        print("Error: Solo digitos por favor.")
        print("Intente nuevamente.")

    print()

print("-"*35)
print("Adios.")
