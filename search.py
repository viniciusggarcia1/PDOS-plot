import re
import os

#caminho_pasta = os.getcwd()  # Obtém o caminho da pasta atual
caminho_pasta = '/mnt/c/Users/vinic/OneDrive/Área de Trabalho/site_testes/PDOS-plot/example'


full_name=[]
# Percorre todos os arquivos e subpastas no caminho da pasta atual
for name in os.listdir(caminho_pasta):
        complete_path = os.path.join(caminho_pasta, name)
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
    
    # Check if matches list has at least two elements
    if len(matches) >= 2:
        # Store the matches in separate vectors
        atoms.append(matches[0])
        spdf.append(matches[1])
        index.append(i)
#    else:
        # Handle the case where matches list does not have enough elements
        # You can choose to skip this entry or handle it in a different way
        #print(f"Skipping entry {i+1}: {full_name[i]}")

#Retirando os átomos duplicados
list_atoms= list(set(atoms))

list_atoms=sorted(list_atoms)

list_spdf=list(set(spdf))
list_spdf.append('total')
list_spdf=sorted(list_spdf)

#print(list_spdf)
#print(list_atoms)



