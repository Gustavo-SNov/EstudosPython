a = [1,2,3]
b = [4,5,6]
c = list()
for x in range(0,3):
    c.append(a[x]+b[x])
print(c)

A =[[1,2,3],[4,5,6]]
B =[[4,1,2],[4,2,3]]
C =[[0,0,0],[0,0,0]]
for linha in range(0,2):
    for coluna in range(0,2):
        C[linha][coluna] = A[linha][coluna]+B[linha][coluna]
print(C)