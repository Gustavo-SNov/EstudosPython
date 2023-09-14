import random

class Dado():

    def __init__(self,valor=0):
        self.v = valor
    
    def __add__(self,other):
        return self.v + other.v
    
def randomizar():
    numeros = [1,2,3,4,5,6]
    v = random.choice(numeros)
    return v

def jogo():
    n1 = randomizar()
    dado1 = Dado(n1)
    n2 = randomizar()
    dado2 = Dado(n2)
    soma = dado1 + dado2
    if (soma == 7):
        print(f"Você ganhou!! Resultado: {soma} // 1° Dado: {n1} e 2° Dado: {n2}")
    else: 
        print(f"Você perdeu!! Resultado: {soma} // 1° Dado: {n1} e 2° Dado: {n2}")


jogo()