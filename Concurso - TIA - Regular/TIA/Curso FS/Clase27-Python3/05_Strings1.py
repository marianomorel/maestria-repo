# ------------------------------------------------------------
# PYTHON 1 - Fundamentos del lenguaje
# 5) Tipos de datos - Strings
# ------------------------------------------------------------

# ------------------------------------------------------------
# Ejemplo 1
# ------------------------------------------------------------
mensaje = "Hola Mundo"
print(mensaje)

# ------------------------------------------------------------
# Ejemplo 2
# ------------------------------------------------------------
mensaje1 = "Hola" + " " + "Mundo"
print(mensaje1)

# ------------------------------------------------------------
# Ejemplo 3
# ------------------------------------------------------------
mensaje3 = "Hola " * 3 + "Mundo"
print(mensaje3)

# ------------------------------------------------------------
# Ejemplo 4
# ------------------------------------------------------------
mensaje4 =  "Hola"
mensaje4 += " "
mensaje4 += "Mundo"
print(mensaje4)


print(len(mensaje4))

# ------------------------------------------------------------
# Ejemplo 5
# ------------------------------------------------------------
# Podemos acceder en forma individual a cada 
# caracter del string mediante un subíndice:
# ------------------------------------------------------------
nombre = "Juan Perez"
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])

print(nombre[-1])
print(nombre[5:6])

#print(nombre[14]) #Ojo, rompe!
#print(nombre[-14]) #Ojo, rompe!
print(nombre[4:140]) # NOrompe!

# ------------------------------------------------------------
# Ejemplo 6
# ------------------------------------------------------------
numero = 12
color = "verde"
print("El color es: " + color + " y el número es: " + str(numero))
print( f"El color es: {color} y el número es: {numero}")


# ------------------------------------------------------------
# Ejemplo 7
# ------------------------------------------------------------
numero = 12
color = "verde"
print("El color es: " + color + "\n y el número es: " + str(numero))

#Estos son los comandos \ disponibles:
# ------------------------------------------------------------
# Secuencia Escape	Significado
# \newline      	Ignorado
# \\	            Backslash (\)
# \'	            Comillas simple (')
# \"            	Comillas doble (")
# \a	            Bell ASCII (BEL)
# \b            	Backspace ASCII (BS)
# \f	            Formfeed ASCII (FF)
# \n	            Linefeed ASCII (LF)
# \N{name}	        Carácter llamado name en base de datos Unicode (Solo Unicode)
# \r	            Carriage Return ASCII (CR)
# \t	            Tabulación Horizontal ASCII (TAB)
# \uxxxx	        Carácter con valor hex 16-bit xxxx (Solamente Unicode). Ver hex.
# \Uxxxxxxxx    	Carácter con valor hex 32-bit xxxxxxxx (Solamente Unicode). Ver hex.
# \v	            Tabulación Vertical ASCII (VT)
# \ooo             	Carácter con valor octal ooo. Ver octal.
# \xhh          	Carácter con valor hex hh. Ver hex.
# ------------------------------------------------------------

print('El \'color\' es: ' + color + '\n y el \'número\' es: ' + str(numero))
print("a \t \t \t otros \t espacios")
print("a \t c \t varios \t espacios")

# ------------------------------------------------------------
# Ejemplo 8
# ------------------------------------------------------------
print( "C:\nombre\Juan\Desktop\Python\Python1\05_Strings1.py" )
print( r"C:\nombre\Juan\Desktop\Python\Python1\05_Strings1.py" ) #Raw String
color = "verde"
print( rf"El \numero\ es color: {color}" )


# ------------------------------------------------------------
# Ejemplo 9
# ------------------------------------------------------------
cadena = "Hola Mundo"
print (cadena)
print (cadena.lower())
print (cadena.upper())
print (cadena.capitalize())

