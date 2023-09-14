a = list()
b = list()
c = list()
print('Matriz A!')
for c in range(0,4):
    for l in range(0,5):
        n = int(input(f'A[{l}][{c}]= '))
        a.append(n)

print('Matriz B!')
for c in range(0,4):
    for l in range(0,5):
        n = int(input(f'B[{l}][{c}]= '))
        b.append(n)

for c in range(0,4):
    for l in range(0,5):
        c(a[l][c]+b[l][c])
print(c)