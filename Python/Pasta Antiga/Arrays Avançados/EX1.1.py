a = [1,2,3,4,5]

n = int(input('Digite um valor para pesquisa: '))
if n in a:
    index = a.index(n)
    print(f'O elemento {n} foi encontrado na posição {index}')
else:
    print(f'O elemento {n} não foi encontrado')
