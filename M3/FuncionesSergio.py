

#Get formated adventures

dic_adventures ={
1:{"Name":"Aventura 1", "Description":"Es la aventura 1", "Charachers":[1, 4, 5]},
2:{"Name":"Aventura 2", "Description":"Es la aventura 2", "Charachers":[3, 6, 7]},
3:{"Name":"Aventura 3", "Description":"Es la aventura 3", "Charachers":[2, 5, 9]}
}


def getFormatedAdventures(adventures):

    prueba = "\n" + "=" * 20 + "Adventures" + "="* 20 + "\n" + "Id Adventure".ljust(20) + \
             "Adventure".ljust(20) + "Description".ljust(20)




    return prueba


print(getFormatedAdventures(dic_adventures))
