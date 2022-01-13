from createCon import createConn

def get_table(query):
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    descripcion = mycursor.description

    lista = []

    for i in descripcion:
        lista.append(i[0])

    tupla0 = tuple(lista)
    resultado.insert(0,tupla0)
    resultado = tuple(resultado)
    return resultado


print(get_table("Select * from USER"))
