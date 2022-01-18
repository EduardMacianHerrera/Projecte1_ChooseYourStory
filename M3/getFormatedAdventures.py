dic_adventures ={
1:{"Name":"Aventura 1", "Description":"Es la aventura 1", "Charachers":["c1", "c2", "c3"]},
2:{"Name":"Aventura 2", "Description":"Es la aventura 2", "Charachers":["c2", "c3", "c4"]},
3:{"Name":"Aventura 3", "Description":"Es la aventura 3", "Charachers":["c1", "c2", "c4"]},
4:{"Name":"Aventura 4", "Description":"Es la aventura 4", "Charachers":["c2", "c3", "c4"]},
5:{"Name":"Aventura 5", "Description":"Es la aventura 5", "Charachers":["c2", "c3", "c4"]}
}

dic_adventures_Mod ={
1009348457654:{"Name":"Aventura 1", "Description":"Es la aventura 1", "Charachers":["c1", "c2", "c3"]},
2:{"Name":"Aventura numero que se correponde con el segundo valor del sistema de numeración decimal excluyendo el cero", "Description":"Es la aventura 3 amigo, perdon la 2, eso eso, la 2 ", "Charachers":["c2", "c3", "c4"]},
3:{"Name":"Aventura 3", "Description":"Es la aventura que consiste en un viaje por los mundos desconocidos mas alla de la Nube de Magallanes", "Charachers":["c1", "c2", "c4"]},
4:{"Name":"Aventura 4", "Description":"Es la aventura 4", "Charachers":["c2", "c3", "c4"]},
5:{"Name":"Aventura 5", "Description":"Si sigues leyendo este rollo considera buscar ayuda profesional", "Charachers":["c2", "c3", "c4"]}
}

# Esta función se divide en varias partes mas sencillas ejecutadas con otras funciones usadas anteriormente, pero levemente modificadas

# el primer print es un getHeader, pero sin las dos lineas de asteriscos arriba y abajo
# la seguna linea es printar con la formula de getHeaderForTableFromTuples, sin las lineas de arriba y abajo
# la tercera linea es un print de asteriscos muy sencillo con el ancho total que especifiquemos
# la cuarta linea es un print de espacios, también con el ancho total

# A partir de aqui, printando una linea extra de espacios, se
# printa como en la función FormatedBody Columns, esta se ejecutara tantas veces como IDs de aventuras tengamos,
# de ahi que se haga un for j en aventuras, se recorre cada ID de diccionario y esta se usa para añadir a la tupla que
# se printara con la función getFormatedBodyColumns los siguientes elementos, el id, el nombre de la aventura y la descripción
# de esta, se une a la variable to_print, que aglutina el resto de elementos que se printaran

# Como se puede ver, hay 3 parametros de entrada, el diccionario adventures, el widht o ancho total, imagino seran los 100-120
# de ancho que nos indicaban y la tupla

def getFormatedAdventures(adventures, width, t_w_columns):
    try:
        def getHeader_Mod1(text, width):
            try:
                if len(text) > width:
                    return "El texto es mayor que el ancho y no se puede formatar correctamente"
                a1 = (width // 2) - (len(text) // 2)
                a2 = (width // 2) - (len(text) // 2)
                if (a1 + a2 + len(text)) > width:
                    a1 -= 1
                elif (a1 + a2 + len(text)) < width:
                    a2 += 1
                Header = (("=" * a1) + (text) + ("=" * a2))
                return Header
            except:
                return "La funcion getHeader no se ha ejecutado correctamente"
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
                if len(tupla_texts) != len(tupla_sizes):
                    return "La longitud de ambas tuplas no es la misma"
                else:
                    return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"
        # A partir de aqui deja de declarar otras funciones y empieza el codigo de la funcion
        if len(t_w_columns) != 3:
            raise ValueError
        for i in t_w_columns:
            if i < 12:
                Error_long =True
                raise ValueError
        to_print = getHeader_Mod1("Adventures", width) + "\n" \
                   + (" " *width) + "\n" \
                   + getHeadeForTableFromTuples_Mod1(("Id Adventure","Adventure","Description"), t_w_columns)+ "\n" \
                   + ("*" *width) + "\n" \
                   + (" " * width) + "\n"
        for j in adventures:
            tupla_t =(str(j), str(adventures[j]["Name"]), str(adventures[j]["Description"]))
            to_print =to_print + getFormatedBodyColumns(tupla_t, t_w_columns)
        return(to_print)
    except:
        if len(t_w_columns) != 3:
            return "La tupla de entrada tiene una longitud distinta de 3 elementos"
        elif Error_long:
            return "Los espacios de separación entre parrafos son demasiado cortos"
        else:
            return "Error en la ejecución de la función getFormatedAdventures"

print(getFormatedAdventures(dic_adventures, 100, (15, 15, 15)))
