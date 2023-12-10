def computador_escolhe_jogada(n,m):
    #retorna um inteiro correspondente a próxima jogada do computador
    jc=1
    while jc!=m:
        if(n-jc)%(m+1)==0:
            return jc
        else:
            jc=jc+1
    return jc
    
