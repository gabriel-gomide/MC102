def computador_escolhe_jogada(n,m):
    
    jc=1
    while jc!=m:
        if(n-jc)%(m+1)==0:
            return jc
        else:
            jc=jc+1
    return jc
    
    
def usuario_escolhe_jogada(n,m):
    
    ju=int(input('Quantas peças você vai tirar?'))
    if ju<=m:
        return ju
    else:
        while ju>m:
            ju=int(input('Quantas peças você vai tirar?'))

    

def partida():
   
    n=int(input('Quantas peças?'))
    m=int(input('Limite de peças por jogada?'))
    vezpc=False
    
    if n%(m+1)==0:
        print()
        print('Você começa!')
        
        
        
    else:
        print()
        print('Computador começa')
        vezpc=True
        
    while n>0:
        if vezpc:
            jc=computador_escolhe_jogada(n,m)
            n=n-jc
            if jc==1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou',jc,'peças')
            vezpc=False

        else:
            ju=usuario_escolhe_jogada(n, m)
            n = n - ju
            if ju==1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', ju, 'peças')
            vezpc = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

            
def campeonato():
    nRodada = 1
    while nRodada <= 3:
        print()
        print('**** Rodada', nRodada, '****')
        print()
        partida()
        nRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')
  
    
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
opcao=int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato'))

if opcao==1:
    print('Voce escolheu uma partida!')
    partida()
elif opcao==2:
    print('Voce escolheu um campeonato!')
    campeonato()
else:
    while opcao!=1 and opcao1!=2:
        opcao=int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato'))
