""" Elaborar um programa que seja uma “Calculadora”, onde o usuário deverá digitar 
uma das seguintes teclas: +, -, *, / ou S. - Caso escolha S, para sair, o programa 
deverá ser encerrado; - Caso escolha +, -, * ou /, como operações aritméticas, o 
programa
deverá solicitar a digitação de dois números quaisquer (número a e número b), um por 
vez, realizar a respectiva operação aritmética (soma, subtração, multiplicação ou 
divisão) entre os respectivos números (a e b, nessa ordem) e então apresentar o seu 
resultado. Após isto, deverá voltar à etapa inicial de digitação das teclas +, -, *, / 
ou S e repetir este item até a digitação da tecla S."""
while True:
    print('-='*30)
    print('Adição = [+]\nSubtração = [-]\nMultiplicação = [*]\nDivisão = [/]\nSair = [S]')
    print('-='*30)
    e = str(input('Escolha: '))
    if e == 'S' or e == 's':
        print('Saindo do programa!')
        break 
    a = float(input('\nDigite o 1° valor: '))
    b = float(input('Digite o 2° valor: '))
    if e == '+':
        print(f'Resultado: {a+b}')
    elif e == '-':
        print(f'Resultado: {a-b}')
    elif e == '*':
        print(f'Resultado: {a*b}')
    elif e == '/':
        print(f'Resultado: {a/b}')
    else:
        print(f'Comando Incorreto!')