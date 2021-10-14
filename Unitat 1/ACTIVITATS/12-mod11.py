#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
# base_url:os.path.dirname(os.path.abspath(__file__))
# open(os.path.join("operaciones.txt"))


numero1 = 0
numero2 = 0
signo = ""
resultado = 0


class NoEsUnNumero(Exception):
    """Llançada quan el valor introduït no és vàlid"""
    pass


class OperacionDesconocida(Exception):
    """Llançada quan operacions desconegudes"""
    pass


def lectura():
    try:
        with open(os.path.join("operaciones.txt"), "r+") as f:
            for linea in f:
               # print(linea)
                numero = linea.split(" ")
                global numero1
                tmp = numero[0].split()
                numero1 = int(tmp[0])
               # print(numero1)
                global signo
                temp = numero[1].split()
                signo = temp[0]
               # print(signo)
                temp2 = numero[2].split()
                global numero2
                numero2 = int(temp2[0])
                if(type(numero1) != int):
                    raise NoEsUnNumero
                if(signo == "+"):
                    def resultado(x, x2): return x+x2
                    print(str(numero1), signo, str(numero2), "=",
                          str(resultado(int(numero1), int(numero2))))
                

                if(signo == "*"):
                    def resultado(x, x2): return x*x2
                    print(numero1, signo, numero2, "=",
                          str(resultado(int(numero1), int(numero2))))

                #else:
                 #   raise OperacionDesconocida
    except NoEsUnNumero:
        print("No es un numero")

    except OperacionDesconocida:
        print("Operación desconocida")

    except:
        print("Todos los demás errores", sys.exc_info()[0])
        pass


lectura()
