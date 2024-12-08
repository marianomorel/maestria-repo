# ------------------------------------------------------------
# Problema 1:
# Implementar una clase llamada Persona que tendrá como atributo
# (variable) su nombre y dos métodos (funciones), uno de dichos
# métodos inicializará el atributo nombre y el siguiente método
# mostrará en la pantalla el contenido del mismo.
# Definir dos objetos de la clase Persona e incorporar una variable
# de clase (piernas).
# ------------------------------------------------------------


# Creamos la clase (class + sustantivo en singular en mayúscula)
class Persona:
    piernas = 2  # Atributo (Variable de clase)

    # Constructor
    def inicializar( self, nombre ):
        self.nombre = nombre

    # Método que muestra datos por la terminal
    def imprimir ( self ):
        print(f"Nombre: {self.nombre}")


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
# Usamos la "nomenclatura del punto".
# Atributos sin (), metodos con ()

print("\033[H\033[J")          # Limpiamos la pantalla

persona1 = Persona()          # Creamos un objeto
persona1.inicializar("Pedro") # Llamamos al constructor con un nombre
persona1.imprimir()           # Mostramos los datos
print(persona1.piernas)

persona2 = Persona()
persona2.inicializar("Carla")
persona2.imprimir()
print(persona2.piernas)