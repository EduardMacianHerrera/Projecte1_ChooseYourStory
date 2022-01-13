t1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo " \
          "seguir con la aventura que estabas viviendo"
t2 = "Estas historias daban al lector una mayor sensación de immersión en la historia"
t3 = "Este formato se ha trasladado al mundo de los videojuegos"

t4 = "Id Adventure"
t5 = "Este muerto esta muy vivo muy vivo muy vivo"
t6 = "Beowulf, se embarca en la busqueda de la espada llamada la Ira de los cielos"


# Dentro de esta función esta formatText_Mod1, una modificación de formatText, que también divide el texto en lineas
# la diferencia es que cada linea será un elemento de una lista.
#
# Tenerlo dentro de una lista nos sera util para printar luego varios textos,
# seleccionando que parte de cada uno debe aparecer en que momento
#
# Los elementos de la funcion formatText_Mod1, las lineas (en formato string), ya vienen todas con el mismo ancho lenLine en los datos
# de entrada, cuando las palabras no llegan a esa longitud, añade espacios " " que al printar no se ven
# pero hacen que la longitud de ese string sea la misma.

# La función getFormatedBodyColumns primero obtiene los parrafos que imprimira uno al lado del otro, estos
# parrafos se obtienen con la función formatText_Mod1 en forma de lista donde cada elemento string es una linea.
#
# Define la variable to_print, que sera toodo lo que tiene que printar, incluyendo espacios entre lineas y saltos de linea
#
# Necesitamos obtener la maxima altura de los parrafos, eso es max_h, la altura de los parrafos sera equivalente a la cantidad
# de elementos que tiene su lista, casa elemento es una linea, cuando acaba debe haber salto de pagina.
# Todos los parrafos que sean menores a max altura, les añadimos tantas lineas vacias de espacios (equivalentes al ancho maximo)
# como lineas o elementos de lista le falten para igualar esa maxima altura.
#
# Vamos a colocar en la variable to_print tooodo lo que queremos imprimir. La idea es que queremos poner la primera linea del primer
# parrafo, luego la primera linea del segundo parrafo, luego la primera del tercer parrafo, asi sucesivamente hasta llegar al salto de linea
# entonces colocaremos las segundas lineas de cada parrafo.
#
# Estas lineas tienen todas el mismo ancho, junto con los 2 espacios minimo que las separan. Ademas, todos los parrafos tienen la misma cantidad
# de lineas, aunque a partir de cierto punto esten vacias y solo sean espacios (Es necesario para que se coloque todo a sitio)


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

tupla_t = (t1, t2, t3, t4, t5, t6)
sizes = (20, 30, 40, 20, 20, 20)
getFormatedBodyColumns(tupla_t,sizes)

# A revisar el problema de anchos cuando hay un error