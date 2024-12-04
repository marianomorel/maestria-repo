# ------------------------------------------------------------
# Ejempolo 8: Colaboración de clases
# Plantear un programa que permita jugar a los dados. Las reglas
# de juego son:
# Se tiran tres dados y si los tres salen con el mismo valor se
# debe mostrar un mensaje que diga "ganó", sino "perdió".
# ------------------------------------------------------------

# Esto lo veremos mas adelante, pero básicamente estamos
# incorporando a este script una forma de generar números
# aleatorios.
import random

# ----------------- Clase Dado -----------------
class Dado:
    def tirar(self):
        self.valor = random.randint( 1, 6)

    def imprimir(self):
        print(f"Valor del dado: {self.valor}")

    def retornar_valor(self):
        return self.valor

# ----------------- Clase Juego De Dados ----------------- 
class JuegoDeDados:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if (self.dado1.retornar_valor() == self.dado2.retornar_valor() 
            and self.dado1.retornar_valor() == self.dado3.retornar_valor()):
            print("Ganó")
        else:
            print("Perdió")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

juego_dados = JuegoDeDados()
juego_dados.jugar()