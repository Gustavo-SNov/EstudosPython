n = int(input("Digite um número inteiro:"))
i = x = 1 
while( x <= len(str(n))-1 and i==1):
    ant = n%10
    atual = (n//10)%10
    if (atual==ant):
        print("sim")
        i = 0
    else:
        n = (n//10)
if(i==1):
    print("não")