#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
def resta(x, x2): return x-x2
def suma(x, x2): return x+x2
def multi(x, x2): return x*x2
def div(x, x2): return x/x2


carpeta = os.path.dirname(__file__)


class NoEsUnNumero(Exception):
    """Llançada quan el valor introduït no és vàlid"""
    pass


class OperacionDesconocida(Exception):
    """Llançada quan operacions desconegudes"""
    pass


def lectura():

    try:
        lectura2 = []
        with open(os.path.join(carpeta, "operaciones.txt"), "r+") as f:

            for linea in f:
                # print(linea)
                numero = linea.split(" ")
                global numero1
                tmp = numero[0].split()
                numero1 = tmp[0]
                # print(numero1)
                global signo
                temp = numero[1].split()
                signo = temp[0]
                # print(signo)
                temp2 = numero[2].split()
                global numero2
                numero2 = temp2[0]
                if(signo == "+"):
                    res = suma(int(numero1), int(numero2))

                elif(signo == "*"):
                    res = multi(int(numero1), int(numero2))

                else:
                    raise OperacionDesconocida
                add = str(str(numero1) + " " + str(signo) + " " + str(numero2)+" " + "= " + str(
                        res) + "\n")
                lectura2.append(add)
        escritura(lectura2)

    except NoEsUnNumero:
        print("No es un numero")

    except OperacionDesconocida:
        print("Operación desconocida")

    except:
        print("Todos los demás errores", sys.exc_info()[0])
        pass


def escritura(lectura2):
    with open(os.path.join(carpeta, "operaciones2.txt"), "w") as f:
        f.writelines(lectura2)


lectura()
