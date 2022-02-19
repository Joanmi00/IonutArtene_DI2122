import sqlite3
from sqlite3 import Error
import os


def sql_conection():
    """Devuelve la conexion a la base de datos
        Parametros:
            sqlite3.connect : funcion que crea una conexion con la bd
            points.db : base de datos que contiene la informacion en  sqlite3

        Torna:
            con : variable que contiene la conexion que establece
                                    sqlite.connect"""
    try:

        con = sqlite3.connect(os.path.join(os.path.dirname(
            __file__), 'bd/user.db'))
        return con

    except Error:
        print(Error)


con = sql_conection()


def sql_read(user, password):
    valor_retorn = ""
    """Funcion que lee la puntuacion guardada en la base de datos
                    en caso contrario devuelve 0"""
    cursorobj = con.cursor()
    cursorobj.execute(
        'select * from Users WHERE user=\'{}\' AND  password={};'.format(user, password))
    try:
        valor_retorn = cursorobj.fetchone()

    except:
        valor_retorn = ""
    return valor_retorn
