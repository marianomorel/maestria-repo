# ------------------------------------------------------------
# Problema 6:
# Plantear una clase que administre dos listas de 5 nombres de
# alumnos y sus notas.Mostrar un menú de opciones que permita:
#
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa.
# ------------------------------------------------------------

class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def __del__(self):
        print('(Objeto eliminado de la memoria)')

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listar aprobados")
            print("4- Finalizar programa")
            print()
            opcion=int(input("Ingrese su opcion: "))
            print("-"*35)
            if opcion==1: self.cargar()
            elif opcion==2: self.listar()
            elif opcion==3: self.notas_altas()
            else: self.finalizar()


    def cargar(self):
        for x in range(5):
            nombre=input("Nombre del alumno: ")
            self.nombres.append(nombre)
            nota=int(input("Nota del alumno  : "))
            self.notas.append(nota)
        print("-"*35)

    def listar(self):
        print("Listado de alumnos:")
        print()
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("-"*35)

    def notas_altas(self):
        print("Listado de aprobados:")
        print()
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("-"*35)

    def finalizar(self):
        print("Programa finalizado!")
        print("-"*35)

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla
alumnos=Alumnos()
alumnos.menu()
