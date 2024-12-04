# ------------------------------------------------------------
# Problema 5:
# Plantear una clase Operaciones que solicite en el método
# __init__ la carga de dos enteros e inmediatamente muestre su
# suma, resta, multiplicación y división. Hacer cada operación
# en otro método de la clase Operación y llamarlos desde el
# mismo método __init__
# ------------------------------------------------------------

class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def __del__(self):
        print('Método delete llamado')

    def sumar(self):
        suma=self.valor1+self.valor2
        print(f"La suma es: {suma}")

    def restar(self):
        resta=self.valor1-self.valor2
        print(f"La resta es: {resta}")

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print(f"El producto es: {producto}")

    def dividir(self):
        division=self.valor1/self.valor2
        print(f"La division es: {division}")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

operacion1 = Operacion()       # Instanciamos el objeto

