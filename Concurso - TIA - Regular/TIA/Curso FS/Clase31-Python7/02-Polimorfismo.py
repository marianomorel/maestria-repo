# ------------------------------------------------------------
#Creamos una clase "Pato"
# ------------------------------------------------------------
class Pato:
    def hablar(self):
        print("¡Cuac! "*3)

# ------------------------------------------------------------
#Creamos una clase "Perro"
# ------------------------------------------------------------
class Perro:
    def hablar(self):
        print("!Guau! "*3)

# ------------------------------------------------------------
#Creamos una clase "Cerdo"
# ------------------------------------------------------------
class Cerdo:
    def hablar(self):
        print("!Oink! "*3)        

# ------------------------------------------------------------
# Función hacer_hablar (Ojo, no es parte de la clase)
# ------------------------------------------------------------
def hacer_hablar(x):
    x.hablar()

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

#Creamos un pato y lo hacemos "hablar:"
mi_pato = Pato()
hacer_hablar(mi_pato)
#Creamos un perro y lo hacemos "hablar:"
mi_perro = Perro()
mi_perro.hablar()
#Creamos un cerdo y lo hacemos "hablar:"
mi_cerdo = Cerdo()
mi_cerdo.hablar()

print()
# Pero todos pueden "hablar" mediante la funcion hacer_hablar()
hacer_hablar(mi_pato)
hacer_hablar(mi_perro)
hacer_hablar(mi_cerdo)

