# ------------------------------------------------------------
# Ejemplo 9: Atributos de clases
# Definir una clase Cliente que almacene un código de cliente y
# un nombre. En la clase Cliente definir un atributo de clase
# de tipo lista que almacene todos los clientes que tienen
# suspendidas sus cuentas corrientes.
# Imprimir por pantalla todos los datos de clientes y el estado
# que se encuentra su cuenta corriente.
# ------------------------------------------------------------


class Cliente:
    # Variables de clase: Los atributos son independientes por cada
    # objeto o instancia de la clase, es decir si definimos tres
    # objetos de la clase Persona, todas las personas tienen un
    # atributo nombre pero cada uno tiene un valor independiente.
    # En algunas situaciones necesitamos almacenar datos que sean
    # compartidos por todos los objetos de dicha clase, en esas
    # situaciones debemos emplear atributos de clase. Para definir
    # un atributo de clase lo hacemos dentro de la clase pero
    # fuera de sus métodos:
    # https://pythones.net/variables-de-clases/

    suspendidos = []

    def __init__(self,codigo,nombre):
        self.codigo = codigo # Variable de Instancia
        self.nombre = nombre # Variable de Instancia

    def imprimir(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("Cliente Activo")
        print("-"*30)

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

cliente1 = Cliente(1,"Juan")
cliente2 = Cliente(2,"Ana")
cliente3 = Cliente(3,"Diego")
cliente4 = Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)