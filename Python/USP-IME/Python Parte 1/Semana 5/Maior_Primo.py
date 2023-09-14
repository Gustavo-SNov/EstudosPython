from math import sqrt

def primo(p):
    soma = 0
    decimal = sqrt(p) - int(sqrt(p))

    if(p == 2 or p == 3 or p == 5 or p ==7):
        return 1
    if(p%2 != 0 and p%3 != 0):
        soma += 1
    if(p%5 != 0 and p%7 !=0):
        soma += 1
    if(decimal != 0):
        soma +=1
    if(soma == 3):
        return 0 
    if(soma <3):
        return -1

def maior_primo(m):
    while(m>=2):
        if (primo(m) == 1 or primo(m) == 0):
            return m    
        m -= 1

n = int(input("Digite um número:"))
print(maior_primo(n))