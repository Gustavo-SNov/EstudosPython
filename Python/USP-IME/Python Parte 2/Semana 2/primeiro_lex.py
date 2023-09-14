def primeiro_lex(lista):
    lex = []
    for i in range(len(lista)):
        lex.append(ord(lista[i][0]))
    n = min(lex)
    for j in range(len(lex)):
        if n == lex[j]:
            return lista[j]
    # lex = ['o','A','a','c']

primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'