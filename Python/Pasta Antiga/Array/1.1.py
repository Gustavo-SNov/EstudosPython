a = list()
b = list()
c = list()
d = list()
for x in range(0,5,1):
    fat = 1
    n = int(input(f'Digite o A[{x}]: '))
    a.append(n)
    b.append(n*3)
    for y in range(1,n+1):
        fat *= y
    c.append(fat)
    d.append(fat-(n*3))


#Exercício 1: elemento de a*c
print(f'Matriz B: {b}')

#Exercício 2: fatorial dos elementos de a
print(f'Matriz C: {c}')

#Exercício 3: elemento de c-b
print(f'Matrizz D: {d}')

#Exercício 4: uma matriz com elementos de a e b
print(f'Matriz E: {a+b}')

#Exercício 5: matriz com elementos de b invertido
b.reverse()
print(f'Matriz F: {b}')
