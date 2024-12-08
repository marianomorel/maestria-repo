# ------------------------------------------------------------
# Creamos una clase "Carrera"
# Contiene el nombre y materias que componen una carrera
# ------------------------------------------------------------
class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {} #Contendrá tuplas (codigo, materia)

    # Este método agrega materias a la coleccion de materias
    def agregar_materia(self, materia, codigo):
        self.materias[codigo] = materia

# ------------------------------------------------------------
# Creamos una clase "Materia"
# Contiene el nombre y los docentes de cada materia
# ------------------------------------------------------------
class Materia:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

#Creamos una carrera y tres materias
carrera1 = Carrera("Ingenieria en Sistemas")
algebra = Materia("Algebra", "Juan Quinteros")
fisica = Materia("Fisica", "Pedro Perez")   
programacion = Materia("Programacion", "Lorena Ríos")

#Agrego las materias a la carrera:
carrera1.agregar_materia(201,algebra)
carrera1.agregar_materia(202,fisica)
carrera1.agregar_materia(203,programacion)


# Imprimo las materias de la carrera
print(carrera1.materias)