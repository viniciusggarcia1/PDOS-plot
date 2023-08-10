import re
import os

#caminho_pasta = os.getcwd()  # Obtém o caminho da pasta atual
path_folder = '/mnt/c/Users/vinic/OneDrive/Área de Trabalho/site_testes/PDOS-plot/example'

def files_directory(path_folder):
        full_name=[]
        # Percorre todos os arquivos e subpastas no caminho da pasta atual
        for name in os.listdir(path_folder):
                complete_path = os.path.join(path_folder, name)
                full_name.append(name)
                
        # Regular expression pattern
        pattern = r'\((\w+)\)'
        
        # Store the matches in separate vectors
        atoms = []
        spdf = [] 
        index=[]  #index guarda as posições de full_name que tem arquivos com o padrão

        # Iterating over the full_name list
        for i in range(len(full_name)):
        # Extract the contents between parentheses
                matches = re.findall(pattern, full_name[i])
                #return matches
        
                # Check if matches list has at least two elements
                if len(matches) >= 2:
                        # Store the matches in separate vectors
                        atoms.append(matches[0])
                        spdf.append(matches[1])
                        index.append(i)

        #Retirando os átomos duplicados
        list_atoms= list(set(atoms))
        list_spdf=list(set(spdf))

        #Colocando em ordem alfabética:
        list_atoms=sorted(list_atoms)
        list_spdf=sorted(list_spdf)

        #adicionando total em list_spdf
        list_spdf.append('total')

        return list_atoms, list_spdf, full_name

def soma(file):
        Es, ldos = np.loadtxt(file, unpack=True, usecols=(0,1))
        ldosS[i] = ldosS[i] + ldos[i]
