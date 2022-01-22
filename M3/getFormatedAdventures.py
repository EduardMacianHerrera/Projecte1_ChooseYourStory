# from get_adventures_with_char import get_adventures_with_chars
#
# dic_adventures = get_adventures_with_chars()

# El diccionario de ejemplo basico
dic_adventures ={
1:{"Name":"Aventura 1", "Description":"Es la aventura 1", "Charachers":["c1", "c2", "c3"]},
2:{"Name":"Aventura 2", "Description":"Es la aventura 2", "Charachers":["c2", "c3", "c4"]},
3:{"Name":"Aventura 3", "Description":"Es la aventura 3", "Charachers":["c1", "c2", "c4"]},
4:{"Name":"Aventura 4", "Description":"Es la aventura 4", "Charachers":["c2", "c3", "c4"]},
5:{"Name":"Aventura 5", "Description":"Es la aventura 5", "Charachers":["c2", "c3", "c4"]},
6:{"Name":"Aventura 6", "Description":"Es la aventura 6", "Charachers":["c1", "c3", "c5"]},
7:{"Name":"Aventura 7", "Description":"Es la aventura 7", "Charachers":["c1", "c2", "c4"]},
8:{"Name":"Aventura 8", "Description":"Es la aventura 8", "Charachers":["c2", "c3", "c5"]},
9:{"Name":"Aventura 9", "Description":"Es la aventura 9", "Charachers":["c1", "c2", "c4"]},
10:{"Name":"Aventura 10", "Description":"Es la aventura 10", "Charachers":["c2", "c3", "c4"]},
11:{"Name":"Aventura 11", "Description":"Es la aventura 11", "Charachers":["c2", "c3", "c4"]},
12:{"Name":"Aventura 12", "Description":"Es la aventura 12", "Charachers":["c1", "c3", "c5"]},
13:{"Name":"Aventura 13", "Description":"Es la aventura 13", "Charachers":["c1", "c2", "c4"]},
}

# Otro diccionario de ejemplo mas enrevesado, con parrafos de distinta longitud para encontrar errores
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

def getFormatedAdventures(adventures, width, t_name_columns, t_w_columns):
    try:
        def tuple_cutter(tuple_to_cut, tuple_ref):
            # Esta función sirve para que en caso de que las tuplas tengan longitudes distintas, la que marca
            # los espacios se recorte para tener la misma longitud que la que tiene los textos de las columnas,
            # asi en vez de saltar un error, lo corrige
            while len(tuple_to_cut) > len(tuple_ref):
                tuple_to_cut = list(tuple_to_cut)[:-1]
            return tuple(tuple_to_cut)
        def tuple_extender(tuple_to_ext, tuple_ref):
            # Función que sirve para añadir valores a la tupla de espacios en caso de que tenga una
            # cantidad de espacios inferior a la de titulos, va añadiendo al final de la lista los valores que ya tenia la
            # tupla ej t = (10, 20) la alargamos a 6 sera t =(10, 20, 10, 20, 10, 20
            values = list(tuple_to_ext)
            pos = 0
            while len(tuple_to_ext) < len(tuple_ref):
                tuple_to_ext = list(tuple_to_ext)
                tuple_to_ext.append(values[pos])
                if pos < len(values) - 1:
                    pos += 1
                else:
                    pos = 0
            tuple_to_ext = tuple(tuple_to_ext)
            return tuple(tuple_to_ext)
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
                if len(tupla_texts) != len(tupla_sizes):
                    return "La longitud de ambas tuplas no es la misma"
                else:
                    return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"
        # A partir de aqui deja de declarar otras funciones y empieza el codigo de la funcion
        ErrorT_SP = False
        Error_long = False
        for f in t_w_columns:
            if type(f) != int:
                ErrorT_SP =True
                raise ValueError
        if len(t_w_columns) > len(t_name_columns):
            t_w_columns =tuple_cutter(t_w_columns, t_name_columns)
        elif len(t_w_columns) < len(t_name_columns):
            t_w_columns =tuple_extender(t_w_columns, t_name_columns)
        max_w = 0
        for word in t_name_columns:
            if len(word) > max_w:
                max_w = len(word)
        for i in t_w_columns:
            if i < max_w:
                Error_long =True
                raise ValueError
        # La razón de este error es que si el espacio que damos para los parrafos es demasiado pequeño respecto al
        # titulo, debajo de un titulo veremos un parrafo muy corto y pegado otro parrafo, aun ocupando el espacio de debajo del titulo
        to_print = getHeader_Mod1("Adventures", width) + "\n" \
                   + (" " *width) + "\n" \
                   + getHeadeForTableFromTuples_Mod1(t_name_columns, t_w_columns)+ "\n" \
                   + ("*" *width) + "\n" \
                   + (" " * width) + "\n"
        count_List =1       #
        Printar_lista = True             #
        Tuples_length_correct = False    #
        Scrollear = True
        while Scrollear:
            # En este caso tupla_t recoge la ID de la aventura, el nombre de la aventura y la descripción de esta
            tupla_t =(str(count_List), str(adventures[count_List]["Name"]), str(adventures[count_List]["Description"]))
            if Tuples_length_correct == False:
                if len(t_w_columns) > len(tupla_t):
                    t_w_columns = tuple_cutter(t_w_columns, tupla_t)
                elif len(t_w_columns) > len(tupla_t):
                    t_w_columns =tuple_extender(t_w_columns, tupla_t)
                Tuples_length_correct = True
            to_print =to_print + getFormatedBodyColumns(tupla_t, t_w_columns) + (" " *width) +"\n"
            if count_List == 3 or count_List > 5:
                if (count_List)%3 ==0 or count_List == len(adventures):
                    print(to_print)
                    scroll = input("Scroll down: + / Scroll up: - / OUT: 0) ")
                    while scroll != "+" and scroll != "-" and scroll != "0" and scroll.isdigit() == False:
                        scroll = input("Scroll down: + / Scroll up: - / OUT: 0) ")
                    if scroll.isdigit():
                        if int(scroll) > 0 and int(scroll) < len(adventures):
                            Num_elegido = scroll
                            print(f"Aventura {Num_elegido} elegida")
                            Printar_lista = False
                            Scrollear = False
                        # while scroll.isdigit() and Scrollear == True:
                        #     if int(scroll) > 0 and int(scroll) < len(adventures):
                        #         Num_elegido = scroll
                        #         print(f"Aventura {Num_elegido} elegida")
                        #         Printar_lista = False
                        #         Scrollear = False
                        #     else:
                        #         scroll = input("Scroll down: + / Scroll up: - / OUT: 0) ")
                        # else:
                        #     if Scrollear == True:
                        #         scroll = input("Scroll down: + / Scroll up: - / OUT: 0) ")
                    print("")
                    to_print = ""
                    if scroll == "0":
                        break
                    if scroll == "-" and count_List > 2:
                        if count_List == 3:
                            count_List =0
                        else:
                            if count_List == len(adventures):
                                count_List = count_List -4
                            else:
                                count_List =count_List -6
            if count_List < (len(adventures)):
                count_List += 1
        if Printar_lista == True:
            print(to_print)
        return Num_elegido
    except:
        if ErrorT_SP:
            return "No todos los valores de la tupla son numeros enteros"
        if Error_long:
            return "Los espacios de separación entre parrafos son demasiado cortos para encajar los" \
                   " titulos de las columnas"
        else:
            return "Error en la ejecución de la función getFormatedAdventures"


tuplas_nombres = ("Id Adventure", "Adventure", "Description", "Otra info")
tuplas_anchos = (30, 15)
Numer_Elegido = getFormatedAdventures(dic_adventures, 120, tuplas_nombres, tuplas_anchos)
print(Numer_Elegido)

