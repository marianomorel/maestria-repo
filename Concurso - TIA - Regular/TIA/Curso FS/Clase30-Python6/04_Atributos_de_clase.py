# ------------------------------------------------------------
# Clase prueba
# ------------------------------------------------------------
class prueba:
    variable = 100
    def __init__(self, nombre):
        self.nombre = nombre

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

# Creamos dos objetos
uno = prueba("Objeto 1")
dos = prueba("Objeto 2")

# Imprimimos en ambos el valor del
# atributo de clase
print("Atributo de clase desde el objeto1:", uno.variable)
print("Atributo de clase desde el objeto2:", dos.variable)
print("Atributo de clase desde la clase:", prueba.variable)
print()

# Cambiamos el valor del atributo de clase
prueba.variable = 150
print("Atributo de clase desde el objeto1:", uno.variable)
print("Atributo de clase desde el objeto2:", dos.variable)
print("Atributo de clase desde la clase:", prueba.variable)
print()

# Esto CREA una nueva propiedad del objeto
# que se llama variable, pero no es la misma
# que el atributo de clase:
uno.variable = 400
print("Atributo de clase desde el objeto1:", uno.variable)
print("Atributo de clase desde el objeto2:", dos.variable)
print()

prueba.variable = 150
print("Atributo de clase desde el objeto1:", uno.variable)
print("Atributo de clase desde el objeto2:", dos.variable)
print()