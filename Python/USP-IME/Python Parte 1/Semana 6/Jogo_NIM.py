
def computador_escolhe_jogada(n,m):
    if(n==m):
        p = m
        print(f"O computador tirou {p} peças.")
        return p
    elif(m==1):
        p = m
        print("O computador tirou uma peça.")
        return p
    else:
        p=1
        while(p<m):
            r = n-p
            if(r%(m+1)==0):
                print(f"O computador tirou {p} peças.")
                return p
            p +=1
        if(p==m):
            print(f"O computador tirou {p} peças.")
            return p
                

def usuario_escolhe_jogada(n,m):
    while(True):
        p = int(input("Quantas peças você vai tirar? "))
        print()
        if(p<=0 or p>m or p>n):
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            if(p==1):
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {p} peças.")
            print()
            return p
        


def partida():     
    while(True):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if (m>n and m<=0):
            print("Partida impossível!")
        else:
            break
    print()
    if (n%(m+1)==0):                                            
        print("Você começa!")
        print()
        while(True):

            p = usuario_escolhe_jogada(n,m)
            n -= p
            if (n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                print(f"Fim do jogo! Você ganhou!")
                return "v"
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
            print()

            p = computador_escolhe_jogada(n,m)
            n-=p
            if (n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                print(f"Fim do jogo! O computador ganhou!")
                return "c"
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
            print()

    else:                                                       
        print("Computador começa!")
        print()
        while(True):
            p = computador_escolhe_jogada(n,m)
            n -= p
            if (n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                print(f"Fim do jogo! O computador ganhou!")
                return "c"
            else:
                print(f"Agora restam {n} peças no tabuleiro.")


            p = usuario_escolhe_jogada(n,m)
            n -= p
            if (n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                print(f"Fim do jogo! Você ganhou!")
                return "v"
            else:
                print(f"Agora restam {n} peças no tabuleiro.")




print()
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
modo_jogo = int(input("2 - para jogar um campeonato "))
print()
if(modo_jogo == 1):
    partida()
if(modo_jogo == 2):
    rodada = c = v = 0
    print("Voce escolheu um campeonato!")
    print()
    while(True):
        rodada += 1
        print(f"**** Rodada {rodada} ****")
        print()
        r = partida()
        if(r == "c"):
            c += 1
        else:
            v += 1
        if(c==3 or v==3):
            print("**** Final do campeonato! ****")
            print()
            print(f"Placar: Você {v} X {c} Computador")
            break
