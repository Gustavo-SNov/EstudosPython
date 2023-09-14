class Triangulo():

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        p = self.a + self.b + self.c
        return p
    
    def tipo_lado(self):
        if (self.a==self.b and self.a==self.c):
            return "equilátero"
        elif(self.a != self.b and self.a != self.c and self.b != self.c):
            return "escaleno"
        else:
            return "isósceles"

    def retangulo(self):
        ret = 0
        if (self.a>self.b and self.a>self.c):
            if (self.a*self.a) == (self.b*self.b + self.c+self.c): 
                ret = 1
        elif(self.b>self.a and self.b>self.c):
            if (self.b*self.b) == (self.a*self.a + self.c+self.c): 
                ret = 1
        elif(self.c>self.a and self.c>self.b):
            if (self.c*self.c) == (self.b*self.b + self.a+self.a): 
                ret = 1
        if (ret==1):
            print(True)
        else:
            print(False)

t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True