# TABELA ASCII --> (A=65 / a = 97) == (Z=90 / z=122)

#maiusculas('Programamos em python 2?')
# deve devolver 'P'

#maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

#maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

def maiusculas(string):
    new_string = ''
    for i in range(len(string)):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            new_string += string[i]
    return new_string

