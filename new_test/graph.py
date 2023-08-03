import numpy as np
from matplotlib import pyplot as plt

def graph_s (file, legd):
    Ep, ldos = np.loadtxt(file, unpack=True, usecols=(0,1))

    plt.plot(Ep, ldos, color='blue', lw=2, zorder=1, label=legd)
    

    # Add legend
    plt.legend(loc='upper right')

    # Add labels and title
    plt.xlabel('$E$-$E_F$ (eV)', fontsize=18)
    plt.ylabel('DOS (States/eV)', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(bottom=0)
    plt.xlim(-10, 1)
    plt.axvline(0, linestyle='dashed', color='gray')

   
