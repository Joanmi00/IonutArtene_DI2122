import sqlite3
from sqlite3 import Error

import juego


def sql_conection():
    """Devuelve la conexion a la base de datos
        Parametros:
            sqlite3.connect : funcion que crea una conexion con la bd
            points.db : base de datos que contiene la informacion en  sqlite3

        Torna:
            con : variable que contiene la conexion que establece sqlite.connect"""
    try:

        con = sqlite3.connect('points.db')
        return con

    except Error:
        print(Error)


con = sql_conection()


def sql_table():
    "Funcion que crea en la base de datos una table si no existe "
    cursorobj = con.cursor()

    try:
        cursorobj.execute("create table if not exists points (puntaje_maximo integer not null)");
    except Error:
        print(Error)

    con.commit()


def sql_insert(puntuacion_max, punt_max_ant):
    """Funcion que inserta la puntuacion_max en la bd
        si punt_max_ant es 0 inserta la la puntuacion_max
        si puntuacion_max es mayor que punt_max_ant hace un update de la base de datos
        en cualquier otro caso sigue con el programa sin ejecutar"""
    cursorobj = con.cursor()

    if punt_max_ant == 0:
        cursorobj.execute('INSERT INTO points VALUES ({})'.format(puntuacion_max))

    if puntuacion_max > punt_max_ant:
        sql_update(puntuacion_max)

    else:
        return

    con.commit()


def sql_update(puntuacion_max):
    """Esta funcion es llamada porsql_insert para actualizar la informacion en la base de datos"""
    cursorobj = con.cursor()
    cursorobj.execute('UPDATE points SET puntaje_maximo={}'.format(puntuacion_max))
    con.commit()
    con.close()


def sql_read():
    """Funcion que lee la puntuacion guardada en la base de datos"""
    cursorobj = con.cursor()
    cursorobj.execute('select puntaje_maximo from points;')
    valor = cursorobj.fetchone()
    return valor[0]
