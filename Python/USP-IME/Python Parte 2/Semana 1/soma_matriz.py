def soma_matrizes(m1,m2):
    linha_m1 = len(m1)
    coluna_m1 = len(m1[0])
    linha_m2 = len(m2)
    coluna_m2 = len(m2[0])
    m3 = []
    if(len(m1)==len(m2) and len(m1[0])==len(m2[0])):
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            m3.append(linha)
        return m3
    else:
        return False
    

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)
