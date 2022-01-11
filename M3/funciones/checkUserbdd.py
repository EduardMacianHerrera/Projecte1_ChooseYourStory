import mysql.connector

mydb = mysql.connector.connect(
  host="debiansql.westeurope.cloudapp.azure.com",
  user="edu",
  password="edu"
)

print(mydb)


mycursor = mydb.cursor()

print(mycursor.execute("select * from project.USER;"))