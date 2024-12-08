#Creamos una clase:

class Gato():
    # Atributos de clase
    tipo_animal = "Mamífero"
    variedad = "Felino"

    # Constructor:
    def __init__(self, nombre, edad, alimentos_favoritos):
        # Estos son los atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.alimentos = alimentos_favoritos
        # Este atributo se crea en el constructor
        self.vive = True

    # Este método nos dice en que etapa de su vida está el gato
    def verEtapaDeVida(self):
        if self.vive:
            print("El gato está vivo")
            if self.edad < 1:
                print("El gato es cachorro")
            elif self.edad < 3:
                print("El gato es joven")
            else:
                print("El gato es adulto")
        else:
            print("El gato está muerto")

    # Este método nos dice si al gato le gusta algo
    def comer(self, alimento):
        if alimento in self.alimentos:
            print("El gato come " + alimento)
        else:
            print("El gato no come " + alimento)

    # El metodo __str__ es un método especial que se
    # ejecuta cuando se imprime un objeto:
    def __str__(self):
        return "El gato se llama " + self.nombre + " y tiene " + str(self.edad) + " años"   



#------------------------------------------
# Creamos un objeto:
mi_gato = Gato("Felix", 2, ["pollo", "pescado"])
print(mi_gato.nombre)        # Muestra su atributo nombre
print(mi_gato.edad)          # Muestra su atributo edad
print(mi_gato.alimentos)     # Muestra su atributo alimentos fav.
print(mi_gato.vive)          # Muestra su atributo vive/no vive

mi_gato.edad = 3             # Cambiamos el atributo edad
print(mi_gato.edad)          # Muestra su atributo edad

print(mi_gato.variedad)      # Muestra la variable de clase

mi_gato.verEtapaDeVida()     # Muestra su etapa de vida
mi_gato.vive = False         # Cambiamos su valor a False...
mi_gato.verEtapaDeVida()     # Muestra su etapa de vida

mi_gato.comer("pollo")       # El gato come pollo
mi_gato.comer("queso")       # El gato no come queso
mi_gato.alimentos += ["queso"] # Añadimos queso a su atributo alimentos
mi_gato.comer("queso")       # El gato come queso

print(mi_gato)               # Muestra su estado

