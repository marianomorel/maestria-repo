# Importo el módulo "mi_modulo.py":
print()
import mi_modulo
print()

print("¡Hola desde  el programa principal.py!")
print("Nombre del módulo importado :", mi_modulo.__name__)
print("Nombre del módulo ejecutado :", __name__)
mi_modulo.hacer_algo()
print("¡Adiós desde el programa principal.py!")