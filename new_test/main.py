import numpy as np
import re
import os
import search as src
import graph as gh

#caminho_pasta = os.getcwd()  # Obtém o caminho da pasta atual
path_folder = '/mnt/c/Users/vinic/OneDrive/Área de Trabalho/site_testes/PDOS-plot/example/'

#print(src.files_directory(path_folder)[2][1])

match=[]
j=1
for i in range(0, len(src.files_directory(path_folder)[2]), 1):

    pattern = rf'\({src.files_directory(path_folder)[0][j]}\)'

    if re.findall(pattern, src.files_directory(path_folder)[2][i]):
        match.append(src.files_directory(path_folder)[2][i])
        
#for i in range(len(match)):
#    print(match[i])

#print(src.files_directory(path_folder)[0])

caminho_completo = os.path.join(path_folder, match[0])

gh.graph_s(caminho_completo, src.files_directory(path_folder)[0][j])