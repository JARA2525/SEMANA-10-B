from SERVICIOS.inventario import Inventario

inv = Inventario()

while True:
    print("\n1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Salir")

    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ")
        p = float(input("Precio: "))
        c = int(input("Cantidad: "))
        inv.agregar_producto(n, p, c)

    elif op == "2":
        inv.mostrar()

    elif op == "3":
        break