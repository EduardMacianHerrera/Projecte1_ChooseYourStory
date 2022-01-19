tupla_ejemlo =(("paso_1 Te encuentras en una situación muy extraña, con 3 puertas frente a ti, una azul, una verde y otra roja:\n"
         "opcion_1 abres la puerta azul de la que sientas que te dara un gran conocimiento\n"
         "opcion_2 abres la puerta verde, de la que sientes que te dara una gran serenidad y felicidad\n"
         "opcion_3 abres la puerta roja, sientes que te dara fuerza y gloria", "Eliges la puerta azul, crees que el conocimiento que te de el viaje es lo mas valioso"), ("paso_2", "seleccion_2"),
        ("paso_3", "seleccion_3"), ("paso_4", "seleccion_4"))

# Entiendo que los datos de entrada tendrian esta estructura, tupla de tuplas donde cada subtubla tiene como primer elemento
# el paso junto a sus opciones y el segundo elemento de la tupla es la descripción de nuestra selección

def replay(tuple, width):
    try:
        def formatText_Mod(text, lenLine, split="\n"):
            try:
                phrase = ""
                word = ""
                to_print = ""
                count = 0
                for i in (text + " "):
                    word = word + i
                    if len(word) > lenLine*(1 +(text.count("\n"))):
                        raise ValueError
                    if i == " ":
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
        for i in range(len(tuple)):
            for k in range(len(tuple[i])):
                paso = input("\n        Press Enter to continue:")
                print(formatText_Mod(tuple[i][k], width))
    except:
        print("La función replay no se ha ejecutado correctamente")


replay(tupla_ejemlo, 100)