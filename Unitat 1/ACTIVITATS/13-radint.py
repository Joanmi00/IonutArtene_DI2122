import random
#finalizado

class ErrorEnterMassaMenut(Exception):
    """Es llançara quan es massa menut el enter introduit"""
    pass


class ErrorEnterMassaGran(Exception):
    """Es llançara quan es massa gran el enter introduit"""
    pass


while True:
    try:
        x = random.randint(0, 100)
        num = input("Ingresa un numero ")
        if num.isdigit():
            if(int(num) > x):
                raise ErrorEnterMassaGran
            elif(int(num) < x):
                raise ErrorEnterMassaMenut

            elif(int(num) == x):
                print("Felicidades has introducido el mismo numero")
                break

        else:
            break

    except ErrorEnterMassaGran:
        print("Has introducido un numero mas grande")

    except ErrorEnterMassaMenut:
        print("Has introducido un numero mas pequeño")
