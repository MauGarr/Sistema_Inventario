class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion

    def actualizr_cantidad(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            return False
        
class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario_inicial(self, archivo):
        with open(archivo, "r", "UTF-8") as f:
            for linea in f:
                instruccion, detalles = linea.strip().split(' ', 1)
                if instruccion == 'crear_producto':
                    nombre, cantidad, precio, ubicacion = detalles.split(';')
                    producto = Producto(nombre, int(cantidad), float(precio), ubicacion)
                    self.productos[nombre + '_' + ubicacion] = producto

    def cargar_instrucciones_movimientos(self, archivo):
        with open(archivo, "r", "UTF-8") as f:
            for linea in f:
                instruccion, detalles = linea.strip().split(' ', 1)
                if instruccion == 'agregar_stock':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    key = nombre + '_' + ubicacion
                    if key in self.productos:
                        self.productos[key].actualizar_cantidad(int(cantidad))
                    else:
        

#Menú
print("-------------------------------------------------------")
print("   Práctica 1 - Lenguajes Formales y de Programación    ")
print("-------------------------------------------------------")
print("# Sistema de Inventario: ")

menuprincipal = int(input("\n 1. Cargar Inventario Inicial \n 2. Cargar Instrucciones de Movimientos \n 3. Crear Informe de Inventario \n 4. Salir \n Ingrese una opción: "))

while menuprincipal !=4:

    if menuprincipal == 1:
        print("---------------------------------")
        print("Cargue los datos del inventario")
        ruta = input("Ingrese los datos: ")

    elif menuprincipal == 2:
        print("-----------------------------------------")
        print("Cargue las instrucciones de movimientos")

    elif menuprincipal == 3:
        print("----------------------------")
        print("Cargando datos del Informe")

    else:   
        print("----------------------------------------")
        print("¡Por favor digita una opción correcta!")
        print("----------------------------------------")

    menuprincipal = int(input("\n 1. Cargar Inventario Inicial \n 2. Cargar Instrucciones de Movimientos \n 3. Crear Informe de Inventario \n 4. Salir \n Ingrese una opción: "))