import mysql.connector

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="python",
        password="programa",
        database="project"
    )
    return mydb

# conection =createConn()
# cursor =conection.cursor()
# cursor.execute("SELECT * FROM ADVENTURE")
# resultados =cursor.fetchall()
# for i in resultados:
#     print(i)
# print(resultados)
# print(createConn())