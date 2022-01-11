t1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo " \
          "seguir con la aventura que estabas viviendo simplemente"

t2 = "Estas historias daban al lector una mayor sensación de immersión en la historia"

t3 = "Este formato se ha trasladado al mundo de los videojuegos"

# Esta función es una modificación de formatText, que también divide el texto en lineas
# la diferencia es que cada linea será un elemento de una lista.
#
# Tenerlo dentro de una lista nos sera util para printar luego varios textos,
# seleccionando que parte de cada uno debe aparecer en que momento
def formatText_list(text, lenLine):
    try:
        phrase =""
        word =""
        to_print =[]
        count =0
        for i in (text +" "):
            word =word +i
            if len(word) > lenLine:
                raise ValueError
            if i ==" ":
                if len(phrase +word) < lenLine:
                    phrase =phrase +word
                    word = ""
                else:
                    to_print.append(phrase)
                    phrase =word
                    word=""
            count +=1
        to_print.append(phrase)
        return to_print
    except:
        if len(word) > lenLine:
            return("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                   "y no se puede formatar correctamente el parrafo")
        else:
            return("La funcion formatText no se ha ejecutado correctamente")

# Esta función primero se asegura de que ambas tuplas tengan la misma longitud
# Posteriormente crea dos listas que contendran por un lado:
# -Los parrafos en formato una lista de listas, cada lista interna es un parrafo y cada elemento de esa lista una linea
# -En una lista de listas de las mismas dimensiones, los espacios, tras cada linea impresa de la lista anterior, se le imprimira
#   justo despues un espacio que la separara de la siguiente linea.

# Si tenemos x parrafos, cada x cantidad de imprimir la linea mas su espacio, todo_ acumulado en una linea
# hay que añadir un salto para que empieze a imprimir abajo
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    try:
        if len(tupla_texts) != len(tupla_sizes):
            raise ValueError
        paragraphs = []
        spaces = []
        count =0
        for i in tupla_texts:
            paragraphs.append(formatText_list(i, tupla_sizes[count]))
            count +=1
        count =0
        for j in paragraphs:
            spaces.append([])
            for k in j:
                max_w = tupla_sizes[count]
                spaces[count].append(" " *(max_w -len(k)))
            count +=1
        to_print =""
        max_h = 0
        for k in paragraphs:
            if len(k) >max_h:
                max_h =len(k)
        for l in range(max_h):
            for p in range(len(paragraphs)):
                if len(paragraphs[p]) > l:
                    to_print =to_print + paragraphs[p][l] + spaces[p][l]
            to_print = to_print +"\n"
        return (to_print)
    except:
        if len(tupla_texts) != len(tupla_sizes):
            return ("La longitud de ambas tuplas no es la misma")
        else:
            return ("La funcion getFormatedBodyColumns no se ha ejecutado correctamente")

tupla_t = (t1, t2, t3, t2)
sizes = (20, 30, 50, 40)
print(getFormatedBodyColumns(tupla_t,sizes))
