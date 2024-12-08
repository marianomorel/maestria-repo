import sqlite3

# Configurar la conexión a la base de datos SQLite
DATABASE = 'inventario.db'

# Obtener la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        codigo INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
''')
conn.commit()
cursor.close()
conn.close()

print("\033[H\033[J")       # Limpiamos la pantalla
# Agregar un producto a la base de datos
# try:
#     # Obtener la conexión a la base de datos
#     conexion = get_db_connection()

#     descripcion = input("Ingrese la descripción del producto: ")
#     stock = int(input("Ingrese la cantidad en stock del producto: "))
#     precio = float(input("Ingrese el precio del producto: "))

#     cursor = conexion.cursor()
#     cursor.execute("INSERT INTO productos (descripcion, cantidad, precio) VALUES (?, ?, ?)",
#                     (descripcion, stock, precio))
#     conexion.commit()
#     cursor.close()

#     print("El producto ha sido agregado correctamente.\n")
# except sqlite3.Error as e:
#     print(f"Error al agregar el producto: {e}\n")
# finally:
#     if conexion:
#         conexion.close()

# Consultar un producto por su código
# try:
#     # Obtener la conexión a la base de datos
#     conexion = get_db_connection()

#     codigo = int(input("Ingrese el código del producto a consultar: "))

#     cursor = conexion.cursor()
#     cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
#     producto = cursor.fetchone()
#     cursor.close()

#     if producto:
#         print("Información del producto:")
#         print(f"Código: {producto['codigo']}")
#         print(f"Descripción: {producto['descripcion']}")
#         print(f"Stock: {producto['cantidad']}")
#         print(f"Precio: {producto['precio']}")
#     else:
#         print("El producto no se encuentra en la base de datos.\n")
# except sqlite3.Error as e:
#     print(f"Error al consultar el producto: {e}\n")
# finally:
#     if conexion:
#         conexion.close()



# Eliminar un producto por su código
# try:
#     # Obtener la conexión a la base de datos
#     conexion = get_db_connection()

#     codigo = int(input("Ingrese el código del producto a eliminar: "))

#     cursor = conexion.cursor()
#     cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
#     conexion.commit()

#     if cursor.rowcount > 0:
#         print("El producto ha sido eliminado correctamente.\n")
#     else:
#         print("El producto no se encuentra en la base de datos.\n")
#     cursor.close()
# except sqlite3.Error as e:
#     print(f"Error al eliminar el producto: {e}\n")
# finally:
#     if conexion:
#         conexion.close()


# try:
#     # Obtener la conexión a la base de datos
#     conexion = get_db_connection()

#     cursor = conexion.cursor()
#     cursor.execute("SELECT * FROM productos")
#     productos = cursor.fetchall()
#     cursor.close()

#     if productos:
#         print("Listado de productos:")
#         for producto in productos:
#             print(f"Código: {producto['codigo']}")
#             print(f"Descripción: {producto['descripcion']}")
#             print(f"Stock: {producto['cantidad']}")
#             print(f"Precio: {producto['precio']}")
#             print()
#     else:
#         print("No hay productos en la base de datos.\n")
# except sqlite3.Error as e:
#     print(f"Error al obtener el listado de productos: {e}\n")
# finally:
#     if conexion:
#         conexion.close()