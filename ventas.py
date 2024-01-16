class Venta:

    def _init_(self, cedulaCliente, fecha, totalPagar):
        self.cedulaCliente = cedulaCliente
        # self.nombreInstrumento = nombreInstrumento -----> BORRAR, YA HAY PRODUCTOS
        self.fecha = fecha
        self.productos = []
        self.totalPagar = totalPagar

    def generarFacturaVenta(self,):
        pass
class VentaSeparado(Venta):

    def _init_(self, nombreCliente, fecha, totalPagar):
        super()._init_(nombreCliente, fecha, totalPagar)
        self.abono = 0
        self.productos = []
    


