import numpy as np
from matplotlib import pyplot as plt
import re
import os
import search as src
import PDOS_graph as gh
import questions as qs
import pTerminalTools as tt


tt.ProgramTitle('pDOS Plot', 'Vinícius G. Garcia', 'viniciusggarcia1@hotmail.com')
tt.box('pDOS Plot')

#caminho_pasta = os.getcwd()  # Obtém o caminho da pasta atual
path_folder = '/mnt/c/Users/vinic/OneDrive/Área de Trabalho/site_testes/PDOS-plot/example/'

#print(src.files_directory(path_folder)[2][1])

match_atoms=[]
match_spdf=[]

E=[]


Efermi=-3
#Efermi=qs.Energy_Fermi ()
choice = qs.DOS_type()['answer']




if choice == 'by atoms':
    ltot=0
    for j in range (len(src.files_directory(path_folder)[0])):

        ldosS=0
        match=[]
        for i in range(0, len(src.files_directory(path_folder)[2]), 1):

            pattern = rf'\({src.files_directory(path_folder)[0][j]}\)'

            #Salva o nome dos arquivos que deram match com o padrão em um vetor
            if re.findall(pattern, src.files_directory(path_folder)[2][i]):
                match.append(src.files_directory(path_folder)[2][i])
        #print(match)
        #print()

        #ldosS = [0] * len(ldos)
        lS=[]
        #ldosS=0
        for k in range(len(match)):
            full_path = os.path.join(path_folder, match[k])
            Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))

            ldosS = ldosS + ldos
        ltot=ltot + ldosS

        # Desloca pro nível de Fermi e plota a contribuição do átmo j
        Es=Es-Efermi
        gh.graph_s(Es, ldosS, src.files_directory(path_folder)[0][j], False)

    #Es=Es-Efermi
    gh.graph_s(Es, ltot, src.files_directory(path_folder)[0][j], True)

    #Salva o gráfico
    plt.tight_layout()
    plt.savefig('graph.png', dpi=800)



if choice == 'by orbital':
    ltot = 0
    # Lista com os átomos e orbitais selecionados pelo usuário
    atoms = qs.atoms_choice(src.files_directory(path_folder)[0])['answer']
    spdf = qs.spdf_choice(src.files_directory(path_folder)[1])['answer']
    
    # coloca os elementos da lista em ordem alfabética
    atoms = sorted(atoms)
    spdf = sorted(spdf)

    print(atoms)
    print(spdf)

    for i in range(len(spdf)):

        pattern_spdf = rf'\({spdf[i]}\)'
        ldosS=0
        for j in range(len(atoms)):

            pattern_atoms = rf'\({atoms[j]}\)'
            match=[]
            for k in range (len(src.files_directory(path_folder)[2])):
                
                a = src.files_directory(path_folder)[2][k]
                if re.findall(pattern_atoms, a) and re.findall(pattern_spdf, a):
                    match.append(src.files_directory(path_folder)[2][k])

            #print(match)
            #print()

            ldosS=0
            for m in range (len(match)):
                full_path = os.path.join(path_folder, match[m])
                Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))
                ldosS = ldosS + ldos
            

            ltot = ltot + ldosS
        
        #plota o gráfico para os orbitais
        if spdf[i] != 'total':
            Ess=Es-Efermi
            gh.graph_s(Ess, ldosS, spdf[i], False)

    #plota o gráfico para a contribuição total
    if 'total' in spdf:
        gh.graph_s(Ess, ltot, None, True)
    
    #Salva o gráfico
    plt.tight_layout()
    plt.savefig('graph.png', dpi=800)