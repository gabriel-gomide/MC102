def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    #passo 1: separar elementos
    imagem= [[0 for j in range(len(imagem_original[0])*2-1)] for i in range((len(imagem_original)*2-1))]
    for i in range(len(imagem_original)):
        for j in range(len(imagem_original[0])):
            imagem[i*2][j*2]=imagem_original[i][j]

    #passo 2:    
    for i in range(len(imagem)): #acrescentei -1
        for j in range(len(imagem[0])): #acrescentei -1
            if i % 2 == 0 and j % 2 != 0:
                imagem[i][j] = ((imagem[i][j-1]+imagem[i][j+1])/2)
    print(imagem)
    #passo 3:
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):            
            if i % 2 != 0 and j % 2 == 0:
                imagem[i][j] = ((imagem[i-1][j]+imagem[i+1][j])/2)                
    #passo 4:
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):            
            if i % 2 != 0 and j % 2 != 0:
                imagem[i][j] = ((imagem[i-1][j-1]+imagem[i-1][j+1]+imagem[i+1][j-1]+imagem[i+1][j+1])/4)
    return imagem

    
def retracao(imagem_original, m, n): #parece q ta funcionando
    if m % 2 == 0:
        teto_m = int(m/2)
    else: 
        teto_m = int((m+1)/2)
    if n % 2 == 0:
        teto_n = int(n/2)
    else: 
        teto_n = int((n+1)/2)
    matriz_B = []        
    for i in range(len(imagem_original)): #linhas
        linha_B_media = []        
        for j in range(len(imagem_original[0])): #colunas
            #print('i:', i, 'j:', j)           
            if i % 2 == 0 and j % 2 == 0 and i < len(imagem_original)-1 and j < len(imagem_original[0])-1:
                matriz_2x2 = []                
                linha_I_2x2 = [imagem_original[i][j], imagem_original[i][j+1]]
                linha_II_2x2 = [imagem_original[i+1][j], imagem_original[i+1][j+1]]
                matriz_2x2.append(linha_I_2x2)                
                matriz_2x2.append(linha_II_2x2)
                media_2x2 = ((matriz_2x2[0][0] + matriz_2x2[0][1] + matriz_2x2[1][0] + matriz_2x2 [1][1])/4)
                linha_B_media.append(media_2x2)                   
                #print('matriz 2x2', matriz_2x2)             
                #print('media', media_2x2)    
                        #matriz_B[L][C] = media_2x2
            elif i % 2 == 0 and j % 2 == 0 and i < len(imagem_original) and j == len(imagem_original[0]):            
                linha_B_media.append((imagem_original[i][j] + imagem_original[i+1][j])/2)
                #print('media', imagem_original[i][j], imagem_original[i+1][j], (imagem_original[i][j] + imagem_original[i+1][j])/2)
                #matriz_B[L][C] = (imagem_original[i][j] + imagem_original[i+1][j])/2
            elif i % 2 == 0 and j % 2 == 0 and i < len(imagem_original)-1 and j == len(imagem_original[0])-1: #nessa linha: acresc -1 no i
                linha_B_media.append((imagem_original[i][j] + imagem_original[i+1][j])/2)
                #print('media', imagem_original[i][j], imagem_original[i+1][j], (imagem_original[i][j] + imagem_original[i+1][j])/2)
            elif i % 2 == 0 and j % 2 == 0 and i == len(imagem_original)-1 and j < len(imagem_original[0])-1: ## tirei a condição i == len(imagem_original) or, acrescentei-1 no j
                linha_B_media.append((imagem_original[i][j] + imagem_original[i][j+1])/2)   
                #print('media', imagem_original[i][j], imagem_original[i][j+1], (imagem_original[i][j] + imagem_original[i][j+1])/2)
                        #matriz_B[L][C] = (imagem_original[i][j] + imagem_original[i][j+1])/2
            elif i == len(imagem_original)-1 and j == len(imagem_original[0])-1:
                linha_B_media.append(imagem_original[i][j])
                #print('media', imagem_original[i][j])
                        #matriz_B[L][C] = imagem_original[i][j]
            else:
                a = False
        if i % 2 == 0: 
            matriz_B.append(linha_B_media)

    return matriz_B
    

# leitura da imagem
tipo_arquivo = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

numero = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento
redimensionamento = input()

# impressão da imagem final

if redimensionamento == 'retracao':
    imagem = retracao(imagem_original, len(imagem_original[0]), len(imagem_original))
elif redimensionamento == 'expansao':
    imagem = expansao(imagem_original)

imprimir_imagem(imagem)
