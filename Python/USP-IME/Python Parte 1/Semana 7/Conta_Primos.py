from math import sqrt
def n_primos(n):
    soma = 0

    p=1
    while(p<=n):
        if(p == 2 or p == 3 or p == 5 or p ==7):
            soma +=1
        elif(p%2 != 0 and p%3 != 0):
            if(p%5 != 0 and p%7 !=0):
                decimal = sqrt(p) - int(sqrt(p))
                if(decimal != 0):
                    soma +=1
        p +=1
    return soma




n = int(input("Digite um número: "))
print(n_primos(n))