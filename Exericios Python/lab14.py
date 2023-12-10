#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Gabriel Barbiero Fagundes Gomide
# RA:247734
#####################################################


def ajudante(tab, la, ca, lf, cf) :
        marcador = [['#' for i in range(len(tab[0]))] for j in range(len(tab))]
        caminho(tab, la, ca, lf, cf, marcador)
        if marcador[lf][cf] == '*':
            return True
        if marcador[lf][cf] == '#':
            return False
        
    
def caminho(tab, la, ca, lf, cf, marcador):

        if la < 0 or ca < 0 or marcador[la][ca]=='*' :
                return
       
        marcador[la][ca] = '*'
        norte(tab, la, ca, lf, cf, marcador)
        sul(tab, la, ca, lf, cf, marcador)
        oeste(tab, la, ca, lf, cf, marcador)
        leste(tab, la, ca, lf, cf, marcador)

        

def norte(tab, la, ca, lf, cf, marcador):
        if tab[la-1][ca]!=tab[la][ca]:
                caminho(tab, la-1, ca, lf , cf, marcador)
                
def sul(tab, la, ca, lf, cf, marcador):
        if la+1<len(tab):
                if tab[la+1][ca]!=tab[la][ca]:
                        caminho(tab, la+1, ca, lf, cf, marcador)

def oeste(tab, la, ca, lf, cf, marcador):
        if tab[la][ca-1]!=tab[la][ca]:
                caminho(tab, la, ca-1, lf, cf, marcador) 

def leste(tab, la, ca, lf, cf, marcador):
        if ca+1<len(tab[0]):
                if tab[la][ca+1]!=tab[la][ca]:
                        caminho(tab, la, ca+1, lf, cf, marcador)


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
