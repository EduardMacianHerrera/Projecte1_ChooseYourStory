 # Función que tiene que te printe la partida, la das la ID y con esa te hace select de la BBDD de GAME

from createCon import createConn

def Get_GameInfo(ID):
    conexion =createConn()
    cursor =conexion.cursor()
    cursor.execute(f"SELECT * FROM GAME WHERE ID_GAME = {ID};")
    GameInfo = cursor.fetchall()
    if conexion.is_connected():
        conexion.disconnect()
    return GameInfo

print(Get_GameInfo(1))

'''SELECT *
FROM GAME
WHERE ID_GAME = ;'''