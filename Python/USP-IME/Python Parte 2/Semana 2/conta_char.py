# Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. 
# Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. 
# Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

# conta_letras('programamos em python')
# deve devolver 6

# conta_letras('programamos em python', 'vogais')
# deve devolver 6

# conta_letras('programamos em python', 'consoantes')
# deve devolver 13

def conta_letras(frase, contar="vogais"):
    vog = frase.count('a') + frase.count('e') +frase.count('i') +frase.count('o') + frase.count('u')
    if contar == "vogais":
        return vog
    else:
        string = ''
        for i in range(len(frase)):
            if frase[i] != ' ':
                string += frase[i]
        cons = len(string) - vog
        return cons

conta_letras('programamos em python')
conta_letras('programamos em python', 'vogais')
conta_letras('programamos em python', 'consoantes')