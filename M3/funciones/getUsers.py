from funciones.checkUserbdd import createConn

def getUsers():
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute("select username, password, ID_USER from USER")
    myresult = mycursor.fetchall()



