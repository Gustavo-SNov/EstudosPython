def soma_elementos(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma

lista = [1,2,3,4,5,6]
resultado = soma_elementos(lista)
print(f"Resultado: {resultado}")