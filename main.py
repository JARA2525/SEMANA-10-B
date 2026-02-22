from SERVICIOS.inventario import Inventario

inv = Inventario()

while True:
    print("\n--- MENU INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Modificar producto")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ")
        p = float(input("Precio: "))
        c = int(input("Cantidad: "))
        inv.agregar_producto(n, p, c)

    elif op == "2":
        inv.mostrar()

    elif op == "3":
        idp = int(input("ID a modificar: "))
        n = input("Nuevo nombre: ")
        p = float(input("Nuevo precio: "))
        c = int(input("Nueva cantidad: "))
        inv.modificar_producto(idp, n, p, c)

    elif op == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")