from createCon import createConn

def get_characters():

    dictChatacters = {}

    con = createConn()
    cursor = con.cursor()
    cursor.execute("select * from CHARACTERS")

    for i in cursor.fetchall():
        dictChatacters[i[0]] = i[1]

    return dictChatacters

print(get_characters())