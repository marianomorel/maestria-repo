# ------------------------------------------------------------
# PYTHON 4 - Funciones
# Ejemplo - Función que devuelve un valor (Return)
# ------------------------------------------------------------

# Definimos una funcion que calcula el area de un triangulo:
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# Invocamos a la funcion area_triangulo():
base = 10
altura = 8
area = area_triangulo(base, altura)
print(f"El area de un triángulo con base={base} y altura={altura} es {area}.")




