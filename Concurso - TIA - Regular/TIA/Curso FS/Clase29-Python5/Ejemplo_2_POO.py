# ------------------------------------------------------------
# Problema 2:
# Implementar una clase llamada Alumno que tenga como atributos
# su nombre y su nota.
# Definir los métodos para inicializar sus atributos, imprimirlos
# y mostrar un mensaje si su estado es “regular” (nota mayor o 
# igual a 4).
# Definir dos objetos de la clase Alumno.
# ------------------------------------------------------------


# Creamos la clase (class + sustantivo en singular en mayúscula)
class Alumno:
    # Constructor
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota   = nota

    # Metodo para mostrar los datos
    def imprimir(self): 
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    # Metodo para ver si está aprobado
    def mostrar_estado(self): 
        if self.nota >= 4:
            print("Regular")
        else:
            print("Desaprobado")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------

print("\033[H\033[J")          # Limpiamos la pantalla

alumno1=Alumno()               # Creamos el objeto
alumno1.inicializar("Diego",2) # Le damos 2 atributos (nombre y nota)
alumno1.imprimir()             # Imprimimos los datos
alumno1.mostrar_estado()       # Vemos si está aprobado
print("-"*30)

alumno2=Alumno()
alumno2.inicializar("Ana",10)  # Creamos el segundo objeto
alumno2.imprimir()             # Imprimimos los datos
alumno2.mostrar_estado()       # Vemos si está aprobado
print("-"*30)

