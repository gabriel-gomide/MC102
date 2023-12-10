import pandas as pd
import os
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
# Selecionando o arquivo
path = r'C:\Users\gabri\OneDrive\Área de Trabalho\Amostras\Medusa 2\Medusa 2-T3-001-1'
file_name = 'Medusa 2-T3-001-1.txt'
full_path = os.path.join(path, file_name)
data = pd.read_csv(full_path, sep="\t", header=None)
i=2
while i!=101:
    # Separando os dois trechos de interesse
    x = data[0]
    y = data[i]
    y = y-min(y)

    # Criando um novo DataFrame com os trechos de interesse
    novo_dataframe = pd.DataFrame({'Coluna_X': x, 'Coluna_Y': y})

    # Ajustando o caminho de destino
    caminho_destino = r'C:\Users\gabri\OneDrive\Área de Trabalho\Amostras\Medusa 2\Medusa 2-T3-001-1'
    novo_arquivo = os.path.join(caminho_destino, 'adosteste'+str(i)+'.csv')

    # Salvando o novo DataFrame no arquivo CSV com o caminho de destino modificado
    novo_dataframe.to_csv(novo_arquivo, index=False)
    i=i+1
    
#%%