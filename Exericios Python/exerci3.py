
def incomodam(n):

    if n<=0:
        return ''

    if n==1:
        return 'incomodam '
    else:
        return 'incomodam ' + incomodam(n-1)

def elefantes(n):
    if n == 1:
        return "Um elefante incomoda muita gente "
    elif n == 2:
        return elefantes(n-1)+ '\n'+ str(n)+ " elefantes "+ incomodam(n) +"muito mais" 
    elif n > 2:
        frase1 = "\n"+str(n-1)+ " elefantes incomodam muita gente"
        frase2 = "\n"+str(n)+" elefantes "+ incomodam(n) +"muito mais"
        return elefantes(n-1) + frase1 +frase2
    else:
        return ""
