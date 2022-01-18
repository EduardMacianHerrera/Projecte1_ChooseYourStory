from createCon import createConn
id_adventure = 7
def get_first_step_adventure():
    proyecto = createConn()
    mycursor = proyecto.cursor()
    mycursor.execute(f"select ID_STEP,description from STEP where ID_ADVENTURE = {id_adventure} and START = 1")
    resultado = mycursor.fetchall()
    if proyecto.is_connected():
        proyecto.close()
    return resultado
print(get_first_step_adventure())