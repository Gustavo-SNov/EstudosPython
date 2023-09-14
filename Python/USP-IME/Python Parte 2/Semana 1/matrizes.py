#   MATRIZ 1D
#   MATRIZ 2D
#       LINHA -> COLUNA
#       COLUNA -> LINHA

def matriz_1d():
    matriz = []
    elementos = int(input("Quantidade de elementos na matriz: "))
    for i in range(0,elementos):
        n = int(input(f"{i+1}°elemento: "))
        matriz.append(n)
    print(f"Matriz 1D = {matriz}")


def matriz_2d():

    matriz = []
    L = int(input("Linhas: "))
    C = int(input("Colunas: "))
    for i in range(0,L):
        linha = []
        for j in range(0,C):
            n = int(input(f"Elemento[{i}][{j}]: "))
            linha.append(n)
        matriz.append(linha)

    # EXIBIR MATRIZ 2D
    for exibir in matriz:
        print(exibir)    

def matriz_2d_transposta(matriz):
    # matriz = [[1,2,3],[4,5,6],[7,8,9]]
    # [1,2,3]   [1,4,7]
    # [4,5,6]   [2,5,8]
    # [7,8,9]   [3,6,9]

    for i in range(0,3): #coluna
        for j in range(0,3): #linha 
            print(matriz[j][i], end=' ')
        print()
    
    



#print("Teste de Matriz 1D")
#matriz_1d()
#print()
#print("Teste de Matriz 2D")
#matriz = matriz_2d()
#print()
print("Teste de Matriz 2D transposta")
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz_2d_transposta(matriz)
