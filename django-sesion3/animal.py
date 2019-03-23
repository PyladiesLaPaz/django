# This Python file uses the following encoding: utf-8
class Perro:
    tipo = 'canino'                 # variable de clase compartida por todas las instancias
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre        # variable de instancia única para la instancia
        self.raza=raza
        self.edad=edad
        self.trucos = []    # crea una nueva lista vacía para cada perro


    def agregar_truco(self, truco):
        self.trucos.append(truco)



d = Perro('Fido','Collie','6')
e = Perro('Buddy','','')
d.tipo                    # compartido por todos los perros
e.tipo                    # compartido por todos los perros
d.nombre                  # único para d
e.nombre                  # único para e


print (d.tipo,d.nombre,d.raza,d.edad)
print (e.tipo,e.nombre,e.raza,e.edad)

d.agregar_truco= raw_input("Adicione el nuevo truco "+str()+":")
print ("El nuevo truco adicionado es")

print (d.tipo,d.nombre,d.raza,d.edad,d.agregar_truco)

