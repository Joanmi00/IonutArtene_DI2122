import random



class ErrorEnterMassaMenut(Exception):
    """Es llançara quan es massa menut el enter introduit"""
    pass


class ErrorEnterMassaGran(Exception):
    """Es llançara quan es massa gran el enter introduit"""
    pass


while True:
    try:
        x=random.randint(0,100)
        num = input("Ingresa un numero ")
        if num.isdigit():
            if(int(num)>x):
                raise ErrorEnterMassaGran
            if(int(num)<x):
                raise ErrorEnterMassaMenut
            
            else:

                break


        else:
            break

    except ErrorEnterMassaGran:
      print("Has introducido un numero mas grande")
    
    except ErrorEnterMassaMenut:
      print("Has introducido un numero mas pequeño")
