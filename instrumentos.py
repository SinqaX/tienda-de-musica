class Instrumento:
    
    def __init__(self, nombre, codigo, cantidad):
        self.nombre = nombre
        self.codigo = codigo
        self.cantidad = cantidad
        

    def consultarDisponibilidad(self,):
        pass

class IntrumentosAlquiler(Instrumento):

    def __init__(self, nombre, codigo, cantidad, valorAlquiler):
        super().__init__(nombre, codigo, cantidad)
        self.valorAlquiler = valorAlquiler
        self.disponible = True

    def __str__(self):
        return f"Instrumento : {self.nombre} \nCódigo: {self.codigo} \nCantidad: {self.cantidad} \nValor de Alquiler: {self.valorAlquiler}\n"


class IntrumentosVenta(Instrumento):

    def __init__(self, nombre, codigo, cantidad, valorIntrumento):
        super().__init__(nombre, codigo, cantidad)
        self.valorIntrumento = valorIntrumento
    
    def __str__(self):
        return f"Instrumento : {self.nombre} \nCódigo: {self.codigo} \nCantidad: {self.cantidad} \nValor del instrumento: {self.valorIntrumento}\n"



