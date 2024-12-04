
# ------------------------------------------------------------
# Defino una clase padre 
# ------------------------------------------------------------
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo        
        self.color = color
    
    def acelerar(self):
        print(self.marca +" Acelerando")

    def frenar(self):
        print(self.marca +" Frenando")

# ------------------------------------------------------------
# Defino una clase hija
# ------------------------------------------------------------
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def frenar(self):
        print(f"¡Este coche {self.marca} {self.color} está frenando!")

# ------------------------------------------------------------
# Defino otra clase hija
# ------------------------------------------------------------
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada, carga):
        super().__init__(marca, modelo, color)
        self.carga = carga


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

# Instancio un coche
mi_coche = Coche("Seat", "Ibiza", "Rojo", "2.0")

# Instancio un camioneta
mi_camioneta = Camioneta("Ford", "Ranger", "Azul", "3.2", "20t")

# Aceleramos y frenamos el coche
mi_coche.acelerar()
mi_coche.frenar()

# Aceleramos y frenamos la camioneta
mi_camioneta.acelerar()
mi_camioneta.frenar()

# Instancio un vehiculo de la clase madre.
# (Esto se puede evitar con el uso de clases abstractas)
mi_vehiculo = Vehiculo("Chevrolet", "Prisma", "Gris")
print(mi_vehiculo.marca)
















