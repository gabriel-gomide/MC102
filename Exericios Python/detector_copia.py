import re

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

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    re.split(r'[,:;]+', sentenca)
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavras=frase.split()
    return palavras

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
   
    sab=(abs(as_a[0]-as_b[0])+abs(as_a[1]-as_b[1])+abs(as_a[2]-as_b[2])
        +abs(as_a[3]-as_b[3])+abs(as_a[4]-as_b[4])+abs(as_a[5]-as_b[5]))/6
        
        
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    #1) Somar tamanho de cada palavra
    #2) Contar quantas palavras
    
    sentenca=separa_sentencas(texto)
    quant_palavras=0
    pala=list()
    fras=list()
    carct=list()
    
    for i in range(len(sentenca)):
        frase=separa_frases(sentenca[i])
        fras=fras+frase
        for i in range(len(frase)):
            palavra=separa_palavras(frase[i])
            pala=pala+palavra
            carct=carct+palavra
            quant_palavras=len(palavra)+quant_palavras
            
    #print(pala)
    delimiter=''
    quant_letras=delimiter.join(carct)
    quant_letras2=delimiter.join(sentenca)
    quant_letras3=delimiter.join(fras)
    tam_medio=len(quant_letras)/quant_palavras           

    #Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
    #1) Número de palavras diferentes
    #2) Quantidade de palavras

    rel_type_token=n_palavras_diferentes(pala)/quant_palavras

    #Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
    #1) Número de palavras que aparecem uma vez
    #2) Total de palavras

    raz_hapax=n_palavras_unicas(pala)/quant_palavras

    #Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    #1) Tamanho do texto
    #2) Número de sentenças

    tam_med_sent=len(quant_letras2)/len(sentenca)

    #Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    #1) Número de frases
    #2) Número de sentenças

    comple=len(fras)/len(sentenca)

    #Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto

    tam_med_fras=len(quant_letras3)/len(fras)

    return [tam_medio, rel_type_token, raz_hapax, tam_med_sent, comple, tam_med_fras]          



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    aux=None
    count = 1
    
    for i in range(len(textos)):
        as_a = calcula_assinatura(textos[i])
        
        sab = compara_assinatura(as_a, ass_cp)
        if aux is None or sab<aux:
            aux=sab
            tes=count
        count=count+1
    print('O autor do texto',tes,'está infectado com COH-PIAH')
    print(tes)
    return tes

ass_cp = le_assinatura()
textos = le_textos()
tes = avalia_textos(textos, ass_cp)
print('O autor do texto',tes,'está infectado com COH-PIAH')

