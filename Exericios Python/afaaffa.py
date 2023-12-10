
#Leitura do número de guerreiros defensores
n_defesa = int(input())

#Lista dos poderes do guerreiros defensores
defesa = [int(input()) for i in range(n_defesa)] 

#Leitura do número de guerreiros atacantes
m_ataque = int(input())

#Lista dos poderes do guerreiros atacantes
ataque = [int(input()) for j in range(m_ataque)] 

ok = True

#modificador do indice dos defensores, esse valor será variado,
#assim, se por exemplo, posição for 1, então ele começará a comparar os
#atacantes a partir do segundo defensor, lembrar que, em uma lista, o primeiro elemento
#tem indice 0
posição = 0

while ok:
    #contadores de pontos
    z_ataq = 0          
    x_def = 0

    #como na lista de atacantes, haverá m_ataque elementos, então
    #b irá de 0 até m_ataque, sendo equivalente ao indice de cada
    #elemento da lista de atacantes
    for b in range(m_ataque):

        #para cada b, compararemos o defensor de posição b
        #com o atacante de posição b, contudo, os atacantes também devem
        #ser comparados com os defensores de indices maiores, então adicionamos o
        #modificador de posição
        soldado_def = defesa[b+posição]
        soldado_ataq = ataque[b]
                
        if soldado_ataq > soldado_def:
            z_ataq = z_ataq + 1
                    
        elif soldado_ataq < soldado_def: 
            x_def = x_def + 1
                    


    if z_ataq > x_def:
        posição = posição + 1  #vendo quem venceu essa batalha
        print('Vitória posicionando as tropas a partir da posição', posição)
        ok = False
        


    #enquanto não vencer, os atacantes vão ser comparados com defensores de indice
    #posterior
    else:
        posição = posição + 1

        #se o modificador posição somado ao número de atacantes
        #for maior que o número de defensores, não faz sentido continuar o programa
        if posição+m_ataque>n_defesa:
            break
        
if ok:
    print('Derrota')
