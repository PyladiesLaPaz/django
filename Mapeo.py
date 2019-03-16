class Mapeo(object):
    def __init__(self, iterable):
        self.lista_de_items = [10]
        self.__actualizar(iterable)

    def actualizar(self, iterable):
        for item in iterable:
            self.lista_de_items.append(item)
            #self.lista_de_items.append= raw_input("Adicione un valor "+str(item)+":")


    __actualizar = actualizar   # copia privada del actualizar() original
   # actualizado=Mapeo()
   # print (actualizado.actualizar)
class SubClaseMapeo(Mapeo):

    def actualizar(self, keys, values):
        # provee una nueva signatura para actualizar()
        # pero no rompe __init__()
        for item in zip(keys, values):
            self.lista_de_items.append(item)
