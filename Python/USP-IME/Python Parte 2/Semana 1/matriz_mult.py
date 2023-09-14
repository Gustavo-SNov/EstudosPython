def sao_multiplicaveis(m1, m2):
    # Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda.
    coluna = len(m1[0])
    linha = len(m2)
    if(coluna == linha):
        return True
    else:
        return False 

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) #=> False

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) #=> True