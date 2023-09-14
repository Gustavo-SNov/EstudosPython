import math

n = int(input('Digite um valor: '))
for e in range(0,16,1):
    print(f'{n} elevado a {e} = {math.pow(n,e)}')
print('\n')
r =1
for x in range(0,16,1):
    print(f'{n} elevado a {x} = {r}')
    r *=3