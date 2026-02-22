from MODELOS.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # Guardar inventario en archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir el archivo.")

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, precio, cantidad = linea.strip().split(",")
                    self.productos.append(Producto(nombre, float(precio), int(cantidad)))
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, creando uno nuevo...")
            open(self.archivo, "w").close()
        except Exception:
            print("Error al leer el archivo (archivo corrupto).")

    # Agregar producto
    def agregar_producto(self, nombre, precio, cantidad):
        self.productos.append(Producto(nombre, precio, cantidad))
        self.guardar_en_archivo()
        print("Producto agregado y guardado.")

    # Mostrar productos
    def mostrar(self):
        for p in self.productos:
            print(p.nombre, p.precio, p.cantidad)