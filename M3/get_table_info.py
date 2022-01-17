from createCon import createConn

def get_table(query):
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    descripcion = mycursor.description

    if proyecto.is_connected():
        proyecto.close()

    lista = []

    for i in descripcion:
        lista.append(i[0])

    tupla0 = tuple(lista)
    resultado.insert(0,tupla0)
    resultado = tuple(resultado)
    return resultado
