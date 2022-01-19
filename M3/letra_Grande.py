import art

def letra_Grande(texto):
    def formatText_Mod2(text, lenLine, split="\n"):
        try:
            text = text.replace('\n', "")
            phrase = ""
            word = ""
            to_print = ""
            count = 0
            for i in (text + " "):
                word = word + i
                if len(word) > lenLine:
                    raise ValueError
                if i == " ":
                    word = word +" "
                    if len(phrase + word) < lenLine:
                        phrase = phrase + word
                        word = ""
                    else:
                        while len(phrase) < lenLine:
                            phrase = phrase + " "
                        to_print = to_print + split + phrase
                        phrase = word
                        word = ""
                count += 1
            while len(phrase) < lenLine:
                phrase = phrase + " "
            to_print = to_print + split + phrase
            return to_print
        except:
            if len(word) > lenLine:
                return ("Al menos una de las palabras tiene una longitud superior a la de la linea\n"
                        "y no se puede formatar correctamente el parrafo")
            else:
                return ("La funcion formatText no se ha ejecutado correctamente")
    if len(texto) > 100:
        formatText_Mod2(texto, 100)
    formatado =art.text2art(texto, font ="small")
    if len(formatado) > 100:
        texto =formatText_Mod2(texto, (len(texto)/2))
        formatado =art.text2art(texto, font ="small",)
    return formatado

texto =letra_Grande("Bienvenido a CHOOSE YOUR HISTORY")
print(texto)
