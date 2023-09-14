n1 = float(input('Digite a nota do 1°Bimestre: '))
n2 = float(input('Digite a nota do 2°Bimestre: '))
m = (n1+n2)/2
if (m>=6):
    print(f'Sua nota: {m}\nAprovado!')
else:
    ne = float(input('Digite a nota do exame: '))
    nm = (m+ne)/2
    if nm >= 5:
        print(f'Sua nota: {nm}\nAprovado!')
    else:
        print(f'Sua nota: {nm}\nReprovado!')