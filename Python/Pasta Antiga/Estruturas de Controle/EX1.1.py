x=1
#Exibir de 1 a 20
while x<=20:
    print( x, end= ' ')
    x += 1
    if x==21:
        print('\n')
x=1
#Exibir valores pares e impares de 1 a 20
while x<=20:
    if x % 2 == 0:
        print(f'{x} é par\n')
    else:
        print(f'{x} é impar\n')
    x += 1