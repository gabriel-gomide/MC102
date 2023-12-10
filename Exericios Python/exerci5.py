imagem_original=[[1, 2, 3],[4, 5, 6],[7, 8, 9],[10,11,12]]

imagem= [[0 for j in range(len(imagem_original[0])*2-1)] for i in range((len(imagem_original)*2-1))]
for i in range(len(imagem_original)):
    for j in range(len(imagem_original[0])):
        imagem[i*2][j*2]=imagem_original[i][j]



print(imagem)
