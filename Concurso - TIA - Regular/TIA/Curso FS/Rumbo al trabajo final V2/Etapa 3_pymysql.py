import pymysql

# -------------------------------------------------------------------
# Definimos la clase "Producto"
# -------------------------------------------------------------------
class Producto:
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion
        self.cantidad = nueva_cantidad
        self.precio = nuevo_precio


# -------------------------------------------------------------------
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class Inventario:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost', 
            port=3306,
            user='root', 
            password='', 
            database='carrito')
        
        self.cursor = self.conexion.cursor()
        self.crear_tabla_productos()

    def crear_tabla_productos(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                codigo INT PRIMARY KEY,
                descripcion VARCHAR(100),
                cantidad INT,
                precio FLOAT
            )
        """)
        self.conexion.commit()

    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        try:
            self.cursor.execute("INSERT INTO productos (codigo, descripcion, cantidad, precio) VALUES (%s, %s, %s, %s)",
                                (codigo, descripcion, cantidad, precio))
            self.conexion.commit()
            print("Producto agregado correctamente.")
        except pymysql.IntegrityError:
            print("El producto ya existe.")

    def consultar_producto(self, codigo):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = %s", (codigo,))
        resultado = self.cursor.fetchone()
        if resultado:
            codigo, descripcion, cantidad, precio = resultado
            producto = Producto(codigo, descripcion, cantidad, precio)
            return producto
        else:
            return False

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        try:
            self.cursor.execute("UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s WHERE codigo = %s",
                                (nueva_descripcion, nueva_cantidad, nuevo_precio, codigo))
            self.conexion.commit()
            print("Producto modificado correctamente.")
        except pymysql.IntegrityError:
            print("Error al modificar el producto.")

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        print("-" * 30)
        for producto in productos:
            codigo, descripcion, cantidad, precio = producto
            print(f"Código: {codigo}")
            print(f"Descripción: {descripcion}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio: {precio}")
            print("-" * 30)

    def eliminar_producto(self, codigo):
        self.cursor.execute("DELETE FROM productos WHERE codigo = %s", (codigo,))
        self.conexion.commit()
        if self.cursor.rowcount > 0:
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")


# -------------------------------------------------------------------
# Definimos la clase "Carrito"
# -------------------------------------------------------------------
class Carrito:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost', user='usuario', password='contraseña', database='nombre_bd')
        self.cursor = self.conexion.cursor()
        self.items = []

    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is False:
            print("El producto no existe.")
            return False
        if producto.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False

        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                inventario.modificar_producto(codigo, producto.descripcion, producto.cantidad - cantidad, producto.precio)
                return True

        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        inventario.modificar_producto(codigo, producto.descripcion, producto.cantidad - cantidad, producto.precio)
        return True

    def quitar(self, codigo, cantidad, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    print("Cantidad a quitar mayor a la cantidad en el carrito.")
                    return False
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                inventario.modificar_producto(codigo, item.descripcion, item.cantidad + cantidad, item.precio)
                return True

        print("El producto no se encuentra en el carrito.")
        return False

    def mostrar(self):
        print("-" * 30)
        for item in self.items:
            print(f"Código: {item.codigo}")
            print(f"Descripción: {item.descripcion}")
            print(f"Cantidad: {item.cantidad}")
            print(f"Precio: {item.precio}")
            print("-" * 30)


# -------------------------------------------------------------------
# Ejemplo de uso de las clases y objetos definidos antes:
# -------------------------------------------------------------------
# Crear una instancia de la clase Inventario
x = Inventario()

# Crear una instancia de la clase Carrito
mi_carrito = Carrito()

# Agregar productos al inventario
x.agregar_producto(1, "Producto 1", 10, 19.99)
x.agregar_producto(2, "Producto 2", 5, 9.99)
x.agregar_producto(3, "Producto 3", 15, 29.99)

# Agregar productos al carrito
mi_carrito.agregar(1, 2, x)  # Agregar 2 unidades del producto con código 1 al carrito
mi_carrito.agregar(3, 1, x)  # Agregar 1 unidad del producto con código 3 al carrito
mi_carrito.quitar(1, 1, x)   # Quitar 1 unidad del producto con código 1 al carrito

mi_carrito.mostrar()
