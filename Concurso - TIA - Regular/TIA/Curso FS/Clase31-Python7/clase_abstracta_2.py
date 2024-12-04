# Importamos ABC y abstractmethod
from abc import ABC, abstractmethod

# Definimos la clase Animal (Abstracta)
class Animal(ABC):

    @abstractmethod  # Este método será completado
    def mover(self): # en cada subclase, con el
        pass         # código pertinente.

    @abstractmethod  # Idem método anterior
    def emitir_sonido(self):
        print("Animal dice: ", end="")

# Definimos la subclase Gato:
class Gato(Animal):
    # Este método completa al de Animal
    def mover(self):
        print("El gato se mueve.")

    # Este método completa al de Animal
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau!")

# Definimos la subclase Perro
class Perro(Animal):
    # Este método completa al de Animal
    def mover(self):
        print("El perro se está moviendo.")

    # Este método completa al de Animal
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau, Guau!")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

g1 = Gato()
g1.mover()
g1.emitir_sonido()

p1 = Perro()
p1.mover()
p1.emitir_sonido()
