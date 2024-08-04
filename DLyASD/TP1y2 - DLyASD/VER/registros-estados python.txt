import math

def transicion(estado, caracter):
    if estado == 0 and caracter == 'c':
        return 1
    elif estado == 1 and caracter == 'a':
        return 2
    elif estado == 2 and caracter == 's':
        return 3
    elif estado == 3 and caracter == 'a':
        return 4
    elif estado == 4 and caracter == ' ':
        return 0
    elif estado == 4 and caracter == 'c':
        return 1
    else:
        return 0

def analizar_oracion(oracion):
    estado_actual = 0
    ocurrencias_casa = 0
    for caracter in oracion:
        estado_actual = transicion(estado_actual, caracter)
        if estado_actual == 4:
            ocurrencias_casa += 1
        elif estado_actual == 5:
            print("Se ha encontrado más de una ocurrencia de 'casa'.")
            break
    print("Número total de ocurrencias de 'casa':", ocurrencias_casa)
    
    # Calcular la cantidad de registros necesarios
    cantidad_estados = 6  # Teniendo en cuenta los estados 0 a 5
    registros_necesarios = math.ceil(math.log2(cantidad_estados))
    print("Cantidad de registros necesarios:", registros_necesarios)

# Ejemplo de uso
oracion = "vamos a nuestra casa luego de casarnos y de hacer la fiesta de casamiento en el salon casasanta"
analizar_oracion(oracion)
