import sqlite3
from sqlite3 import Error
import os


def sql_conection():
    """Devuelve la conexion a la base de datos
        Args:
            sqlite3.connect : funcion que crea una conexion con la bd
            users.db : base de datos que contiene la informacion en  sqlite3

        T:
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
    """Funcion que lee los usuarios guardados en la base de datos


    Args:
        user (Str): Parametro que lo recibe de la vista segun lo que ponga el usuario
        password (Integer): Parametro que lo recibe de la vista segun lo que ponga el usuario

    Returns:
        valor_retorn : Si la base de datos le devuelve informacion 
                        devolvera esa info si no devolvera vacio
    """
    valor_retorn = ""

    cursorobj = con.cursor()
    cursorobj.execute(
        'select * from Users WHERE user=\'{}\' AND  password={};'.format(user, password))
    try:
        valor_retorn = cursorobj.fetchone()

    except:
        valor_retorn = ""
    return valor_retorn
