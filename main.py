products = []

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
        productCategory = input("Ingrese la categoría: ")
        productPrice = input("Ingrese el precio (sin centavos): $ ")

        products.append([productName, productCategory, productPrice])
        print(f"\n  ✅ Producto {productName} agregado correctamente.")

    elif option == "2":
        print("\n *** 📝 Lista de Productos *** ")
        if len(products) == 0:
            print("🙁 No hay productos registrados")
        else:
            print(
                f"{'n°':<2} {'Nombre de Producto':<20}{'Categoria':<15}{'Precio':<10}"
            )
            print("-" * 50)
            for i in range(len(products)):
                print(
                    f"{i+1:<2}{products[i][0]:<20}{products[i][1]:<15}{products[i][2]:<10}"
                )
            print("-" * 50)
    elif option == "3":
         print("\n *** 🔎 Buscar Productos *** ")
         productToSearch = input ("Ingrese el nombre del producto a buscar: ")
         foundProduct = False

         for i in range (len(products)):
             if products[i][0].lower() == productToSearch.lower():
                 print(f" 🕵🏻‍♀️ Producto encontrado en el indice {i+1}")
                 print(f"Nombre:{products [i][0]}")
                 print(f"Categoría:{products [i][1]}")
                 print(f"Precio:$ {products [i][2]}")
                 foundProduct = True
                 break
         if not foundProduct:
            print(f"\n  No se encontró el producto {productToSearch}")

    elif option == "4":
         print("\n *** 🗑️ Eliminar Productos *** ")
         if len(products) == 0:
            print("No hay productos para eliminar")
         else:
            print("Productos Disponibles")
            for i in range (len(products)):
                print(f"{i+1}. {products[i][0]} - {products[i][1]} - {products[i][2]}")

            indexProduct = input("Ingrese el número de producto a eliminar: ")
            try:
                ipr = int(indexProduct) - 1

                if ipr >=0 and ipr < len(products):
                    deleted_products = products.pop(ipr)
                    print(f"✅ Producto { deleted_products[0]} eliminado correctamente")
                else:
                    print("❌ Índice no válido")
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingrese un número.")

    elif option == "5":
        print("☺️ Gracias por usar el sistema de gestión de Productos ")
        break
    else:
        print("❌ Opción no válida, ingrese un número del 1 al 5 ")