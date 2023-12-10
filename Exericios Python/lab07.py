
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome:Gabriel Barbiero Fagundes Gomide
# RA:24734
###################################################

# Leitura das tropas de defesa
defesa=int(input())
aux=1
defensores=list()
while defesa>=aux:
    podd=int(input())
    defensores.append(podd)
    aux=aux+1
    
# Leitura das tropas de ataque
ataque=int(input())
aux2=1
atacantes=list()
while ataque>=aux2:
    poda=int(input())
    atacantes.append(poda)
    aux2=aux2+1

# Processamento da guerra

vitoria=False
i=0
while not vitoria:
    aux3=0
    for a in range(len(atacantes)):
        if atacantes[a]>defensores[a+i]:
            aux3=aux3+1
        elif atacantes[a]<defensores[a+i]:
            aux3=aux3-1
    #print(i, i+1, ':',aux3)
    if aux3>0:
        vitoria=True
        posicao=i+1
    else:
        i=i+1
        if i>(len(defensores)-len(atacantes)):
            break
# Saída de dados
if vitoria==False:
    print('Derrota')
else:
    print('Vitória posicionando as tropas a partir da posição', posicao)
