import datetime

tupla1 =(('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA -DESCRIPCION', 'NUMERO VECES SELECCIONADA', "errr"))

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
                if len(tupla_texts) > len(tupla_sizes):
                    return "La longitud de la tupla de parrafos es superior a la de titulos"
                else:
                    return "La funcion getFormatedBodyColumns no se ha ejecutado correctamente"
        # A partir de aqui deja de declarar otras funciones y empieza el codigo de la funcion
        ErrorT_SP =False
        Error_long =False
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
        for j in adventures:
            # La tupla_t es lo que se tiene que modificar, entra los parrafos
            tupla_t =adventures
            if len(t_w_columns) > len(tupla_t):
                t_w_columns = tuple_cutter(t_w_columns, tupla_t)
            elif len(t_w_columns) > len(tupla_t):
                t_w_columns =tuple_extender(t_w_columns, tupla_t)
            to_print =to_print + getFormatedBodyColumns(tupla_t, t_w_columns) + (" " *width) +"\n"
        return(to_print)
    except:
        if ErrorT_SP:
            return "No todos los valores de la tupla son numeros enteros"
        if Error_long:
            return "Los espacios de separación entre parrafos son demasiado cortos para encajar los" \
                   " titulos de las columnas"
        else:
            return "Error en la ejecución de la función getFormatedAdventures"

tupla1 =(('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA -DESCRIPCION', 'NUMERO VECES SELECCIONADA'))
tuplas_nombres = ("Id AVENTURA-NOMBRE", "ID PASO-DESCRIPCION", "ID RESPUESTA-DESCRIPCION", "NUMERO VECES SELECCIONADA")
tuplas_anchos = (30, 30)
print(getFormatedAdventures(tupla1, 120, tuplas_nombres, tuplas_anchos))
