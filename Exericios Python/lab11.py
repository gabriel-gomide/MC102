#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
#####################################################
# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())
  
# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())
  
# Processamento
def rotacao(peca_velha):
    peca_rotacionada = [[0 for j in range(len(peca_velha))]for i in range(len(peca_velha[0]))]
    for linha in range(len(peca_velha)):
        for coluna in range(len(peca_velha[linha])):
            peca_rotacionada[coluna][len(peca_velha) - 1 - linha] = peca_velha[linha][coluna]
    return peca_rotacionada
    
def encaixe(peca_rotacionada,i,j):
    for a in range(len(peca_rotacionada)):
        for b in range(len(peca_rotacionada[a])):
            if peca_rotacionada[a][b]=='X':
                if tabuleiro[a+i][b+j]=='X':
                    return 0
                    break
    return 1
a=0
for i in range(T-P+1):
    for j in range(len(tabuleiro[i])-len(peca[0])+1):
        a=encaixe(peca,i,j)+a
        
peca90=rotacao(peca)
b=0
for i in range(T-len(peca[0])+1):
    for j in range(len(tabuleiro[0])-len(peca90[0])+1):
        b=encaixe(peca90,i,j)+b
        
        
peca180=rotacao(peca90)
c=0
for i in range(T-P+1):
    for j in range(len(tabuleiro[i])-len(peca[0])+1):
        c=encaixe(peca180,i,j)+c
        
peca270=rotacao(peca180)
d=0
for i in range(T-len(peca[0])+1):
    for j in range(len(tabuleiro[i])-len(peca270[0])+1):
        d=encaixe(peca270,i,j)+d
                    
# Impressão do resultado
a=str(a)
b=str(b)
c=str(c)
d=str(d)
print(a+','+b+','+c+','+d)
