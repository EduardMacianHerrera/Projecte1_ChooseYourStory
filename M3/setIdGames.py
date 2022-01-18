from funciones.funciones import *


def setIdGame():
    conn = createConn()

    cursor = conn.cursor()

    cursor.execute("select ID_GAME from GAME order by ID_GAME desc limit 1")

    res = cursor.fetchall()

    lastId = res[0][0]
    return lastId + 1

setIdGame()

