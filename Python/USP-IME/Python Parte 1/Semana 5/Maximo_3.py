def maximo(a,b,c):
    if(a!=b and b!=c and a!=c):
        if(a>b and a>c):
            return a
        elif(b>a and b>c):
            return b
        elif(c>a and c>b):
            return c
    elif(a==b):
        if(a>c):
            return a
        else:
            return c
    elif(b==c):
        if(b>a):
            return b
        else:
            return a
    elif(c==a):
        if(c>b):
            return c
        else:
            return b
    elif(a==b==c):
        return a
    
n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número:"))
n3 = int(input("Digite o 3° número:"))

print(maximo(n1,n2,n3))