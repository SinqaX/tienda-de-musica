import os
from tienda import *
#documento donde van a ir los menus y algunas funciones

    
def main():
    while True:
        try:
            os.system("cls")
            print("\n------------- Menú Principal -------------")
            print("1. Manejo de Usuarios")
            print("2. Manejo de Ventas")
            print("3. Manejo de Alquiler")
            print("4. Manejo de Inventario")
            print('------------------------------------------------------')
            print("0. Salir")
            opcion=Leer.int("Digite la opcion que desea seleccionar-> ")
            match opcion:
                case 1:
                    os.system("cls")
                    mostrar_menu_usuario()
                    os.system("pause")
                case 2:
                    os.system("cls")
                    mostrar_menu_venta()
                    os.system("pause")

                case 3:
                    os.system("cls")
                    mostrar_menu_Alquiler()
                    os.system("pause")

                case 4:
                    os.system("cls")
                    mostrar_menu_inventario()
                    os.system("pause")

                case 0:
                    tienda.guardarDatos()
                    print("Saliendo del programa...")
                    
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    os.system("pause")
                    main()
        except ValueError:
            print("algo salio mal vuelve a intentarlo")

def mostrar_menu_usuario():
    while True:
        try:
            os.system("cls")
            print("\n------------- Menú Manejo de Usuarios -------------")
            print("1. Agregar Usuario")
            print("2. Consultar Usuario")
            print("3. Eliminar Usuario")
            print("4. Mostrar Usuarios")
            print('------------------------------------------------------')
            print("0. Volver al menú principal")
            opcion=Leer.int("Digite la opcion que desea seleccionar-> ")
            match opcion:
                case 1:
                    os.system("cls")
                    tienda.agregarUsuario()
                    os.system("pause")
                case 2:
                    os.system("cls")
                    tienda.consultarUsuario()
                    os.system("pause")

                case 3:
                    os.system("cls")
                    tienda.eliminarUsuario()
                    os.system("pause")

                case 4:
                    os.system("cls")
                    tienda.mostrarUsuarios()
                    os.system("pause")

                case 0:
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    os.system("pause")
                    mostrar_menu_usuario()
        except ValueError:
            print("algo salio mal vuelve a intentarlo")


def mostrar_menu_venta():
    print("\n------------- Menú Manejo de Ventas -------------")
    print("1. Generar Venta")
    print("2. Consultar Venta")
    print("4. Eliminar Venta")
    print("5. Mostrar Ventas")
    print('------------------------------------------------------')
    print("0. Salir")

def mostrar_menu_Alquiler():
    while True:
        try:
            os.system("cls")
            print("\n------------- Menú Manejo de Alquileres -------------")
            print("1. Generar Alquiler de Instrumento")
            print("2. Consultar Alquiler")
            print("3. Devolucion de Alquiler")
            print("4. Mostrar Alquileres")
            print('------------------------------------------------------')
            print("0. Salir")
            opcion=Leer.int("Digite la opcion que desea seleccionar-> ")
            match opcion:
                case 1:
                    os.system("cls")
                    tienda.generarAlquiler()
                    os.system("pause")
                case 2:
                    os.system("cls")
                    tienda.consultarPrestamosUsuario()
                    os.system("pause")

                case 3:
                    os.system("cls")
                    tienda.devolucionInstrumento()
                    os.system("pause")

                case 4:
                    os.system("cls")
                    pass
                    os.system("pause")

                case 0:
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    os.system("pause")
                    mostrar_menu_Alquiler()
        except ValueError:
            print("algo salio mal vuelve a intentarlo")

def mostrar_menu_inventario():
    print("\n------------- Menú Manejo de Inventario -------------")
    print("1. Agregar Instrumento")
    print("2. Consultar Instrumento")
    print("3. Mostrar Instrumentos")
    print("4. Eliminar Instrumento")
    print('------------------------------------------------------')
    print("0. Salir")


if __name__=="__main__":
    main()