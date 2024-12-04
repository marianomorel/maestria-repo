# ------------------------------------------------------------
# Ejmeplo 7: Colaboración de clases
# Un banco tiene 3 clientes que pueden hacer depósitos y 
# extracciones. 
# El banco necesita obtener, al final del día, un reporte 
# de la cantidad de dinero que sus clientes han depositado.
# ------------------------------------------------------------

# ------------------------- Clase Cliente --------------------
class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self,monto):
        self.monto += monto

    def extraer(self,monto):
        self.monto -= monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(f"{self.nombre} tiene depositada la suma de {self.monto}")

# ------------------------- Clase Banco --------------------
class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + \
                self.cliente2.retornar_monto() + \
                self.cliente3.retornar_monto()
        print(f"El total de dinero en el banco es: {total}")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

banco1 = Banco() # Instanciamos un objeto Banco
banco1.operar()  # Realizamos las operaciones
banco1.depositos_totales() # Consultamos el estado

# Por supuesto, podemos utilizar instancias de la clase
# Cliente desde fuera de Banco!
cliente1 = Cliente("Alberto")
cliente1.depositar(100)
cliente1.extraer(10)
print(cliente1.retornar_monto())
