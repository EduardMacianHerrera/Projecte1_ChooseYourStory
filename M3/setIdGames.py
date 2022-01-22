from funciones.funciones import *

# Acabar

def setIdGame():

    try:
        conn = createConn()

        cursor = conn.cursor()

        cursor.execute("select ID_GAME from GAME order by ID_GAME desc limit 1")

        check1 = False
        check2 = False

        resultado = cursor.fetchall()
        if resultado == []:
            resultado = ((0,), (0,))
        idGame = resultado[0][0] + 1
        user = input("Usuario: ")
        cursor.execute(f'select ID_USER from USER where username = "{user}"')
        idUser = cursor.fetchall()[0][0]
        check1 = True
        character = input("Character: ")
        cursor.execute(f'select ID_CHARACTER from `CHARACTER` where character_name = "{character}"')
        isChar = cursor.fetchall()[0][0]
        check2 = True
        adventure = input("Adventure: ")
        cursor.execute(f'select ID_ADVENTURE from ADVENTURE where adventure_name = "{adventure}"')
        idAdventure = cursor.fetchall()[0][0]

        if conn.is_connected():
            conn.close()
        insertCurrentGame(idGame, idUser, isChar, idAdventure)
        return
    except IndexError:
        if not check1:
            print("L'usuari no existeix")
            return
        elif not check2:
            print("El personatge no existeix")
            return
        else:
            print("L'aventura no existeix")
            return
