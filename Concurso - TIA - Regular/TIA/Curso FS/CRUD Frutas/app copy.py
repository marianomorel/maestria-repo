from flask import Flask,app,render_template,request,redirect,flash,url_for
from flaskext.mysql import MySQL
from datetime import datetime
import os #Nos pemite acceder a los archivos
from flask import send_from_directory #Acceso a las carpetas
validacion=False
usuario=""


app = Flask(__name__)
app.secret_key="123Prueba!"
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
app.config['MYSQL_DATABASE_TABLE']='empleados'
mysql.init_app(app)

CARPETA= os.path.join('uploads') #Referencia a la carpeta
app.config['CARPETA']=CARPETA #Indicamos que vamos a guardar esta ruta de la carpeta

@app.route("/")
def index():
    global validacion
    validacion=False
    return render_template("empleados/index.html")


@app.route('/ingresar', methods=['POST'])
def ingresar():
    _usuario=request.form["txtUsuario"]
    _password=request.form["txtPassword"]
    sql="SELECT * FROM `usuarios` WHERE `Usuario` LIKE %s"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,_usuario)
    global usuario
    usuario=cursor.fetchall()

    if usuario!=() and _password==usuario[0][1]:
        global validacion
        validacion=True
        return redirect("inicio")
    else: 
        flash("Usuario o contraseña erroneos")
        return render_template("empleados/index.html")


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
        return send_from_directory(app.config['CARPETA'], nombreFoto)

@app.route("/invitado")
def invitado():
    sql = "SELECT * FROM `empleados` ORDER BY nombre;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    conn.commit()
    return render_template("empleados/invitado.html", empleados=empleados)

    
@app.route('/inicio')
def inicio():
    sql = "SELECT * FROM `empleados` ORDER BY nombre;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    conn.commit()
    
    if validacion:
        return render_template("empleados/inicio.html", empleados=empleados,cosa=usuario[0][0])
    else:
        return redirect('/')

@app.route('/destroy/<int:id>') #Recibe como parámetro el id del registro
def destroy(id):
    if validacion:
        conn = mysql.connect() #Se conecta a la conexión mysql.init_app(app)
        cursor = conn.cursor() #Almacenaremos lo que ejecutamos
        cursor.execute("SELECT foto FROM `empleados` WHERE id=%s",id) #Buscamos la foto
        fila= cursor.fetchall() #Traemos toda la información
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0])) #Ese valor seleccionado se encuentra en la posición 0 y la fila 0
        cursor.execute("DELETE FROM   WHERE id=%s", (id)) #En vez de pasarle el string la escribimos
        conn.commit() #Cerramos la conexión
        return redirect('/inicio') #Regresamos de donde vinimos
    else:
        return redirect('/')

@app.route('/edit/<int:id>') #Recibe como parámetro el id del registro
def edit(id):
    if validacion:
        conn = mysql.connect() #Se conecta a la conexión mysql.init_app(app)
        cursor = conn.cursor() #Almacenaremos lo que ejecutamos
        cursor.execute("SELECT * FROM ´empleados´ WHERE id=%s", (id)) #Ejecutamos la sentencia SQL sobre el id
        empleados=cursor.fetchall() #Traemos toda la información
        conn.commit() #Cerramos la conexión
        return render_template('empleados/edit.html', empleados=empleados)
    else:
        return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    if validacion:
        _nombre=request.form['txtNombre'].title().strip
        _correo=request.form['txtCorreo']
        _foto=request.files['txtFoto']
        id=request.form['txtID']
        sql = "UPDATE `empleados` SET `nombre`=%s, `correo`=%s WHERE id=%s;"
        datos=(_nombre,_correo,id)
        conn = mysql.connect() #Se conecta a la conexión mysql.init_app(app)
        now= datetime.now()
        tiempo= now.strftime("%Y%H%M%S_") #Años horas minutos y segundos
        cursor = conn.cursor() #Almacenaremos lo que ejecutamos
        cursor.execute("SELECT foto FROM `empleados`   WHERE id=%s", id) #Buscamos la foto
        fila= cursor.fetchall() #Traemos toda la información
        extension=_foto.filename.split(".")
        if _foto.filename !="":
            nuevoNombreFoto=tiempo+_nombre+"."+extension[1]
            _foto.save("uploads/"+nuevoNombreFoto)
            os.remove(os.path.join(app.config['CARPETA'], fila[0][0])) #Ese valor seleccionado se encuentra en la posición 0 y la fila 0
        else:
            nuevoNombreFoto=fila
        cursor.execute("UPDATE `empleados`  SET foto=%s WHERE id=%s", (nuevoNombreFoto, id)) #Buscamos la foto
        cursor.execute(sql,datos)
        conn.commit() #Cerramos la conexión
        return redirect('/inicio')
    else:
        return redirect('/')


@app.route("/create")
def create():
    if validacion:
        return render_template("empleados/create.html")
    else:
        return redirect('/')

@app.route('/store', methods=['POST'])
def storage():
    if validacion:
        _nombre=request.form["txtNombre"].title()
        _correo=request.form["txtCorreo"]
        _foto=request.files["txtFoto"]
        if _nombre=="" or _correo=="" or _foto.filename=="":
            flash("Debe rellenar todos los campos")
            return redirect(url_for('create'))
        now=datetime.now()
        tiempo=now.strftime("%Y%H%M%S_")
        extension=_foto.filename.split(".")
        if _foto.filename !="":
            nuevoNombreFoto=tiempo+_nombre+"."+extension[1]
            _foto.save("uploads/"+nuevoNombreFoto)

        datos=(_nombre,_correo,nuevoNombreFoto)
        sql="INSERT INTO `empleados`  (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
        return redirect('/inicio') 
    else:
        return redirect('/')

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    usuario=(request.form["txtUsuario"],request.form['txtPassword'])
    sql="INSERT INTO `usuarios` (`Usuario`, `password`) VALUES (%s, %s)"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,usuario)
    conn.commit()
    return redirect('/inicio') 

@app.route("/modificar_usuario")
def modificar_usuario():
    if validacion:
        usuario_viejo=request.form["txtUsuario_viejo"]
        nUsuario=request.form["txtUsuario"]
        pUsuario=request.form['txtPassword']
        usuario=(nUsuario,pUsuario)
        sql="UPDATE `usuarios` SET `Usuario`= %s, SET `password`= %s WHERE usuario=%s;"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT ´Usuario´ FROM ´usuarios´ ;") #Ejecutamos la sentencia SQL
        usuarios=cursor.fetchall()
        if nUsuario not in usuarios or nUsuario==usuario_viejo:
            cursor.execute(sql,usuario)
        else:
            flash("Nombre de usuario no disponible")
        conn.commit()
        return redirect('/inicio') 


if __name__=="__main__":
    app.run(debug=True)