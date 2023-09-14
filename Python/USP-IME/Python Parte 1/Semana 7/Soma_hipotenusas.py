n=25
h=co=ca=1
soma = 0
while(h<=n):
    while(ca<h):
        while(co<h):
            if(h*h==(ca*ca +co*co)):
                soma += h
            co +=1
        co=1
        ca+=1
    ca=1
    h+=1
print(soma)