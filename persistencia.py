import sqlite3

# Crea la conexión con la DB SQLite
def conectar():
    conexion = sqlite3.connect("inventario.db")
    return conexion

# Crea la tabla productos si todavía no existe
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)

    conexion.commit()
    conexion.close()


crear_tabla()

# Inserta un nuevo producto en la base de datos
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO productos
        (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, cantidad, precio, categoria)
    )

    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()

    return productos
def obtener_productos_stock_bajo(limite):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE cantidad <= ?",
        (limite,)
    )

    productos = cursor.fetchall()

    conexion.close()

    return productos

def buscar_producto_por_id(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id_producto,)
    )

    producto = cursor.fetchone()

    conexion.close()

    return producto

# Elimina un producto de la base de datos
def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM productos WHERE id = ?",
        (id_producto,)
    )

    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()

    return filas_afectadas

def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE productos
        SET nombre = ?,
            descripcion = ?,
            cantidad = ?,
            precio = ?,
            categoria = ?
        WHERE id = ?
        """,
        (nombre, descripcion, cantidad, precio, categoria, id_producto)
    )

    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()

    return filas_afectadas
