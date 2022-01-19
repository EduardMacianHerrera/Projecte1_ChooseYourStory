from funciones.funciones import *

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
    while flag_main:
        while flag_menuPrincipal:
            opc = getOpt("\n1)Login\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit","Elige tu opción: ",[1,2,3,4,5],{},["w","e",-1])
            if opc == "1":
                flag_menuPrincipal = False
                flag_aventura = True
            elif opc == "2":
                createUser()
            elif opc == "3":
                print("Replay")
            elif opc == "4":
                print("Reports")
            elif opc == "5":
                return


        while flag_aventura:
            user = login()
            idsUsuarios = getUserIds()
            for i in range(len(idsUsuarios[0])):
                if idsUsuarios[0][i] == user:
                    idUser = idsUsuarios[1][i]
            print("What adventure do you want to play?")

            adventures = get_adventures_with_chars()
            characters = get_characters()

            print(adventures)
            print(characters)

            print(getFormatedAdventures(adventures))  # HACER QUE SE MUESTRE DE 3 EN 3
            idAdventure = int(getOpt("", "\nWhat adventure do you want to play? (0 go back) ", list(adventures.keys()), {}, [0]))


            if idAdventure == "0":  # ACABAR
                flag_aventura = False
                flag_menuPrincipal = True

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
            #game_context = {"idGame":idGame, "idAdventure":,"nameAdventure":, "user":, "idUser":, "idChar":}
            flag_createGame = False
            flag_steps = True
        while flag_steps:
            print("Pasos")

main()