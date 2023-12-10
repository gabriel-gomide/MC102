

def ajudante(tab, la, ca, lf, cf) :
        m = len(tab)
        n = len(tab[0])   
        marcador = [[False for i in range(n)] for j in range(m)]
        dfs(tab, la, ca, lf, cf, marcador)
        if marcador[lf][cf] == True:
            return True
        if marcador[lf][cf] == False:
            return False
        return True
     
def dfs(tab, la, ca,lf, cf, marcador) :
        m = len(tab)
        n = len(tab[0])
        
        marcador = [[False for i in range(n)] for j in range(m)]
        dfs(tab, la, ca, lf, cf, marcador)
        if marcador[lf][cf] == True:
            return True
        if marcador[lf][cf] == False:
            return False
        return True
    
        if la < 0 or ca < 0 or la+1 > m or ca > n-1 or marcador[la][ca] :
            return
        marcador[la][ca] = True
        if marcador[la][ca]==marcador[lf][cf]:
            return True
        print(marcador)
        if tab[la-1][ca]!=tab[la][ca]:
            dfs(tab, la-1, ca, lf , cf, marcador) # Move left
        if la+1<len(tab):
            if tab[la+1][ca]!=tab[la][ca]:
                dfs(tab, la+1, ca, lf, cf, marcador) # Move Right
        if tab[la][ca-1]!=tab[la][ca]:
            dfs(tab, la, ca-1, lf, cf, marcador) # Move top
        if ca+1<len(tab[0]):
            if tab[la][ca+1]!=tab[la][ca]:
                dfs(tab, la, ca+1, lf, cf, marcador) # Move bottom		
	
tabuleiro=[[0,1,1,1],
           [0,0,0,0],
           [0,1,0,1],
           [1,0,1,0]]

#find path
la=0 # source x
ca= 0 # source y
lf = 1 # destination x
cf = 3 # destination y
m = len(tabuleiro)
n = len(tabuleiro[0])
marcador = [[False for i in range(n)] for j in range(m)]
print(dfs(tabuleiro,la,ca,lf,cf,marcador))
