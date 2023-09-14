from math import sqrt,pow

def delta(a,b,c):
    delta = pow(b,2) - (4*a*c)
    r1 = (-b + sqrt(delta))/(2*a)
    r2 = (-b - sqrt(delta))/(2*a)
    if (delta>=0):
        if (r1<r2):
            return print("as raízes da equação são:",r1,"e",r2)
        else:
           return print("as raízes da equação são:",r2,"e",r1) 
    else:
        return print("esta equação não possui raízes reais")

a = float(input("Digite o valor de a (Diferente de zero):"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

print("Resultado:", delta(a,b,c))