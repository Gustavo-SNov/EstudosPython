n = int(input('Digite um valor: '))
fat = 1
for x in range(n,0,-1):
    fat *= x
print(f'1° Resultado: {fat}\n')
fat = 1
for y in range(1,n+1):
    fat *= y
print(f'2° Resultado: {fat}')

