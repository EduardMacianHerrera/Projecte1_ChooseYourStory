from createCon import createConn

def getIdGame():
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute("select ID_GAME from GAME")
    resultado = mycursor.fetchall()


    lista = []

    for i in resultado:
        lista.append(i[0])

    tupla0 = tuple(lista)

    if proyecto.is_connected():
        proyecto.close()

    return tupla0
print(getIdGame())