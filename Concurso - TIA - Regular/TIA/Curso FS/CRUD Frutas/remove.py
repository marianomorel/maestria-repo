#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################################################
# Aplicación que limpia los comentarios y eliminar las lineas en blanco. EXPERIMENTAL
# Realiza un backup del archivo antes de procesarlo. 
# No borra lineas que contengan comillas DESPUES del ultimo # (A MEJORAR)
# Borra a partir de la linea 10, para proteger encabezados como este.
#
# Iniciado el 25/05/2020           Finalizado el
###################################################################################################

# Importo librerias a utilizar ####################################################################
import sys
import argparse
import os
from datetime import date
from datetime import datetime

# Gestino argumentos de la linea de comandos. #####################################################
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Muestra el archivo generado", action="store_true")
parser.add_argument("-f", "--file",    help="Nombre de archivo a remover las lineas de comando")

args = parser.parse_args()


if args.file:  #Si no se pasa un nombre de archivo, salgo.
    # Aquí procesamos lo que se tiene que hacer con cada argumento    
    now = datetime.now()   #Genero el nombre del archivo de backup a partir de la fecha y hora del sistema.
    archivo_back = args.file+"_BACK_" + format(now.day)+"-"+format(now.month)+"-"+format(now.year)+"__"+format(now.hour)+"-"+format(now.minute)+"-"+format(now.second)
    
    # Renombro archivos antes de comenzar
    archivo_in   = args.file
    os.rename(args.file, archivo_back)

    # Si corresponde, muestro los nombres de los archivos.
    if args.verbose:
        print ("*** Limpiando comentarios del archivo fuente.\n")
        print ("El nombre de archivo a procesar es: ", args.file)
        print ("El nombre de archivo de backup es : ", archivo_back)
        print ("\n\n")

    # Abro los archivos de trabajo, como lectura uno, escritura el otro
    code = open(archivo_back,"r")
    code_back = open(args.file,"w")

    j = 0 #Esta variable cuenta las lineas procesadas
    for  i,linea in enumerate(code):
        lineaActual = linea            #Copio la linea para editarla
        j = j+1
        
        if j>10:                       #Solo procesa si la linea es mayor a 10 
            if len(linea) >1:          #Solo procesa si la linea NO ESTA en blanco....   
                numeral = lineaActual.find("#")    #Busco posicion del comentario
                comilla = lineaActual.rfind("\"")   #Busco posicion de las comillas desde el final de la linea

                # Veo si el comentario es el primer caracter de la linea
                aux = lineaActual.strip()

                if  aux.find("#") != 0:  #si no es cero, no es una linea de comentario completa
                    #La linea debe ser copiada, solo hasta el eventual comentario final.
                    numeral = lineaActual.rfind("#")    #Busco posicion del comentario desde la derecha
                    if numeral > comilla: #Si hay comentario al final, lo borro.
                        code_back.write(lineaActual[0:numeral]+"\n")
                        if args.verbose:
                            print (lineaActual[0:numeral])
                    else: #Copio la linea completa si no tiene comentario    
                        code_back.write(lineaActual)
                        if args.verbose:
                            print (lineaActual)
                                        

        else:   #Primeras lineas, o las copio.
            code_back.write(lineaActual)
            if args.verbose:
                print (lineaActual)

  
