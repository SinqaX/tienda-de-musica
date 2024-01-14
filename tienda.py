from leer import *
from usuario import Usuario
from leer import Leer
from instrumentos import IntrumentosAlquiler, IntrumentosVenta
import random
from datetime import datetime
import os
from ventas import Venta
from alquiler import Alquiler
import pickle
class Tienda:

    codigosUtilizados = set()

    def __init__(self):
        self.usuarios = []
        self.instrumentosVenta = []
        self.instrumentosAlquiler = []
        self.ventas = []
        self.ventasSeparado = []
    
    def agregarUsuario(self):
        try:
            nombre = Leer.string("ingrese su nombre -> ")
            cedula = Leer.int("ingrese su numero de cedula sin puntos ni comas -> ")
            usuarioencontrado = self.encontrarUsuario(cedula)
            if not usuarioencontrado:
                self.usuarios.append(Usuario(nombre, cedula))
            else:
                print("el usuario que intenta ingresar ya se encuentra registrado")
        except ValueError:
            print("algo salio mal vuelve a intentarlo")

    def encontrarUsuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula==cedula:
                return usuario
        return None
    
    def consultarUsuario(self, cedula):
        try:
            encontrado=self.encontrarUsuario(cedula)
            if encontrado:
                for usuario in self.usuarios:
                    if usuario.cedula==cedula:
                        print(f"Nombre: {usuario.nombre} \nCedula: {usuario.cedula}\n")
            return False
        except ValueError:
            print("algo salio mal vuelve a intentarlo")

    def mostrarUsuarios(self):
        enumerator=1
        for usuario in self.usuarios:
            print(f"""
                ------N{enumerator}------
                Nombre: {usuario.nombre}
                Cedula: {usuario.cedula}""")
            enumerator+=1

    def eliminarUsuario(self):
        try:
            cedula = Leer.int("ingrese su numero de cedula sin puntos ni comas -> ")
            usuario_encontrado = self.encontrarUsuario(cedula)

            if usuario_encontrado:
                self.consultarUsuario(cedula)
                confirmacion = Leer.string("¿Está seguro de eliminar este usuario? (Si/No) -> ").lower()

                if confirmacion == 'si':
                    # Utilizando enumerate para obtener el índice y valor al mismo tiempo
                    for i, usuario in enumerate(self.usuarios):
                        if usuario.cedula == cedula:
                            del self.usuarios[i]
                            print("Usuario eliminado exitosamente.")
                            return
                else:
                    print("Eliminación cancelada.")
            else:
                print("Usuario no encontrado.")
        except ValueError:
            print("algo salio mal vuelve a intentarlo")
            
    def generarCodigoInstrumento(self,tipo):
        while True:
            if tipo == 1:
                codigo = 1 + random.randint(1, 99)
            elif tipo == 2:
                codigo = 2 + random.randint(1, 99)
            else:
                raise ValueError("Tipo de instrumento no válido")

            if codigo not in self.codigosUtilizados:
                self.codigosUtilizados.add(codigo)
                return codigo
    
    def agregarInstrumento(self):
        try:
            instrumento = Leer.string("ingrese el nombre del instrumento -> ")
            cantidad = Leer.int("ingrese la cantidad de instrumentos que quiere agregar -> ")
            opcion = Leer.int("ingrese su opcion : (1) para instrumentos de ventas, (2) para intrumentos de alquiler -> ")
            if opcion == 1:
                codigo = self.generarCodigoInstrumento(opcion)
                encontrarinstrumento = self.encontrarIntrumentoVenta(codigo)
                if not encontrarinstrumento:
                    valor = Leer.int("ingrese el costo del instrumento -> ")
                    self.instrumentosVenta.append(IntrumentosVenta(instrumento, codigo, cantidad, valor))
                    print("\ninstrumento agregado exitosamente")
                else:
                    print("el instrumento que intenta ingresar ya se encuentra registrado ")
            elif opcion == 2:
                codigo = self.generarCodigoInstrumento(opcion)
                encontrarinstrumento = self.encontrarIntrumentoAlquiler(codigo)
                if not encontrarinstrumento:
                    valor = Leer.int("ingrese el valor del alquiler del instrumento -> ")
                    self.instrumentosAlquiler.append(IntrumentosAlquiler(instrumento, codigo, cantidad, valor))
                    print("\ninstrumento agregado exitosamente")
                else:
                    print("el instrumento que intenta ingresar ya se encuentra registrado ")
            else:
                raise ValueError("la opcion que ingresaste no es valida -> ")
        except ValueError:
            print("algo salio mal vuelve a intentarlo -> ")

    def encontrarIntrumentoVenta(self, codigo):
        for instrumento in self.instrumentosVenta:
            if instrumento.codigo == codigo:
                return instrumento
        return None
    
    def encontrarIntrumentoAlquiler(self, codigo):
        for instrumento in self.instrumentosAlquiler:
            if instrumento.codigo == codigo:
                return instrumento
        return None

    def consultarStock(self):
        self.consultarInstrumentosAlquiler()
        self.consultarInstrumentosVenta()

    def consultarInstrumentosVenta(self):
        if len(self.instrumentosVenta) == 0:
            print("no hay instrumentos agregados")
        else:
            print("\nINSTRUMENTO PARA VENTA\n")
            for instrumento in self.instrumentosVenta:
                print(instrumento)

    def consultarInstrumentosAlquiler(self):
        if len(self.instrumentosAlquiler) == 0:
            print("no hay instrumentos agregados")
        else:
            print("\nINSTRUMENTO PARA ALQUILER\n")
            for instrumento in self.instrumentosAlquiler:
                print(instrumento)
    
    def eliminarInstrumento(self):
        try:
            codigo = Leer.int("ingrese el codigo del instrumento que desea eliminar -> ")
        except ValueError:
            print("Error: El código debe ser un número entero.")
            return

        instrumento_venta = self.encontrarIntrumentoVenta(codigo)
        instrumento_alquiler = self.encontrarIntrumentoAlquiler(codigo)

        if instrumento_venta or instrumento_alquiler:
            confirmacion = Leer.string(f"¿Estás seguro de eliminar el instrumento con código {codigo}? (Sí/No): ").lower()
            if confirmacion == 'si':
                if instrumento_venta:
                    self.instrumentosVenta.remove(instrumento_venta)
                if instrumento_alquiler:
                    self.instrumentosAlquiler.remove(instrumento_alquiler)
                print("\nInstrumento eliminado exitosamente")
            else:
                print("Eliminación cancelada")
        else:
            print("El instrumento no se encuentra en la lista")

    def generarAlquiler(self):
        self.consultarInstrumentosAlquiler()
        try:
            codigo = Leer.int("ingrese el codigo del instrumento que se va alquilar -> ")
            cedula = Leer.int("ingrese la cedula del usuario que quiere alquilar el instrumento -> ")
            instrumento = self.encontrarIntrumentoAlquiler(codigo)
            usuario = self.encontrarUsuario(cedula)
            if instrumento and usuario:
                if instrumento.disponible:
                    if instrumento.cantidad > 0:
                        tiempo = Leer.int("ingrese el tiempo que quiere alquilar el instrumento (en dias) -> ")
                        salvamento = Leer.string("para generar su alquiler debe dejar su cedula como salvamento de el alquiler, acepta (Si/No) -> ").lower()
                        if salvamento == "si":
                            
                                alquiler = Alquiler(usuario.nombre, cedula, tiempo, instrumento.nombre, instrumento.valorAlquiler*tiempo)  
                                alquiler.salvamento = True
                                usuario.prestamos.append(alquiler)
                                instrumento.cantidad -=1
                                print(f"\nalquiler exitoso. {usuario.nombre}  ha pedido prestado el instrumento :{instrumento.nombre} por {tiempo} dias con un costo de ${instrumento.valorAlquiler*tiempo} ")
                        elif salvamento == "no":
                            print("lo sentimos pero para poder hacer el alquiler del prestamo es obligatorio dejar el salvamento")
                        else:
                            print("la opcion que ingresaste no es valida")
                else:
                    print("El instrumento no está disponible para ser alquilado")
            else:
                print("instrumento o usuario no encontrados.")   
        except ValueError:
            print("algo salio mal vuelve a intentarlo")
        
    def encontrarIntrumentoAlquilerPorNombre(self, nombre):
        for instrumento in self.instrumentosAlquiler:
            if instrumento.nombre == nombre:
                return instrumento
        return None

    def devolucionAlquiler(self):
        try:
            cedula = Leer.int("Ingrese la cedula del usuario que está devolviendo el instrumento alquilado -> ")
            usuario = self.encontrarUsuario(cedula)

            if usuario and len(usuario.prestamos) > 0:
                print("\nInstrumentos en préstamo:")
                for i, alquiler in enumerate(usuario.prestamos, start=1):
                    print(f"{i}. {alquiler.nombreInstrumento} (Factura N° {alquiler.numeroFactura})")

                opcion = Leer.int("\nIngrese el número de factura del instrumento que desea devolver -> ")

                if 1 <= opcion <= len(usuario.prestamos):
                    alquiler_devuelto = usuario.prestamos[opcion - 1]
                    alquiler_devuelto.salvamento = False  # Desactivar el salvamento
                    instrumento = self.encontrarIntrumentoAlquilerPorNombre(alquiler_devuelto.nombreInstrumento)
                    instrumento.cantidad += 1  # Aumentar la cantidad disponible del instrumento
                    usuario.prestamos.remove(alquiler_devuelto)
                    print(f"\nDevolución exitosa. {usuario.nombre} ha devuelto el instrumento {alquiler_devuelto.nombreInstrumento}.")
                else:
                    print("Opción inválida.")
            else:
                print("Usuario no encontrado o no tiene instrumentos en préstamo.")
        except ValueError:
            print("Algo salió mal. Vuelve a intentarlo.")
    
    def prestamosUsuario(self, cedula):
        usuario = self.encontrarUsuario(cedula)
        if usuario:
            for alquileres in usuario.prestamos:
                print(alquileres)
        else:
            print("el usuario no se encuentra registrado ")

        
    def consultarPrestamosUsuario(self):
        try:
            cedula = Leer.int("ingrese la cedula del usuario que quiere consultar por sus prestamos -> ")
            encontrado = self.encontrarUsuario(cedula)
            if encontrado:
                if len(encontrado.prestamos) > 0:
                    self.prestamosUsuario(cedula)
                else:
                    print("el usuario no tiene prestamos pendientes por el momento ")
            else:
                print("el usuario no se encuentra registrado")
        except ValueError:
            print("algo salio mal vuelve a intentarlo")

    def guardarDatos(self):
        try:
            #cambiar ruta para el archivo para que les funciones
            nombre_archivo = "C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\tienda-de-musica\\datosTIendaMusica"
            with open(nombre_archivo, 'wb') as archivo:
                datos_tienda = {
                    'usuarios': self.usuarios,
                    'instrumentosVenta': self.instrumentosVenta,
                    'instrumentosAlquiler': self.instrumentosAlquiler,
                    'ventas': self.ventas,
                    'ventasSeparado': self.ventasSeparado
                }
                pickle.dump(datos_tienda, archivo)
            print(f"Datos guardados exitosamente en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargarDatos(self):
        try:
            #cambiar ruta para el archivo para que les funciones
            nombre_archivo = "C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Segundo_Semestre_U\\tienda-de-musica\\datosTIendaMusica"
            with open(nombre_archivo, 'rb') as archivo:
                datos_tienda = pickle.load(archivo)
                self.usuarios = datos_tienda['usuarios']
                self.instrumentosVenta = datos_tienda['instrumentosVenta']
                self.instrumentosAlquiler = datos_tienda['instrumentosAlquiler']
                self.ventas = datos_tienda['ventas']
                self.ventasSeparado = datos_tienda['ventasSeparado']
            print(f"Datos cargados exitosamente desde {nombre_archivo}")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    def generarVenta(self,):
        totalPagar = 0 
        ced = Leer.string('Cedula del cliente-> ')
        fechHorActual = datetime.now()
        fech = fechHorActual.strftime("%Y-%m-%d")
        opcion = Leer.int('Ingrese la opcion: (1)Venta de contado (2)Venta separado ')
        if opcion==1:
            productos = []
            while True:
                self.consultarInstrumentosVenta()
                codigo = Leer.string('Ingrese el codigo del instrumento-> ')
                instrumento = self.encontrarIntrumentoVenta(codigo)
                if instrumento==None:
                    print('El instrumento no se ha encontrado...')
                    os.system('pause')
                else:
                    if instrumento.cantidad<0:
                        print('No hay mas unidades de este instrumento...')
                        os.system('pause')
                        continue
                    else:
                        i=0
                        while i<len(self.instrumentosVenta):
                            if codigo==self.instrumentosVenta[i].codigo:
                                self.instrumentosVenta[i].codigo -= 1
                                totalPagar += self.instrumentosVenta[i].valorIntrumento
                                print('Venta satisfactoria ...')
                                productos.append(self.instrumentosVenta[i])
                                break
                            i+=1
                        a = Leer.string('Desea ingresar un nuevo producto? (s/n) -> ')
                        if a.lower()=='s':
                            continue
                        elif a.lower()=='n':
                            break
                        else:
                            print('Opcion no valida...')
                            os.system('pause')
            venta = Venta(ced,fech,totalPagar)
            venta.productos=productos 
        elif opcion==2:
             pass
                             


    # def generarPrestamo(self,):
    #     pass

    # def cambioPorGarantia(self,):
    #     pass

    # def devolucionInstrumento(self,):
    #     pass

    # def modificarDisponibilidadInstrumento(self,):
    #     pass

tienda = Tienda()
tienda.cargarDatos()
# tienda.agregarUsuario()
# tienda.agregarUsuario()
tienda.mostrarUsuarios()
# tienda.eliminarUsuario()
# tienda.mostrarUsuarios() # Verificar que el usuario fue eliminado
# tienda.agregarInstrumento()
# tienda.agregarInstrumento()
tienda.consultarStock()
tienda.guardarDatos()
# tienda.eliminarInstrumento()
# tienda.consultarStock()
tienda.generarAlquiler()
tienda.consultarPrestamosUsuario()
tienda.devolucionAlquiler()
tienda.consultarPrestamosUsuario()
# tienda.consultarPrestamosUsuario()
# tienda.generarVenta()

    #MODIFICACION FUNCIONES ALQUILER 

    # #CONSULTAR ALQUILER
        
    

    #DEVOLVER ALQUILER
        
    # def devolver_recurso(self, codigo_recurso):
    #     recurso = self.buscar_recurso(codigo_recurso)
    #     if recurso:
    #         prestamo = next((p for p in self.prestamos if p.recurso == recurso), None)
    #         if prestamo:
    #             prestamo_usuario_nombre = f"{prestamo.usuario.tipo} {prestamo.usuario.nombre}"
    #             self.prestamos.remove(prestamo)
    #             recurso.disponible = True
    #             print(f"Devolución exitosa. {prestamo_usuario_nombre} ha devuelto {recurso.nombre}.")
    #         else:
    #             print(f"El recurso {recurso.nombre} no está prestado actualmente.")
    #     else:
    #         print("Recurso no encontrado.")


            







