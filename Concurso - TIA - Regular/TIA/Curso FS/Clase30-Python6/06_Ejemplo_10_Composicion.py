# ------------------------------------------------------------
# Ejemplo 10: Objetos dentro de objetos (Composición)
# ------------------------------------------------------------

class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo      = titulo
        self.duracion    = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f"{self.titulo} ({self.lanzamiento})"


# ------------------------------------------------------------
class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

peli = Pelicula("El Padrino", 175, 1972)

cata = Catalogo([peli])  # Añado una lista con una película al catalogo
cata.mostrar()           # Muestro el catalogo

# Añadimos otra película
cata.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  
cata.mostrar()           # Muestro el catalogo
