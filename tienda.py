from leer import *
from usuario import Usuario
class Tienda:

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
            print("-Usuario nuevo agregado-")
            usu = Usuario(nombre, cedula)
            self.usuarios.append(usu)

    def encontrarUsuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula==cedula:
                return True
        return False
    
    def consultarUsuario(self,cedula):
        encontrado=self.encontrarUsuario(cedula)
        if encontrado:
            for usuario in self.usuarios:
                if usuario.cedula==cedula:
                    print(f"""Nombre: {usuario.nombre}
                              Cedula: {usuario.cedula}""")
        return False
    def consultarUsuarios(self):
        enumerator=1
        for usuario in self.usuarios:
            print(f"""
                ------N{enumerator}------
                Nombre: {usuario.nombre}
                Cedula: {usuario.cedula}""")
            enumerator+=1

    def eliminarUsuario(self, cedula):
        usuario_encontrado = self.encontrarUsuario(cedula)

        if usuario_encontrado:
            self.consultarUsuario(cedula)
            confirmacion = Leer.string("¿Está seguro de eliminar este usuario? (s/n) -> ")

            if confirmacion.lower() == 's':
                # Utilizando enumerate para obtener el índice y valor al mismo tiempo
                for i, usuario in enumerate(self.usuarios):
                    if usuario.cedula == cedula:
                        del self.usuarios[i]
                        print("Usuario eliminado exitosamente.")
                        return

            print("Eliminación cancelada.")
        else:
            print("Usuario no encontrado.")



    def agregarInstrumento(self, instrumento):
        pass

    def consultarStock(self):
        pass
    
    def registrarUsuario(self,):
        pass

    
    def ingresarInstrumentos(self,):
        pass
    
    def consultarInstrumentosVenta(self,):
        pass

    def consultarInstrumentosprestamo(self,):
        pass

    def generarVenta(self,):
        pass

    def generarPrestamo(self,):
        pass

    def cambioPorGarantia(self,):
        pass

    def devolucionInstrumento(self,):
        pass

    def consultarInstrumentoEnBodega(self,):
        pass

    def modificarDisponibilidadInstrumento(self,):
        pass

