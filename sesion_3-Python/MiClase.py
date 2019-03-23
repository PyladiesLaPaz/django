# This Python file uses the following encoding: utf-8

class MiClase:
    """Simple clase de ejemplo"""
    i = 12345
    def f(self):
        return ('Hola mundo')
    def __init__(self):
        self.datos = [1,2]

x = MiClase()
print (x.i)
print x.f()
print (x.datos)
'''Lo que tienen de especial los métodos es que el objeto es pasado como el primer argumento de la función. 
En nuestro ejemplo, la llamada x.f() es exactamente equivalente a MiClase.f(x)'''
#xf = x.f
#while True:
#    print(xf())