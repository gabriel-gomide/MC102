import pandas as pd
df=pd.read_csv('output.txt' , sep = '\t')
df.head(30)
df.plot()
df['meu tempo']=df['Stop (s)']-df['Start (s)']
df.head()
df['t queda (s)'].mean()
df['meu tempo'].mean()
