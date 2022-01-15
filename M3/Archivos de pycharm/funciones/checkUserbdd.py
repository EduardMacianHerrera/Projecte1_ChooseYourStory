from funciones.createCon import createConn


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

  password = (password,)

  if password not in myresult:
    return -1
  else:
    return 1
