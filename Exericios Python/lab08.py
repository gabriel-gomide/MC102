###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome:Gabriel Barbiero Fagundes Gomide
# RA:247734
###################################################

# Leitura da palavra
palavra = input()

# Leitura dos palpites e impressão do resultado para cada palpite
aux=True
count=0
ab=0
while aux:
    palpite=input()
    palpite_saida=list(palpite)
    #print(palpite_saida)
    for i in range(len(palpite_saida)):
        if palpite_saida[i]==palavra[i]:
            palpite_saida[i]=palpite_saida[i].upper()
        elif palpite_saida[i] in palavra:
            palpite_saida=palpite_saida
        else:
             palpite_saida[i]='_'
    print(''.join(palpite_saida))
    a=''.join(palpite_saida)
    count=count+1
    if count>=6:
        aux=False
    if a==palavra.upper():
        ab=1
        break
        



# Impressão da linha final
if ab==1:
    print("Resposta correta")
else:
    print("Palavra correta:", palavra)
