from usuario import Usuario
from leer import Leer
from instrumentos import Instrumento, IntrumentosAlquiler, IntrumentosVenta
import random

class Tienda:
    codigosUtilizados = set()
    def __init__(self):
        self.usuarios = []
        self.instrumentosVenta = []
        self.instrumentosAlquiler = []
        self.ventas = []
        self.ventasSeparado = []
        self.prestamos = []
    
    def agregarUsuario(self, nombre, cedula):
        usuarioencontrado = self.encontrarUsuario(cedula)
        if not usuarioencontrado:
            self.usuarios.append(Usuario(nombre, cedula))
        else:
            print("el usuario que intenta ingresar ya se encuentra registrado")

    def encontrarUsuario(self, cedula):
        if cedula not in self.usuarios:
            return True
        return False

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
    
    def agregarInstrumento(self, instrumento, cantidad):

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
        else: print("la opcion ingresada no es valida ")


        
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
    

    def eliminarInstrumento(self, codigo):
        try:
            codigo = int(codigo)
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



    def generarVenta(self,):
        pass

    def generarPrestamo(self,):
        pass

    def cambioPorGarantia(self,):
        pass

    def devolucionInstrumento(self,):
        pass

    def modificarDisponibilidadInstrumento(self,):
        pass

