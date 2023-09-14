a = int(input('Digite o valor do lado A: '))
b = int(input('Digite o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('É um triângulo equilátero!')
    elif a!=b!=c:
        print('É um triângulo escaleno!')
    else:
        print('É um triângulo isóceles!')
else:
    print('Não é um triângulo!')