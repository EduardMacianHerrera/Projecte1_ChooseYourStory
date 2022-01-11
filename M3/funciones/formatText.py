text1="Aventura de poker inter dimensional en el bar de Moe Sizlak"

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

print(formatText(text1, 18, "\n"))