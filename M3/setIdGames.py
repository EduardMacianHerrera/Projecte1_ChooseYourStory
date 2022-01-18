from funciones.funciones import *

# Acabar

def setIdGame():
    conn = createConn()

    cursor = conn.cursor()

    cursor.execute("select ID_GAME from GAME order by ID_GAME desc limit 1")

    resultado = cursor.fetchall()
    idGame = resultado[0][0] + 1
    user = input("Usuario: ")
    cursor.execute(f'select ID_USER from USER where username = "{user}"')
    idUser = cursor.fetchall()[0][0]
    character = input("Character: ")
    cursor.execute(f'select ID_CHARACTER from `CHARACTER` where character_name = "{character}"')
    isChar = cursor.fetchall()[0][0]
    adventure = input("Adventure: ")
    cursor.execute(f'select ID_ADVENTURE from ADVENTURE where adventure_name = "{adventure}"')
    idAdventure = cursor.fetchall()[0][0]
    insertCurrentGame(idGame,idUser,isChar,idAdventure)



setIdGame()

