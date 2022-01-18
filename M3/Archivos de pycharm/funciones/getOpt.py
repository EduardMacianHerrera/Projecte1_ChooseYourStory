
#Get opt

textOpts = "\n1)Login\n2)Create User\n3)Show Adventures\n4)Exit"
inputText="->Option: "
rangoLista = [1,2,3,4]
excepciones = ["w","e",-1]
dictExcepciones = {10:"t", "lol":9}


def getOpt(textOpts = "", inputOptText="", rangeList=[], dictionary = {}, exceptions = []):

    correctOpc, useException = False, False
    leftMargin = 50

    while not correctOpc:

        useException = False

        opciones = textOpts.split("\n")

        for i in opciones:
            print(" " * leftMargin + i)

        opc = input("\n" + " " * leftMargin + inputOptText)

        for i in rangeList:
            if opc == str(i):
                correctOpc = True
                break

        if len(exceptions) != 0:
            for i in exceptions:
                if str(i) == opc:
                    print("Has pulsado la", i)
                    useException = True
                    break

        if len(dictionary) != 0:
            for j, k in dictionary.items():
                if str(j) == opc:
                    print("Has pulsado la", j)
                    useException = True
                elif str(k) == opc:
                    print("Has pulsado la", k)
                    useException = True

        if not correctOpc and not useException:
            print(" " * leftMargin + "===== Invalid option =====")

    return opc

