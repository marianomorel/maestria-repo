# ------------------------------------------------------------
# Clase que representa personas:
class Persona:
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'({self.cedula}) {self.apellido}, {self.nombre} '

# ------------------------------------------------------------
# Clase quel representa destrezas de la Persona
class Destreza:
    def __init__(self, area, herramienta, experiencia):
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia

    def __str__(self):
        return f'{self.area} {self.herramienta} {self.experiencia}'

# ------------------------------------------------------------
# Clase que hereda de Persona y Destreza
class Jefe(Persona, Destreza):
    def __init__(self, cedula, nombre, apellido, area, herramienta, experiencia, grupo):
        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)
        # Nuevos atributos
        self.grupo = grupo

    def __str__(self):
        cadena = f"{self.cedula}: {self.nombre} {self.apellido},\nArea: '{self.area}', \nHerramienta: {self.herramienta}, \nGrupo: {self.grupo}"
        return cadena


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla   
     
print("-"*30)
persona1 = Persona(123456789, 'Juan', 'Perez')
print("Persona1:")
print(persona1)
print("-"*30)

destreza1 = Destreza('Programacion', 'Python', 'Experto')
print("Destreza1:")
print(destreza1)
print("-"*30)

jefe1 = Jefe(123456789, 'Ana', 'Jaurez', 'Diseño', 'Interfaz', 'Junior', '1')
print("Jefe1:")
print(jefe1)
print("-"*30)

