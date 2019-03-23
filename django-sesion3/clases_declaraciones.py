# This Python file uses the following encoding: utf-8
def prueba_ambitos():
    def hacer_local():
        algo = "algo local"
    #def hacer_nonlocal():
    #    nonlocal algo
    #    algo = "algo no local"
    def hacer_global():
        global algo
        algo = "algo global"
    algo = "algo de prueba"
    hacer_local()
    print("Luego de la asignacion local:", algo)
    #hacer_nonlocal()
    #print("Luego de la asignacion no local:", algo)
    hacer_global()
    print("Luego de la asignación global:", algo)

prueba_ambitos()
print("-------------")
print("In global scope:", algo)