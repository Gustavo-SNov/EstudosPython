def remove_repetidos(lista):
    lista.sort()
    nova_lista = []
    for x in lista:
        if x not in nova_lista:
            nova_lista.append(x) 
    return nova_lista

lista = []
nova_lista = remove_repetidos(lista)
print(nova_lista)
