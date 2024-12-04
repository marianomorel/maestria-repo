# Esta línea se ejecuta al llamar al módulo.
print()
print("¡Hola desde mi_modulo.py!")


# Función de prueba
def hacer_algo():
    print("  Mensaje de la función 'hacer_algo'")


# El código dentro del if solo se ejecuta cuando
# este módulo es el principal.
if __name__ == "__main__":
    print('Ejecutando como programa principal')
    print("Nombre del módulo ejecutado :", __name__)


