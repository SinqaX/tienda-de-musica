from leer import *
from usuario import Usuario
from leer import Leer
from instrumentos import IntrumentosAlquiler, IntrumentosVenta
import random
from datetime import datetime
import os
from ventas import Venta
from alquiler import Alquiler
class Tienda:

    codigosUtilizados = set()

    def __init__(self):
        self.usuarios = []
        self.instrumentosVenta = []
        self.instrumentosAlquiler = []
        self.ventas = []
        self.ventasSeparado = []
        self.prestamos = []
    
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

    def registrarAlquiler(self):
        self.consultarInstrumentosAlquiler()
        try:
            codigo = Leer.int("ingrese el codigo del instrumento que se va alquilar")
            cedula = Leer.int("ingrese la cedula del usuario que quiere alquilar el instrumento")
            instrumento = self.encontrarIntrumentoAlquiler(codigo)
            usuario = self.encontrarUsuario(cedula)
            if instrumento and usuario:
                if instrumento.disponible:
                    tiempo = Leer.int("ingrese el tiempo que quiere alquilar el instrumento (en dias) -> ")
                    alquiler = Alquiler(usuario.nombre, cedula, tiempo, instrumento.nombre, instrumento.valorAlquiler*tiempo)
                    self.prestamos.append(alquiler)
                    instrumento.disponible = False
                    print(f"alquiler exitoso. {usuario.nombre}  ha pedido prestado el instrumento :{instrumento.nombre} por {tiempo} dias. ")
                else:
                    print("El instrumento no está disponible para ser alquilado")
            else:
                print("instrumento o usuario no encontrados.")   
        except ValueError:
            print("algo salio mal vuelve a intentarlo")


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

# tienda = Tienda()

# tienda.agregarUsuario()
# tienda.agregarUsuario()
# tienda.mostrarUsuarios
# tienda.eliminarUsuario()
# tienda.mostrarUsuarios() # Verificar que el usuario fue eliminado
# tienda.agregarInstrumento()
# tienda.agregarInstrumento()
# tienda.consultarStock()
# tienda.eliminarInstrumento()
# tienda.consultarStock()
        

    #MODIFICACION FUNCIONES ALQUILER 

    # #CONSULTAR ALQUILER
        
    # def consultar_recursos_prestados_usuario(self, codigo_usuario):
    #     usuario = self.buscar_usuario(codigo_usuario)
    #     if usuario:
    #         prestamos_usuario = [p.recurso.nombre for p in self.prestamos if p.usuario == usuario]
    #         if prestamos_usuario:
    #             print(f"{usuario.tipo} {usuario.nombre} tiene los siguientes recursos prestados:")
    #             for recurso_nombre in prestamos_usuario:
    #                 print(f"- {recurso_nombre}")
    #         else:
    #             print(f"{usuario.tipo} {usuario.nombre} no tiene recursos prestados actualmente.")
    #     else:
    #         print("Usuario no encontrado.")

    # #DEVOLVER ALQUILER
        
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


            







