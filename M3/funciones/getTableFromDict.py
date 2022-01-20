'''
import datetime

#getTableFromDict

dict = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName':
'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}

tuple_of_keys = ("Username","Name","CharacterName", "date")
weigth_of_columns = (20, 30, 20, 20)


def getTableFromDict(tuple_of_keys, wight_of_columns, dict_of_data):

    data = ""

    try:
        for i in dict_of_data:
            data += str(i)
            for j in range(len(weigth_of_columns)):
                data += " " * wight_of_columns[j] + str(dict_of_data[i][tuple_of_keys[j]])
            data += "\n"

    except:
        print("** Debes introducir el mismo número de keys que de weigth **")

    return data
'''