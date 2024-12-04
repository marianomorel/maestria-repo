#-------------------------------------------------------------
# Importamos ABC y abstractmethod desde abc
# ------------------------------------------------------------
from abc import ABC, abstractmethod

# ------------------------------------------------------------
# Clase que representa animales:
class Animal(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def hablar(self):
        print("Está diciendo: ", end="")
# ------------------------------------------------------------
# Clase que representa perros:
class Perro(Animal):
    def comer(self):
        print("Está comiendo un hueso")

    def hablar(self):
        super().hablar()
        print("Guau!")

# ------------------------------------------------------------
# Clase que representa gatos:
class Gato(Animal):
    def comer(self):
        print("Está tomando leche")

    def hablar(self):
        super().hablar()
        print("Miau!")


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla   

# Instanciamos un perro:
perro1 = Perro()
perro1.hablar()
perro1.comer()

# Instanciamos un gato:
gato1 = Gato()
gato1.hablar()
gato1.comer()

# Intentamos instanciar un Animal:
# animal1 = Animal()   # Es imposible porque Animal es abstracto