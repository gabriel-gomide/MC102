#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Jonatas Rodrigues de Menezes
# RA: 246533
#####################################################

# Leitura dos dados
L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]
for i in range(len(tabuleiro)):
    tabuleiro[i].insert(0,-1)
    tabuleiro[i].append(-1)
lista_=[-1 for j in range(len(tabuleiro[0]))]
tabuleiro.insert(0,lista_)
tabuleiro.append(lista_)
l1+=1
c1+=1
l2+=1
c2+=1

#Contadores:
N = 0
S = 0
L = 0
O = 0

#Caminho
def caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O): #cor = cor final
    A = tabuleiro[linha_atual][coluna_atual] #cor atual
    B = tabuleiro[linha_fim][coluna_fim]
    Norte = tabuleiro[linha_atual-1][coluna_atual]
    Sul = tabuleiro[linha_atual+1][coluna_atual]
    Leste = tabuleiro[linha_atual][coluna_atual+1]
    Oeste = tabuleiro[linha_atual][coluna_atual-1]
    if (linha_atual, coluna_atual) == (linha_fim, coluna_fim):
        return True
    else:
        if N==0 and S==0 and L==0 and O==0:
            if A!=-1 and Norte!=-1 and A!=Norte:
                N+=1
                C = caminho(tabuleiro,linha_atual-1,coluna_atual,linha_fim,coluna_fim,Norte,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Sul!=-1 and A!=Sul:
                S+=1
                C = caminho(tabuleiro,linha_atual+1,coluna_atual,linha_fim,coluna_fim,Sul,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Leste!=-1 and A!=Leste:
                L+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual+1,linha_fim,coluna_fim,Leste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Oeste!=-1 and A!=Oeste:
                O+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual-1,linha_fim,coluna_fim,Oeste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            else:
                if A!=-1:
                    A=-1
                    C = caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O)
                    if C == True:
                        return True
                    else:
                        return False
                else:
                    return False
        elif N==1:
            N-=1
            if A!=-1 and Norte!=-1 and A!=Norte:
                N+=1
                C = caminho(tabuleiro,linha_atual-1,coluna_atual,linha_fim,coluna_fim,Norte,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Leste!=-1 and A!=Leste:
                L+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual+1,linha_fim,coluna_fim,Leste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Oeste!=-1 and A!=Oeste:
                O+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual-1,linha_fim,coluna_fim,Oeste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            else:
                if A!=-1:
                    A=-1
                    C = caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O)
                    if C == True:
                        return True
                    else:
                        return False
                else:
                    return False
        elif S==1:
            S-=1
            if A!=-1 and Sul!=-1 and A!=Sul:
                S+=1
                C = caminho(tabuleiro,linha_atual+1,coluna_atual,linha_fim,coluna_fim,Sul,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Leste!=-1 and A!=Leste:
                L+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual+1,linha_fim,coluna_fim,Leste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Oeste!=-1 and A!=Oeste:
                O+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual-1,linha_fim,coluna_fim,Oeste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            else:
                if A!=-1:
                    A=-1
                    C = caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O)
                    if C == True:
                        return True
                    else:
                        return False
                else:
                    return False
        elif L==1:
            L-=1
            if A!=-1 and Norte!=-1 and A!=Norte:
                N+=1
                C = caminho(tabuleiro,linha_atual-1,coluna_atual,linha_fim,coluna_fim,Norte,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Sul!=-1 and A!=Sul:
                S+=1
                C = caminho(tabuleiro,linha_atual+1,coluna_atual,linha_fim,coluna_fim,Sul,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Leste!=-1 and A!=Leste:
                L+=1
                C = caminho(tabuleiro,linha_atual,coluna_atual+1,linha_fim,coluna_fim,Leste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            else:
                if A!=-1:
                    A=-1
                    C = caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O)
                    if C == True:
                        return True
                    else:
                        return False
                else:
                    return False
        elif O==1:
            O-=1
            if A!=-1 and Norte!=-1 and A!=Norte:
                N+=1
                caminho(tabuleiro,linha_atual-1,coluna_atual,linha_fim,coluna_fim,Norte,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Sul!=-1 and A!=Sul:
                S+=1
                caminho(tabuleiro,linha_atual+1,coluna_atual,linha_fim,coluna_fim,Sul,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            elif A!=-1 and Oeste!=-1 and A!=Oeste:
                O+=1
                caminho(tabuleiro,linha_atual,coluna_atual-1,linha_fim,coluna_fim,Oeste,N,S,L,O)
                if C == True:
                    return True
                else:
                    return False
            else:
                if A!=-1:
                    A=-1
                    caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor,N,S,L,O)
                    if C == True:
                        return True
                    else:
                        return False
                else:
                    return False

# Verificação se existe um caminho
if caminho(tabuleiro,l1,c1,l2,c2,tabuleiro[l2][c2],N,S,L,O) == True:
  print("caminho encontrado")
else:
  print("caminho nao encontrado")
