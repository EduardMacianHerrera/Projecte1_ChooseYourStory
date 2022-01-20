'''
from createCon import createConn

def get_characters():

    dictChatacters = {}

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select * from `CHARACTERS`")

    for i in cursor.fetchall():
        dictChatacters[i[0]] = i[1]

    if conexion.is_connected():
        conexion.close()

    return dictChatacters

print(get_characters())
'''