import sqlite3

DATABASE = 'misdatos.db'

def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#-----------------------------------
conn = conectar()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
        codigo INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )''')

conn.commit()
cursor.close()
conn.close()

#-----------------------------------
#Guardar datos de un producto

desc = "Discos 3TB"
precio = 104500
stock = 1

conn = conectar()
cursor = conn.cursor()

cursor.execute('''INSERT INTO productos 
                (descripcion,cantidad,precio)
                VALUES(?,?,?)''',
                (desc,stock,precio  )
)

conn.commit()
cursor.close()
conn.close()


#-----------------------------------
# consultar datos de un producto
try:
    conn = conectar()
    cursor = conn.cursor()
    codigo = 1
    cursor.execute('''SELECT * FROM productos 
                    WHERE codigo = ?''', (codigo,))

    producto = cursor.fetchone()
    print(producto["codigo"])
    print(producto["descripcion"])
    print(producto["cantidad"])
    print(producto["precio"])

    conn.commit()
    cursor.close()
    conn.close()
except:
    print("Ocurrió un error....")
finally:
    print("Consulta finalizada")