from math import factorial

def fatorial(x):
    return factorial(x)

n = int(input("Digite o número de elementos totais:"))
k = int(input("Digite o número de elemetnos no arranjo:"))

resultado = (fatorial(n))/(fatorial(k)*fatorial (n-k))

print("Número de combinações possíveis:",int(resultado))
