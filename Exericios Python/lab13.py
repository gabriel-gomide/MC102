###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Gabriel Barbiero Fagundes Gomide
# RA: 247734
###################################################

# Leitura de dados
top=True
votos=list()
apuracao=dict({})
while top:
    candidato=input()
    if candidato=='0':
        top=False
    votos.append(candidato)
for i in range(len(votos)):
    a=votos.count(votos[i])
    if votos[i]=='Branco':
        votos[i]='Brancos'
    if votos[i]=='Nulo':
        votos[i]='Nulos'
    if votos[i] not in apuracao:
        apuracao[votos[i]]=a
    
# Saída de dados


for i in sorted(apuracao, key=apuracao.get, reverse=True):
    if i!='Brancos' and i!='Nulos' and i!='0':
        print(i, apuracao[i])

print('Brancos', apuracao['Brancos'])
print('Nulos', apuracao['Nulos'])
