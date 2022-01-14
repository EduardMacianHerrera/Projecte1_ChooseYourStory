from get_table_info import get_table

t1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo " \
          "seguir con la aventura que estabas viviendo"
t2 = "Estas historias daban al lector una mayor sensación de immersión en la historia"
t3 = "Este formato se ha trasladado al mundo de los videojuegos"

t4 = "Id Adventure"
t5 = "Este muerto esta muy vivo muy vivo muy vivo"
t6 = "Beowulf, se embarca en la busqueda de la espada llamada la Ira de los cielos"

def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin ="  "):
    def formatText_Mod1(text, lenLine):
        try:
            phrase = ""
            word = ""
            to_print = []
            count = 0
            for i in (text + " "):
                word = word + i
                if len(word) > lenLine:
                    raise ValueError
                if i == " ":
                    if len(phrase + word) < lenLine:
                        phrase = phrase + word
                        word = ""
                    else:
                        while len(phrase) < lenLine:
                            phrase = phrase + " "
                        to_print.append(phrase)
                        phrase = word
                        word = ""
                count += 1
            while len(phrase) < lenLine:
                phrase = phrase + " "
            to_print.append(phrase)
            return to_print
        except:
            if len(word) > lenLine:
                return ["Al menos una de las ",
                        "palabras tiene una  ",
                        "longitud superior a ",
                        "la de la linea y no ",
                        "se puede formatar el",
                        "parrafo"]
            else:
                return ["La funcion          ",
                        "formatText no se ha ",
                        "ejecutado           ",
                        "correctamente       "]
    try:
        if len(tupla_texts) != len(tupla_sizes):
            raise ValueError
        paragraphs = []
        count =0
        for i in tupla_texts:
            paragraphs.append(formatText_Mod1(i, tupla_sizes[count]))
            count +=1
        to_print =""
        max_h = 0
        for j in paragraphs:
            if len(j) > max_h:
                max_h =len(j)
        count =0
        for k in paragraphs:
            while len(k) < max_h:
                k.append(" " *tupla_sizes[count])
            count +=1
        for l in range(max_h):
            for p in range(len(paragraphs)):
                to_print =to_print + paragraphs[p][l] +margin
            to_print = to_print +"\n"
        print(to_print)
        return (to_print)
    except:
        if len(tupla_texts) != len(tupla_sizes):
            return ("La longitud de ambas tuplas no es la misma")
        else:
            return ("La funcion getFormatedBodyColumns no se ha ejecutado correctamente")



def getFormatedTable(queryTable,title=""):
    for i in range (1,len(queryTable)):
        getFormatedBodyColumns(queryTable[i],(20,20,20))

getFormatedTable(get_table("select ID_USER,username,password from USER"))
