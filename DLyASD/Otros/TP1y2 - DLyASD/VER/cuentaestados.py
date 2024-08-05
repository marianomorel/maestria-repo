import math

#el estado 6 es el estado 7 del diagrama de estados. no confundir

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
        return 5
    elif estado == 1 and caracter == ' ':
        return 0
    elif estado == 1 and caracter != 'a':
        return 6
    elif estado == 2 and caracter != 's':
        return 6
    elif estado == 3 and caracter != 'a':
        return 6
    elif estado == 4 and caracter != ' ':
        return 6
    elif estado == 5 and caracter != 'c':
        return 6 
    elif estado == 5 and caracter == 'c':
        return 1
    else:
        return 0  # Reiniciar el estado si no se cumple ninguna condición

def analizar_oracion(oracion):
    estado_actual = 0
    ocurrencias_casa = 0
    for caracter in oracion:
        estado_actual = transicion(estado_actual, caracter)
        if estado_actual == 5:
            ocurrencias_casa += 1
            estado_actual = 0  # Reiniciar el estado al encontrar una ocurrencia completa de "casa"
        elif estado_actual == 6:
            estado_actual = 0  # Reiniciar el estado si no se encuentra "casa"
    
    # Se agrega este condicional para reiniciar el estado si la última palabra es "casa"
    if estado_actual == 4:
        ocurrencias_casa += 1
    
    print("Número total de ocurrencias de 'casa':", ocurrencias_casa)
    
    # Calcular la cantidad de registros necesarios
    cantidad_estados = 7  # Teniendo en cuenta los estados 0 a 6
    registros_necesarios = math.ceil(math.log2(cantidad_estados))
    print("Cantidad de registros necesarios:", registros_necesarios)

# Ejemplo de uso
oracion = "casa la saca casacasa casa"
analizar_oracion(oracion)
