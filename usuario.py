class Usuario:
    
    def __init__(self, nombre, contraseña, codigo, tipo):
        self.nombre = nombre
        self.contraseña = contraseña
        self.codigo = codigo
        self.tipo = tipo 
    
    
    def registrarUsuario(self,):
        pass

    def iniciarSesion(self,):
        pass
    
    def habilitarFunciones(self,):
        pass

class Admin(Usuario):

    def __init__(self, nombre, contraseña, codigo, tipo, pinUnicoAdmin):
        super().__init__(nombre, contraseña, codigo, tipo)
        self.pinUnicoAdmin = pinUnicoAdmin
    
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

class Cliente(Usuario):

    def __init__(self, nombre, contraseña, codigo, tipo):
        super().__init__(nombre, contraseña, codigo, tipo)
    
    def consultarInstrumentosVenta(self,):
        pass

    def consultarInstrumentosprestamo(self,):
        pass

    def historialMovimientos(self,):
        pass
    

