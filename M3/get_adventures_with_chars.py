import mysql.connector

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="python",
        password="programa",
        database="project"
    )
    return mydb

cursor =createConn().cursor()
cursor.execute("SELECT * FROM adventures")
print(cursor.fetchall())
print(createConn())