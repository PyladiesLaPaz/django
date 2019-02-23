import os


def menu():
    os.system("clear")
    print(">> Opciones << ")
    print("\t1 Accion 1")
    print("\t2 Accion 2")
    print("\t3 Accion 3")
    print("\t4 Accion 4")
    print("\t0 Salir")


while True:
    menu()

    option = input("Ingresa tu opcion ")

    print(type(option))
    
    if option == "1":
        print("")
        print(1+2)
        input("Se realizo la accion \n... Presiona Enter para continuar ")

    elif option == "2":
        print("")
        print("\n")
        input("Se realizo la accion \n... Presiona Enter para continuar ")
        

    elif option == "3":
        print("")

        print("\n")
        input(" >>> Se realizo la accion \n... Presiona Enter para continuar ")        


    elif option == "4":
        print("")

        print("\n")
        input(" >>> Se realizo la accion \n... Presiona Enter para continuar ")        


    elif option == "5":
        print("")

        print("\n")
        input(" >>> Se realizo la accion \n... Presiona Enter para continuar ")        


    elif option == "0":
        print("Bye ...")
        break

    else:
        print("")
        input("No ingresaste ninguna opcion \n presiona enter para continuar ")
