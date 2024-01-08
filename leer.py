class Leer:
    @staticmethod
    def int(mensaje="Ingrese un entero: "):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print("Error: Por favor, ingrese un entero válido.")

    @staticmethod
    def float(mensaje="Ingrese un número decimal: "):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("Error: Por favor, ingrese un número decimal válido.")

    @staticmethod
    def string(mensaje="Ingrese una cadena de texto: "):
        while True:
            try:
                valor = input(mensaje)
                if valor.isalpha():
                    return valor
                else:
                    raise ValueError("Error: Por favor, ingrese una cadena de texto válida.")
            except ValueError as e:
                print(e)

