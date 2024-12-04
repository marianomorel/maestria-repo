# ------------------------------------------------------------
# Problema 3:
# Confeccionar una clase que represente un empleado. Definir
# como atributos su nombre y su sueldo. En el método __init__
# cargar los atributos por teclado y luego en otro método
# imprimir sus datos y por último uno que imprima un mensaje
# si debe pagar impuestos (si el sueldo supera a 3000).
# ------------------------------------------------------------

class Empleado:

    # Constructor (__init__ se invoca automaticamente al crear un objeto)
    def __init__(self):
        self.nombre = input("Nombre del empleado : ")
        self.sueldo = float(input("Salario del empleado: "))

    # Método que se invoca automaticamente al destruir el objeto.
    def __del__(self):
        print("-"*30)
        print('Objeto eliminado de la memoria')
        
    # Método que muestra datos por la terminal
    def imprimir(self):
         print(f"Nombre: {self.nombre}")
         print(f"Sueldo: {self.sueldo}")

    # Método que imprime un mensaje si debe pagar impuestos
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

empleado1 = Empleado()         # Instanciamos un objeto
empleado1.imprimir()           # Mostramos los datos
empleado1.paga_impuestos()     # Llamamos al método que imprime un mensaje


