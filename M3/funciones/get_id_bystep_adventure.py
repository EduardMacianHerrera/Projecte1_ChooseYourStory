from createCon import createConn

global idAventura
idAventura = 2

dict = { 2: {'Description': 'Efectivamente, el puente es elc├ímino mas corto, no contabas con que el puente se descolgar├¡a, y no sobrevives a la caida. FIN','answers_in_step': (), 'Final_Step': 1}}

def getIdByStepAdventure():
    #Ens retornarà el diccionariid_by_stepsamb nomésels passos relacionats ambl'aventura que estem jugant

    dictResult = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f"select * from STEP where ID_ADVENTURE = {idAventura}")
    result = cursor.fetchall()

    for i in result:
        dictResult[i[0]] = {"Description": i[1], "answers_in_step":[], "Final_Step": i[2]} #Faltan los pasos

    for i in dictResult:
        cursor.execute(f"select ID_OPTION from `OPTION` where ID_STEP_FROM = {i}")
        idOptions = cursor.fetchall()
        for j in idOptions:
            dictResult[i]["answers_in_step"].append(j[0])
        dictResult[i]["answers_in_step"] = tuple(dictResult[i]["answers_in_step"])

    if conexion.is_connected():
        conexion.close()

    return dictResult

