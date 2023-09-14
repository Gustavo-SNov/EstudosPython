import math

n1 = float(input('Digite a nota do 1°Bimestre: '))
n2 = float(input('Digite a nota do 2°Bimestre: '))
m = (n1+n2)/2
r = m - int(m)
if r > 0.5:
    print(f'Sua média é {math.ceil(m)}!')
elif r < 0.5:
    print(f'Sua média é {math.floor(m)}!')
else:
    print(f'Sua média é {m}!')