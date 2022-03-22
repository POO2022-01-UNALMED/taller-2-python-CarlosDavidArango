class Asiento:
    def __init__(self, color, precio, regsitro):
        self.color = color
        self.precio = precio
        self.registro = regsitro
    def cambiarColor(self, color):
        if (color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegstro(self, registro):
        self.regiistro = registro
    def asignarTipo(self, tipo):
        if(tipo == "gasolina" or tipo == "electrico"):
            self.tipo = tipo


class Auto:
    cantdadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        cantidad = 0
        for i in range(len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                cantidad += 1
        return cantidad
    def verificarIntegridad(self):
        integridad = True
        if (self.motor.registro != self.registro):
            integridad = False
        for i in range(len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                if ((self.asientos[i]).registro != self.registro):
                    integridad = False
                    break
        if (integridad):
            return "Auto original"
        else:
            return " Las piezas no son originales"

