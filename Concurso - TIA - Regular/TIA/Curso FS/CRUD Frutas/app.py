#---------------------------------------------------------------------------------------
# CRUD
# Iniciado el 11/08/2021
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
# Importo las librerias
#---------------------------------------------------------------------------------------
import socket
from datetime import datetime, time
import xlwt                 # Solo para exporar datos - Escribir en XLS
import pymysql              # Solo para exporar datos - Acceso a la DB
import sys                  # Solo para exporar datos - Manejo de files

# Importo las librerias propias de Flask
from flask import send_from_directory  # Acceso a las carpetas
from flask import (Flask, app, flash, redirect, render_template, request, url_for)
from flaskext.mysql import MySQL


# Importo las librerias relaciondas con la gestion de los archivos PDF
from reportlab.lib.enums       import TA_JUSTIFY,  TA_LEFT, TA_CENTER , TA_RIGHT
from reportlab.lib.pagesizes   import letter
from reportlab.platypus        import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus        import Table, TableStyle, PageBreak
from reportlab.lib.styles      import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units       import inch
from reportlab.lib             import utils
from reportlab.pdfbase         import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Esta bandera indica si el usuario está logueado correctamente.
validacion = False   # Asumo que el usuario NO está validado
usuario    = ""      # Nombre del usuario (No usado por ahora)

#---------------------------------------------------------------------------------------
# Conexion con la base de datos
#---------------------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key="123Prueba!"
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']     = 'localhost'
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB']       = 'casa_paez'
app.config['MYSQL_DATABASE_TABLE']    = 'paez'
mysql.init_app(app)


#---------------------------------------------------------------------------------------
#  Pantalla de Login
#---------------------------------------------------------------------------------------
@app.route("/")
def index():
    global validacion
    validacion=False
    return render_template("paez/index.html")

#---------------------------------------------------------------------------------------
#  Verifica que el usuario esté validado.
#---------------------------------------------------------------------------------------
@app.route('/ingresar', methods=['POST'])
def ingresar():
    _usuario  = request.form["txtUsuario"]
    _password = request.form["txtPassword"]
    sql     = "SELECT * FROM `usuarios` WHERE `usu_name` LIKE %s"
    conn    = mysql.connect()
    cursor  = conn.cursor()
    cursor.execute(sql,_usuario)
    global usuario
    usuario = cursor.fetchall()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if usuario!=() and _password==usuario[0][1]:
        global validacion
        validacion=True
        return redirect("inicio")
    else:
        return render_template("paez/index.html")

#---------------------------------------------------------------------------------------
#  Menu principal
#---------------------------------------------------------------------------------------
@app.route('/inicio')
def inicio():
     # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/inicio.html")
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado tipo, de prueba. Enlaza con listado.html
#---------------------------------------------------------------------------------------
@app.route('/listado')
def listado():
    sql = "SELECT * FROM `productos` ORDER BY pro_descrip;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    productos=cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado.html", productos=productos)
    else:
        return redirect('/')



#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona la configuracion del listado de precios ALFABETICO
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_x")
def listado_pro_x():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_x.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
@app.route('/listado_precios', methods=['POST'])
def listado_precios():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id = request.form['txtPro_Ven_Id']
        Pro_Cat_Id = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id = request.form["txtPro_Sub_Id"]

        Pro_Ven_Idx = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Idx = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Idx = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )

        str1 = "pro_ven_id IS NOT NULL"
        str2 = "pro_cat_id IS NOT NULL"
        str3 = "pro_sub_id IS NOT NULL"

        if Pro_Ven_Idx != 0:
            str1 = "pro_ven_id LIKE "+str(Pro_Ven_Idx)
        if Pro_Cat_Idx != 0:
            str2 = "pro_cat_id LIKE "+str(Pro_Cat_Idx)
        if Pro_Sub_Idx != 0:
            str3 = "pro_sub_id LIKE "+str(Pro_Sub_Idx)

        sql = "SELECT * FROM `productos` WHERE "+str1+" AND "+str2+" AND "+str3+" ORDER BY pro_descrip;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_precios.html", productos=productos, ven=Pro_Ven_Id, cat=Pro_Cat_Id, sub=Pro_Sub_Id)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona la configuracion del listado de precios (por ID)
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_x2")
def listado_pro_x2():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_x2.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
@app.route('/listado_precios2', methods=['POST'])
def listado_precios2():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id = request.form['txtPro_Ven_Id']
        Pro_Cat_Id = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id = request.form["txtPro_Sub_Id"]

        Pro_Ven_Idx = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Idx = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Idx = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )

        str1 = "pro_ven_id IS NOT NULL"
        str2 = "pro_cat_id IS NOT NULL"
        str3 = "pro_sub_id IS NOT NULL"

        if Pro_Ven_Idx != 0:
            str1 = "pro_ven_id LIKE "+str(Pro_Ven_Idx)
        if Pro_Cat_Idx != 0:
            str2 = "pro_cat_id LIKE "+str(Pro_Cat_Idx)
        if Pro_Sub_Idx != 0:
            str3 = "pro_sub_id LIKE "+str(Pro_Sub_Idx)

        sql = "SELECT * FROM `productos` WHERE "+str1+" AND "+str2+" AND "+str3+" ORDER BY pro_id;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_precios2.html", productos=productos, ven=Pro_Ven_Id, cat=Pro_Cat_Id, sub=Pro_Sub_Id)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
#  Listado de productos para edicion
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona la configuracion del listado de precios....
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_y")
def listado_pro_y():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_y.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
@app.route('/listado_prod_ed', methods=['POST'])
def listado_prod_ed():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id = request.form['txtPro_Ven_Id']
        Pro_Cat_Id = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id = request.form["txtPro_Sub_Id"]

        Pro_Ven_Idx = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Idx = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Idx = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )

        str1 = "pro_ven_id IS NOT NULL"
        str2 = "pro_cat_id IS NOT NULL"
        str3 = "pro_sub_id IS NOT NULL"

        if Pro_Ven_Idx != 0:
            str1 = "pro_ven_id LIKE "+str(Pro_Ven_Idx)
        if Pro_Cat_Idx != 0:
            str2 = "pro_cat_id LIKE "+str(Pro_Cat_Idx)
        if Pro_Sub_Idx != 0:
            str3 = "pro_sub_id LIKE "+str(Pro_Sub_Idx)

        sql = "SELECT * FROM `productos` WHERE "+str1+" AND "+str2+" AND "+str3+" ORDER BY pro_descrip;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_prod_ed.html", productos=productos, ven=Pro_Ven_Id, cat=Pro_Cat_Id, sub=Pro_Sub_Id)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
@app.route('/consulta_pro_id')
def consulta_pro_id():
    if validacion:
        return render_template("paez/consulta_pro_id.html")
    else:
        return redirect('/')
#---------------------------------------------------------------------------------------
@app.route('/listado_prod_ed_id', methods=['POST'])
def listado_prod_ed_id():
    if validacion:
        # Recupero los valores del formulario
        Pro_Id = int(request.form['txtPro_Id'])

        if Pro_Id != 0:
            str1 = "pro_id LIKE "+str(Pro_Id)

        sql = "SELECT * FROM `productos` WHERE pro_id LIKE "+ str(Pro_Id) + " ORDER BY pro_id;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_prod_modif.html", productos=productos)
    else:
        return redirect('/')



#---------------------------------------------------------------------------------------
@app.route('/consulta_pro_codigo')
def consulta_pro_codigo():
    if validacion:
        return render_template("paez/consulta_pro_codigo.html")
    else:
        return redirect('/')
#---------------------------------------------------------------------------------------
@app.route('/listado_prod_ed_cod', methods=['POST'])
def listado_prod_ed_cod():
    if validacion:
        # Recupero los valores del formulario
        Pro_Codigo = request.form['txtPro_Codigo']

        sql = "SELECT * FROM `productos` WHERE pro_codigo LIKE "+ str(Pro_Codigo) + " ORDER BY pro_codigo;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_prod_modif.html", productos=productos)
    else:
        return redirect('/')



#---------------------------------------------------------------------------------------
@app.route('/consulta_pro_descrip')
def consulta_pro_descrip():
    if validacion:
        return render_template("paez/consulta_pro_descrip.html")
    else:
        return redirect('/')
#---------------------------------------------------------------------------------------
@app.route('/listado_prod_ed_descrip', methods=['POST'])
def listado_prod_ed_descrip():
    if validacion:
        # Recupero los valores del formulario
        Pro_Descrip = request.form['txtPro_Descrip']

        sql = "SELECT * FROM `productos` WHERE pro_descrip LIKE '%"+ str(Pro_Descrip) + "%' ORDER BY pro_descrip;"
        print (sql)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_prod_modif.html", productos=productos)
    else:
        return redirect('/')




#---------------------------------------------------------------------------------------
#  Listado de productos para edicion DE PRECIOS EN GRUPO
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona el grupo a editar.
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_z")
def listado_pro_z():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_z.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
@app.route('/listado_prod_precios', methods=['POST'])
# Ojo...llamo a "listado_prod_precios", pero se renderiza la misma página de edicion (listado_prod_ed.html)
def listado_prod_precios():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id    = request.form['txtPro_Ven_Id']
        Pro_Cat_Id    = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id    = request.form["txtPro_Sub_Id"]
        Pro_Aumento   = request.form["txt_Aumento"]
        Pro_Descuento = request.form["txt_Descuento"]

        Pro_Ven_Idx = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Idx = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Idx = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )

        str1 = "pro_ven_id IS NOT NULL"
        str2 = "pro_cat_id IS NOT NULL"
        str3 = "pro_sub_id IS NOT NULL"

        try:
            Aumento = float(Pro_Aumento)
        except:
            Aumento = 0

        try:
            Descuento = float(Pro_Descuento)
        except:
            Descuento = 0

        porciento = str(1 + ((Aumento - Descuento)/100 ))

        if Pro_Ven_Idx != 0:
            str1 = "pro_ven_id LIKE "+str(Pro_Ven_Idx)
        if Pro_Cat_Idx != 0:
            str2 = "pro_cat_id LIKE "+str(Pro_Cat_Idx)
        if Pro_Sub_Idx != 0:
            str3 = "pro_sub_id LIKE "+str(Pro_Sub_Idx)

        actualizado = str(datetime.now() )


        datos = (
                porciento,
                actualizado
                )
        #UPDATE Persona SET Telefono='4553999' WHERE Nombre='Juan' OR Nombre='Pablo' OR Nombre='María';

        # Actualizo los registros seleccionados ----------------------------------------------------------------
        sql = "UPDATE `productos` SET  pro_buy_value = pro_buy_value * %s, pro_sale_value1 = pro_buy_value * (1+pro_margin1/100),pro_sale_value2 = pro_buy_value * (1+pro_margin2/100),pro_sale_value3 = pro_buy_value * (1+pro_margin3/100), pro_update_date = %s WHERE "+str1+" AND "+str2+" AND "+str3+";"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        productos=cursor.fetchall()
        conn.commit()

        # Muestro la tabla actualizada---------------------------------------------------------------------------
        sql = "SELECT * FROM `productos` WHERE "+str1+" AND "+str2+" AND "+str3+" ORDER BY pro_descrip;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        productos=cursor.fetchall()
        conn.commit()


        return render_template("paez/listado_prod_ed.html", productos=productos, ven=Pro_Ven_Id, cat=Pro_Cat_Id, sub=Pro_Sub_Id)
    else:
        return redirect('/')






#---------------------------------------------------------------------------------------
#  Dar de alta Usuarios nuevos
#---------------------------------------------------------------------------------------
@app.route("/alta_usu")
def create_usu():
    if validacion:
        return render_template("paez/alta_usu.html")
    else:
        return redirect('/')

@app.route('/store_usu', methods=['POST'])
def storage_usu():
    if validacion:
        # Recupero los valores del formulario
        Usu_Name = request.form["txtUsu_Name"]
        Usu_Pass = request.form["txtUsu_Pass"]

        # Y los agrego a la base de datos:
        datos = (
        Usu_Name,
        Usu_Pass)

        sql = "INSERT INTO `usuarios` (`usu_name`, `usu_pass`) VALUES ( %s, %s);"

        conn   = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/alta_usu')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de usuarios (POR NOMBRE)
#---------------------------------------------------------------------------------------
@app.route('/listado_usu')
def listado_usu():
    sql      = "SELECT * FROM `usuarios` ORDER BY usu_name;"
    conn     = mysql.connect()
    cursor   = conn.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_usu.html", usuarios=usuarios)
    else:
        return redirect('/')




#---------------------------------------------------------------------------------------
#  Dar de alta Categorias
#---------------------------------------------------------------------------------------
@app.route("/alta_cat")
def create_cat():
    if validacion:
        return render_template("paez/alta_cat.html")
    else:
        return redirect('/')


@app.route('/store_cat', methods=['POST'])
def storage_cat():
    if validacion:
        # Recupero los valores del formulario
        Cat_Name = request.form["txtCat_Name"]
        Cat_Desc = request.form["txtCat_Desc"]

        # Y los agrego a la base de datos:
        datos = (
        Cat_Name,
        Cat_Desc)


        sql = "INSERT INTO `categorias` (`cat_id`, `cat_name`, `cat_desc`) VALUES (NULL, %s, %s);"

        conn   = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/alta_cat')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de categorias (POR NOMBRE) Para editar
#---------------------------------------------------------------------------------------
@app.route('/listado_cat_ed')
def listado_cat_ed():
    sql         = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    categorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_cat_ed.html", categorias=categorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de categorias (POR NOMBRE)
#---------------------------------------------------------------------------------------
@app.route('/listado_cat')
def listado_cat():
    sql         = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    categorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_cat.html", categorias=categorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de categorias (POR CODIGO)
#---------------------------------------------------------------------------------------
@app.route('/listado_cat1')
def listado_cat1():
    sql         = "SELECT * FROM `categorias` ORDER BY cat_id;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    categorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_cat1.html", categorias=categorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Modificar datos de categorias
#---------------------------------------------------------------------------------------
@app.route('/edit_cat/<int:id>')    # Recibe como parámetro el id del registro
def edit_cat(id):
    if validacion:
        conn      = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor    = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `categorias` WHERE cat_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        categorias = cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión

        return render_template('paez/edit_cat.html', categorias=categorias)
    else:
        return redirect('/')

@app.route('/update_cat', methods=['POST'])
def update_cat():
    if validacion:
        # Recupero los valores del formulario
        id        = request.form['txtCat_Id']
        Cat_Name  = request.form["txtCat_Name"]
        Cat_Desc  = request.form["txtCat_Desc"]


        # Muestro los valores por la consola
        print(id)
        print(Cat_Name)
        print(Cat_Desc)

        # Y modifico el registro en la base de datos:
        datos = (
            Cat_Name,
            Cat_Desc,
            id)

        sql = "UPDATE `categorias` SET  `cat_name`=%s, `cat_desc`=%s WHERE cat_id=%s;"

        conn   = mysql.connect() # Se conecta a la conexión mysql
        cursor = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute(sql,datos)
        conn.commit()            # Cerramos la conexión

        sql         = "SELECT * FROM `categorias` ORDER BY cat_name;"
        conn        = mysql.connect()
        cursor      = conn.cursor()
        cursor.execute(sql)
        categorias = cursor.fetchall()
        conn.commit()

        return render_template("paez/listado_cat_ed.html", categorias=categorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Borrar una Categoria
#---------------------------------------------------------------------------------------
@app.route('/destroy_cat/<int:id>') #Recibe como parámetro el id del registro
def destroy_cat(id):
    if validacion:
        #Primero me aseguro que no haya productos con ese codigo de categoria
        sql       = "select * from `productos` WHERE pro_cat_id=%s"
        conn      = mysql.connect()
        cursor    = conn.cursor()
        registros = cursor.execute(sql, id)
        conn.commit()


        if registros == 0:   # Solo borro si no hay productos con ese ID
            conn   = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `categorias` WHERE cat_id=%s", (id))
            conn.commit()

        sql         = "SELECT * FROM `categorias` ORDER BY cat_name;"
        conn        = mysql.connect()
        cursor      = conn.cursor()
        cursor.execute(sql)
        categorias = cursor.fetchall()
        conn.commit()

        return render_template("paez/listado_cat_ed.html", categorias=categorias)

    else:
        return redirect('/')





#---------------------------------------------------------------------------------------
#  Dar de alta SUB Categorias
#---------------------------------------------------------------------------------------
@app.route("/alta_sub")
def create_sub():
    if validacion:
        return render_template("paez/alta_sub.html")
    else:
        return redirect('/')

@app.route('/store_sub', methods=['POST'])
def storage_sub():
    if validacion:
        # Recupero los valores del formulario
        Sub_Name = request.form["txtSub_Name"]
        Sub_Desc = request.form["txtSub_Desc"]

        # Y los agrego a la base de datos:
        datos = (
        Sub_Name,
        Sub_Desc)


        sql = "INSERT INTO `subcategorias` (`sub_id`, `sub_name`, `sub_desc`) VALUES (NULL, %s, %s);"

        conn   = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/alta_sub')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de subcategorias (POR NOMBRE) Para editar
#---------------------------------------------------------------------------------------
@app.route('/listado_sub_ed')
def listado_sub_ed():
    sql           = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn          = mysql.connect()
    cursor        = conn.cursor()
    cursor.execute(sql)
    subcategorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_sub_ed.html", subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de SUB Categorias (POR NOMBRE)
#---------------------------------------------------------------------------------------
@app.route('/listado_sub')
def listado_sub():
    sql         = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    subcategorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_sub.html", subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de SUB Categorias (POR CODIGO)
#---------------------------------------------------------------------------------------
@app.route('/listado_sub1')
def listado_sub1():
    sql         = "SELECT * FROM `subcategorias` ORDER BY sub_id;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    subcategorias = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_sub1.html", subcategorias=subcategorias)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Modificar datos de subcategorias
#---------------------------------------------------------------------------------------
@app.route('/edit_sub/<int:id>')    # Recibe como parámetro el id del registro
def edit_sub(id):
    if validacion:
        conn      = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor    = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `subcategorias` WHERE sub_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        subcategorias = cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión

        return render_template('paez/edit_sub.html', subcategorias=subcategorias)
    else:
        return redirect('/')

@app.route('/update_sub', methods=['POST'])
def update_sub():
    if validacion:
        # Recupero los valores del formulario
        id        = request.form['txtSub_Id']
        Sub_Name  = request.form["txtSub_Name"]
        Sub_Desc  = request.form["txtSub_Desc"]

        # Y modifico el registro en la base de datos:
        datos = (
            Sub_Name,
            Sub_Desc,
            id)

        sql = "UPDATE `subcategorias` SET  `sub_name`=%s, `sub_desc`=%s WHERE sub_id=%s;"

        conn   = mysql.connect() # Se conecta a la conexión mysql
        cursor = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute(sql,datos)
        conn.commit()            # Cerramos la conexión
        return redirect('/listado_sub_ed')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Borrar una subcategoria
#---------------------------------------------------------------------------------------
@app.route('/destroy_sub/<int:id>') #Recibe como parámetro el id del registro
def destroy_sub(id):
    if validacion:
        sql       = "select * from `productos` WHERE pro_sub_id=%s"
        conn      = mysql.connect()
        cursor    = conn.cursor()
        registros = cursor.execute(sql, id)
        conn.commit()

        if registros == 0:   # Solo borro si no hay productos con ese ID
            conn   = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `subcategorias` WHERE sub_id=%s", (id))
            conn.commit()

        sql         = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
        conn        = mysql.connect()
        cursor      = conn.cursor()
        cursor.execute(sql)
        subcategorias = cursor.fetchall()
        conn.commit()

        return render_template("paez/listado_sub_ed.html", subcategorias=subcategorias)
    else:
        return redirect('/')




#---------------------------------------------------------------------------------------
#  Dar de alta proveedores. Enlaza con alta_ven.html
#---------------------------------------------------------------------------------------
@app.route("/alta_ven")
def create_ven():
    if validacion:
        return render_template("paez/alta_ven.html")
    else:
        return redirect('/')

@app.route('/store_ven', methods=['POST'])
def storage_ven():
    if validacion:
        # Recupero los valores del formulario
        Ven_Name     = request.form["txtVen_Name"]
        Ven_Descrip  = request.form["txtVen_Descrip"]
        Ven_Direc    = request.form["txtVen_Direc"]
        Ven_Loca     = request.form["txtVen_Loca"]
        Ven_Telef    = request.form["txtVen_Telef"]
        Ven_Telec    = request.form["txtVen_Telec"]
        Ven_Email    = request.form["txtVen_Email"]
        Ven_CBU      = request.form["txtVen_CBU"]
        Ven_Contacto = request.form["txtVen_Contacto"]

        # Y los agrego a la base de datos:
        datos = (
        Ven_Name,
        Ven_Descrip,
        Ven_Direc,
        Ven_Loca,
        Ven_Telef,
        Ven_Telec,
        Ven_Email,
        Ven_CBU,
        Ven_Contacto
        )


        sql = "INSERT INTO `proveedores` (`ven_id`, `ven_name`, `ven_desc`, `ven_direc`, `ven_loca`, `ven_telef`, `ven_telec`, `ven_email`, `ven_cbu`, `ven_contacto`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/alta_ven')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de proveedores (POR NOMBRE)
#---------------------------------------------------------------------------------------
@app.route('/listado_ven_ed')
def listado_ven_ed():
    sql         = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    proveedores = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_ven_ed.html", proveedores=proveedores)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Listado de proveedores (POR CODIGO)
#---------------------------------------------------------------------------------------
@app.route('/listado_ven')
def listado_ven():
    sql         = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn        = mysql.connect()
    cursor      = conn.cursor()
    cursor.execute(sql)
    proveedores = cursor.fetchall()
    conn.commit()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        return render_template("paez/listado_ven.html", proveedores=proveedores)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Modificar datos de proveedores
#---------------------------------------------------------------------------------------
@app.route('/edit_ven/<int:id>')    # Recibe como parámetro el id del registro
def edit_ven(id):
    if validacion:
        conn        = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor      = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `proveedores` WHERE ven_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        proveedores = cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión

        return render_template('paez/edit_ven.html', proveedores=proveedores)
    else:
        return redirect('/')

@app.route('/update_ven', methods=['POST'])
def update_ven():
    if validacion:
        # Recupero los valores del formulario
        id           = request.form['txtVen_Id']
        Ven_Name     = request.form["txtVen_Name"]
        Ven_Desc     = request.form["txtVen_Desc"]
        Ven_Direc    = request.form["txtVen_Direc"]
        Ven_Loca     = request.form["txtVen_Loca"]
        Ven_Telef    = request.form["txtVen_Telef"]
        Ven_Telec    = request.form["txtVen_Telec"]
        Ven_Email    = request.form["txtVen_Email"]
        Ven_CBU      = request.form["txtVen_CBU"]
        Ven_Contacto = request.form["txtVen_Contacto"]

        # Y modifico el registro en la base de datos:
        datos = (
            Ven_Name,
            Ven_Desc,
            Ven_Direc,
            Ven_Loca,
            Ven_Telef,
            Ven_Telec,
            Ven_Email,
            Ven_CBU,
            Ven_Contacto,
            id)

        sql = "UPDATE `proveedores` SET  `ven_name`=%s, `ven_desc`=%s, `ven_direc`=%s, `ven_loca`=%s, `ven_telef`=%s, `ven_telec`=%s, `ven_email`=%s, `ven_cbu`=%s, `ven_contacto`=%s WHERE ven_id=%s;"

        conn   = mysql.connect() # Se conecta a la conexión mysql
        cursor = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute(sql,datos)
        conn.commit()            # Cerramos la conexión

        sql         = "SELECT * FROM `proveedores` ORDER BY ven_name;"
        conn        = mysql.connect()
        cursor      = conn.cursor()
        cursor.execute(sql)
        proveedores = cursor.fetchall()
        conn.commit()

        return render_template("paez/listado_ven_ed.html", proveedores=proveedores)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Consultar datos de proveedores - Busca los datos del proveedor y los envia al html
#  donde se muestran
#---------------------------------------------------------------------------------------
@app.route('/mostrar_ven/<int:id>')    # Recibe como parámetro el id del registro
def mostrar_ven(id):
    if validacion:
        conn      = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor    = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `proveedores` WHERE ven_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        proveedores = cursor.fetchall() #Traemos toda la información
        conn.commit()                   #Cerramos la conexión

        return render_template('paez/mostrar_ven.html', proveedores=proveedores)
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Borrar  un proveedor
#---------------------------------------------------------------------------------------
@app.route('/destroy_ven/<int:id>') #Recibe como parámetro el id del registro
def destroy_ven(id):
    if validacion:
        conn   = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `proveedores` WHERE ven_id=%s", (id))
        conn.commit()

        sql         = "SELECT * FROM `proveedores` ORDER BY ven_name;"
        conn        = mysql.connect()
        cursor      = conn.cursor()
        cursor.execute(sql)
        proveedores = cursor.fetchall()
        conn.commit()

        return render_template("paez/listado_ven_ed.html", proveedores=proveedores)
    else:
        return redirect('/')







#---------------------------------------------------------------------------------------
#  Dar de alta productos. Enlaza con alta_prod.html
#---------------------------------------------------------------------------------------
@app.route("/altaprod")
def create_prod():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/alta_prod.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')

@app.route('/store_pro', methods=['POST'])
def storage_pro():
    if validacion:
        # Recupero los valores del formulario
        Pro_Descrip   = request.form["txtPro_Descrip"]
        Pro_Cat_Id    = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id    = request.form["txtPro_Sub_Id"]
        Pro_Ven_Id    = request.form["txtPro_Ven_Id"]
        Pro_Codigo    = request.form["txtPro_Codigo"]
        Pro_Buy_Date  = request.form["txtPro_Buy_Date"]
        Pro_Buy_Value = request.form["txtPro_Buy_Value"]
        Pro_Margin1   = request.form["txtPro_Margin1"]
        Pro_Margin2   = request.form["txtPro_Margin2"]
        Pro_Margin3   = request.form["txtPro_Margin3"]
        Pro_Stock     = request.form["txtPro_Stock"]

        # Y les doy el formato adecuado para guardarlos en la base de datos.
        Pro_Ven_Id      = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Id      = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Id      = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )
        Pro_Codigo      = Pro_Codigo[0:11]
        try:
            Pro_Buy_Date    = datetime.strptime(Pro_Buy_Date, '%d/%m/%Y')
        except:
            Pro_Buy_Date = datetime.now()

        try:
            Pro_Buy_Value = float(Pro_Buy_Value)
        except:
            Pro_Buy_Value = 0

        try:
            Pro_Margin1 = float(Pro_Margin1)
        except:
            Pro_Margin1 = 0

        try:
            Pro_Margin2 = float(Pro_Margin2)
        except:
            Pro_Margin2 = 0

        try:
            Pro_Margin3 = float(Pro_Margin3)
        except:
            Pro_Margin3 = 0

        try:
            Pro_Stock = int(Pro_Stock)
        except:
            Pro_Stock = 0

        Pro_Sale_Value1 = Pro_Buy_Value * (1 + Pro_Margin1/100)
        Pro_Sale_Value2 = Pro_Buy_Value * (1 + Pro_Margin2/100)
        Pro_Sale_Value3 = Pro_Buy_Value * (1 + Pro_Margin3/100)
        Pro_Update_Date = datetime.now()

        # Y los agrego a la base de datos:
        datos = (
        Pro_Cat_Id,
        Pro_Sub_Id,
        Pro_Ven_Id,
        Pro_Descrip,
        Pro_Buy_Value,
        Pro_Buy_Date,
        Pro_Margin1,
        Pro_Sale_Value1,
        Pro_Margin2,
        Pro_Sale_Value2,
        Pro_Margin3,
        Pro_Sale_Value3,
        Pro_Update_Date,
        Pro_Stock,
        Pro_Codigo)


        sql = "INSERT INTO `productos` (`pro_id`, `pro_cat_id`, `pro_sub_id`, `pro_ven_id`, `pro_descrip`, `pro_buy_value`,`pro_buy_date`,`pro_margin1`, `pro_sale_value1`,`pro_margin2`, `pro_sale_value2`,`pro_margin3`, `pro_sale_value3`,`pro_update_date`, `pro_stock`, `pro_codigo`) VALUES (NULL, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/altaprod')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Modificar datos de productos - Busca los datos del producto y los envia al html
#  donde se muestran los datos a modificar.
#---------------------------------------------------------------------------------------
@app.route('/edit_pro/<int:id>')    # Recibe como parámetro el id del registro
def edit_pro(id):
    if validacion:
        conn      = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor    = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `productos` WHERE pro_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        productos = cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión

        # Busco los datos correspondientes a los id que tiene ese producto
        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `proveedores` WHERE ven_id=%s", (productos[0][3]))
        ven_name = cursor.fetchall()
        conn.commit()

        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `categorias` WHERE cat_id=%s", (productos[0][1]))
        cat_name = cursor.fetchall()
        conn.commit()

        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `subcategorias` WHERE sub_id=%s", (productos[0][2]))
        sub_name = cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        proveedores=cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        categorias=cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        subcategorias=cursor.fetchall()
        conn.commit()

        return render_template('paez/edit_pro.html', productos=productos,  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias, ven = productos[0][3], ven_name=ven_name[0][1],cat = productos[0][1], cat_name=cat_name[0][1], sub = productos[0][2], sub_name=sub_name[0][1])
    else:
        return redirect('/')

@app.route('/update_pro', methods=['POST'])
def update_pro():
    if validacion:
        # Recupero los valores del formulario
        id            = request.form['txtPro_Id']
        Pro_Descrip   = request.form["txtPro_Descrip"]
        Pro_Cat_Id    = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id    = request.form["txtPro_Sub_Id"]
        Pro_Ven_Id    = request.form["txtPro_Ven_Id"]
        Pro_Buy_Date  = request.form["txtPro_Buy_Date"]
        Pro_Codigo    = request.form["txtPro_Codigo"]
        Pro_Buy_Value = request.form["txtPro_Buy_Value"]
        Pro_Margin1   = request.form["txtPro_Margin1"]
        Pro_Margin2   = request.form["txtPro_Margin2"]
        Pro_Margin3   = request.form["txtPro_Margin3"]
        Pro_Stock     = request.form["txtPro_Stock"]

        # Y les doy el formato adecuado para guardarlos en la base de datos.
        Pro_Ven_Id      = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
        Pro_Cat_Id      = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
        Pro_Sub_Id      = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )
        Pro_Codigo      = Pro_Codigo[0:11]

        try:
            Pro_Buy_Date = datetime.strptime(Pro_Buy_Date, '%d/%m/%Y')
        except:
            Pro_Buy_Date = datetime.now()

        try:
            Pro_Buy_Value = float(Pro_Buy_Value)
        except:
            Pro_Buy_Value = 0

        try:
            Pro_Margin1 = float(Pro_Margin1)
        except:
            Pro_Margin1 = 0

        try:
            Pro_Margin2 = float(Pro_Margin2)
        except:
            Pro_Margin2 = 0

        try:
            Pro_Margin3 = float(Pro_Margin3)
        except:
            Pro_Margin3 = 0

        try:
            Pro_Stock = int(Pro_Stock)
        except:
            Pro_Stock = 0

        Pro_Sale_Value1 = Pro_Buy_Value * (1 + Pro_Margin1/100)
        Pro_Sale_Value2 = Pro_Buy_Value * (1 + Pro_Margin2/100)
        Pro_Sale_Value3 = Pro_Buy_Value * (1 + Pro_Margin3/100)
        Pro_Update_Date = datetime.now()

        # Y modifico el registro en la base de datos:
        datos = (
        Pro_Cat_Id,
        Pro_Sub_Id,
        Pro_Ven_Id,
        Pro_Descrip,
        Pro_Buy_Value,
        Pro_Buy_Date,
        Pro_Margin1,
        Pro_Sale_Value1,
        Pro_Margin2,
        Pro_Sale_Value2,
        Pro_Margin3,
        Pro_Sale_Value3,
        Pro_Update_Date,
        Pro_Stock,
        Pro_Codigo,
        id)

        sql = "UPDATE `productos` SET `pro_cat_id`=%s, `pro_sub_id`=%s, `pro_ven_id`=%s, `pro_descrip`=%s, `pro_buy_value`=%s,`pro_buy_date`=%s,`pro_margin1`=%s, `pro_sale_value1`=%s,`pro_margin2`=%s, `pro_sale_value2`=%s,`pro_margin3`=%s, `pro_sale_value3`=%s,`pro_update_date`=%s,`pro_stock`=%s,`pro_codigo`=%s WHERE pro_id=%s;"

        conn   = mysql.connect() # Se conecta a la conexión mysql
        cursor = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute(sql,datos)
        conn.commit()            # Cerramos la conexión
        return render_template('paez/listado_pro_y.html')
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Consultar datos de productos - Busca los datos del producto y los envia al html
#  donde se muestran los datos
#---------------------------------------------------------------------------------------
@app.route('/mostrar_pro/<int:id>')    # Recibe como parámetro el id del registro
def mostrar_pro(id):
    if validacion:
        conn      = mysql.connect() # Se conecta a la conexión mysql.init_app(app)
        cursor    = conn.cursor()   # Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM `productos` WHERE pro_id=%s", (id)) # Ejecutamos la sentencia SQL sobre el id
        productos = cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión

        # Busco los datos correspondientes a los id que tiene ese producto
        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `categorias` WHERE cat_id=%s", (productos[0][1]))
        cat_name = cursor.fetchall()
        conn.commit()

        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `subcategorias` WHERE sub_id=%s", (productos[0][2]))
        sub_name = cursor.fetchall()
        conn.commit()

        conn     = mysql.connect()
        cursor   = conn.cursor()
        cursor.execute("SELECT * FROM `proveedores` WHERE ven_id=%s", (productos[0][3]))
        ven_name = cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        proveedores=cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        categorias=cursor.fetchall()
        conn.commit()

        sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        subcategorias=cursor.fetchall()
        conn.commit()

        return render_template('paez/mostrar_pro.html', productos=productos,  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias, ven = productos[0][3], ven_name=ven_name[0][1],cat = productos[0][1], cat_name=cat_name[0][1], sub = productos[0][2], sub_name=sub_name[0][1])
    else:
        return redirect('/')

#---------------------------------------------------------------------------------------
#  Borrar  un producto
#---------------------------------------------------------------------------------------
@app.route('/destroy_pro/<int:id>') #Recibe como parámetro el id del registro
def destroy_pro(id):
    if validacion:
        conn   = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `productos` WHERE pro_id=%s", (id))
        conn.commit()
        return render_template("paez/listado_pro_y.html")
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
# Genero una copia de seguridad en la base de datos.
#---------------------------------------------------------------------------------------
@app.route('/backup')
def backup():

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if validacion:
        # Conexion con la base de datos
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
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        current_date = now.strftime("%Y_%m_%d")
        date = current_date+"_"+current_time

        bookname = 'copia_datos_'+date+'.xls'
        workbook.save(bookname)

        return render_template("paez/backup_ready.html", bookname=bookname)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
# Genero el listado en PDF, ordenador por "tipo", filtrado por proveedor, rubro, y subrubro
#---------------------------------------------------------------------------------------
def GeneroPDF( tipo , Pro_Ven_Id, Pro_Cat_Id, Pro_Sub_Id, bookname):
    #--------------------------------------------------------------------------------------------
    # listado
    #--------------------------------------------------------------------------------------------
    listado = []
    estilos = getSampleStyleSheet()
    pdfmetrics.registerFont(TTFont('Cousine', "Cousine.ttf"))
    estilos.add(ParagraphStyle(fontName='Cousine',fontSize = 10,name='Justify',  alignment=TA_JUSTIFY))
    estilos.add(ParagraphStyle(fontName='Cousine',fontSize = 10,name='Left',     alignment=TA_LEFT))
    estilos.add(ParagraphStyle(fontName='Cousine',fontSize = 10,name='Right',    alignment=TA_RIGHT))
    estilos.add(ParagraphStyle(fontName='Cousine',fontSize = 10,name='Center',   alignment=TA_CENTER))
    estilos.add(ParagraphStyle(fontName='Cousine',fontSize = 20,name='Titulo',   alignment=TA_CENTER))

    Pro_Ven_Id = int(Pro_Ven_Id[0:Pro_Ven_Id.find(" ")] )
    Pro_Cat_Id = int(Pro_Cat_Id[0:Pro_Cat_Id.find(" ")] )
    Pro_Sub_Id = int(Pro_Sub_Id[0:Pro_Sub_Id.find(" ")] )

    str1 = "ven_id IS NOT NULL"
    str2 = "cat_id IS NOT NULL"
    str3 = "sub_id IS NOT NULL"

    if Pro_Ven_Id != 0:
        str1 = "ven_id LIKE "+str(Pro_Ven_Id)
        sql = "SELECT * FROM `proveedores` WHERE "+str1+";"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        proveedores=cursor.fetchall()
        conn.commit()
        proveedor = proveedores[0][1]
    else:
        proveedor = "Todos"

    if Pro_Cat_Id != 0:
        str2 = "cat_id LIKE "+str(Pro_Cat_Id)
        sql = "SELECT * FROM `categorias` WHERE "+str2+";"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        categorias=cursor.fetchall()
        conn.commit()
        categoria = categorias[0][1]
    else:
        categoria = "Todas"

    if Pro_Sub_Id != 0:
        str3 = "sub_id LIKE "+str(Pro_Sub_Id)
        sql = "SELECT * FROM `subcategorias` WHERE "+str3+";"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        subcategorias=cursor.fetchall()
        conn.commit()
        subcategoria = subcategorias[0][1]
    else:
        subcategoria = "Todas"


    # Busco los productos a listar, y los traigo ordenados.
    sql = "SELECT * FROM `productos` WHERE pro_"+str1+" AND pro_"+str2+" AND pro_"+str3+" ORDER BY "+tipo+";"
    print (sql)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    productos=cursor.fetchall()
    conn.commit()


    #--------------------------------------------------------------------------------------------
    # Datos de configuracion necesarios para la generación del PDF
    #--------------------------------------------------------------------------------------------
    espacio  = "&nbsp;"

    if tipo == "pro_id":
        titulo = "CODIGO"

    if tipo == "pro_descrip":
        titulo = "DESCRIPCION"

    doc1 = SimpleDocTemplate(bookname,      #Defino el tamaño y características de la hoja:
                            pagesize     = letter,
                            rightMargin  = 20,
                            leftMargin   = 20,
                            topMargin    = 32,
                            bottomMargin = 18)

    #--------------------------------------------------------------------------------------------
    # Y los "imprimo" en el PDF
    #--------------------------------------------------------------------------------------------
    pagina = 1

    for i in range(0,len(productos)):
        # Veo si hay un salto de página, para imprimir encabezados:
        if i%40 ==0:
            listado.append(Paragraph("LISTADO", estilos["Titulo"]))
            listado.append(Paragraph(espacio, estilos["Titulo"]))
            listado.append(Paragraph("Productos por "+titulo, estilos["Titulo"]))
            listado.append(Paragraph("Página:" +str(pagina), estilos["Right"]))
            listado.append(Paragraph(espacio, estilos["Titulo"]))
            listado.append(Paragraph("-"*92, estilos["Center"]))
            listado.append(Paragraph("Prov: "+proveedor + " | " + "Cat: "+categoria + " | " + "SubCat: "+subcategoria, estilos["Center"]))
            listado.append(Paragraph("-"*92, estilos["Center"]))
            listado.append(Paragraph(espacio*3+"ID"+espacio*7+"CODIGO"+espacio+"DESCRIPCION"+espacio*56+"PRECIO", estilos["Left"]))
            listado.append(Paragraph("-"*92, estilos["Center"]))
            pagina = pagina +1


        aux = len(str(productos[i][0]))
        p_id = espacio*(5-aux) + str(productos[i][0])

        aux = len(str(productos[i][15]))
        if aux <12:
            p_codigo  = espacio*(12-aux) + productos[i][15]

        p_descrip = productos[i][4]+ "."*(100)
        p_descrip = p_descrip[0:57]

        p_precio  = "{:,.2f} $".format(productos[i][8])
        aux = len(p_precio)
        p_precio = espacio*(16-aux) + p_precio

        listado.append(Paragraph(  p_id     + " " +
                                   p_codigo + " " +
                                   p_descrip + " " +
                                   p_precio,
                        estilos["Left"]))

        # Dejo una linea en blanco cada 4:
        if (i+1)%4 == 0:
            listado.append(Paragraph(espacio, estilos["Left"]))

    doc1.build(listado)


#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona la configuracion del listado de precios en PDF (por ID)
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_PDF1")
def listado_pro_PDF1():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_PDF1.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
#  Llamo a la funcion que genera el listado de precios en PDF (por ID)
#---------------------------------------------------------------------------------------
@app.route('/listado_precios_PDF1', methods=['POST'])
def listado_precios_PDF1():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id = request.form['txtPro_Ven_Id']
        Pro_Cat_Id = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id = request.form["txtPro_Sub_Id"]

        #---------------------------------------------------------------------------------------
        # Genero el listado, con la fecha y hora en su nombre
        #---------------------------------------------------------------------------------------
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        current_date = now.strftime("%Y_%m_%d")
        date = current_date+"_"+current_time

        bookname = 'Precios(CODIGO)_'+date+'.pdf'

        GeneroPDF( "pro_id" , Pro_Ven_Id, Pro_Cat_Id, Pro_Sub_Id, bookname)

        return render_template("paez/listado_ready.html", bookname=bookname)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
#  Pantalla donde se selecciona la configuracion del listado de precios en PDF (por Descripcion)
#---------------------------------------------------------------------------------------
@app.route("/listado_pro_PDF2")
def listado_pro_PDF2():
    # Busco los vendedores cargados:
    sql = "SELECT * FROM `proveedores` ORDER BY ven_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    proveedores=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `categorias` ORDER BY cat_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    categorias=cursor.fetchall()
    conn.commit()

    sql = "SELECT * FROM `subcategorias` ORDER BY sub_name;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    subcategorias=cursor.fetchall()
    conn.commit()
    if validacion:
        return render_template("paez/listado_pro_PDF2.html",  proveedores=proveedores, categorias=categorias, subcategorias=subcategorias)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
#  Llamo a la funcion que genera el listado de precios en PDF (por Descripcion)
#---------------------------------------------------------------------------------------
@app.route('/listado_precios_PDF2', methods=['POST'])
def listado_precios_PDF2():
    if validacion:
        # Recupero los valores del formulario
        Pro_Ven_Id = request.form['txtPro_Ven_Id']
        Pro_Cat_Id = request.form["txtPro_Cat_Id"]
        Pro_Sub_Id = request.form["txtPro_Sub_Id"]

        #---------------------------------------------------------------------------------------
        # Genero el listado, con la fecha y hora en su nombre
        #---------------------------------------------------------------------------------------
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        current_date = now.strftime("%Y_%m_%d")
        date = current_date+"_"+current_time

        bookname = 'Precios(Descripcion)_'+date+'.pdf'

        GeneroPDF( "pro_descrip" , Pro_Ven_Id, Pro_Cat_Id, Pro_Sub_Id, bookname)

        return render_template("paez/listado_ready.html", bookname=bookname)
    else:
        return redirect('/')


#---------------------------------------------------------------------------------------
#  Lanza la app
#---------------------------------------------------------------------------------------
if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
    #print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

    #app.run(debug=True, host=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0], port=5000)
