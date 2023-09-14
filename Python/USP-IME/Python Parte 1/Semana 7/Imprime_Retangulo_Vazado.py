largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
linha = coluna = 1
if(largura>2 and altura >2 ):
    while(linha<=altura):
        if(linha == 1 or linha == altura):
            while(coluna<=largura):
                print("#",end="")
                coluna+=1
            print()
            coluna=1
        else:
            while(coluna<=largura):
                if(coluna==1 or coluna==largura):
                    print("#",end="")
                else:
                    print(" ",end="")
                coluna+=1
            print()
            coluna = 1
        linha +=1
else:
    while(linha<=altura):
        while(coluna<=largura):
            print("#",end="")
            coluna +=1
        print()
        linha +=1
        coluna=1
