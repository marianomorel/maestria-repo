import pymysql

# Conexión a la base de datos
conexion = pymysql.connect(
    host="localhost",  # Cambiar por la dirección del servidor de la base de datos si es necesario
    user="root",  # Cambiar por el nombre de usuario de la base de datos
    password="",  # Cambiar por la contraseña de la base de datos
    database="mibasededatos"
)

# Crear la base de datos si no existe
def crear_basededatos():
    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mibasededatos")
        cursor.close()
        print("La base de datos 'mibasededatos' ha sido creada, o ya existía.")
    except pymysql.Error as e:
        print(f"Error al crear la base de datos: {e}")

# Crear la tabla 'productos' si no existe
def crear_tabla_productos():
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                codigo INT PRIMARY KEY AUTO_INCREMENT,
                descripcion VARCHAR(255),
                stock INT,
                precio FLOAT
            )
        """)
        cursor.close()
        print("La tabla 'productos' ha sido creada, o ya existía.")
    except pymysql.Error as e:
        print(f"Error al crear la tabla 'productos': {e}")

# Agregar un producto a la base de datos
def agregar_producto():
    try:
        # Pedir datos al usuario
        descripcion = input("Ingrese la descripción del producto: ")
        stock = int(input("Ingrese la cantidad en stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (descripcion, stock, precio) VALUES (%s, %s, %s)",
                       (descripcion, stock, precio))
        conexion.commit()
        cursor.close()

        print("El producto ha sido agregado correctamente.")
    except pymysql.Error as e:
        print(f"Error al agregar el producto: {e}")

# Consultar un producto por su código
def consultar_producto():
    try:
        codigo = int(input("Ingrese el código del producto a consultar: "))

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE codigo = %s", (codigo,))
        producto = cursor.fetchone()
        cursor.close()

        if producto:
            print("Información del producto:")
            print(f"Código: {producto[0]}")
            print(f"Descripción: {producto[1]}")
            print(f"Stock: {producto[2]}")
            print(f"Precio: {producto[3]}")
        else:
            print("El producto no se encuentra en la base de datos.")
    except pymysql.Error as e:
        print(f"Error al consultar el producto: {e}")

# Eliminar un producto por su código
def eliminar_producto():
    try:
        codigo = int(input("Ingrese el código del producto a eliminar: "))

        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE codigo = %s", (codigo,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("El producto ha sido eliminado correctamente.")
        else:
            print("El producto no se encuentra en la base de datos.")
        cursor.close()
    except pymysql.Error as e:
        print(f"Error al eliminar el producto: {e}")

# Listar todos los productos en la base de datos
def listar_productos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()

        if productos:
            print("Listado de productos:")
            for producto in productos:
                print("------------------------")
                print(f"Código: {producto[0]}")
                print(f"Descripción: {producto[1]}")
                print(f"Stock: {producto[2]}")
                print(f"Precio: {producto[3]}")
        else:
            print("No hay productos en la base de datos.")
    except pymysql.Error as e:
        print(f"Error al listar los productos: {e}")

# Menú de opciones
while True:
    print("\n\n--- MENÚ ---")
    print("1. Crear la base de datos 'mibasededatos'")
    print("2. Crear la tabla 'productos'")
    print("3. Agregar un producto")
    print("4. Consultar un producto")
    print("5. Eliminar un producto")
    print("6. Listar todos los productos")
    print("0. Salir\n")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        crear_basededatos()
    elif opcion == "2":
        crear_tabla_productos()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        consultar_producto()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        listar_productos()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Cerrar la conexión a la base de datos
conexion.close()
