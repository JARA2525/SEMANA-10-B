# SERVICIOS/inventario.py

from MODELOS.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # Guardar inventario
    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            for p in self.productos:
                f.write(f"{p.id},{p.nombre},{p.precio},{p.cantidad}\n")

    # Cargar inventario
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    idp, nombre, precio, cantidad = linea.strip().split(",")
                    self.productos.append(Producto(int(idp), nombre, float(precio), int(cantidad)))
        except FileNotFoundError:
            print("Archivo no encontrado, creando uno nuevo...")
        except Exception:
            print("Error al leer archivo")

    # Agregar producto
    def agregar_producto(self, nombre, precio, cantidad):
        nuevo_id = len(self.productos) + 1
        self.productos.append(Producto(nuevo_id, nombre, precio, cantidad))
        self.guardar_en_archivo()
        print("Producto agregado")

    # Mostrar productos
    def mostrar(self):
        for p in self.productos:
            print(p.id, p.nombre, p.precio, p.cantidad)

    # Modificar producto
    def modificar_producto(self, idp, n, p, c):
        encontrado = False

        for prod in self.productos:
            if prod.id == idp:
                prod.nombre = n
                prod.precio = p
                prod.cantidad = c
                encontrado = True
                break

        if encontrado:
            self.guardar_en_archivo()
            print("Producto modificado correctamente")
        else:
            print("Producto no encontrado")