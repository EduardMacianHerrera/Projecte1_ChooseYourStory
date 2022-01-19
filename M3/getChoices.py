import mysql.connector

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="python",
        password="programa",
        database="project"
    )
    return mydb
#ID_STEP
#ID_OPTION

ID_GAME = 2
def getChoices():
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(f"select ID_STEP,ID_OPTION from RECORD where ID_GAME = {ID_GAME}")
    resultado = mycursor.fetchall()

    lista = []

    for i in resultado:
        lista.append(i)

    tupla0 = tuple(lista)

    if proyecto.is_connected():
        proyecto.close()

    return tupla0
print(getChoices())