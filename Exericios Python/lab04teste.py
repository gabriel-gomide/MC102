###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Gabriel Barbiero Fagundes Gomide
# RA:247734
###################################################

# leitura da sequência de compras e vendas
operacao=int(input())
estoque=0
venda=0
erro=list()
while operacao!=0:
    if -operacao>estoque:
        erro.append(-operacao)
        
    elif -operacao<=estoque:
        if operacao<0:
            venda=venda+1
        estoque=operacao+estoque
    operacao=int(input())
    
    
# impressão da saída
for op in erro:
    print('Quantidade indisponível para a venda de' ,op, 'unidades.')
print('Quantidade de vendas realizadas:', venda)
print('Quantidade em estoque:', estoque)

