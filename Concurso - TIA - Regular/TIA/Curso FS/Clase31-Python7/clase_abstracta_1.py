from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass

perro = Animal()

#TypeError: Can't instantiate abstract class Animal with abstract method mover