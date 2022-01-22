import mysql.connector
import datetime
import art
import time

import time

tituloAscii = [
    "                    ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ ███████╗               █████╗ \n",
    "                    ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗██╔════╝              ██╔══██╗\n",
    "                    ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║███████╗              ███████║ \n",
    "                    ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║╚════██║              ██╔══██║ \n",
    "                    ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝███████║              ██║  ██║ \n",
    "                    ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ╚══════╝              ╚═╝  ╚═╝ \n",

    "           ██████╗██╗  ██╗ ██████╗ ███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗\n",
    "          ██╔════╝██║  ██║██╔═══██╗██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝\n",
    "          ██║     ███████║██║   ██║███████╗█████╗       ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ███████╗   ██║   ██║   ██║██████╔╝ ╚████╔╝ \n",
    "          ██║     ██╔══██║██║   ██║╚════██║██╔══╝        ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ╚════██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝ \n",
    "          ╚██████╗██║  ██║╚██████╔╝███████║███████╗       ██║   ╚██████╔╝╚██████╔╝██║  ██║    ███████║   ██║   ╚██████╔╝██║  ██║   ██║ \n ",
    "          ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ "]

reports=[
"                    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗\n",
"                    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝\n",
 "                                 ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗                 \n",
 "                                 ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝                 \n",
 "                                 ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ███████╗                 \n",
 "                                 ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║                 \n",
 "                                 ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████║                 \n",
 "                                 ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝                 \n",
"                    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗    █████╗\n",
"                    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝    ╚════╝\n"]

fin=["\n ███╗      ███╗      ███╗      ███╗      ███╗      ███╗      ███╗      ███╗      ███╗\n",
"██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗    ██╔██╗\n",
"╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝    ╚═╝╚═╝\n",




"                            ███████╗██╗███╗   ██╗                                          \n",
"                            ██╔════╝██║████╗  ██║                                          \n",
"                            █████╗  ██║██╔██╗ ██║                                          \n",
"                            ██╔══╝  ██║██║╚██╗██║                                          \n",
"                            ██║     ██║██║ ╚████║                                          \n",
"                            ╚═╝     ╚═╝╚═╝  ╚═══╝                                          \n",





"██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗    ██╗\n",
"╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝    ╚═╝\n\n"]

end=["\n                     ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗\n",
        "                    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝        \n",
        "                    ██║  ███╗██████╔╝███████║██║     ██║███████║███████╗        \n",
        "                    ██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║        \n",
        "                    ╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║        \n",
        "                     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝        \n",
        "                                                                                \n",
        "        ██████╗  ██████╗ ██████╗          ██╗██╗   ██╗ ██████╗  █████╗ ██████╗     ██╗\n",
        "        ██╔══██╗██╔═══██╗██╔══██╗         ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗    ██║\n",
        "        ██████╔╝██║   ██║██████╔╝         ██║██║   ██║██║  ███╗███████║██████╔╝    ██║\n",
        "        ██╔═══╝ ██║   ██║██╔══██╗    ██   ██║██║   ██║██║   ██║██╔══██║██╔══██╗    ╚═╝\n",
        "        ██║     ╚██████╔╝██║  ██║    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║    ██╗\n",
        "        ╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝"]


# Edu


def animacion(lista):
    for i in lista:
        print(i, end="")
        time.sleep(0.25)

def normal(lista):
    for i in lista:
        print(i, end="")

def login():
    check = False
    while not check:
        user = input("Username: ")
        password = input("Password: ")
        res = checkUserbdd(user, password)
        if res == 1:
            check = True
        elif res == -1:
            print("La contraseña no es correcta")
        else:
            print("El usuario no existe")
    print(f"Hello, {user}, lets play!!")
    return user


def titulo(str):
    return ("=" * 20 + str + 20 * "=")


def main():
    flag_menuPrincipal = True
    flag_main = True
    flag_aventura = False
    flag_characters = False
    flag_steps = False
    flag_createGame = False
    flag_replay = False
    flag_reports = False
    logueado = False
    tituloCheck = 0
    global game_context
    while flag_main:
        while flag_menuPrincipal:
            if tituloCheck == 0:
                animacion(tituloAscii)
                tituloCheck = 1
                print()
            else:
                normal(tituloAscii)
                print()

            if not logueado:
                game_context = {"idGame": 0, "idAdventure": 0, "idUser": 0, "username": "", "idChar": 0, "name_adventure": ""}
                opc = getOpt("\n1)Login\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit","Elige tu opción: ",[1,2,3,4,5],{},["w","e",-1])
                if opc == "1":
                    flag_menuPrincipal = False
                    flag_aventura = True
                elif opc == "2":
                    createUser()
                elif opc == "3":
                    flag_replay = True
                    flag_menuPrincipal = False
                elif opc == "4":
                    flag_reports = True
                    flag_menuPrincipal = False
                elif opc == "5":
                    animacion(end)
                    return
            else:
                opc = getOpt("\n1)Logout\n2)Play\n3)Replay Adventures\n4)Reports\n5)Exit", "Elige tu opción: ",
                             [1, 2, 3, 4, 5], {}, ["w", "e", -1])
                if opc == "1":
                    logueado = False
                    print(f'Goodbye {game_context["username"]}, come back soon!\n')
                elif opc == "2":
                    flag_menuPrincipal = False
                    flag_aventura = True
                elif opc == "3":
                    flag_replay = True
                    flag_menuPrincipal = False
                elif opc == "4":
                    flag_reports = True
                    flag_menuPrincipal = False
                elif opc == "5":
                    animacion(end)
                    return

        while flag_aventura:
            if not logueado:
                user = login()
                idsUsuarios = getUserIds()
                for i in range(len(idsUsuarios[0])):
                    if idsUsuarios[0][i] == user:
                        idUser = idsUsuarios[1][i]
            logueado = True
            game_context = {"idGame": 0, "idAdventure": 0, "idUser": idUser, "username": user, "idChar": 0, "name_adventure": ""}

            print("What adventure do you want to play?")

            adventures = get_adventures_with_chars()
            characters = get_characters()


            print(getFormatedAdventures(adventures))  # HACER QUE SE MUESTRE DE 3 EN 3
            idAdventure = int(getOpt("", "\nWhat adventure do you want to play? (0 go back) ", list(adventures.keys()), {}, [0]))


            if idAdventure == 0:
                flag_aventura = False
                flag_menuPrincipal = True
                break

            print(getHeader(adventures[idAdventure]["Name"]))
            fila1 = (list(adventures[idAdventure].keys())[0] + ":",adventures[idAdventure][list(adventures[idAdventure].keys())[0]])
            fila2 = (list(adventures[idAdventure].keys())[1] + ":",adventures[idAdventure][list(adventures[idAdventure].keys())[1]])
            print(getFormatedBodyColumns(fila1, (20,100), margin="  ")) # MIRAR LO DEL MARGEN
            print(getFormatedBodyColumns(fila2, (20, 100), margin=" "))  # MIRAR LO DEL MARGE
            flag_characters = True
            flag_aventura = False

        while flag_characters:
            listaPersonajes = []

            for i in characters:
                if i in adventures[idAdventure]["characters"]:
                    listaTemp =  [i,characters[i]]
                    listaPersonajes.append(listaTemp)

            idPersonajes = []
            for i in range(len(listaPersonajes)):
                idPersonajes.append(listaPersonajes[i][0])
                listaPersonajes[i][0] = str(listaPersonajes[i][0])
                string = listaPersonajes[i][0] + ") "+ listaPersonajes[i][1] + "\n"
                listaPersonajes[i] = string


            textoPersonajes = "".join(listaPersonajes)
            print(titulo("Characters"))
            print(textoPersonajes)
            idCharacter = int(getOpt("","\nSelect your Character (0 go back): ", idPersonajes,{},[0])) # QUE PUEDA VOLVER HACIA ATRAS
            if idCharacter == 0:
                flag_characters = False
                flag_aventura = True

            print(f'You have selected play with {characters[idCharacter]}\n')
            input("Enter to continue")
            flag_characters = False
            flag_createGame = True

        while flag_createGame:
            idGame = lastIdGame()
            insertCurrentGame(idGame, idUser, idCharacter, idAdventure)
            game_context = {"idGame": idGame, "idAdventure": idAdventure, "idUser": idUser, "username":user, "idChar": idCharacter, "name_adventure": adventures[idAdventure]["Name"]}
            flag_createGame = False
            flag_steps = True

        while flag_steps:
            id_by_steps = get_id_by_step_adventure()
            idAnswer_ByStep_Adventure = get_answers_bystep_adventure()
            idFirstStep = get_first_step_adventure()[0][0]
            elecciones(id_by_steps,idAnswer_ByStep_Adventure,idFirstStep)


            flag_steps = False
            flag_menuPrincipal = True

        while flag_replay: # HACER QUE PUEDAS ESCOGER PARTIDA
            game_context = {"idGame": 25, "idAdventure": 4, "idUser": 2, "username":user,"idChar": 7, "name_adventure": "En busca de la gráfica perdida"}
            tupla = getChoices()
            replay(tupla)
            flag_replay = False
            flag_menuPrincipal = True

        while flag_reports:
            normal(reports)
            opc = int(getOpt("\n1)Most used answer\n2)Player with more games played\n3)Games played by user\n4)Back","Option: ",[1,2,3,4]))
            if opc == 1:
                print(most_used_answer())
                input("Press enter to continue: ")
            elif opc == 2:
                print(get_player_with_more_games_played())
                input("Press enter to continue: ")
            elif opc == 3:
                user = input("What user do you want to see?\n")
                print(games_played_by_user(user))
                input("Press enter to continue: ")
            elif opc == 4:
                flag_menuPrincipal = True
                flag_reports = False





def replay(choices):
    id_by_steps = get_id_by_step_adventure()
    idAnswer_ByStep_Adventure = get_answers_bystep_adventure()
    for i in choices:
        idStep = i[0]
        idOpcion = i[1]
        repeticion(id_by_steps,idAnswer_ByStep_Adventure,idStep,idOpcion)

def repeticion(id_by_steps,idAnswer_ByStep_Adventure,idFirstStep,idOpcion):
    print(getHeader(game_context["name_adventure"]))
    print(formatText(id_by_steps[idFirstStep]["Description"], 120))


    if id_by_steps[idFirstStep]["Final_Step"] == 1:
        print()
        input("Enter to continue\n\n")
        return
    print("\nOptions: ")

    respuestas = id_by_steps[idFirstStep]["answers_in_step"]
    opciones = []
    rango = []
    for i in respuestas:
        key = (i, idFirstStep)
        rango.append(i)
        desc = idAnswer_ByStep_Adventure[key]["Description"]
        string = str(i) + ") " + desc
        opciones.append(string)

    textOpciones = "\n".join(opciones)

    opc = getOpt(textOpciones, "\nEnter to continue: \n", rango, dictionary={}, exceptions=[""])

    print(f"Option {idOpcion} selected")
    keyPaso = (idOpcion, idFirstStep)
    print()

    if not idAnswer_ByStep_Adventure[keyPaso]["Resolution_answer"] == "":
        print(idAnswer_ByStep_Adventure[keyPaso]["Resolution_answer"])
        print()
    input("Enter to continue\n\n")
    return


def elecciones(id_by_steps,idAnswer_ByStep_Adventure,idFirstStep):
    print(getHeader(game_context["name_adventure"]))
    print(formatText(id_by_steps[idFirstStep]["Description"],120))

    if id_by_steps[idFirstStep]["Final_Step"] == 1:
        insertCurrentChoice(game_context["idGame"], idFirstStep, 58)
        normal(fin)
        input("\nEnter to continue: \n")
        return

    print("\nOptions: ")

    respuestas = id_by_steps[idFirstStep]["answers_in_step"]
    opciones = []
    rango = []
    for i in respuestas:
        key = (i, idFirstStep)
        rango.append(i)
        desc = idAnswer_ByStep_Adventure[key]["Description"]
        string = str(i) + ") " + desc
        opciones.append(string)

    textOpciones = "\n".join(opciones)

    opc = int(getOpt(textOpciones, "\nSelect Option: \n", rango, dictionary={}, exceptions=[]))
    keyPaso = (opc, idFirstStep)
    insertCurrentChoice(game_context["idGame"], idFirstStep, opc)
    print()
    if not idAnswer_ByStep_Adventure[keyPaso]["Resolution_answer"] == "":
        print(idAnswer_ByStep_Adventure[keyPaso]["Resolution_answer"])
        print()
    input("Enter to continue\n\n")
    nextStep = idAnswer_ByStep_Adventure[keyPaso]["NextStep_Adventure"]
    elecciones(id_by_steps,idAnswer_ByStep_Adventure,nextStep)










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

def lastIdGame():
    conn = createConn()
    cursor = conn.cursor()

    cursor.execute("select ID_GAME from GAME order by ID_GAME desc limit 1")
    resultado = cursor.fetchall()
    if resultado == []:
        resultado = ((0,),(0,))

    return resultado[0][0] + 1

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


def get_adventures_with_chars():
    conexion = createConn()
    cursor = conexion.cursor()

    cursor.execute("select ADVENTURE.ID_ADVENTURE, adventure_name, description from ADVENTURE")
    resAdventure = cursor.fetchall()
    cursor.execute("Select * from STARS")
    resStars = cursor.fetchall()

    if conexion.is_connected():
        conexion.close()

    adventures = {}

    for i in resAdventure:
        lista = []
        for n in resStars:
            if n[0] == i[0]:
                lista.append(n[1])
        diccTemp = {i[0]: {"Name": i[1], "Description": i[2], "characters": lista}}
        adventures.update(diccTemp)

    return adventures

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
    if resultado == []:
        resultado = ((0,),(0,))
    conn.commit()
    if conn.is_connected():
        conn.close()
    insertUser(resultado[0][0] + 1, user, password)
    return


# Sergio


def get_player_with_more_games_played():

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select u.username, count(e.ID_USER) as 'num_partidas' from USER u inner join GAME e on u.ID_USER = e.ID_USER group by e.ID_USER order by num_partidas desc limit 1;")

    resultado = cursor.fetchall()

    return getFormatedReports(resultado, 120, ("NOMBRE USUARIO", "PARTIDAS JUGADAS"), (30))



def getFormatedReports(adventures, width, t_name_columns, t_w_columns):
    #try:
        def tuple_cutter(tuple_to_cut, tuple_ref):
            # Esta función sirve para que en caso de que las tuplas tengan longitudes distintas, la que marca
            # los espacios se recorte para tener la misma longitud que la que tiene los textos de las columnas,
            # asi en vez de saltar un error, lo corrige
            while len(tuple_to_cut) > len(tuple_ref):
                tuple_to_cut = list(tuple_to_cut)[:-1]
            return tuple(tuple_to_cut)
        def tuple_extender(tuple_to_ext, tuple_ref):
            # Función que sirve para añadir valores a la tupla de espacios en caso de que tenga una
            # cantidad de espacios inferior a la de titulos, va añadiendo al final de la lista los valores que ya tenia la
            # tupla ej t = (10, 20) la alargamos a 6 sera t =(10, 20, 10, 20, 10, 20
            values = list(tuple_to_ext)
            pos = 0
            while len(tuple_to_ext) < len(tuple_ref):
                tuple_to_ext = list(tuple_to_ext)
                tuple_to_ext.append(values[pos])
                if pos < len(values) - 1:
                    pos += 1
                else:
                    pos = 0
            tuple_to_ext = tuple(tuple_to_ext)
            return tuple(tuple_to_ext)
        def getHeader_Mod1(text, width):
            try:
                if len(text) > width:
                    return "El texto es mayor que el ancho y no se puede formatar correctamente"
                a1 = (width // 2) - (len(text) // 2)
                a2 = (width // 2) - (len(text) // 2)
                if (a1 + a2 + len(text)) > width:
                    a1 -= 1
                elif (a1 + a2 + len(text)) < width:
                    a2 += 1
                Header = (("=" * a1) + (text) + ("=" * a2))
                return Header
            except:
                return "La funcion getHeader no se ha ejecutado correctamente"
        def getHeadeForTableFromTuples_Mod1(t_name_columns, t_size_columns, title=""):
            try:
                to_print = ""
                count = 0
                for i in t_size_columns:
                    to_print = to_print + t_name_columns[count] + (" " * (i - len(t_name_columns[count]) +2))
                    count += 1
                return to_print
            except:
                return "Error en la función getHeadeForTableFromTuples_Mod1"
        def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin="  "):
            def formatText_Mod1(text, lenLine):
                try:
                    phrase = ""
                    word = ""
                    to_print = []
                    count = 0
                    for i in (text + " "):
                        word = word + i
                        if len(word) > lenLine:
                            raise ValueError
                        if i == " ":
                            if len(phrase + word) < lenLine:
                                phrase = phrase + word
                                word = ""
                            else:
                                while len(phrase) < lenLine:
                                    phrase = phrase + " "
                                to_print.append(phrase)
                                phrase = word
                                word = ""
                        count += 1
                    while len(phrase) < lenLine:
                        phrase = phrase + " "
                    to_print.append(phrase)
                    return to_print
                except:
                    if len(word) > lenLine:
                        return ["Al menos una de las ",
                                "palabras tiene una  ",
                                "longitud superior a ",
                                "la de la linea y no ",
                                "se puede formatar el",
                                "parrafo             "]
                    else:
                        return ["La funcion          ",
                                "formatText no se ha ",
                                "ejecutado           ",
                                "correctamente       "]
            try:
                if len(tupla_texts) != len(tupla_sizes):
                    raise ValueError
                paragraphs = []
                count = 0
                for i in tupla_texts:
                    i = str(i)
                    paragraphs.append(formatText_Mod1(i, tupla_sizes[count]))
                    count += 1
                to_print = ""
                max_h = 0
                for j in paragraphs:
                    if len(j) > max_h:
                        max_h = len(j)
                count = 0
                for k in paragraphs:
                    while len(k) < max_h:
                        k.append(" " * tupla_sizes[count])
                    count += 1
                for l in range(max_h):
                    for p in range(len(paragraphs)):
                        to_print = to_print + paragraphs[p][l] + margin
                    to_print = to_print + "\n"
                return (to_print)
            except:
                if len(tupla_texts) != len(tupla_sizes):
                    return "La longitud de ambas tuplas no es la misma"
                else:
                    return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"
        # A partir de aqui deja de declarar otras funciones y empieza el codigo de la funcion
        ErrorT_SP = False
        Error_long = False
        if (type(t_w_columns)) == int:
            t_w_columns = [t_w_columns, t_w_columns]
        for f in t_w_columns:
            if type(f) != int:
                ErrorT_SP =True
                raise ValueError
        if len(t_w_columns) > len(t_name_columns):
            t_w_columns =tuple_cutter(t_w_columns, t_name_columns)
        elif len(t_w_columns) < len(t_name_columns):
            t_w_columns =tuple_extender(t_w_columns, t_name_columns)
        max_w = 0
        for word in t_name_columns:
            if len(word) > max_w:
                max_w = len(word)
        for i in t_w_columns:
            if i < max_w:
                Error_long =True
                raise ValueError
        # La razón de este error es que si el espacio que damos para los parrafos es demasiado pequeño respecto al
        # titulo, debajo de un titulo veremos un parrafo muy corto y pegado otro parrafo, aun ocupando el espacio de debajo del titulo
        to_print = getHeader_Mod1("Adventures", width) + "\n" \
                   + getHeadeForTableFromTuples_Mod1(t_name_columns, t_w_columns)+ "\n" \
                   + ("*" *width) + "\n" \
                   + (" " * width) + "\n"
        for j in adventures:
            # En este caso tupla_t recoge la ID de la aventura, el nombre de la aventura y la descripción de esta
            tupla_t =(j)
            if len(t_w_columns) > len(str(tupla_t)):
                t_w_columns = tuple_cutter(t_w_columns, tupla_t)
            elif len(t_w_columns) < len(tupla_t):
                t_w_columns =tuple_extender(t_w_columns, tupla_t)
            to_print =to_print + getFormatedBodyColumns(tupla_t, t_w_columns) + (" " *width) +"\n"
        return(to_print)

def games_played_by_user(username):

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f"select a.ID_ADVENTURE ,a.adventure_name, g.date from USER u inner join GAME g on u.ID_USER = g.ID_USER inner join ADVENTURE a on g.ID_ADVENTURE = a.ID_ADVENTURE where u.username = '{username}'")

    result = cursor.fetchall()

    if result != []:
        return getFormatedReports(result, 120, ("ID AVENTURE", "NAME", "DATE"), (30))
    else:
        return "**El usuario no tiene partidas**"

def most_used_answer():

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select a.ID_ADVENTURE, a.adventure_name, s.ID_STEP ,s.description, o.ID_OPTION, o.description, count(r.ID_OPTION) as 'cuenta' from RECORD r inner join `OPTION` o on r.ID_OPTION = o.ID_OPTION inner join STEP s on o.ID_STEP_FROM = s.ID_STEP inner join ADVENTURE a on s.ID_ADVENTURE = a.ID_ADVENTURE group by r.ID_OPTION order by cuenta desc limit 5")
    respuesta = cursor.fetchall()

    listaResultado = []

    for i in respuesta:
        elementoLista = []
        id_aventura_nombre = str(i[0]) + " " +"-" + " " + str(i[1])
        id_paso_descripcion = str(i[2]) + " " + "-" + " " + str(i[3])
        id_opcion_descripcion = str(i[4]) + " " + "-" + " " + str(i[5])
        elementoLista.append(id_aventura_nombre)
        elementoLista.append(id_paso_descripcion)
        elementoLista.append(id_opcion_descripcion)
        elementoLista.append(str(i[6]))
        listaResultado.append(elementoLista)

    return getFormatedReports(listaResultado, 120, ("ID AVENTURA - NOMBRE", "ID PASO - DESCRIPCION", "ID RESPUESTA - DESCRIPCTION", "NUMERO VECES SELECCIONADO"), (30, 30, 30, 30))





def get_answers_bystep_adventure():

    idAnswers_byStep_Adventure_dic = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f'select ID_STEP from STEP where ID_ADVENTURE = {game_context["idAdventure"]}')
    idPasoAventura = cursor.fetchall() #Saca las id de los pasos de la aventura de la variable


    optionTable = []
    for i in idPasoAventura:
        cursor.execute(f"select * from `OPTION` where ID_STEP_FROM = {i[0]}")
        optionTable = cursor.fetchall() #Tabla con las opciones de los pasos de la aventura
        for j in optionTable:
            idAnswers_byStep_Adventure_dic[(j[0], i[0])] = {"Description": j[1], "Resolution_answer":j[2], "NextStep_Adventure":j[8]}


    return idAnswers_byStep_Adventure_dic

def get_id_by_step_adventure():
    #Ens retornarà el diccionariid_by_stepsamb nomésels passos relacionats ambl'aventura que estem jugant
    global game_context
    id_by_steps = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f'select * from STEP where ID_ADVENTURE = {game_context["idAdventure"]}')
    result = cursor.fetchall()

    for i in result:
        id_by_steps[i[0]] = {"Description": i[1], "answers_in_step":[], "Final_Step": i[2]} #Faltan los pasos

    for i in id_by_steps:
        cursor.execute(f"select ID_OPTION from `OPTION` where ID_STEP_FROM = {i}")
        idOptions = cursor.fetchall()
        for j in idOptions:
            id_by_steps[i]["answers_in_step"].append(j[0])
        id_by_steps[i]["answers_in_step"] = tuple(id_by_steps[i]["answers_in_step"])

    if conexion.is_connected():
        conexion.close()

    return id_by_steps


def getFormatedAnswers(idAnswers, text, lenLine, leftMargin):

    if lenLine >= 7:

        wordsList = text.split()  #Añadir el texto en lista
        count = 1
        for i in range(len(wordsList)):
            wordsList.insert(count, " ")
            count += 2

        option = " " * leftMargin + str(idAnswers) + ") "
        lenCount = 0

        for i in option: #Para tener en cuenta el len de la id
            lenCount += 1

        for i in range(len(wordsList)):
            for j in wordsList[i]:

                if j != " ":
                    lenCount += 1
                    if lenCount > lenLine:
                        wordsList.insert(i, "\n")
                        wordsList.insert(i + 1, " " * leftMargin)
                        lenCount = 0

        for i in wordsList:
            for j in i:
                option += j

        return option

    else:
        return("Lenline mínimo de 7 letras loko")


def get_characters():

    dictChatacters = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select * from `CHARACTER`")

    for i in cursor.fetchall():
        dictChatacters[i[0]] = i[1]

    if conexion.is_connected():
        conexion.close()

    return dictChatacters


def getTableFromDict(tuple_of_keys, wight_of_columns, dict_of_data):

    data = ""

    try:
        for i in dict_of_data:
            data += str(i)
            for j in range(len(wight_of_columns)):
                data += " " * wight_of_columns[j] + str(dict_of_data[i][tuple_of_keys[j]])
            data += "\n"

    except:
        print("** Debes introducir el mismo número de keys que de weigth **")

    return data



def getOpt(textOpts = "", inputOptText="", rangeList=[], dictionary = {}, exceptions = []):

    correctOpc, useException = False, False
    leftMargin = 50

    while not correctOpc:

        useException = False

        opciones = textOpts.split("\n")

        for i in opciones:
            print(" " * leftMargin + i)

        opc = input("\n" + " " * leftMargin + inputOptText) # No suma el leftMArgin

        for i in rangeList:
            if opc == str(i):
                correctOpc = True
                break

        if len(exceptions) != 0:
            for i in exceptions:
                if str(i) == opc:
                    return opc

        if len(dictionary) != 0:
            for j, k in dictionary.items():
                if str(j) == opc:
                    return opc
                elif str(k) == opc:
                    return opc

        if not correctOpc and not useException:
            print(" " * leftMargin + "===== Invalid option =====")
            input(" " * leftMargin + "Press enter to continue")

    return opc



# Irene

def getChoices():
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(f'select ID_STEP,ID_OPTION from RECORD where ID_GAME = {game_context["idGame"]}')
    resultado = mycursor.fetchall()

    lista = []

    for i in resultado:
        lista.append(i)

    tupla0 = tuple(lista)

    if proyecto.is_connected():
        proyecto.close()

    return tupla0


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

def get_first_step_adventure():
    global game_context
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(f'select ID_STEP,description from STEP where ID_ADVENTURE = {game_context["idAdventure"]} and START = 1')
    resultado = mycursor.fetchall()
    if proyecto.is_connected():
        proyecto.close()
    return resultado


def get_table(query):
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    descripcion = mycursor.description

    if proyecto.is_connected():
        proyecto.close()

    lista = []

    for i in descripcion:
        lista.append(i[0])

    tupla0 = tuple(lista)
    resultado.insert(0,tupla0)
    resultado = tuple(resultado)
    return resultado


def getIdGame():
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute("select ID_GAME from GAME")
    resultado = mycursor.fetchall()


    lista = []

    for i in resultado:
        lista.append(i[0])

    tupla0 = tuple(lista)

    if proyecto.is_connected():
        proyecto.close()

    return tupla0


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



# Albert

def letra_Grande(texto):
    def formatText_Mod2(text, lenLine, split="\n"):
        try:
            text = text.replace('\n', "")
            phrase = ""
            word = ""
            to_print = ""
            count = 0
            for i in (text + " "):
                word = word + i
                if len(word) > lenLine:
                    raise ValueError
                if i == " ":
                    word = word +" "
                    if len(phrase + word) < lenLine:
                        phrase = phrase + word
                        word = ""
                    else:
                        while len(phrase) < lenLine:
                            phrase = phrase + " "
                        to_print = to_print + split + phrase
                        phrase = word
                        word = ""
                count += 1
            while len(phrase) < lenLine:
                phrase = phrase + " "
            to_print = to_print + split + phrase
            return to_print
        except:
            if len(word) > lenLine:
                return ("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                        "y no se puede formatar correctamente el parrafo")
            else:
                return ("La funcion formatText no se ha ejecutado correctamente")
    if len(texto) > 100:
        formatText_Mod2(texto, 100)
    formatado =art.text2art(texto, font ="small")
    if len(formatado) > 100:
        texto =formatText_Mod2(texto, (len(texto)/2))
        formatado =art.text2art(texto, font ="small",)
    return formatado



'''def replay(choices):
    try:
        id_by_steps = get_id_by_step_adventure()
        idAnswer_ByStep_Adventure = get_answers_bystep_adventure()
        choices = list(choices)
        for i in range(len(choices)):
            choices[i] = list(choices[i])
            id1 = choices[i][0]
            keyTemp = (choices[i][1], choices[i][0])
            choices[i][0] = id_by_steps[choices[i][0]]["Description"]

            if id_by_steps[id1]["Final_Step"] == 1:
                choices[i][1] = ""
            else:
                choices[i][1] = idAnswer_ByStep_Adventure[keyTemp]["Resolution_answer"]
                choices[i].insert(1, idAnswer_ByStep_Adventure[keyTemp]["Description"])

        choices = tuple(choices)

        width = 120
        def formatText_Mod(text, lenLine, split="\n"):
            try:
                phrase = ""
                word = ""
                to_print = ""
                count = 0
                for i in (text + " "):
                    word = word + i
                    if len(word) > lenLine*(1 +(text.count("\n"))):
                        raise ValueError
                    if i == " ":
                        if len(phrase + word) < lenLine:
                            phrase = phrase + word
                            word = ""
                        else:
                            while len(phrase) < lenLine:
                                phrase = phrase + " "
                            to_print = to_print + split + phrase
                            phrase = word
                            word = ""
                    count += 1
                while len(phrase) < lenLine:
                    phrase = phrase + " "
                to_print = to_print + split + phrase
                return to_print
            except:
                if len(word) > lenLine:
                    return ("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                            "y no se puede formatar correctamente el parrafo")
                else:
                    return ("La funcion formatText no se ha ejecutado correctamente")
        for i in range(len(choices)):
            for k in range(len(choices[i])):
                if not choices[i][k] == "":
                    paso = input("\n        Press Enter to continue:")
                    print(formatText_Mod(choices[i][k], width))
        paso = input("\n        Press Enter to continue:")
        return
    except:
        print("La función replay no se ha ejecutado correctamente")
'''

def formatText(text, lenLine, split ="\n"):
    try:
        phrase =""
        word =""
        to_print =""
        count =0
        for i in (text +" "):
            word =word +i
            if len(word) > lenLine:
                raise ValueError
            if i ==" ":
                if len(phrase +word) < lenLine:
                    phrase =phrase +word
                    word = ""
                else:
                    while len(phrase) < lenLine:
                        phrase =phrase +" "
                    to_print =to_print +split +phrase
                    phrase =word
                    word=""
            count +=1
        while len(phrase) < lenLine:
            phrase = phrase + " "
        to_print = to_print +split +phrase
        return to_print
    except:
        if len(word) > lenLine:
            return("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                   "y no se puede formatar correctamente el parrafo")
        else:
            return("La funcion formatText no se ha ejecutado correctamente")


def getFormatedAdventures(adventures):
    try:
        ErrorT_SP = False
        Error_long = False
        width = 120
        t_name_columns = ("Id Adventure","Adventure","Description")
        t_w_columns = (20,20,80)
        def tuple_cutter(tuple_to_cut, tuple_ref):
            # Esta función sirve para que en caso de que las tuplas tengan longitudes distintas, la que marca
            # los espacios se recorte para tener la misma longitud que la que tiene los textos de las columnas,
            # asi en vez de saltar un error, lo corrige
            while len(tuple_to_cut) > len(tuple_ref):
                tuple_to_cut = list(tuple_to_cut)[:-1]
            return tuple(tuple_to_cut)
        def tuple_extender(tuple_to_ext, tuple_ref):
            # Función que sirve para añadir valores a la tupla de espacios en caso de que tenga una
            # cantidad de espacios inferior a la de titulos, va añadiendo al final de la lista los valores que ya tenia la
            # tupla ej t = (10, 20) la alargamos a 6 sera t =(10, 20, 10, 20, 10, 20
            values = list(tuple_to_ext)
            pos = 0
            while len(tuple_to_ext) < len(tuple_ref):
                tuple_to_ext = list(tuple_to_ext)
                tuple_to_ext.append(values[pos])
                if pos < len(values) - 1:
                    pos += 1
                else:
                    pos = 0
            tuple_to_ext = tuple(tuple_to_ext)
            return tuple(tuple_to_ext)
        def getHeader_Mod1(text, width):
            try:
                if len(text) > width:
                    return "El texto es mayor que el ancho y no se puede formatar correctamente"
                a1 = (width // 2) - (len(text) // 2)
                a2 = (width // 2) - (len(text) // 2)
                if (a1 + a2 + len(text)) > width:
                    a1 -= 1
                elif (a1 + a2 + len(text)) < width:
                    a2 += 1
                Header = (("=" * a1) + (text) + ("=" * a2))
                return Header
            except:
                return "La funcion getHeader no se ha ejecutado correctamente"
        def getHeadeForTableFromTuples_Mod1(t_name_columns, t_size_columns, title=""):
            try:
                to_print = ""
                count = 0
                for i in t_size_columns:
                    to_print = to_print + t_name_columns[count] + (" " * (i - len(t_name_columns[count]) +2))
                    count += 1
                return to_print
            except:
                return "Error en la función getHeadeForTableFromTuples_Mod1"
        def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin="  "):
            def formatText_Mod1(text, lenLine):
                try:
                    phrase = ""
                    word = ""
                    to_print = []
                    count = 0
                    for i in (text + " "):
                        word = word + i
                        if len(word) > lenLine:
                            raise ValueError
                        if i == " ":
                            if len(phrase + word) < lenLine:
                                phrase = phrase + word
                                word = ""
                            else:
                                while len(phrase) < lenLine:
                                    phrase = phrase + " "
                                to_print.append(phrase)
                                phrase = word
                                word = ""
                        count += 1
                    while len(phrase) < lenLine:
                        phrase = phrase + " "
                    to_print.append(phrase)
                    return to_print
                except:
                    if len(word) > lenLine:
                        return ["Al menos una de las ",
                                "palabras tiene una  ",
                                "longitud superior a ",
                                "la de la linea y no ",
                                "se puede formatar el",
                                "parrafo             "]
                    else:
                        return ["La funcion          ",
                                "formatText no se ha ",
                                "ejecutado           ",
                                "correctamente       "]
            try:
                if len(tupla_texts) != len(tupla_sizes):
                    raise ValueError
                paragraphs = []
                count = 0
                for i in tupla_texts:
                    i = str(i)
                    paragraphs.append(formatText_Mod1(i, tupla_sizes[count]))
                    count += 1
                to_print = ""
                max_h = 0
                for j in paragraphs:
                    if len(j) > max_h:
                        max_h = len(j)
                count = 0
                for k in paragraphs:
                    while len(k) < max_h:
                        k.append(" " * tupla_sizes[count])
                    count += 1
                for l in range(max_h):
                    for p in range(len(paragraphs)):
                        to_print = to_print + paragraphs[p][l] + margin
                    to_print = to_print + "\n"
                return (to_print)
            except:
                if len(tupla_texts) != len(tupla_sizes):
                    return "La longitud de ambas tuplas no es la misma"
                else:
                    return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"
        # A partir de aqui deja de declarar otras funciones y empieza el codigo de la funcion
        for f in t_w_columns:
            if type(f) != int:
                ErrorT_SP =True
                raise ValueError
        if len(t_w_columns) > len(t_name_columns):
            t_w_columns =tuple_cutter(t_w_columns, t_name_columns)
        elif len(t_w_columns) < len(t_name_columns):
            t_w_columns =tuple_extender(t_w_columns, t_name_columns)
        max_w = 0
        for word in t_name_columns:
            if len(word) > max_w:
                max_w = len(word)
        for i in t_w_columns:
            if i < max_w:
                Error_long =True
                raise ValueError
        # La razón de este error es que si el espacio que damos para los parrafos es demasiado pequeño respecto al
        # titulo, debajo de un titulo veremos un parrafo muy corto y pegado otro parrafo, aun ocupando el espacio de debajo del titulo
        to_print = getHeader_Mod1("Adventures", width) + "\n" \
                   + (" " *width) + "\n" \
                   + getHeadeForTableFromTuples_Mod1(t_name_columns, t_w_columns)+ "\n" \
                   + ("*" *width) + "\n" \
                   + (" " * width) + "\n"
        for j in adventures:
            # En este caso tupla_t recoge la ID de la aventura, el nombre de la aventura y la descripción de esta
            tupla_t =(str(j), str(adventures[j]["Name"]), str(adventures[j]["Description"]))
            if len(t_w_columns) > len(tupla_t):
                t_w_columns = tuple_cutter(t_w_columns, tupla_t)
            elif len(t_w_columns) > len(tupla_t):
                t_w_columns =tuple_extender(t_w_columns, tupla_t)
            to_print =to_print + getFormatedBodyColumns(tupla_t, t_w_columns) + (" " *width) +"\n"
        return(to_print)
    except:
        if ErrorT_SP:
            return "No todos los valores de la tupla son numeros enteros"
        if Error_long:
            return "Los espacios de separación entre parrafos son demasiado cortos para encajar los" \
                   " titulos de las columnas"
        else:
            return "Error en la ejecución de la función getFormatedAdventures"


# Dentro de esta función esta formatText_Mod1, una modificación de formatText, que también divide el texto en lineas
# la diferencia es que cada linea será un elemento de una lista.
#
# Tenerlo dentro de una lista nos sera util para printar luego varios textos,
# seleccionando que parte de cada uno debe aparecer en que momento
#
# Los elementos de la funcion formatText_Mod1, las lineas (en formato string), ya vienen todas con el mismo ancho lenLine en los datos
# de entrada, cuando las palabras no llegan a esa longitud, añade espacios " " que al printar no se ven
# pero hacen que la longitud de ese string sea la misma.

# La función getFormatedBodyColumns primero obtiene los parrafos que imprimira uno al lado del otro, estos
# parrafos se obtienen con la función formatText_Mod1 en forma de lista donde cada elemento string es una linea.
#
# Define la variable to_print, que sera toodo lo que tiene que printar, incluyendo espacios entre lineas y saltos de linea
#
# Necesitamos obtener la maxima altura de los parrafos, eso es max_h, la altura de los parrafos sera equivalente a la cantidad
# de elementos que tiene su lista, casa elemento es una linea, cuando acaba debe haber salto de pagina.
# Todos los parrafos que sean menores a max altura, les añadimos tantas lineas vacias de espacios (equivalentes al ancho maximo)
# como lineas o elementos de lista le falten para igualar esa maxima altura.
#
# Vamos a colocar en la variable to_print tooodo lo que queremos imprimir. La idea es que queremos poner la primera linea del primer
# parrafo, luego la primera linea del segundo parrafo, luego la primera del tercer parrafo, asi sucesivamente hasta llegar al salto de linea
# entonces colocaremos las segundas lineas de cada parrafo.
#
# Estas lineas tienen todas el mismo ancho, junto con los 2 espacios minimo que las separan. Ademas, todos los parrafos tienen la misma cantidad
# de lineas, aunque a partir de cierto punto esten vacias y solo sean espacios (Es necesario para que se coloque todo a sitio)


def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin ="  "):
    def formatText_Mod1(text, lenLine):
        try:
            phrase = ""
            word = ""
            to_print = []
            count = 0
            for i in (text + " "):
                word = word + i
                if len(word) > lenLine:
                    raise ValueError
                if i == " ":
                    if len(phrase + word) < lenLine:
                        phrase = phrase + word
                        word = ""
                    else:
                        while len(phrase) < lenLine:
                            phrase = phrase + " "
                        to_print.append(phrase)
                        phrase = word
                        word = ""
                count += 1
            while len(phrase) < lenLine:
                phrase = phrase + " "
            to_print.append(phrase)
            return to_print
        except:
            if len(word) > lenLine:
                return ["Al menos una de las ",
                        "palabras tiene una  ",
                        "longitud superior a ",
                        "la de la linea y no ",
                        "se puede formatar el",
                        "parrafo"]
            else:
                return ["La funcion          ",
                        "formatText no se ha ",
                        "ejecutado           ",
                        "correctamente       "]
    try:
        if len(tupla_texts) != len(tupla_sizes):
            raise ValueError
        paragraphs = []
        count =0
        for i in tupla_texts:
            i =str(i)
            paragraphs.append(formatText_Mod1(i, tupla_sizes[count]))
            count +=1
        to_print =""
        max_h = 0
        for j in paragraphs:
            if len(j) > max_h:
                max_h =len(j)
        count =0
        for k in paragraphs:
            while len(k) < max_h:
                k.append(" " *tupla_sizes[count])
            count +=1
        for l in range(max_h):
            for p in range(len(paragraphs)):
                to_print =to_print + paragraphs[p][l] +margin
            to_print = to_print +"\n"
        return (to_print)
    except:
        if len(tupla_texts) != len(tupla_sizes):
            return ("La longitud de ambas tuplas no es la misma")
        else:
            return ("La funcion getFormatedBodyColumns no se ha ejecutado correctamente")


def getHeader(text):
    try:
        width = 120
        if len(text) > width:
            return "\nEl texto es mayor que el ancho y no se puede formatar correctamente"
        a1 = (width//2) -(len(text)//2)
        a2 =  (width//2) -(len(text)//2)
        if (a1 +a2 +len(text)) > width:
            a1 -=1
        elif (a1 +a2 +len(text)) < width:
            a2 +=1
        Header = ("*"*width) + ("\n") + (("="*a1) +(text) +("="*a2)) + ("\n") + ("*"*width)
        return Header
    except:
        print("La funcion getHeader no se ha ejecutado correctamente")


def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
    to_print =""
    count =0
    for i in t_size_columns:
        to_print =to_print + t_name_columns[count] + (" "*i)
        count +=1
    print("=" *len(to_print))
    print(to_print)
    print("*" *len(to_print))


def getReplayAdventures():
    conexion =createConn()
    cursor =conexion.cursor()
    cursor.execute("SELECT GAME.ID_USER, Us.username, GAME.ID_ADVENTURE, Ad.adventure_name, GAME.ID_CHARACTER, Ch.character_name FROM GAME JOIN ADVENTURE Ad ON GAME.ID_ADVENTURE = Ad.ID_ADVENTURE JOIN USER Us ON Us.ID_USER = GAME.ID_USER JOIN `CHARACTER` Ch ON Ch.ID_CHARACTER = GAME.ID_CHARACTER")
    # Proceso de desconexión, en el fallo de la query de debajo
    # se comprueba que la connexión no esta hecha
    res2 = cursor.fetchall()
    if conexion.is_connected():
        conexion.disconnect()
    # cursor.execute("SELECT * FROM ADVENTURE")


    return res2



