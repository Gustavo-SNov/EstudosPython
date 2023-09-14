#Exibir 1 a 20
for x in range(1,21,1):
    print(x , end = ' ')

print('\n')

#Exibir pares e impares de 1 a 20
for y in range(1,21,1):
    if y % 2 == 0:
        print(f'{y} é par!')
    else:
        print(f'{y} é impar!')
