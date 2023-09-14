s = 0
atual = 1
x = 1
anterior = 0
while s<15:
    print(atual, end = ' ')
    atual = x + anterior
    anterior = x
    x = atual
    s += 1