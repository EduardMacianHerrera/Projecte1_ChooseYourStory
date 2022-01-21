t_nombre_columnas =("column1","column2","column3", "column4")
t_tamaños =(10,20,30,20)

# def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
#     to_print =""
#     count =0
#     for i in t_size_columns:
#         to_print =to_print + t_name_columns[count] + (" "*i)
#         count +=1
#     print("=" *len(to_print))
#     print(to_print)
#     print("*" *len(to_print))
#
# getHeadeForTableFromTuples(t_nombre_columnas, t_tamaños)


def getHeadeForTableFromTuples_Mod1(t_name_columns, t_size_columns, title=""):
    try:
        to_print = ""
        count = 0
        for i in t_size_columns:
            to_print = to_print + t_name_columns[count] + ("_" * (i - len(t_name_columns[count]) + 2))
            count += 1
        return to_print
    except:
        return "Error en la función getHeadeForTableFromTuples_Mod1"

print(getHeadeForTableFromTuples_Mod1(t_nombre_columnas, t_tamaños))