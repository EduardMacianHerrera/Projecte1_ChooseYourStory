#Funció que chequea si el format del password és correcte.Un password correcte tindrà una longitud entre 8 i 12 caràcters.
# Alguna lletra majúscula, alguna lletra minúscula, algun número, algun caràcter especial,sense espais.

def checkPassword():
    while True:

        try:
            letras = 0
            numeros = 0
            mayusculas = 0
            minusculas = 0
            espacioBlanco = 0

            password = input("Introduce tu contraseña, esta debe tener, mayusculas,minusculas,numeros, letras y de 8 a 12 caracteres: ")

            if len(password) < 8 or len(password) > 12:
                raise ValueError

            for i in password:
                if i.isalpha():
                    letras += 1

                if i.isdigit():
                    numeros += 1

                elif i.isupper():
                    mayusculas += 1

                elif i.islower():
                    minusculas += 1

                elif i == " ":
                    espacioBlanco += 1


            if numeros < 1 or mayusculas < 1 or minusculas < 1 or espacioBlanco >= 1:
                raise ValueError

            else:
                return True

        except ValueError:

            if len(password) < 8 or len(password) > 12:
                print("La contraseña debe tener de 8 a 12 caracteres.")
                return False
            elif espacioBlanco >= 1:
                print("No puede contener espacios en blanco.")
                return False
            elif letras < 1:
                print("Te falta escribir letras.")
                return False
            elif mayusculas < 1:
                print("Te falta escribir mayusculas.")
                return False
            elif minusculas < 1:
                print("Te falta escribir minusculas.")
                return False
            elif numeros < 1:
                print("Te falta escribir números.")
                return False


print(checkPassword())
