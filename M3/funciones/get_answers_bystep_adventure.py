from createCon import createConn

global idAventura
idAventura = 10


def getAnswersByStepAdventure():

    idAnswers_byStep_Adventure_dic = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f"select ID_STEP from STEP where ID_ADVENTURE = {idAventura} ")
    idPasoAventura = cursor.fetchall() #Saca las id de los pasos de la aventura de la variable

    print(idPasoAventura)

    optionTable = []
    for i in idPasoAventura:
        cursor.execute(f"select * from `OPTION` where ID_STEP_FROM = {i[0]}")
        optionTable = cursor.fetchall() #Tabla con las opciones de los pasos de la aventura
        for j in optionTable:
            idAnswers_byStep_Adventure_dic[(j[0], i[0])] = {"Description": j[1], "Resolution_answer":j[2], "NextStep_Adventure":j[8]}

    return idAnswers_byStep_Adventure_dic


