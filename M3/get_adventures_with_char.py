
from createCon import createConn

def get_adventures_with_chars():
    conexion = createConn()
    cursor = conexion.cursor()

    cursor.execute("select ADVENTURE.ID_ADVENTURE, adventure_name, description from ADVENTURE")
    resAdventure = cursor.fetchall()
    cursor.execute("Select * from STARS")
    resStars = cursor.fetchall()

    adventures = {}

    for i in resAdventure:
        lista = []
        for n in resStars:
            if n[0] == i[0]:
                lista.append(n[1])
        diccTemp = {i[0]: {"Name": i[1], "Description": i[2], "characters": lista}}
        adventures.update(diccTemp)

    return adventures


print(get_adventures_with_chars())
