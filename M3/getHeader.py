text1="Aventura de poker inter dimensional en el bar de Moe Sizlak"

def getHeader(text, width):
    try:
        if len(text) > width:
            return "\nEl texto es mayor que el ancho y no se puede formatar correctamente"
        a1 = (width//2) -(len(text)//2)
        a2 =  (width//2) -(len(text)//2)
        if (a1 +a2 +len(text)) > width:
            a1 -=1
        elif (a1 +a2 +len(text)) < width:
            a2 +=1
        Header = ("*"*width) + ("\n") + (("="*a1) +(text) +("="*a2)) + ("\n") + ("*"*width)
        return Header
    except:
        print("La funcion getHeader no se ha ejecutado correctamente")

print(getHeader(text1, 80))