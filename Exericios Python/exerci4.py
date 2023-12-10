n=int(input('Digite um número inteiro:'))

sa=0
while n!=0:
    sa=sa+(n%10)
    n=n//10

print(sa)
