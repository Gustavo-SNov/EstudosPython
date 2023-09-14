#ignorar espaços antes e depois do nome e primeira letra maiúscula e seus demais caracteres minúsculos

#menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

#menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

#menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José

def menor_nome(strings):
    nome = []
    tam = []
    string = []
    for x in range(len(strings)):
        nome.append(strings[x].strip().capitalize())
        tam.append(len(nome[x]))
    string.append(nome)
    string.append(tam)
    n = min(string[1])
    for y in range(len(string[1])):
        if n == string[1][y]:
            return string[0][y]

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])