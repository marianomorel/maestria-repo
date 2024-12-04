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
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        #Fecha no puede ser anterior a 2006
        self.fecha_inicio = fecha

    @property
    def fecha_inicio(self):
        #print("Estoy obteniendo la fecha de inicio")
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha):
        # print("Estoy seteando la fecha de inicio")
        if fecha < 2006:
            self._fecha_inicio = 2006
        else:
            self._fecha_inicio = fecha



# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

#Creamos una carrera y tres materias
carrera1 = Carrera("Ingenieria en Sistemas")
algebra = Materia("Algebra", "Juan Quinteros", 2004)
fisica = Materia("Fisica", "Pedro Perez", 2012)   
programacion = Materia("Programacion", "Lorena Ríos",2022)

#Agregamos las materias a la carrera:
carrera1.agregar_materia(201,algebra)
carrera1.agregar_materia(202,fisica)
carrera1.agregar_materia(203,programacion)

# Veo la fecha de inicio de dictado de algunas materia:
print(f"La fecha de inicio de {algebra.nombre} es {algebra.fecha_inicio}")
print(f"La fecha de inicio de {fisica.nombre} es {fisica.fecha_inicio}")
print(f"La fecha de inicio de {programacion.nombre} es {programacion.fecha_inicio}")




