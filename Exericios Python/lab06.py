##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:Gabriel Barbiero Fagundes Gomide
# RA:247734
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
a=True
b=list()
while a:
    mov=int(input())
    aux=mov-1
    if mov==0:
        a=False
    else:
        b=torre[0:mov]
        b.reverse()
        for i in range(len(torre)):
            if i>=mov:
                b.append(torre[i])
        #print(b)
        torre=b
        #print(torre)
        #print(torre)
#print(torre)
# Impressão da saída
if b==sorted(torre):
    print('Torre estavel')
else:
    print('Torre instavel')
