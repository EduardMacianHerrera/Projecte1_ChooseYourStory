text1="Aventura de poker inter dimensional en el bar de Moe Sizlak"

def formatText(text, lenLine, split ="\n"):
    try:
        phrase =""
        word =""
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
                    while len(phrase) < lenLine:
                        phrase =phrase +" "
                    to_print =to_print +split +phrase
                    phrase =word
                    word=""
            count +=1
        while len(phrase) < lenLine:
            phrase = phrase + " "
        to_print = to_print +split +phrase
        print(to_print)
        return to_print
    except:
        if len(word) > lenLine:
            return("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                   "y no se puede formatar correctamente el parrafo")
        else:
            return("La funcion formatText no se ha ejecutado correctamente")

formatText(text1, 18)