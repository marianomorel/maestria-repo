import xlwt
import pymysql
import sys
from datetime import datetime

#---------------------------------------------------------------------------------------
# Conexion con la base de datos
#---------------------------------------------------------------------------------------
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'casa_paez', 
    charset = 'utf8')

cursor = conn.cursor()

#---------------------------------------------------------------------------------------
# Funcion que guarda los datos de la tabla Nombre en la hoja "Nombre"
#---------------------------------------------------------------------------------------
def saveSheet(nombre):
    sql = "select * from "+nombre+";"

    count = cursor.execute(sql)
    cursor.scroll(0, mode='relative')

    result = cursor.fetchall()
    fields = cursor.description

    sheet = workbook.add_sheet(nombre.capitalize() , cell_overwrite_ok=True)

    for field in range(0, len(fields)):
        sheet.write(0,field, fields[field][0])

    row = 1
    col = 0

    for row in range (1, len(result)+1):
        for col in range (0, len(fields)):
            sheet.write(row, col, u'%s'%result[row-1][col])

#---------------------------------------------------------------------------------------
# Preparo los datos de cada tabla en el libro.
#---------------------------------------------------------------------------------------
workbook = xlwt.Workbook()
saveSheet("productos")
saveSheet("categorias")
saveSheet("subcategorias")
saveSheet("proveedores")
saveSheet("usuarios")


#---------------------------------------------------------------------------------------
#  Guardo el libro completo, con la fecha y hora en su nombre
#---------------------------------------------------------------------------------------
date = str(datetime.now())
workbook.save('copia_datos_'+date+'.xls')
