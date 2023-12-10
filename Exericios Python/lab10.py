#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]
#teste
#print(matriz) #tudo certo

# Leitura e processamento dos caminhos

primeiro_time=input()
jogadores_totais=int(input())
ponto_azul=0
ponto_vermelho=0
for i in range(jogadores_totais):
    coordenadas=[0,0]
    caminho=input()
    lista_caminho=list(caminho)
    #teste
  #  print(lista_caminho)
    
    for movimento in lista_caminho:
        
        
        if movimento=='N':
            coordenadas[0]=coordenadas[0]-1 
            
        if movimento=='S':
            coordenadas[0]=coordenadas[0]+1 
            
        if movimento=='O':
            coordenadas[1]=coordenadas[1]-1 
            
        if movimento=='L':
            coordenadas[1]=coordenadas[1]+1
            
 #       print(coordenadas[0], coordenadas[1])

        if matriz[coordenadas[0]][coordenadas[1]]== '*':
            if i%2!=0:
                if primeiro_time=='azul':
                    
                    ponto_vermelho=ponto_vermelho+1
                else:
                    ponto_azul=ponto_azul+1
            elif i%2==0:
                if primeiro_time=='vermelho':
                    ponto_vermelho=ponto_vermelho+1
                else:
                    
                    ponto_azul=ponto_azul+1
            matriz[coordenadas[0]][coordenadas[1]]='.'
        
#print('pontos' , ponto_azul, ponto_vermelho)            

# Impressão da saída
print('Tesouros encontrados pelo time azul:', ponto_azul)
print('Tesouros encontrados pelo time vermelho:', ponto_vermelho)
if ponto_azul>ponto_vermelho:
    print('Vitoria do time azul')
elif ponto_azul<ponto_vermelho:
    print('Vitoria do time vermelho')

else:
    print('Empate')
