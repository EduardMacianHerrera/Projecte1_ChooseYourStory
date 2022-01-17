from get_table_info import get_table
import datetime

tupla1 =(('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA -DESCRIPCION', 'NUMERO VECES SELECCIONADA', "errr"))

    def getHeadeForTableFromTuples_Mod1(t_name_columns, t_size_columns, title=""):
        try:
            to_print = ""
            count = 0
            for i in t_size_columns:
                to_print = to_print + t_name_columns[count] + (" " * (i - len(t_name_columns[count]) +2))
                count += 1
            return to_print
        except:
            return "Error en la función getHeadeForTableFromTuples_Mod1"
    def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin="  "):
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
                            "parrafo             "]
                else:
                    return ["La funcion          ",
                            "formatText no se ha ",
                            "ejecutado           ",
                            "correctamente       "]
        try:
            if len(tupla_texts) != len(tupla_sizes):
                raise ValueError
            paragraphs = []
            count = 0
            for i in tupla_texts:
                i = str(i)
                paragraphs.append(formatText_Mod1(i, tupla_sizes[count]))
                count += 1
            to_print = ""
            max_h = 0
            for j in paragraphs:
                if len(j) > max_h:
                    max_h = len(j)
            count = 0
            for k in paragraphs:
                while len(k) < max_h:
                    k.append(" " * tupla_sizes[count])
                count += 1
            for l in range(max_h):
                for p in range(len(paragraphs)):
                    to_print = to_print + paragraphs[p][l] + margin
                to_print = to_print + "\n"
            return (to_print)
        except:
            if len(tupla_texts) > len(tupla_sizes):
                return "La longitud de la tupla de parrafos es superior a la de titulos"
            else:
                return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"


def getFormatedTable(queryTable,title=""):
    for i in range (len(queryTable)):
        print(getFormatedAdventures(queryTable[i],120,queryTable[0],(20,20)))
print(getFormatedTable(get_table("select * from ADVENTURE")))
