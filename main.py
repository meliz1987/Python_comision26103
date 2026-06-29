from persistencia import *
from menu import mostrar_menu
from util import pedir_entero, pedir_float

# Crea la tabla al iniciar el programa
crear_tabla()


while True:
    mostrar_menu()
    option = input("seleccione una opción (1 - 7): ")

    if option == "1":
        print("\n *** ➕ Agregar Producto *** ")
        nombre = input("Nombre: ").strip()
        descripcion = input("Descripción: ").strip()
        cantidad = pedir_entero("Cantidad: ")
        precio = pedir_float("Precio:$ ")
        categoria = input("Categoría: ").strip()

        agregar_producto(nombre, descripcion, cantidad, precio, categoria)

        print(f" \n✅ Producto {nombre} agregado correctamente.")        

    elif option == "2":
        print("\n *** 📝 Lista de Productos *** ")
        productos = obtener_productos()

        if len(productos) == 0:
            print("🙁 No hay productos registrados")
        else:
            print(
                f"{'ID':<5}"
                f"{'Nombre':<30}"
                f"{'Cantidad':<10}"
                f"{'Precio':<12}"
                f"{'Categoría':<15}"
            )

            print("-" * 75)

            for producto in productos:
                print(
                    f"{producto[0]:<5}"
                    f"{producto[1]:<30}"
                    f"{producto[3]:<10}"
                    f"${producto[4]:<11.2f}"
                    f"{producto[5]:<15}"
                )

            print("-" * 75)

    elif option == "3":
        print("\n *** 🔎 Buscar Productos *** ")
        id_producto = pedir_entero("ID: ")
        producto = buscar_producto_por_id(id_producto)

        if producto:
            print("\n🕵🏻‍♀️ Producto encontrado:")
            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Cantidad: {producto[3]}")
            print(f"Precio: $ {producto[4]:.2f}")
            print(f"Categoría: {producto[5]}")
        else:
            print("❌ No se encontró un producto con ese ID.")

    elif option == "4":
        print("\n *** 🗑️ Eliminar Productos *** ")
        id_producto = pedir_entero("ID a eliminar: ")
        producto = buscar_producto_por_id(id_producto)

        if producto:
            eliminar_producto(id_producto)
            print(f"✅ Producto '{producto[1]}' eliminado correctamente.")
        else:
            print("❌ No existe un producto con ese ID.")
    
    elif option == "5":
        print("\n *** ✏️ Actualizar Producto *** ")
        id_producto = pedir_entero("ID: ")

        producto = buscar_producto_por_id(id_producto)

        if producto:
            nombre = input(f"Nombre [{producto[1]}]: ") or producto[1]
            descripcion = input(f"Descripción [{producto[2]}]: ") or producto[2]
            cantidad = input(f"Cantidad [{producto[3]}]: ") or producto[3]
            precio = input(f"Precio [{producto[4]}]: ") or producto[4]
            categoria = input(f"Categoría [{producto[5]}]: ") or producto[5]

            actualizar_producto(id_producto, nombre, descripcion, int(cantidad), float(precio), categoria)
            print("✅ Producto actualizado correctamente.")


    elif option == "6":
        print("\n *** 📦 Reporte de Stock Bajo *** ")
        limite = pedir_entero("Límite: ")
        productos = obtener_productos_stock_bajo(limite)

        if len(productos) == 0:
            print("✅ No hay productos con stock bajo.")
        else:
            print(
                f"{'ID':<5}"
                f"{'Nombre':<30}"
                f"{'Cantidad':<10}"
            )
            print("-" * 45)

            for producto in productos:
                print(
                    f"{producto[0]:<5}"
                    f"{producto[1]:<30}"
                    f"{producto[3]:<10}"
                )
    elif option == "7":
            print("☺️ Gracias por usar el sistema de gestión de Productos ")
            break
    else:
            print("❌ Opción no válida, ingrese un número del 1 al 7 ")