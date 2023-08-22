class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion

    def actualizar_cantidad(self, cantidad):
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
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                instruccion, detalles = linea.strip().split(' ', 1)
                if instruccion == 'crear_producto':
                    nombre, cantidad, precio, ubicacion = detalles.split(';')
                    producto = Producto(nombre, int(cantidad), float(precio), ubicacion)
                    self.productos[nombre + '_' + ubicacion] = producto

    def cargar_instrucciones_movimientos(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                instruccion, detalles = linea.strip().split(' ', 1)
                if instruccion == 'agregar_stock':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    key = nombre + '_' + ubicacion
                    if key in self.productos:
                        self.productos[key].actualizar_cantidad(int(cantidad))
                    else:
                        print(f"Error: Producto '{nombre}' no exite en la ubicación '{ubicacion}'.")
                elif instruccion == 'vender_producto':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    key = nombre + '_' + ubicacion
                    if key in self.productos:
                        if self.productos[key].vender(int(cantidad)):
                            print(f"Venta de {cantidad} unidades de '{nombre}' en '{ubicacion}' realizada.")
                        else:
                            print(f"Error: Cantidad insuficiente de '{nombre}' en '{ubicacion}'.")
                    else:
                        print(f"Error: Producto '{nombre}' no existe en la ubicación '{ubicacion}'.")

    def ordenar_por_ubicacion(self):
        sorted_products = sorted(self.productos.values(), key=lambda producto: producto.ubicacion)
        return sorted_products

    def crear_informe_inventario(self, archivo):
        productos_ordenados = self.ordenar_por_ubicacion()
        with open(archivo, 'w', encoding="UTF-8") as f:
            f.write("Informe de Inventario:\n")
            f.write("Ordenado por Ubicación\n")
            f.write("{:<15} {:<10} {:<15} {:<15} {:<10}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"))
            f.write("-" * 70 + "\n")

            for producto in productos_ordenados:
                valor_total = producto.cantidad * producto.precio_unitario
                f.write("{:<15} {:<10} ${:<15} ${:<15} {:<10}\n".format(producto.nombre, producto.cantidad, producto.precio_unitario, valor_total, producto.ubicacion))

def main(): 
    inventario = Inventario()

    print("-------------------------------------------------------")
    print("   Práctica 1 - Lenguajes Formales y de Programación    ")
    print("-------------------------------------------------------")
    print("# Sistema de Inventario: ")

#Menú
    while True:

        print("\nMenú Principal:")
        print("1. Cargar Inventario Inicial")
        print("2. Cargar Instrucciones de Movimientos")
        print("3. Crear Informe de Inventario")
        print("4. Salir")
        opcion = input("Inrese una opción: ")

        if opcion == '1':
            archivo_inventario = input("Ingrese el nombre del archivo (.inv): ")
            inventario.cargar_inventario_inicial(archivo_inventario)
            print("\n----------------------------------------")
            print("Inventario Inicial Cargado Exitosamente.")
            print("----------------------------------------")

        elif opcion == '2':
            archivo_movimientos = input("Ingrese el nombre del archivo (.mov): ")
            inventario.cargar_instrucciones_movimientos(archivo_movimientos)
            print("\n---------------------------------------------------")
            print("Instrucciones de Movimientos Cargados Exitosamente.")
            print("----------------------------------------------------")
            
        elif opcion == '3':
            archivo_informe = input("Ingrese el nombre del archivo de informe (.txt): ")
            inventario.crear_informe_inventario(archivo_informe)
            print("\n----------------------------------------")
            print(f"Informe de inventario creado en '{archivo_informe}'.")
            print("----------------------------------------")
            

        elif opcion == '4':
            print("------------------------")
            print("Saliendo del programa.")
            print("------------------------")
            break

        else:
            print("\nOpción Inválidad. Por favor, ingresar una opción válida.")

if __name__ == "__main__":
    main()