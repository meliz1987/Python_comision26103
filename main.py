from persistencia import *
from menu import mostrar_menu
from util import pedir_entero, pedir_float

crear_tabla()


while True:
    mostrar_menu()
    option = input("seleccione una opción (1 - 7): ")

    if option == "1":
        print("\n *** ➕ Agregar Producto *** ")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        cantidad = pedir_entero("Cantidad: ")
        precio = pedir_float("Precio:$ ")
        categoria = input("Categoría: ")

        agregar_producto(nombre, descripcion, cantidad, precio, categoria)

        print(f" \n✅ Producto {nombre} agregado correctamente.")        

    elif option == "2":
        print("\n *** 📝 Lista de Productos *** ")

        productos = obtener_productos()
        for p in productos:
            print(p)

    elif option == "3":
        print("\n *** 🔎 Buscar Productos *** ")
        id_producto = pedir_entero("ID: ")
        producto = buscar_producto_por_id(id_producto)

        if producto:
            print(producto)
        else:
            print("❌ No se encontró un producto con ese ID.")

    elif option == "4":
        print("\n *** 🗑️ Eliminar Productos *** ")
        id_producto = pedir_entero("ID a eliminar: ")
        eliminar_producto(id_producto)
        print(f"✅ Producto '{producto[1]}' eliminado correctamente.")
    
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
        for p in productos:
            print(p)

    elif option == "7":
            print("☺️ Gracias por usar el sistema de gestión de Productos ")
            break
    else:
            print("❌ Opción no válida, ingrese un número del 1 al 7 ")