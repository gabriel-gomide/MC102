###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247634
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    #passo1
    imagem_expandida= [[0 for j in range(len(imagem_original[0])*2-1)] for i in range((len(imagem_original)*2-1))]
    for i in range(len(imagem_original)):
        for j in range(len(imagem_original[0])):
            
            imagem_expandida[i*2][j*2]=imagem_original[i][j]
            

    #passo2
    for i in range(len(imagem_expandida)):
        for j in range(len(imagem_expandida[0])):
            if i%2==0 and j%2!=0 or i==0 and j%2!=0:
                imagem_expandida[i][j]=(imagem_expandida[i][j-1]+imagem_expandida[i][j+1])/2

    #passo3
    for i in range(len(imagem_expandida)):
        for j in range(len(imagem_expandida[0])):
            if i%2!=0 and j%2==0:
                imagem_expandida[i][j]=(imagem_expandida[i-1][j]+imagem_expandida[i+1][j])/2
    

    #passo4
    for i in range(len(imagem_expandida)):
        for j in range(len(imagem_expandida[0])):
            if i%2!=0 and j%2!=0:
                imagem_expandida[i][j]=(imagem_expandida[i-1][j-1]+imagem_expandida[i-1][j+1]+imagem_expandida[i+1][j-1]+imagem_expandida[i+1][j+1])/4
    return imagem_expandida

def retracao(imagem_original):
    a=len(imagem_original)
    b=len(imagem_original[0])
    #Linhas pares e colunas pares
    if a%2==0 and b%2==0:
        im_retracao=[[0 for j in range(len(imagem_original[0])//2)] for i in range((len(imagem_original)//2))]
        for i in range(len(im_retracao)):
            for j in range(len(im_retracao[0])):
                im_retracao[i][j]=(imagem_original[i*2+1][j*2+1]+imagem_original[i*2][j*2+1]+imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/4
                     
    #Linhas impares e colunas pares                 
    if a%2!=0 and b%2==0:
        im_retracao=[[0 for j in range((len(imagem_original[0])+1)//2)] for i in range(((len(imagem_original)+1)//2))]
        for i in range(len(im_retracao)):
            for j in range(len(im_retracao[0])):
                if i*2+1<len(imagem_original):
                    im_retracao[i][j]=(imagem_original[i*2+1][j*2+1]+imagem_original[i*2][j*2+1]+imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/4
                else:
                    im_retracao[i][j]=(imagem_original[i*2][j*2+1]+imagem_original[i*2][j*2])/2
                    
    #Linhas pares e colunas impares
    if a%2==0 and b%2!=0:
        im_retracao=[[0 for j in range(((len(imagem_original[0])+1)//2))] for i in range((len(imagem_original)+1)//2)]
        
        for i in range(len(im_retracao)):
            for j in range(len(im_retracao[0])):
                if j*2+1<len(imagem_original[0]):
                    im_retracao[i][j]=(imagem_original[i*2+1][j*2+1]+imagem_original[i*2][j*2+1]+imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/4
                else:
                    im_retracao[i][j]=(imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/2
    #Linhas impares e colunas impares
    if a%2!=0 and b%2!=0:
        im_retracao=[[0 for j in range((len(imagem_original[0])+1)//2)] for i in range((len(imagem_original)+1)//2)]
        for i in range(len(im_retracao)):
            for j in range(len(im_retracao[0])):

                if j*2+1<len(imagem_original[0]) and i*2+1<len(imagem_original):
                    im_retracao[i][j]=(imagem_original[i*2+1][j*2+1]+imagem_original[i*2][j*2+1]+imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/4
                    
                if j*2+1>=len(imagem_original[0]) and i*2+1>=len(imagem_original):
                    im_retracao[i][j]=imagem_original[i*2][j*2]
                    
                if i*2+1<len(imagem_original) and j*2+1>=len(imagem_original[0]):
                    im_retracao[i][j]=(imagem_original[i*2+1][j*2]+imagem_original[i*2][j*2])/2
                    
                if j*2+1<len(imagem_original[0]) and i*2+1>=len(imagem_original):
                    im_retracao[i][j]=(imagem_original[i*2][j*2+1]+imagem_original[i*2][j*2])/2
    #print('AQUI', len(im_retracao),len(im_retracao[0]))                
    return im_retracao
# leitura da imagem
_ = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

operacao=input()

# impressão da imagem final
if operacao=='expansao':
    imagem=expansao(imagem_original)
    imprimir_imagem(imagem)
if operacao=='retracao':
    imagem=retracao(imagem_original)
    imprimir_imagem(imagem)

