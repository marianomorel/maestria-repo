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
# Guardo datos en la hoja "Productos"
#---------------------------------------------------------------------------------------
sql = "select * from productos;"

count = cursor.execute(sql)
cursor.scroll(0, mode='relative')

result = cursor.fetchall()
fields = cursor.description

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Productos', cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0,field, fields[field][0])

row = 1
col = 0

for row in range (1, len(result)+1):
    for col in range (0, len(fields)):
        sheet.write(row, col, u'%s'%result[row-1][col])

#---------------------------------------------------------------------------------------
# Guardo datos en la hoja "Categorias"
#---------------------------------------------------------------------------------------
sql = "select * from categorias;"

count = cursor.execute(sql)
cursor.scroll(0, mode='relative')

result = cursor.fetchall()
fields = cursor.description

sheet = workbook.add_sheet('Categorias', cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0,field, fields[field][0])

row = 1
col = 0

for row in range (1, len(result)+1):
    for col in range (0, len(fields)):
        sheet.write(row, col, u'%s'%result[row-1][col])

#---------------------------------------------------------------------------------------
# Guardo datos en la hoja "Subcategorias"
#---------------------------------------------------------------------------------------
sql = "select * from subcategorias;"

count = cursor.execute(sql)
cursor.scroll(0, mode='relative')

result = cursor.fetchall()
fields = cursor.description

sheet = workbook.add_sheet('Subategorias', cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0,field, fields[field][0])

row = 1
col = 0

for row in range (1, len(result)+1):
    for col in range (0, len(fields)):
        sheet.write(row, col, u'%s'%result[row-1][col])



#---------------------------------------------------------------------------------------
# Guardo datos en la hoja "Proveedores"
#---------------------------------------------------------------------------------------
sql = "select * from proveedores;"

count = cursor.execute(sql)
cursor.scroll(0, mode='relative')

result = cursor.fetchall()
fields = cursor.description

sheet = workbook.add_sheet('Proveedores', cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0,field, fields[field][0])

row = 1
col = 0

for row in range (1, len(result)+1):
    for col in range (0, len(fields)):
        sheet.write(row, col, u'%s'%result[row-1][col])


#---------------------------------------------------------------------------------------
# Guardo datos en la hoja "usuarios"
#---------------------------------------------------------------------------------------
sql = "select * from usuarios;"

count = cursor.execute(sql)
cursor.scroll(0, mode='relative')

result = cursor.fetchall()
fields = cursor.description

sheet = workbook.add_sheet('Usuarios', cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0,field, fields[field][0])

row = 1
col = 0

for row in range (1, len(result)+1):
    for col in range (0, len(fields)):
        sheet.write(row, col, u'%s'%result[row-1][col])






#---------------------------------------------------------------------------------------
#  Guardo el libro completo, con la fecha y hora en su nombre
#---------------------------------------------------------------------------------------
date = str(datetime.now())
workbook.save('copia_datos_'+date+'.xls')
