import re
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
    frases=re.split(r'[,:;]+', sentenca)
    return frases

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavras=frase.split()
    return palavras

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    #1) Somar tamanho de cada palavra
    #2) Contar quantas palavras
    sentenca=separa_sentencas(texto)
    frase=separa_frases(sentenca)
    palavra=separa_palavras(frase)

    quant_palavras=0

    for i in range(len(sentenca)):
        for i in range(len(frase)):
            for i in range(len(palavra)):
                quant_palavras=i+quant_palavras

    return quant_palavras
        
    




    
    
texto=le_textos()
for i in range(len(texto)):
    calcula_assinatura(texto)
