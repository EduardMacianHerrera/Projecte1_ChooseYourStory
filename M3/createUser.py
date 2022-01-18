#Funció que chequea si el format del password és correcte.Un password correcte tindrà una longitud entre 8 i 12 caràcters.
# Alguna lletra majúscula, alguna lletra minúscula, algun número, algun caràcter especial,sense espais.

import mysql.connector

def checkPassword(password):
    while True:

        try:
            letras = 0
            numeros = 0
            mayusculas = 0
            minusculas = 0
            espacioBlanco = 0



            if len(password) < 8 or len(password) > 12:
                raise ValueError

            for i in password:
                if i.isalpha():
                    letras += 1

                if i.isdigit():
                    numeros += 1

                elif i.isupper():
                    mayusculas += 1

                elif i.islower():
                    minusculas += 1

                elif i == " ":
                    espacioBlanco += 1


            if numeros < 1 or mayusculas < 1 or minusculas < 1 or espacioBlanco >= 1:
                raise ValueError

            else:
                return True

        except ValueError:

            if len(password) < 8 or len(password) > 12:
                print("La contraseña debe tener de 8 a 12 caracteres.")
                return False
            elif espacioBlanco >= 1:
                print("No puede contener espacios en blanco.")
                return False
            elif letras < 1:
                print("Te falta escribir letras.")
                return False
            elif mayusculas < 1:
                print("Te falta escribir mayusculas.")
                return False
            elif minusculas < 1:
                print("Te falta escribir minusculas.")
                return False
            elif numeros < 1:
                print("Te falta escribir números.")
                return False


#Funció que chequea que un usuari tingui el format correcte.
# longitud entre 6 i 10 i alfanumèric.
# Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatgeinformatiu i retornarà False.
# En cas que el password compleixi tots els requeriments, ens retornarà True

def checkUser(user):
    while True:
        try:
            longitud = 0
            letras = 0
            numeros= 0



            if len(user) >= 6 and len(user) <= 10:
               longitud += 1

            for i in user:
                if i.isdigit():
                    numeros += 1
                if i.isalpha():
                    letras += 1

            if letras < 1 or numeros < 1 or longitud < 1:
                raise ValueError
            else:
                return True

        except ValueError:

            if len(user) < 6 or len(user) > 10:
                print("El nombre de usuario debe tener de 6 a 10 caracteres.")
                return False

            elif letras < 1:
                print("Te falta escribir letras.")
                return False

            elif numeros < 1:
                print("Te falta escribir números.")
                return False

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

def createConn():
    mydb = mysql.connector.connect(
        host="debiansql.westeurope.cloudapp.azure.com",
        user="python",
        password="programa",
        database="project"
    )
    return mydb

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

# Funcion final para la creacion de usuarios

# REVISAR CON VIDEO PARA QUE DE MAS DE UN INTENTO

def createUser():
    user = input("Username: ")
    check = userExists(user)
    while check:
        print("El usuario ya existe")
        user = input("Username: ")
        check = userExists(user)
    check = checkUser(user)
    while not check:
        user = input("Username: ")
        check = checkUser(user)
    password =input("Password: ")
    check = checkPassword(password)
    while not check:
        password = input("Password: ")
        check = checkPassword(password)
    conn = createConn()
    cursor = conn.cursor()
    cursor.execute("select ID_USER from USER order by ID_USER desc limit 1")
    resultado = cursor.fetchall()
    conn.commit()
    if conn.is_connected():
        conn.close()
    insertUser(resultado[0][0] + 1, user, password)
    return




createUser()