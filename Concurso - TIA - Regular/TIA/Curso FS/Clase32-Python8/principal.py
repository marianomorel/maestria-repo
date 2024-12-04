#--------------------------------------------------------------------
# Este es mi módulo principal.
#--------------------------------------------------------------------

# Importo funciones desde el paquete utilidades:
from utilidades import impuestos
from utilidades import calculos

# Las dos lineas anteriores se pueden cambiar por esta:
# from utilidades import impuestos, calculos
# o por esta:
# from utilidades import *

# Importando de esta manera, no necesito nombrar el módulo
# al usar la función
from utilidades.cadenas import invierte_cadena

# Importando de esta manera, no necesito nombrar el módulo
# al usar la función  y puedo cambiar su nombre
from utilidades.cadenas import hola_mundo as hola

monto = int(input("Introduzca un monto entero: "))

# Llama función definida en el módulo "impuestos"
print ("El impuesto IVA de 21%:", impuestos.impuesto_iva21(monto))

numero = int(input("Introduzca un monto entero a sumar: "))

# Llam a funciones definida en el módulo "calculos"
print ("Si sumo 20 el resultado es:", calculos.sumar_20(numero))
print ("Si a 20 resto", numero,", el resultado es:", calculos.restar_20(numero))

print(invierte_cadena("Hola Mundo!"))
print(hola())