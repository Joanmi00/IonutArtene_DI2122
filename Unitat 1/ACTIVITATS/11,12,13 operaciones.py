#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


numero1 = 0
numero2 = 0
signo = ""
datos2 = []


def lectura():
 try:
    with open("operaciones.txt", "r") as f:
        for linea in f:
            print (linea)
            global numero1
            numero1 = linea[0]
           # print(numero1)
            global signo
            signo = linea[1]
           # print(signo)
            global numero2
            numero2 = linea[2]
            #print(numero2)
            operaciones(signo, int(numero1), int(numero2))
 except IndexError as index:
     print("Ha habido un error tipo index",index) 
     pass

 except ZeroDivisionError as zerro:
     print("ha habido un error2",zerro)
     pass

 except:
  print("todos los errores",sys.exc_info()[0])
  pass

def operaciones(signo, numero1, numero2):
    if(signo == "+"):
        def suma(x, x2): return x+x2
        print(suma(numero1, numero2))
        return
        

    if(signo == "*"):
        def multi(x, x2): return x*x2
        print(multi(numero1, numero2))
        return
        


lectura()

