from createCon import createConn
from getFormatedReports import getFormatedReports

def games_played_by_user(username):

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute(f"select a.ID_ADVENTURE ,a.adventure_name, g.date from USER u inner join GAME g on u.ID_USER = g.ID_USER inner join ADVENTURE a on g.ID_ADVENTURE = a.ID_ADVENTURE where u.username = '{username}'")

    result = cursor.fetchall()

    if result != []:
        return getFormatedReports(result, 120, ("ID AVENTURE", "NAME", "DATE"), (30))
    else:
        return "**El usuario no tiene partidas**"

print(games_played_by_user("irene2"))