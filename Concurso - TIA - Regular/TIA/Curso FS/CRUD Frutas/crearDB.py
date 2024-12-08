# Importo la libreria para acceder a mysql
import mysql.connector

nombre_DB   = "casa_paez"

nombre_TBL1 = "usuarios"
nombre_TBL2 = "proveedores"
nombre_TBL3 = "categorias"
nombre_TBL4 = "subcategorias"
nombre_TBL5 = "productos"

# Primero debo  conectarme a la base de datos:
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)

#---------------------------------------------------------------------------------------
# Veo si la base de datos existe. Si no existe, la creo:
#---------------------------------------------------------------------------------------
try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE "+nombre_DB)
    print("La base de datos "+nombre_DB+" se creó correctamente.")
except:
    print("La base de datos "+nombre_DB+" estaba presente.")


#---------------------------------------------------------------------------------------
# Si no existen las tablas, las creo dentro de la base de datos.
#---------------------------------------------------------------------------------------

# Tabla de usuarios
try:
    mycursor.execute("USE "+nombre_DB)
    mycursor = mydb.cursor()

    sql = "CREATE TABLE `"+nombre_DB+"`.`"+nombre_TBL1+"` ( " +\
            "`usu_name`     VARCHAR(32) PRIMARY KEY,"                     +\
            "`usu_pass`     VARCHAR(16));"
    mycursor.execute(sql)
    print("La tabla "+nombre_TBL1+" se creó correctamente.")
except:
    print("La tabla "+nombre_TBL1+" NO pudo crearse.")


# Tabla de proveedores
try:
    mycursor.execute("USE "+nombre_DB)
    mycursor = mydb.cursor()

    sql = "CREATE TABLE `"+nombre_DB+"`.`"+nombre_TBL2+"` ( " +\
            "`ven_id`       INT(10) NOT NULL AUTO_INCREMENT," +\
            "`ven_name`     VARCHAR(64) NOT NULL,"            +\
            "`ven_desc`     VARCHAR(255) NOT NULL,"           +\
            "`ven_direc`    VARCHAR(64),"                     +\
            "`ven_loca`     VARCHAR(64),"                     +\
            "`ven_telef`    VARCHAR(32),"                     +\
            "`ven_telec`    VARCHAR(32),"                     +\
            "`ven_email`    VARCHAR(64),"                     +\
            "`ven_cbu`      VARCHAR(22),"                     +\
            "`ven_contacto` VARCHAR(64),"                     +\
            "PRIMARY KEY (`ven_id`));"
    mycursor.execute(sql)
    print("La tabla "+nombre_TBL2+" se creó correctamente.")
except:
    print("La tabla "+nombre_TBL2+" NO pudo crearse.")


# Tabla de categorias
try:
    mycursor.execute("USE "+nombre_DB)
    mycursor = mydb.cursor()

    sql = "CREATE TABLE `"+nombre_DB+"`.`"+nombre_TBL3+"` ( " +\
            "`cat_id`    INT(10) NOT NULL AUTO_INCREMENT,"    +\
            "`cat_name`  VARCHAR(64) NOT NULL,"               +\
            "`cat_desc`  VARCHAR(255) NOT NULL,"              +\
            "PRIMARY KEY (`cat_id`));"
    mycursor.execute(sql)
    print("La tabla "+nombre_TBL3+" se creó correctamente.")
except:
    print("La tabla "+nombre_TBL3+" NO pudo crearse.")


# Tabla de subcategorias
try:
    mycursor.execute("USE "+nombre_DB)
    mycursor = mydb.cursor()

    sql = "CREATE TABLE `"+nombre_DB+"`.`"+nombre_TBL4+"` ( " +\
            "`sub_id`    INT(10) NOT NULL AUTO_INCREMENT,"    +\
            "`sub_name`  VARCHAR(64) NOT NULL,"               +\
            "`sub_desc`  VARCHAR(255) NOT NULL,"              +\
            "PRIMARY KEY (`sub_id`));"
    mycursor.execute(sql)
    print("La tabla "+nombre_TBL4+" se creó correctamente.")
except:
    print("La tabla "+nombre_TBL4+" NO pudo crearse.")


# Tabla de productos
try:
    mycursor.execute("USE "+nombre_DB)
    mycursor = mydb.cursor()

    sql = "CREATE TABLE `"+nombre_DB+"`.`"+nombre_TBL5+"` ( "     +\
            "`pro_id`           INT(10) NOT NULL AUTO_INCREMENT," +\
            "`pro_cat_id`       INT(10),"                         +\
            "`pro_sub_id`       INT(10),"                         +\
            "`pro_ven_id`       INT(10),"                         +\
            "`pro_descrip`      VARCHAR(256) NOT NULL,"           +\
            "`pro_buy_value`    FLOAT(10,2),"                     +\
            "`pro_buy_date`     DATE,"                            +\
            "`pro_margin1`      FLOAT( 5,2),"                     +\
            "`pro_sale_value1`  FLOAT(10,2),"                     +\
            "`pro_margin2`      FLOAT( 5,2),"                     +\
            "`pro_sale_value2`  FLOAT(10,2),"                     +\
            "`pro_margin3`      FLOAT( 5,2),"                     +\
            "`pro_sale_value3`  FLOAT(10,2),"                     +\
            "`pro_update_date`  DATE,"                            +\
            "`pro_stock`        INT(12),"                         +\
            "`pro_codigo`       VARCHAR(12),"                     +\
            "PRIMARY KEY (`pro_id`));"
    mycursor.execute(sql)
    print("La tabla "+nombre_TBL5+" se creó correctamente.")
except:
    print("La tabla "+nombre_TBL5+" NO pudo crearse.")


mydb.commit()   # Debería cerrar la conexión
