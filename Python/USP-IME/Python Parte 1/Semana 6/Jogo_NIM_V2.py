def partida():
    #   LOOPING DE VALIDADE DE PARTIDA!
    validade = 0
    while(validade == 0):
        n = int(input("\nQuantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if(n>0 and m<=n):
            validade +=1
        else:
            print("\nOops! Partida inválida! Tente de novo.\n")

    #   LOOPING PARTIDA!

    #   USUÁRIO COMEÇA!
    if(n % (m+1) ==0):
        print("\nVoce começa!\n")
        while(n!=0):
            p = usuario_escolhe_jogada(n,m)
            n -= p
            p = computador_escolhe_jogada(n,m)
            n -= p

    #   COMPUTADOR COMEÇA!
    else:
        print("\nComputador começa!\n")
        while(n!=0):
            p = computador_escolhe_jogada(n,m)
            n -= p
            if(n==0):
                break
            p = usuario_escolhe_jogada(n,m)
            n -= p

def computador_escolhe_jogada(n,m):
    p=0
    #   PLANO A
    if(n==m):
        p = m
    
    #   PLANO B
    elif(m==1):
        p = 1

    #   PLANO C
    elif(n<m):
        p = n
    
    #   PLANO D
    else:
        while(p<=m):
            if( (n-p) % (m+1) == 0):
                break
            p += 1
            if(p==m):
                break
            
        
    # CONFIRMAÇÃO DE N° DE PEÇAS RETIRADAS PELO PC
    if(p==1):
        print("O Computador tirou uma peça.")
    else:
        print(f"O Computador tirou {p} peças.")

    # CONFIRMAÇÃO DE N° DE PEÇAS RESTANTES   
    if ((n-p) == 1):
        print("Agora resta apenas uma peça no tabuleiro.\n")
    elif((n-p) == 0):
        print("Fim do jogo! O computador ganhou!\n")
    else:
        print(f"Agora restam {n-p} peças no tabuleiro.\n")

    return p

def usuario_escolhe_jogada(n,m):
    validade = 0
    while(validade != 1):
        p = int(input("Quantas peças você vai tirar? "))
        if(p <= m and p > 0 and p <= n):
            validade = 1

            # CONFIRMAÇÃO DE N° DE PEÇAS RETIRADAS PELO USUÁRIO
            if(p==1):
                print("Voce tirou uma peça.")
            else:
                print(f"Voce tirou {p} peças.")
                
            # CONFIRMAÇÃO DE N° DE PEÇAS RESTANTES
            if ((n-p) == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print(f"Agora restam {n-p} peças no tabuleiro.\n")

            return p
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")

def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    c=1
    while(c <= 3):
        print(f"**** Rodada {c} ****")
        partida()
        c += 1  
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador\n")



print("\nBem-vindo ao jogo do NIM! Escolha:\n")
while(True):
    print("1 - para jogar uma partida isolada")
    modo_jogo = int(input("2 - para jogar um campeonato "))
        # Escolha do modo de jogo
    if( modo_jogo == 1):
        partida()
    elif(modo_jogo ==2):
        campeonato()
    else: 
        print("\nComando Inválido!\n")
