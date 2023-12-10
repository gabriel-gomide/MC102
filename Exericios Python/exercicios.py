def media(lista):
    if len(lista)==2:
        return (lista[0]+lista[1])/2
    return ((lista[0]+lista[1])+media(lista[2:]))/3


def soma(n):
    if n==0:
        return 0
    return n+soma(n-1)

def soma_harmonica(n):
    if n==1:
        return 1
    return 1/n+soma_harmonica(n-1)

print(soma_harmonica(5))
