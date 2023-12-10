###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
###################################################

# Leitura de dados
estoque = {}
compra ={}
venda ={}
saida=list()
produtos=list()
C=0
V=0
# Processamento
FIM=False
while not FIM:
    operacao=input()
    if operacao=='FIM':
        FIM=True
        break
    else:
        operacao=operacao.split(' :')
        N=operacao[0]
        X=int(operacao[1])
        
        if N in estoque:
            if estoque[N]>=-X:
                estoque[N]=estoque[N]+X
                if X>0:

                    compra[N]=compra[N]+1
                elif X<0:
                    
                    venda[N]=venda[N]+1
            else:
                print("Quantidade indisponivel para a venda de" , -X , "unidade(s) do produto " + N + ".")
            #print(estoque)
        else:
            if X>0:
                
                estoque[N]=X
                compra[N]=1
                venda[N]=0
                produtos.append(N)
                #print(produtos)
            elif X<0:
                print("Quantidade indisponivel para a venda de" , -X ,"unidade(s) do produto " + N + ".")


produtos=sorted(produtos)
for n in produtos:
    print("Produto:" , n)
    print("Quantidade em Estoque:" ,estoque[n])
    print("Pedidos de Compra:", compra[n])
    print("Pedidos de Venda:", venda[n])


  
