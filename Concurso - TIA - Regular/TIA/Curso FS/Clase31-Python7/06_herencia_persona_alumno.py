# Superclase
class Persona:
    #Clase que representa una persona.
    def __init__(self, identificacion, nombre, apellido, dni):
        #Constructor de Persona
        self.id = identificacion  # Atributo de instancia
        self.nombre = nombre      # Atributo de instancia
        self.apellido = apellido  # Atributo de instancia
        self.dni = dni            # Atributo de instancia

    # Método str:
    def __str__(self):
        return f"{self.id} - DNI - {self.dni} {self.apellido}, {self.nombre}"

# Subclase
class AlumnoCodo(Persona): # Parametro: superclase
    # Clase que representa a un alumno de Codo a Codo
    def __init__(self, identificacion, nombre, apellido, dni, curso):
        # Constructor de Alumno
        # Invocamos al constructor de la superclase:
        Persona.__init__(self, identificacion, nombre, apellido, dni)
        # agregamos el atributo propio del alumno
        self.curso = curso

    # Método str propio de la subclase AlumnoCodo:
    def __str__(self):
        cadena = f"{self.id} - DNI - {self.dni} \n"
        cadena += f"{self.apellido},{self.nombre} \n"
        cadena += f"Carrera: {self.curso}"
        return cadena 

# Programa principal
p1 = Persona(3, "Carlos", "Kleiber", 32456812)
print(p1)
a1 = AlumnoCodo(1, "Eliana", "Vera", 27416319, "Full Stack")
print(a1)