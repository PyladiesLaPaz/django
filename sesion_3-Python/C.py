# This Python file uses the following encoding: utf-8
# Función definida fuera de la clase
def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1
    def g(self):
        return 'hola mundo'
    h = g
new=C()
#print f.min
print new.g()
print new.f(23,4)