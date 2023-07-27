import pDOS_plot as pDOS
import search as src
import numpy as np
from matplotlib import pyplot as plt

def graph_s ():
	for i in range(0, pDOS.posi_counter, 1):
		if pDOS.list_spdf[i]=='s':
			for j in range (0, lOrb_counter/3, 1):
				Es, ldoss, pdoss = np.loadtxt(pDOS.full_name[pDOS.lOrb[i][j]], unpack=True, usecols=(0,1,2))
				ldoss_tot=ldoss_tot+ldoss
	#return plt.plot(Es, ldoss_tot, color='blue', lw=1, zorder=1, label='s')
