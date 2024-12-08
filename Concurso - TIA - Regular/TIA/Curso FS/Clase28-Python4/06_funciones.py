# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función que devuelve un valor (Return)
# ------------------------------------------------------------

# Definimos una funcion que determina si un triángulo es
# rectángulo a partir de la longitud de sus lados:

def es_rectángulo(cateto1, cateto2, hipotenusa):
    hipotenusa_calulada = (cateto1**2 +cateto2**2)**0.5

    if hipotenusa_calulada == hipotenusa:
        return True
    else:
        return False


# Invocamos a la funcion area_triangulo():
print(es_rectángulo(12,35,37))

# ------------------------------------------------------------
# Una terna pitagórica es un conjunto ordenado de tres números
# enteros positivos a, b, c que se puede asociar con las 
# longitudes de los dos catetos y de la hipotenusa correspondiente,
# formando un triángulo rectángulo.
#
# Algunas ternas pitagoricas para probar la función de este ejemplo:
# (3,4,5)
# (5,12,13)
# (8,15,17)
# (12,35,37)
# (13,36,39)
# ------------------------------------------------------------



