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
            usu = Usuario(nombre, cedula)
            self.usuarios.append(usu)

    def encontrarUsuario(self, cedula):
        if cedula not in self.usuarios:
            return True
        return False

    def agregarInstrumento(self, instrumento):
        pass

    def consultarStock(self):
        pass
    
    def registrarUsuario(self,):
        pass

    def iniciarSesion(self,):
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

    
