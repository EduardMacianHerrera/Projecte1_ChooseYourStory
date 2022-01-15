from funciones.checkUserbdd import createConn

def getUsers():
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute("select username, password, ID_USER from USER")
    myresult = mycursor.fetchall()

    diccFinal = {}

    for i in myresult:
        diccTemp = {i[0]:{"password": i[1],"idUser": i[2]}}
        diccFinal.update(diccTemp)

    return diccFinal
