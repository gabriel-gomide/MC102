n=input()
m=input()

n=list(n)
m=list(m)
for i in range(len(n)):
        while n[i]in m:
            m.remove(n[i])
print(' '.join(m))
