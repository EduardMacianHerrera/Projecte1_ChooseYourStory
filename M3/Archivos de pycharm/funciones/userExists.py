from funciones.createCon import createConn

def userExists(user):
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute("select username from USER")
    myresult = mycursor.fetchall()

    user = (user,)
    if user not in myresult:
        return False
    else:
        return True
