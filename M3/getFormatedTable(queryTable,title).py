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