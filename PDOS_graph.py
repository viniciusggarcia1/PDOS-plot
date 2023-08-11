import numpy as np
from matplotlib import pyplot as plt

def graph_spdf (E, ldos, legd, marker):
    #Es, ldos = np.loadtxt(file, unpack=True, usecols=(0,1))
    if marker == False:
        plt.plot(E, ldos, lw=2, zorder=1, label=legd)
    if marker == True:
        plt.plot(E, ldos, color='black', lw=2, zorder=1, label='Total')
    

    # Add legend
    plt.legend(loc='upper right')

    # Add labels and title
    plt.xlabel('$E$-$E_F$ (eV)', fontsize=18)
    plt.ylabel('DOS (States/eV)', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(bottom=0)
    plt.autoscale(enable=True, axis='both', tight=True)
    plt.xlim(-20, 5)
    plt.axvline(0, linestyle='dashed', color='gray')

'''
def graph_p (E, file, legd, marker):
    zdos, xdos, ydos = np.loadtxt(file, unpack=True, usecols=(2,3,4))
    if marker == False:
        plt.plot(E, ldos, lw=2, zorder=1, label=legd)
    if marker == True:
        plt.plot(E, ldos, color='black', lw=2, zorder=1, label='Total')
    

    # Add legend
    plt.legend(loc='upper right')

    # Add labels and title
    plt.xlabel('$E$-$E_F$ (eV)', fontsize=18)
    plt.ylabel('DOS (States/eV)', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(bottom=0)
    plt.autoscale(enable=True, axis='both', tight=True)
    #plt.xlim(-3, 3)
    plt.axvline(0, linestyle='dashed', color='gray')
'''