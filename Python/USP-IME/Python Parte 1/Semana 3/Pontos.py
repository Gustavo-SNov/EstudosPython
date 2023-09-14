from math import sqrt,pow

x1 = float(input("Digite a coordenada de x1:"))
y1 = float(input("Digite a coordenada de y1:"))

x2 = float(input("Digite a coordenada de x2:"))
y2 = float(input("Digite a coordenada de y2:"))

d = sqrt(pow((x1-x2),2) + pow((y1-y2),2))

if (d>=10):
    print("longe")
else:
    print("perto")