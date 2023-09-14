def imprime_matriz(minha_matriz):
    linha = len(minha_matriz)
    coluna = len(minha_matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if(j == coluna-1):
                print(minha_matriz[i][j], end = "")
            else:
                print(minha_matriz[i][j], end = " ")
        print()

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
