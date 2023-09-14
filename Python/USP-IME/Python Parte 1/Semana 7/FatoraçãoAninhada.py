def fatoração(n):
    print(n,"=", end=" ")
    while(n>1):
        if(n%2==0):
            n = n/2
            print("2",end="") 
        elif(n%3==0):
            n = n/3
            print("3",end="")
        elif(n%5==0):
            n = n/5
            print("5",end="")   
        elif(n%7==0):
            n = n/7
            print("7",end="")
        if(n>1):
            print("*",end="")






n=1
while(n>=1):
    print()
    n = int(input("Digite um número inteiro positvo:"))
    if(n>1):
        fatoração(n)
    elif(n==1):
        print("fatoração de 1 é 1!")

