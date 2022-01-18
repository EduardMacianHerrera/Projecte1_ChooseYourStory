from funciones.createCon import createConn

# Poner la id

def insertUser(user,password):
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute(
        f'insert into USER (username,password,user_creation,date_creation,date_mod,user_mod) values ("{user}","{password}",user(),now(),now(),user())')
    mydb.commit()

