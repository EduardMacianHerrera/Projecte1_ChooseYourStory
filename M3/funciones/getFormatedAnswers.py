'''
from createCon import createConn


textoPrueba = "Aprovechas y le robas su ultima judia magica (puede venirte bien en combate)"

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

print(getFormatedAnswers(142, textoPrueba, 100,5))



keyAnswer, count = 0,0
for i in dict.keys():
    for j in i:
        if count < 1:
            keyAnswer = j
            count += 1

getFormatedAnswers(keyAnswer, dict[(keyAnswer,1)]["Resolution_Anwer"], 2, 1)


'''

