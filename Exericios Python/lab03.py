###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
###################################################

# leitura de dados
dia = int(input())
hora = int(input())
minuto = int(input())
estudante = str(input())
pagamento = str(input())

# valor do ingresso inteiro
dia1 = 30.00
noite1 = 30.00
dia2 = 15.00
noite2 = 20.00
dia3 = 15.00
noite3 = 20.00
dia4 = 15.00
noite4 = 30.00
dia5 = 20.00
noite5 = 30.00
dia6 = 20.00
noite6 = 40.00
dia7 = 30.00
noite7 = 40.00

# valor a pagar



if dia==1:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite1 / 2
        elif pagamento=='C':
            ingresso=0.7 * noite1
        else:
            ingresso=noite1
    else:
        if estudante=='S':
            ingresso=dia1 / 2
        elif pagamento=='C':
            ingresso=0.7 * dia1
        else:
            ingresso=dia1        
    

if dia==2:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite2 / 2
        elif pagamento=='C':
            ingresso=0.5 * noite2
        else:
            ingresso=noite2
    else:
        if estudante=='S':
            ingresso=dia2 / 2
        elif pagamento=='C':
            ingresso=0.5 * dia2
        else:
            ingresso=dia2    



if dia==3:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite3 / 2
        elif pagamento=='C':
            ingresso=0.5 * noite3
        else:
            ingresso=noite3
        
    else:
        if estudante=='S':
            ingresso=dia3 / 2
        elif pagamento=='C':
            ingresso=0.5 * dia3
        else:
            ingresso=dia3


if dia==4:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite4 / 2
        elif pagamento=='C':
            ingresso=0.5 * noite4
        else:
            ingresso=noite4
        
    else:
        if estudante=='S':
            ingresso=dia4 / 2
        elif pagamento=='C':
            ingresso=0.5 * dia4
        else:
            ingresso=dia4

if dia==5:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite5 / 2
        elif pagamento=='C':
            ingresso=0.5 * noite5
        else:
            ingresso=noite5
        
    else:
        if estudante=='S':
            ingresso=dia5 / 2
        elif pagamento=='C':
            ingresso=0.5 * dia5
        else:
            ingresso=dia5


if dia==6:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite6 / 2
        elif pagamento=='C':
            ingresso=0.7 * noite6
        else:
            ingresso=noite6
        
    else:
        if estudante=='S':
            ingresso=dia6 / 2
        elif pagamento=='C':
            ingresso=0.5 * dia6
        else:
            ingresso=dia6

if dia==7:
    if hora>18 and minuto>=30 or hora>=19:
        if estudante=='S':
            ingresso=noite7 / 2
        elif pagamento=='C':
            ingresso=0.8 * noite7
        else:
            ingresso=noite7
        
    else:
        if estudante=='S':
            ingresso=dia7 / 2
        elif pagamento=='C':
            ingresso=0.8 * dia7
        else:
            ingresso=dia7

       
# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))
