#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Gabriel Barbiero Fagundes Gomide
# RA:247734
#####################################################
def ajudante(tab, la, ca, lf, cf) :
        marcador = [[False for i in range(len(tab[0]))] for j in range(len(tab))]
        caminho(tab, la, ca, lf, cf, marcador)
        if marcador[lf][cf] == True:
            return True
        if marcador[lf][cf] == False:
            return False
        return True
    
def caminho(tab, la, ca, lf, cf, marcador):

    if la < 0 or ca < 0 or la+1 > len(tab) or ca+1>len(tab[0]) or marcador[la][ca] :
        return
    
    marcador[la][ca] = True
    if marcador[la][ca]==marcador[lf][cf]:
            return True
        
    if tab[la-1][ca]!=tab[la][ca]:
        caminho(tab, la-1, ca, lf , cf, marcador) # norte
        
    if la+1<len(tab):
        if tab[la+1][ca]!=tab[la][ca]:
            caminho(tab, la+1, ca, lf, cf, marcador) # sul
            
    if tab[la][ca-1]!=tab[la][ca]:
        caminho(tab, la, ca-1, lf, cf, marcador) # oeste
        
    if ca+1<len(tab[0]):
        if tab[la][ca+1]!=tab[la][ca]:
            caminho(tab, la, ca+1, lf, cf, marcador) # leste	
           
# Leitura dos dados
L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

# Verificação se existe um caminho
a=ajudante(tabuleiro,l1,c1,l2,c2)

if a==True:
  print("caminho encontrado")
else:
  print("caminho nao encontrado")
