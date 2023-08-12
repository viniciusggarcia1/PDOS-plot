# ------------------------------------------------------------------------------------ #
#                                                                                      #
# Reads pdos files from Quantum Espresso and plots using matplotlib                    #
#                                                                                      #
# Vinícius G. Garcia - UFES                                                            #
# Aug 2023                                                                             #
#                                                                                      #
# ------------------------------------------------------------------------------------ #

import numpy as np
from matplotlib import pyplot as plt
import re
import os
import cairosvg
import search as src
import PDOS_graph as gh
import questions as qs
import pTerminalTools as tt


tt.ProgramTitle('pDOS Plot', 'Vinícius G. Garcia', 'viniciusggarcia1@hotmail.com')
tt.box('Code to plot PDOS from Quantum Espresso files')


match_atoms=[]
match_spdf=[]

E=[]

#Pega o nível de Fermi
#Efermi=-3
Efermi=qs.Energy_Fermi ()

#Pega o intervalo em x para plot do gráfico
inter_x=qs.Energy_graphx()

#Pergunta se o plot vai ser por átomo ou por orbitais
choice = qs.DOS_type()['answer']



if choice == 'by atoms':
    atoms = qs.atoms_choice(src.files_directory(src.path_folder)[0])['answer']
    pdos_tot = qs.pdos_tot()['answer']

    ltot=0
    for j in range (len(atoms)):

        ldosS=0

        match=[]
        for i in range(0, len(src.files_directory(src.path_folder)[2]), 1):

            pattern = rf'\({atoms[j]}\)'

            #Salva o nome dos arquivos que deram match com o padrão em um vetor
            if re.findall(pattern, src.files_directory(src.path_folder)[2][i]):
                match.append(src.files_directory(src.path_folder)[2][i])

        for k in range(len(match)):
            full_path = os.path.join(src.path_folder, match[k])
            Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))

            ldosS = ldosS + ldos
            ltot = ltot + ldos

        # Desloca pro nível de Fermi e plota a contribuição do átmo j
        Es=Es-Efermi
        gh.graph_spdf(Es, ldosS, atoms[j], False, inter_x)

    if pdos_tot == 'yes':
        #Es=Es-Efermi
        gh.graph_spdf(Es, ltot, None, True, inter_x)

    #Salva o gráfico
    
    plt.tight_layout()
    plt.savefig('temp_graph.svg', format="svg")
    plt.close()

    # Converter o arquivo SVG para PDF usando o cairosvg
    cairosvg.svg2pdf(url='temp_graph.svg', write_to='graph.pdf')



if choice == 'by orbital':
    ltot = 0
    zdosP = 0
    xdosP = 0
    ydosP = 0
    ldosS2 = 0
    ltotx = 0
    ltoty = 0
    ltotz = 0
    ltotxyz = 0
    # Lista com os átomos e orbitais selecionados pelo usuário
    atoms = qs.atoms_choice(src.files_directory(src.path_folder)[0])['answer']
    spdf = qs.spdf_choice(src.files_directory(src.path_folder)[1])['answer']
    
    # coloca os elementos da lista em ordem alfabética
    atoms = sorted(atoms)
    spdf = sorted(spdf)

    #Pergunta se o usuário quer plotar as contribuições por orbital
    yn = qs.yn()['answer']

    #spdf.append('d')

    #Armazena as componentes dos orbitais que o usuário quer plotar
    if yn == 'yes':
        if 'p' in spdf:
            qt_orb_p= qs.orbital_component_p()['answer']
        if 'd' in spdf:
            qt_orb_d= qs.orbital_component_d()['answer']

    comp_orb=[]
    if yn == 'yes':
        if 'p' in spdf:
            comp_orb.append('p')
        if 'd' in spdf:
            comp_orb.append('d')
    
    comp_orb=sorted(comp_orb)


    for i in range(len(spdf)):

        pattern_spdf = rf'\({spdf[i]}\)'
        ldosS=0

        for j in range(len(atoms)):

            pattern_atoms = rf'\({atoms[j]}\)'
            match=[]
            for k in range (len(src.files_directory(src.path_folder)[2])):
                
                a = src.files_directory(src.path_folder)[2][k]
                if re.findall(pattern_atoms, a) and re.findall(pattern_spdf, a):
                    match.append(src.files_directory(src.path_folder)[2][k])
     
            for m in range (len(match)):
                full_path = os.path.join(src.path_folder, match[m])

                if yn == 'no':
                    Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))
                    
                    ldosS = ldosS + ldos
                    ltot = ltot + ldos
                    
                else:
 
                    if spdf[i] == 'p':
                        Es, ldos, zdos, xdos, ydos = np.loadtxt(full_path, unpack=True, usecols=(0,1,2,3,4))
                        zdosP = zdosP + zdos
                        xdosP = xdosP + xdos
                        ydosP = ydosP + ydos
                        
                        ltotx = ltotx + xdos
                        ltoty = ltoty + ydos
                        ltotz = ltotz + zdos

                        ltot = ltot + ldos

                    if spdf[i] == 's':
                        Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))
                        #ldosS = ldosS + ldos
                        ldosS2 = ldosS2 + ldos
                        ltot = ltot + ldos
                    
                    #fazer mesmo procedimento para orbitais d e f
                    if spdf[i] == 'd':
                        Ed, ldos, dz2, dzx, dzy, dx2_y2, dxy = np.loadtxt(full_path, unpack=True, usecols=(0,1,2,3,4,5,6))
                    
                    if spdf[i] == 'f':
                        Es, ldos = np.loadtxt(full_path, unpack=True, usecols=(0,1))
                        ldosf = ldosf + ldos
                        ltot = ltot + ldos
                        ####ACHO QUE O ORBITAL f ESTÁ QUASE PRONTO!!!###########
                        

                        #print('hahaha')
                

        #plota o gráfico para os orbitais
        if spdf[i] != 'total':
            Ess=Es-Efermi
            if yn == 'no':
                gh.graph_spdf(Ess, ldosS, spdf[i], False, inter_x)
                
        
    if yn == 'yes':
        if 's' in spdf:
            gh.graph_spdf(Ess, ldosS2, 's', False, inter_x)
            
        if 'px' in (qt_orb_p):
            gh.graph_spdf(Ess, xdosP, '$p_x$', False, inter_x)

        if 'py' in (qt_orb_p):
            gh.graph_spdf(Ess, ydosP, '$p_y$', False, inter_x)

        if 'pz' in (qt_orb_p):
            gh.graph_spdf(Ess, zdosP, '$p_z$', False, inter_x)

        if ('px' in (qt_orb_p) or 'py' in (qt_orb_p) or 'pz' in (qt_orb_p)) and 'total' in spdf:
            ltotxyz = gh.sum_spdf(spdf, qt_orb_p ,ldosS2, ltotx, ltoty, ltotz)
            gh.graph_spdf(Ess, ltotxyz, None, True, inter_x)

    #plota o gráfico para a contribuição total
    if 'total' in spdf and yn == 'no':
        gh.graph_spdf(Ess, ltot, None, True, inter_x)

    
    
    #Salva o gráfico
    plt.tight_layout()
    plt.savefig('temp_graph.svg', format="svg")
    plt.close()

    # Converter o arquivo SVG para PDF usando o cairosvg
    cairosvg.svg2pdf(url='temp_graph.svg', write_to='graph.pdf')