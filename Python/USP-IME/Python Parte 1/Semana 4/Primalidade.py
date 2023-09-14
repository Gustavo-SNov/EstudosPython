n = int(input("Digite um número inteiro:"))
not_primo = 0

if(n<=1):
    not_primo = 1
elif(n!=2 and n%2 == 0):
    not_primo = 1
elif(n!=3 and n%3 == 0):
    not_primo = 1
elif(n!=5 and n%5 == 0):
    not_primo = 1
elif(n!= 7 and n%7 == 0):
    not_primo = 1
if(not_primo == 1):
    print("não primo")
else:
    print("primo")
