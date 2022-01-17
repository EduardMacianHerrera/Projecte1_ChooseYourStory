import mysql.connector


# Edu

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="python",
        password="programa",
        database="project"
    )
    return mydb


def userExists(user):
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute("select username from USER")
    myresult = mycursor.fetchall()
    if mydb.is_connected():
        mydb.close()

    user = (user,)
    if user not in myresult:

        return False
    else:
        return True



def insertUser(id,user,password):
    mydb = createConn()

    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            f'insert into USER (ID_USER,username,password,user_creation,date_creation) values ({id},"{user}","{password}",user(),now())')
        mydb.commit()
        if mydb.is_connected():
            mydb.close()
        return
    except:
        print("La ID de USER ya existe")
        if mydb.is_connected():
            mydb.close()
        return


def insertCurrentGame(idGame,idUser,isChar,idAdventure):
    conn = createConn()

    cursor = conn.cursor()

    try:
        cursor.execute(
            f"insert into GAME(ID_GAME,date,user_creation,date_creation,ID_CHARACTER,ID_USER,ID_ADVENTURE) values ({idGame},now(),user(),now(),{isChar},{idUser},{idAdventure})")

        conn.commit()
        if conn.is_connected():
            conn.close()
        return

    except:
        print("La ID de GAME ya existe")
        if conn.is_connected():
            conn.close()
        return

def getUsers():
    mydb = createConn()

    mycursor = mydb.cursor()
    mycursor.execute("select username, password, ID_USER from USER")
    myresult = mycursor.fetchall()
    if mydb.is_connected():
        mydb.close()
    diccFinal = {}

    for i in myresult:
        diccTemp = {i[0]:{"password": i[1],"idUser": i[2]}}
        diccFinal.update(diccTemp)


    return diccFinal


def getUserIds():
  mydb = createConn()

  mycursor = mydb.cursor()
  mycursor.execute("select username, ID_USER from USER")
  myresult = mycursor.fetchall()

  lista = [[],[]]
  if mydb.is_connected():
      mydb.close()

  for i,n in myresult:
    lista[0].append(i)
    lista[1].append(n)


  return lista


def checkUserbdd(user,password):
  mydb = createConn()

  mycursor = mydb.cursor()
  mycursor.execute("select username from USER")
  myresult = mycursor.fetchall()

  user = (user,)
  if user not in myresult:
    return 0

  mycursor.execute(f"select password from USER where username = '{user[0]}'")
  myresult = mycursor.fetchall()
  if mydb.is_connected():
      mydb.close()

  password = (password,)

  if password not in myresult:
    return -1
  else:
    return 1


def insertCurrentChoice(idGame,actual_id_step,id_answer):
    conn = createConn()
    cursor = conn.cursor()

    cursor.execute(f'insert into RECORD values (user(),now(),null,null,{idGame},{actual_id_step},{id_answer})')
    conn.commit()
    if conn.is_connected():
        conn.close()
    return