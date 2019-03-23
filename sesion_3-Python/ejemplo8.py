class Bolsa:
    def __init__(self):
        self.datos = []
    def agregar(self, x):
        self.datos.append(x)
    def dobleagregar(self, x):
        self.agregar(x)
        self.agregar(x)

"""Otros mensajes que verifican el tipo de la clase o subclase que esta heredando"""
print("Es int o alguna clase derivada de int")
print (isinstance(Bolsa, int))
print("Es True si bool es una subclase de int")
print(issubclass(bool, int))
print("Es False porque float no es una subclase de int")
print(issubclass(float, int))