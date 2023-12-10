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

while operacao!=0:
    if operacao>0:
        estoque=operacao+estoque
    if operacao<0:
        venda=-operacao+venda
        estoque=operacao+estoque
        if estoque<0:
            print('Quantidade indisponível para a venda de', -operacao , 'unidades')
    operacao=int(input())

# impressão da saída
print('Quantidade de vendas realizadas:', venda)
print('Quantidade em estoque:', estoque)