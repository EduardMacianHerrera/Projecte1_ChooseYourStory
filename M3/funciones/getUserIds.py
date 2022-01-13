from funciones.createCon import createConn

def getUserIds():
  mydb = createConn()

  mycursor = mydb.cursor()
  mycursor.execute("select username, ID_USER from USER")
  myresult = mycursor.fetchall()

  lista = [[],[]]

  for i,n in myresult:
    lista[0].append(i)
    lista[1].append(n)

  return lista
