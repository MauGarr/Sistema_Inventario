
print("-------------------------------------------------------")
print("   Práctia 1 - Lenguajes Formales y de Programación    ")
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