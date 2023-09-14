lista = []
n=1
while(n!=0):
    n = int(input("Digite um número: "))
    if(n!=0):
        lista.append(n)
    if(n==0):
        lista.reverse()

for x in lista:
    print(x)