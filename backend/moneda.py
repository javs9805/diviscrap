import datetime

class Moneda:
    nombre: str
    compra: float
    venta: float
    def __init__(self,nombre,compra,venta,timestamp):
        self.nombre = nombre
        self.compra = compra
        self.venta = venta
        self.timestamp = timestamp

    def getNombre(self):
        return self.nombre
    def getCompra(self):
        return self.compra
    def getVenta(self):
        return self.venta
    def getTimestamp(self):
        return self.timestamp
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "compra": self.compra,
            "venta": self.venta,
            "timestamp": self.timestamp
        }