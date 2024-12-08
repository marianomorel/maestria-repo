#--------------------------------------------------------------------
# Este es un módulo que contiene funciones para cadenas
#--------------------------------------------------------------------

# Devuelve una cadena invertida:
def invierte_cadena(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

#--------------------------------------------------------------------
# Tip: fijate como funcionaria esto:
# def invierte_cadena(cadena):
#     return cadena[::-1]
#--------------------------------------------------------------------

# Devuelve "Hola Mundo"
def hola_mundo():
    return "Hola Mundo"


print(invierte_cadena("pepe"))