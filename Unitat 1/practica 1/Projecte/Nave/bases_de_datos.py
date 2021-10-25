import sqlite3
from sqlite3 import Error


def sql_conection():
    try:
        con = sqlite3.connect('points.db')
        return con

    except Error:
        print(Error)

con =sql_conection()
def sql_table():
    cursorobj = con.cursor()

    try:
        cursorobj.execute("create table if not exists points (puntaje_maximo integer not null)");
    except Error:
        print(Error)

    con.commit()


def sql_insert(puntuacion_max, punt_max_ant):
    cursorobj = con.cursor()

    if punt_max_ant == 0:
        cursorobj.execute('INSERT INTO points VALUES ({})'.format(puntuacion_max))
    else:
        sql_update(puntuacion_max)

    con.commit()
    con.close()


def sql_update( puntuacion_max):
    cursorobj = con.cursor()
    cursorobj.execute('UPDATE points SET puntaje_maximo={}'.format(puntuacion_max))
    con.commit()


def sql_read(self):
    cursorobj = self.con.cursor()
    cursorobj.execute('select puntaje_maximo from points')
    valor = cursorobj.fetchone()
    self.con.close()
    return valor[0]

