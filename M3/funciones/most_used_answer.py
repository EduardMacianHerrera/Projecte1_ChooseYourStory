from createCon import createConn
from getFormatedReports import getFormatedReports


def most_used_answer():

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select a.ID_ADVENTURE, a.adventure_name, s.ID_STEP ,s.description, o.ID_OPTION, o.description, count(r.ID_OPTION) as 'cuenta' from RECORD r inner join `OPTION` o on r.ID_OPTION = o.ID_OPTION inner join STEP s on o.ID_STEP_FROM = s.ID_STEP inner join ADVENTURE a on s.ID_ADVENTURE = a.ID_ADVENTURE group by r.ID_OPTION order by cuenta desc limit 5")
    respuesta = cursor.fetchall()

    listaResultado = []

    for i in respuesta:
        elementoLista = []
        id_aventura_nombre = str(i[0]) + " " +"-" + " " + str(i[1])
        id_paso_descripcion = str(i[2]) + " " + "-" + " " + str(i[3])
        id_opcion_descripcion = str(i[4]) + " " + "-" + " " + str(i[5])
        elementoLista.append(id_aventura_nombre)
        elementoLista.append(id_paso_descripcion)
        elementoLista.append(id_opcion_descripcion)
        elementoLista.append(str(i[6]))
        listaResultado.append(elementoLista)

    return getFormatedReports(listaResultado, 120, ("ID AVENTURA - NOMBRE", "ID PASO - DESCRIPCION", "ID RESPUESTA - DESCRIPCTION", "NUMERO VECES SELECCIONADO"), (30, 30, 30, 30))


print(most_used_answer())





