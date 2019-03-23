# This Python file uses the following encoding: utf-8

class Padre(object):
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def funcion_metodo_clase_padre_1(self):
        print self.p1,"Ejecuta una funcion/método de clase padre"

    def funcion_metodo_clase_padre_2(self):
        print self.p2,"Ejecuta una funcion/método de clase padre"



class Hija(Padre):
    def __init__(self,p1,p2,p3,h1,h2):
        Padre.__init__(self, p1,p2,p3)
        self.h1 = h1
        self.h2 = h2

    def funcion_metodo_clase_hija_1(self):
        print self.p1,"metodo hija"



class Nieta(Hija):
    def __init__(self, p1,p2,p3,h1,h2,n1,n2):
        Hija.__init__(self,p1,p2,p3,h1,h2)
        self.n1 = n1
        self.n2 = n2

    def funcion_metodo_clase_nieta_1(self):
        print self.p1,"metodo nieta"

p1 = 2
p2 = 4
p3 = 6
h1 = 3
h2 = 5
n1 = 10
n2 = 20  

hija = Hija(p1,p2,p3,h1,h2)     
hija.funcion_metodo_clase_padre_1()
hija.funcion_metodo_clase_padre_2()
hija.funcion_metodo_clase_hija_1()
nieta = Nieta(p1,p2,p3,h1,h2,n1,n2)     
nieta.funcion_metodo_clase_nieta_1()
nieta.funcion_metodo_clase_padre_1()