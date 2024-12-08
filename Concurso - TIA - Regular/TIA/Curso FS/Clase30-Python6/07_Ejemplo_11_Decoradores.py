#Getters y Setters
# Encapsulamiento: atributos privados
# decorador @property
# https://codigofacilito.com/articulos/decoradores-python


class Bebidas:
   def __init__(self):
       self.__bebida = 'Naranja'
   @property
   def favorita(self):
       return f"La bebida preferida es: {self.__bebida}"

   @favorita.setter
   def favorita(self, bebida):
       self.__bebida = bebida

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla
obj1 = Bebidas()
obj1.favorita = "Pomelo"
print(obj1.gaseosa)
print(obj1.favorita)    # Pomelo
