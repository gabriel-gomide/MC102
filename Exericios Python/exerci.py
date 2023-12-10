imagem_original = []
for i in range(7):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

print(len(imagem_original))
print(len(imagem_original[0]))
imagem_expandida= [[0 for j in range(len(imagem_original[0])*2-1)] for i in range((len(imagem_original)*2-1))]
print(len(imagem_expandida))
print(len(imagem_expandida[0]))
for i in range(len(imagem_original)):
    for j in range(len(imagem_original[i])):
        print(i, j)
        imagem_expandida[i*2][j*2]=imagem_original[i][j]
print(imagem_expandida)
