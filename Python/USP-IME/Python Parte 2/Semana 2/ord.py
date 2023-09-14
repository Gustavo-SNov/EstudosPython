a = ["gato"]
b = ["telhado"]
soma_a = 0
soma_b = 0
for i in range(len(a)):
    for j in range(len("gato")):
        soma_a += int(ord(a[i][j]))
for i in range(len(b)):
    for j in range(len("telhado")):
        soma_b += int(ord(b[i][j]))
        
print(f"A{soma_a} e B{soma_b}")