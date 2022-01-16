from createCon import createConn
from getHeader import getHeader

dict ={(142, 1): {'Description': 'Escoge el camino del centro, del que parecen provenir ruidos de ramas al romperse y astillarse ...',
                 'Resolution_Anwer': 'Piensas que para ser digno de la espada de las valkirias, debes de afrontar tus miedos y peligros que acechan',
                 'NextStep_Adventure': 3}}



#Get formated answers:

def getFormatedAnswers(idAnswers, text, lenLine, leftMargin):

    conexion = createConn()
    cursor = conexion.cursor()

    cursor.execute(f"select description from `OPTION` where ID_OPTION = {idAnswers}")
    respuesta = cursor.fetchall()

    print(getHeader("Nombre aventura", 100))
    print(text + "\nOptions:")
    print("\n" + (" " * leftMargin) + respuesta[0][0])


keyAnswer, count = 0,0
for i in dict.keys():
    for j in i:
        if count < 1:
            keyAnswer = j
            count += 1

getFormatedAnswers(keyAnswer, dict[(keyAnswer,1)]["Resolution_Anwer"], 2, 1)


#Falta nombre aventura y numeración de respuestas


