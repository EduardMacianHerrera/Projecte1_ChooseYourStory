#Funció que chequea que un usuari tingui el format correcte.
# longitud entre 6 i 10 i alfanumèric.
# Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatgeinformatiu i retornarà False.
# En cas que el password compleixi tots els requeriments, ens retornarà True

def checkUser(user):
    while True:
        try:
            longitud = 0
            letras = 0
            numeros= 0

            if len(user) >= 6 and len(user) <= 10:
               longitud += 1

            for i in user:
                if i.isdigit():
                    numeros += 1
                if i.isalpha():
                    letras += 1

            if letras < 1 or numeros < 1 or longitud < 1:
                raise ValueError
            else:
                return True

        except ValueError:

            if len(user) < 6 or len(user) > 10:
                print("El nombre de usuario debe tener de 6 a 10 caracteres.")
                return False

            elif letras < 1:
                print("Te falta escribir letras.")
                return False

            elif numeros < 1:
                print("Te falta escribir números.")
                return False

print(checkUser())