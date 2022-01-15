from createCon import createConn

def getReplayAdventures():
    conexion =createConn()
    cursor =conexion.cursor()
    # Esta query es provisional para testear que la conexión se ha hecho correctamente,
    # no es la del ejercicio
    cursor.execute("SELECT * FROM GAME")
    resReplay = cursor.fetchall()
    # Proceso de desconexión, en el fallo de la query de debajo
    # se comprueba que la connexión no esta hecha
    if conexion.is_connected():
        conexion.disconnect()
    # cursor.execute("SELECT * FROM ADVENTURE")
    # res2 =cursor.fetchall()

    return res2

print(getReplayAdventures())