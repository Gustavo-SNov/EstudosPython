class Triangulo():

    # Método Construtor
    def __init__(self,ladoA,ladoB,ladoC,altura):
        self.a = ladoA
        self.b = ladoB
        self.c = ladoC
        self.h = altura

    def tipo(self):
        print("Definindo o tipo do triângulo")
        if (self.a == self.b == self.c):
            return "Triângulo Equilátero"
        elif(self.a != self.b != self.c):
            return "Triângulo Escaleno"
        else:
            return "Triângulo Isósceles"

a = int(input("Digite o valor do lado A: "))
b = int(input("Digite o valor do lado B: "))
c = int(input("Digite o valor do lado C: "))
h = int(input("Digite o valor da altura: "))

t1 = Triangulo(a,b,c,h)
print(t1.tipo())
        
    
