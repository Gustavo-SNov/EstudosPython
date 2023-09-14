from math import sqrt,pow

a = float(input("Digite o valor de a (Diferente de zero):"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

if (a==0):
    print("Não é uma equação de segundo grau!")
else:
    delta = pow(b,2) - (4*a*c)
    if (delta>0):
        r1 = (-b + sqrt(delta))/(2*a)
        r2 = (-b - sqrt(delta))/(2*a)
        if (r1<r2):
            print("as raízes da equação são",r1,"e",r2)
        else:
           print("as raízes da equação são",r2,"e",r1) 
    elif (delta==0):
        r = (-b)/(2*a)
        print("a raiz desta equação é",r)
    else:
        print("esta equação não possui raízes reais")