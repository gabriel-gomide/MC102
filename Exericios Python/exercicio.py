name=open('mbox-short.txt')

di=dict()
for line in name:
    line=line.rstrip()
    if not line.startswith('From'):continue
    if line.startswith('From:'):continue
    words=line.split()
 
    for sed in words:
        if sed!=words[1]:continue
        di[sed]=di.get(sed,0)+1


bigcount=None
bigword=None
for sed,count in di.items():
    if bigcount is None or count>bigcount:
        bigword=sed
        bigcount=count
print(bigword,bigcount)
    

