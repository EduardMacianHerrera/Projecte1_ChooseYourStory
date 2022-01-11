t1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo " \
          "seguir con la aventura que estabas viviendo simplemente"


def formatText(text, lenLine, split):
    try:
        phrase =""
        word =""
        word2 =""
        to_print =""
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
                    to_print =to_print +split +phrase
                    phrase =word
                    word=""
            count +=1
        to_print = to_print +split +phrase
        to_print =to_print +split +word2
        return to_print
    except:
        if ValueError:
            return("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                   "y no se puede formatar correctamente el parrafo")
        else:
            return("La funcion formatText no se ha ejecutado correctamente")
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    try:
        if len(tupla_texts) !=len(tupla_sizes):
            raise ValueError
        count =0
        for i in tupla_texts:
            print(formatText(i, tupla_sizes[count], "\n"))
            count +=1
    except:
        if len(tupla_texts) !=len(tupla_sizes):
            print("La tupla de textos y la tupla de tamaños no tienen la misma longitud\n"
                  "y no se puede ejecutar correctamente el formateo")
        else:
            print("La funcion getFormatedBodyColumns no se ha ejecutado correctamente")

tupla_t = (t1, t1, t1)
sizes = (20, 30, 50)
getFormatedBodyColumns(tupla_t,sizes)