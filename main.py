import sqlite3


def conectar():
    conexion = sqlite3.connect("inventario.db")
    return conexion


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


while True:
    print("\n" + "=" * 50)
    print(" ******* SISTEMA DE GESTIÓN DE PRODUCTOS ******* ")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Ver producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    option = input("seleccione una opción (1 - 5): ")

    if option == "1":
        print("\n *** ➕ Agregar Producto *** ")
        productName = ""
        while productName == "":
            productName = input("Ingrese el nombre: ").strip()
            if productName == "":
                print("⚠️ El nombre del producto no puede estar vacío.")
            productDescription = input("Ingrese la descripción: ")
        productCategory = input("Ingrese la categoría: ")
        productQuantity = int(input("Ingrese la cantidad: "))
        productPrice = float(input("Ingrese el precio: $ "))

        agregar_producto(
            productName,
            productDescription,
            productQuantity,
            productPrice,
            productCategory
        )

        print(f" \n✅ Producto {productName} agregado correctamente.")        

    elif option == "2":
        print("\n *** 📝 Lista de Productos *** ")

        productos = obtener_productos()

        if len(productos) == 0:
            print("🙁 No hay productos registrados")
        else:
            print(
                f"{'ID':<5}{'Nombre':<20}{'Cantidad':<10}{'Precio':<12}{'Categoría':<15}"
            )
            print("-" * 65)

            for producto in productos:
                print(
                    f"{producto[0]:<5}"
                    f"{producto[1]:<20}"
                    f"{producto[3]:<10}"
                    f"${producto[4]:<11.2f}"
                    f"{producto[5]:<15}"
                )

            print("-" * 65)
    elif option == "3":
        print("\n *** 🔎 Buscar Productos *** ")

        try:
            id_producto = int(input("Ingrese el ID del producto: "))

            producto = buscar_producto_por_id(id_producto)

            if producto:
                print(" \n 🕵🏻‍♀️ Producto encontrado:")
                print(f"ID: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2]}")
                print(f"Cantidad: {producto[3]}")
                print(f"Precio: $ {producto[4]}")
                print(f"Categoría: {producto[5]}")
            else:
                print("❌ No se encontró un producto con ese ID.")

        except ValueError:
            print("❌ Debe ingresar un número.")

    elif option == "4":
        print("\n *** 🗑️ Eliminar Productos *** ")

        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))

            producto = buscar_producto_por_id(id_producto)

            if producto:
                eliminar_producto(id_producto)
                print(f"✅ Producto '{producto[1]}' eliminado correctamente.")
            else:
                print("❌ No existe un producto con ese ID.")

        except ValueError:
            print("❌ Debe ingresar un número.")

    elif option == "5":
        print("☺️ Gracias por usar el sistema de gestión de Productos ")
        break
    else:
        print("❌ Opción no válida, ingrese un número del 1 al 5 ")