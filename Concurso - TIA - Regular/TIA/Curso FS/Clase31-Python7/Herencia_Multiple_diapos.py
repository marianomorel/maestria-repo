
class Persona: # Superclase
    def __init__(self, identificacion, nombre, apellido, dni):
        self.id = identificacion 
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    def __str__(self): # Método str:
        return f"{self.id} - DNI - {self.dni} {self.apellido}, {self.nombre}"

class Ciudad: # Superclase
    pais = "Argentina" # Atributo de clase
    def __init__(self, nombre, codigo_postal):
        self.nombre = nombre
        self.cp = codigo_postal
    def __str__(self): # Método str:
        return f"({self.cp}) {self.nombre}"

class AlumnoCodo(Persona, Ciudad): # Subclase
    def __init__(self, identificacion, nombre, apellido, dni, curso):
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