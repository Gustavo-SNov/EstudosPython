def maior_elemento(lista):
    n = max(lista)
    for x in range(0,len(lista)):
        if(n == lista[x]):
            print(f"posição: {x+1}")
    return max(lista)

lista = [1,7,3,2,8,8,0,1]
maior = maior_elemento(lista)
print(maior)