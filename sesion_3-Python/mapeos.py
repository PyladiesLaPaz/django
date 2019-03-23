class Mapeo:
    def __init__(self, iterable):
        self.lista_de_items = []
        self.__actualizar(iterable)

    def actualizar(self, iterable):
        for item in iterable:
            self.lista_de_items.append(item)

    __actualizar = actualizar   # copia privada del actualizar() original

    #actualizado=Mapeo()
    #print (actualizado.actualizar)

class SubClaseMapeo(Mapeo):

    def actualizar(self, keys, values):
        # provee una nueva signatura para actualizar()
        # pero no rompe __init__()
        for item in zip(keys, values):
            self.lista_de_items.append(item)