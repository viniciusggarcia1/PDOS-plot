import numpy as np
from matplotlib import pyplot as plt
import re
import os
import search as src
import graph as gh

#caminho_pasta = os.getcwd()  # Obtém o caminho da pasta atual
path_folder = '/mnt/c/Users/vinic/OneDrive/Área de Trabalho/site_testes/PDOS-plot/example/'

#print(src.files_directory(path_folder)[2][1])

match=[]
E=[]

x = 1

#Es, ldos = np.loadtxt(match[i], unpack=True, usecols=(0,1))
if x == 1:
    ltot=0
    for j in range (len(src.files_directory(path_folder)[0])):

        for i in range(0, len(src.files_directory(path_folder)[2]), 1):

            pattern = rf'\({src.files_directory(path_folder)[0][j]}\)'

            if re.findall(pattern, src.files_directory(path_folder)[2][i]):
                match.append(src.files_directory(path_folder)[2][i])

        #ldosS = [0] * len(ldos)
        lS=[]
        ldosS=0
        for k in range(len(match)):
            full_path = os.path.join(path_folder, match[k])
            Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))

            ldosS = ldosS + ldos
        ltot=ltot + ldosS
        gh.graph_s(Es, ldosS, src.files_directory(path_folder)[0][j], False)

    gh.graph_s(Es, ltot, src.files_directory(path_folder)[0][j], True)
    plt.tight_layout()
    plt.savefig('graph.png', dpi=800)

        
#for i in range(len(match)):
#    print(match[i])

#print(src.files_directory(path_folder)[0])

'''
caminho_completo = os.path.join(path_folder, match[0])

gh.graph_s(caminho_completo, src.files_directory(path_folder)[0][j])
plt.tight_layout()
plt.savefig('graph.png', dpi=800)
'''