# ------------------------------------------------------------
# Encapsulacion:
# encapsular consiste en hacer que los atributos o métodos
# internos a una clase no se puedan acceder ni modificar desde
# fuera, sino que tan solo el propio objeto pueda acceder a ellos.
# ------------------------------------------------------------

# Creamos la clase "Coche":
class Coche:
	# Metodo constructor (Estado inicial)
    def __init__(self):
        self.__ruedas      = 4       # Encapsulamos el atributo
        self.__largoChasis = 280     # Encapsulamos el atributo
        self.__anchoChasis = 145     # Encapsulamos el atributo
        self.__en_marcha   = False   # Encapsulamos el atributo

   # Metodos --------------------------------
    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        # Compruebo que todo esté ok en el coche.
        if self.__en_marcha:
            chequeo = self.__chequeo_interno()

        if self.__en_marcha and chequeo:
            return "EN MARCHA"
        elif self.__en_marcha and not chequeo:
            return "ALGO HA FALLADO EN EL CHEQUEO. NO ARRANCAMOS."
        else:
            return "PARADO"

    # Método que comprueba el "estado interno" del coche
    # Está encapsulado (privado)
    def __chequeo_interno(self):
        print("Comprobando el coche.")
        self.gasolina = "Ok"
        self.combustible = "Ok"
        self.puertas = "Cerradas"
        if self.gasolina == "Ok" and self.combustible == "Ok" and self.puertas == "Cerradas":
            return True
        else:
            return False

    def caracteristicas(self): # Método para mostrar datos del objeto
        print("El coche tiene: " + str(self.__ruedas) + " ruedas")
        print("El coche tiene: " + str(self.__largoChasis) + " de largo")
        print("El coche tiene: " + str(self.__anchoChasis) + " de ancho")



# ------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

coche1 = Coche()   
print(coche1.arrancar(True))
print(coche1.arrancar(False))
print(coche1.arrancar(True))

#print(coche1.ruedas)              # Esto no se permite mas porque es un atributo privado
#coche1.ruedas = 6                 # Esto no se permite mas porque es un atributo privado
#print(coche1.ruedas)              # Esto no se permite mas porque es un atributo privado

#print(coche1.chequeo_interno())   # Esto no se permite mas porque es un atributo privado

