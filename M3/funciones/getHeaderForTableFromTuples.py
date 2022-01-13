t_nombre_columnas =("column1","column2","column3")
t_tamaños =(10,20,30)

def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
    to_print =""
    count =0
    for i in t_size_columns:
        to_print =to_print + t_name_columns[count] + (" "*i)
        count +=1
    print("=" *len(to_print))
    print(to_print)
    print("*" *len(to_print))

getHeadeForTableFromTuples(t_nombre_columnas, t_tamaños)