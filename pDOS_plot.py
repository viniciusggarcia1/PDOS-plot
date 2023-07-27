import questions as qs
import search as src
import graph_structure as gst
import numpy as np
from matplotlib import pyplot as plt
import pTerminalTools as  tt
 
tt.ProgramTitle('pDOS Plot', 'Vinícius G. Garcia', 'viniciusggarcia1@hotmail.com')
#print('===========================pDOS Plot===========================')
tt.box('pDOS Plot')

if qs.DOS_type()['answer'] == 'by atoms':

	qs.atoms_choice()
	qs.spdf_choice()

	posi = np.zeros((len(src.list_atoms), len(src.index)), dtype=int)
	lOrb = np.zeros((len(src.list_spdf)-1, len(src.index)), dtype=int)
	posi_counter=0
	lOrb_counter=0

	for i in range (0, len(src.list_atoms), 1):
		for j in range (0, len(src.index), 1):
			if src.list_atoms[i]==src.atoms[j]:
				posi[i][j]=src.index[j]
				posi_counter+=1
			else:
				posi[i][j]= -123
				
	for i in range (0, len(src.list_spdf)-1, 1):
		for j in range (0, len(src.index), 1):
			if src.list_spdf[i]==src.spdf[j]:
				lOrb[i][j]=src.index[j]
				lOrb_counter+=1
			else:
				lOrb[i][j]= -123

		
	print(src.list_atoms)
	print(src.list_spdf)
	print(len(src.list_spdf))
	print(src.list_spdf)
	print(len(posi))
	
	
	for j in range (0, len(src.index), 1):
		if lOrb[0][j] != -123:
			print(src.full_name[lOrb[0][j] ] )
	for j in range (0, len(src.index), 1):
		if lOrb[1][j] != -123:
			print(src.full_name[lOrb[1][j] ] )

'''		
	for j in range (0, len(src.index), 1):
		if posi[0][j] != -123:
			print(src.full_name[posi[0][j] ] )
			
	for j in range (0, len(src.index), 1):
		if posi[1][j] != -123:
			print(src.full_name[posi[1][j] ] )
	
	for j in range (0, len(src.index), 1):
		if posi[2][j] != -123:
			print(src.full_name[posi[2][j] ] )
			
'''			
E_fermi=qs.Energy_Fermi()
print(E_fermi)


'''
def graph_s ():
	for i in range(0, 20, 1):
		if src.list_spdf[i]=='s':
			for j in range (0, 20, 1):
				Es, ldoss, pdoss = np.loadtxt(src.full_name[lOrb[i][j]], unpack=True, usecols=(0,1,2))
				ldoss_tot=ldoss_tot+ldoss

graph_s ()

plt.show()

PAREI AQUI ~~~ PRECISO COLOCAR ESSE LOOP NO GRAPH_STRUCTURE!!!
'''
#print(src.full_name)
	
	#print (posi)			
	
	#print(src.atoms)
	#print(src.full_name[src.index[39]])
 #   for i in range(0,len(src.full_name)):
    	
    	#index[i]
    	
    	#qs.atoms_choice()['answer'][i]
    
    
    
#    print(qs.atoms_choice()['answer'])


	
    
    
    
    
  
    
    
    
    
    
    
    
#else:
#    print("ORBITALLLLLLLLL")





