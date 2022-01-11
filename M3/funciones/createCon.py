import mysql.connector

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="edu",
        password="edu",
        database="project"
    )
    return mydb