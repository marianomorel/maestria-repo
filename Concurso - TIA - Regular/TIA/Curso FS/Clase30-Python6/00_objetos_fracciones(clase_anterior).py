# ------------------------------------------------------------
# PYTHON 5 - Objetos
# Ejemplo - Creamos una clase e instanciamos objetos
# ------------------------------------------------------------
# Creamos la clase "Fraccion".
# Esta clase tiene un constructor que recibe dos parámetros:
# numerador y denominador.
# La clase tiene métodos que devuelven cadenan con el
# resultado de sumar, restar, multiplicar y dividir una
# fracción con otra.
#
# DESAFIO: Crear un método que "simplifque" la fracción
# antes de imprimirla. (Pista: buscar el mayor común divisor)
# ------------------------------------------------------------

class Fraccion():
    # Constructor
    def __init__(self, numerador, denominador):
        self.nume = numerador
        self.deno = denominador
    
    # Método para mostrar datos
    def __str__(self):
        return f"{self.nume} / {self.deno}"

    # Método para sumar
    def sumar(self, otra):
        numerador = self.nume * otra.deno + self.deno * otra.nume
        denominador = self.deno * otra.deno
        return Fraccion(numerador, denominador)

    # Método para multiplicar
    def multiplicar(self, otra):
        numerador = self.nume * otra.nume
        denominador = self.deno * otra.deno
        return Fraccion(numerador, denominador)

    # Método para dividir
    def dividir(self, otra):
        numerador = self.nume * otra.deno
        denominador = self.deno * otra.nume
        return Fraccion(numerador, denominador)

    # Método para restar
    def restar(self, otra):  
        numerador = self.nume * otra.deno - self.deno * otra.nume
        denominador = self.deno * otra.deno
        return Fraccion(numerador, denominador)

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")       # Limpiamos la pantalla

fraccion1 = Fraccion(1, 2)  # Creamos un objeto
fraccion2 = Fraccion(3, 2)  # Creamos otro objeto

# Un tercer objeto es la suma de los dos primeros
fraccion3 = fraccion1.sumar(fraccion2)
# Mostramos el resultado de la suma
print(f"{fraccion1}  +  {fraccion2}  =  {fraccion3}")

# Hacemos el producto de Fraccion1 por Fraccion2
fraccion4 = fraccion1.multiplicar(fraccion2)
# Mostramos el resultado del producto
print(f"{fraccion1}  *  {fraccion2}  =  {fraccion4}")

# Hace la división de Fraccion1 por Fraccion2
fraccion5 = fraccion1.dividir(fraccion2)
# Mostramos el resultado de la división
print(f"{fraccion1}  /  {fraccion2}  =  {fraccion5}")

# Hace la resta de Fraccion1 por Fraccion2
fraccion6 = fraccion1.restar(fraccion2)
# Mostramos el resultado de la resta
print(f"{fraccion1}  -  {fraccion2}  =  {fraccion6}")



