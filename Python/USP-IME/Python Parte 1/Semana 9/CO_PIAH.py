import re
#                       RECEBE DADOS                        #
#----------------------------------------------------------------------------------------------------------#
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos
#----------------------------------------------------------------------------------------------------------#

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # RECEBE ASSINATURA DO ALUNO INFECTADO(as_b) E A ASSINATURA DO TEXTO(as_a)
    somatoria = 0
    soma = 0
    for tam in range(0,len(as_a)):
        soma = as_a[tam]-as_b[tam]
        if(soma < 0):
            soma = soma * (-1)
        somatoria += soma

    return (somatoria/6)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #   (1) separa_sentencas    (2)separa_frases   (3)separa_palavras
    #   texto -(1)-> sentença -(2)-> frase -(3)-> palavras

    sentencas = separa_sentencas(texto) #LISTA COM TODAS AS SENTENÇAS

    for sentenca in range(0,len(sentencas)):
        frases = separa_frases(sentenca) #LISTA COM TODAS AS FRASES

    for frase in range(0,len(frases)):   
        palavras = separa_palavras(frase) #LISTA COM TODAS AS PALAVRAS    

    n_carac_fra = 0
    for n in range(0,len(frases)):
        n_carac_fra += len(frases[n]) #N° DE CARACTERES POR FRASE

    n_carac_sent = 0
    for n in range(0,len(sentencas)):
        n_carac_sent += len(sentencas[n]) #N° DE CARACTERES POR SENTENÇA

    n_carac_pal = 0
    for soma in range(0,len(palavras)):
        n_carac_pal += len(palavras[soma]) #N° DE CARACTERES POR PALAVRAS

    n_uni = len(n_palavras_unicas(palavras))
    n_dif = len(n_palavras_diferentes(palavras))
    n_sent = len(sentencas)

    total_palavras = len(palavras)
    total_sentencas = len(sentencas)
    total_frases = len(frases)

    wal = (n_carac_pal)/(total_palavras)
    ttr = (n_dif)/(total_palavras)
    hlr = (n_uni)/(total_palavras)
    sal = (n_carac_sent)/(n_sent)
    sac = (total_frases)/(total_sentencas)
    pal = (n_carac_fra)/(total_frases)

    return [wal,ttr,hlr,sal,sac,pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.''' 
    
    # LOOPING DE CALCULO DAS ASSINATURAS DOS TEXTOS E ARMAZENAR EM OUTRA LISTA CHAMADA                          ASSINATURAS = []
    for assinar in range(0,len(textos)):
        assinaturas = [calcula_assinatura(textos[assinar])]

    # LOOPING DE COMPARAÇÃO DAS ASSINATURAS COM A ASSINATURA INFECTADA E ARMAZENAR EM OUTRA LISTA CHAMADA       SIMILARIDADE = []
    for comparar in range(0,len(assinaturas)):
        similaridade = [compara_assinatura(assinaturas[comparar], ass_cp)]

    # USAR INFECTADO = MIN(SIMILARIDADE) E MOSTRAR SUA POSIÇÃO
    infectado = min(similaridade)
    for infec in range(0,len(similaridade)):
        if(infectado == similaridade[infec]):
            print(f"\nO autor do texto {infec+1} está infectado com COH-PIAH")


ass_cp = le_assinatura()    #DADOS DA ASSINATURA INFECTADO
textos = le_textos()        #TEXTOS PARA COMPARAÇÃO

avalia_textos(textos, ass_cp)