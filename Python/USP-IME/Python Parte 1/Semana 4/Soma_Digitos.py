n = int(input("Digite um número inteiro:"))
x = soma = 0
div = n

while(x < len(str(n))):
    soma += (div%10)
    div = div//10
    x += 1
print(soma)